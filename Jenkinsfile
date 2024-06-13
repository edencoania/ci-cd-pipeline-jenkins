pipeline {
    agent
    {
        label "agent3"
    }
    environment {
        target_ip_address = "172.31.9.1"
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-creds')

    }

    stages
    {

       stage('SCM')
          {
              steps
              {
                checkout scm
                }
          }

       stage('clean')
       {
             steps
             {
                script
                {
                    slackSend(color: '#00FF00', message: 'Build STARTED!')
                }
		sh "docker image prune -f"

		sh "docker container prune -f"
		sh "docker buildx prune -f"
		sh "docker system prune -f"             
}
       }

       stage('build')
       {
             steps
             {
                script
                {
                    slackSend(color: '#00FF00', message: 'Build STARTED!')
                }
                sh "docker build -t app:weather -f ./weather/gunicorn_deploy/Dockerfile ./weather/gunicorn_deploy/"
                sh "docker build -t nginx:weather -f ./weather/nginx_deploy/Dockerfile ./weather/nginx_deploy/"
             }
       }

       stage('test')
       {
            steps
            {
               echo 'Notify GitLab'
               updateGitlabCommitStatus name: 'test', state: 'pending'
               echo 'test step goes here'
               echo "---------------------------------- unit test------------------------------------"
               echo "run the app bare metal"
               sh "python3 weather/gunicorn_deploy/app.py&"
               echo "test the app bare metal"
               sh "python3 weather/tests/unit_test_weather.py"
               echo "close the app bare metal"
               sh "pkill -9 python3"
               echo " ---------------------------------- unit-test passed ----------------------------------"

               echo "smoke test and running build - in order to run selenium tests"
               sh "docker run -d --name eden_app -p 80:80 app:weather"

               echo "---------------------------------- running selenium testing----------------------------------"
               sh "python3 weather/tests/selenium_weather.py"
               echo " ---------------------------------- selenium tests passed ----------------------------------"

               sh "docker stop eden_app"
               sh "docker rm eden_app"

               updateGitlabCommitStatus name: 'test', state: 'success'

            }
       }

        stage('push-to-dockerhub')
        {
            steps
            {
                sh 'docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW'
                sh "docker tag app:weather edencoania/release:app-manual"//${env.JOB_NAME}${env.BUILD_NUMBER}"
                sh "docker tag nginx:weather edencoania/release:nginx-manual" //${env.JOB_NAME}${env.BUILD_NUMBER}"

                sh "docker push edencoania/release:app-manual" //${env.JOB_NAME}${env.BUILD_NUMBER}"
                sh "docker push edencoania/release:nginx-manual" //${env.JOB_NAME}${env.BUILD_NUMBER}"
                }
           }


       stage('deploy')
           {
                steps
                {
                script{
                    slackSend(color: '#00FF00', message: 'private aws ip of deploy is 172-31-18-254!')
                }
                    sh 'sudo chmod 600 ./weather/weather.pem'
                    sh 'sudo scp -o StrictHostKeyChecking=no -i ./weather/weather.pem weather/compose.yaml ubuntu@${target_ip_address}:/home/ubuntu/'


                    sh 'sudo ssh -o StrictHostKeyChecking=no -i "./weather/weather.pem" ubuntu@${target_ip_address} "sudo docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW"'

                    sh 'sudo ssh -o StrictHostKeyChecking=no -i "./weather/weather.pem" ubuntu@${target_ip_address}  "sudo docker-compose down && sudo docker pull edencoania/release:nginx-manual && sudo docker pull edencoania/release:app-manual"'


                    sh 'sudo ssh -o StrictHostKeyChecking=no -i "./weather/weather.pem" ubuntu@${target_ip_address}  "sudo docker-compose --env-file .env up --force-recreate -d"'
                }
           }
       }
       post
       {
            always
            {
                echo "always"
                sh "docker system prune -f"
            }
            success
            {
                script
                {
                    slackSend(color: '#00FF00', message: 'Build deployed successfully!')
                    slackSend(color: '#00FF00', message: "${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                }
            }
            unsuccessful
            {
               script{
                    slackSend(color: '#FF0000', message: 'Build failed!')
               }
            }
        }
        }
