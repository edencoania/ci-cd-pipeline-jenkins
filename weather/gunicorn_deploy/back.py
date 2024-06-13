import datetime
import requests
#API_Key="d5bb8e5e422846f1bba142931230511"
API_Key = "FWGQHHB3JCJ8L4MM8EUNRDPYQ"

def get_week_forecast(city):
    start_date = datetime.date.today()
    week_ahead = start_date + datetime.timedelta(days=7)
    if city == "":
        city = "tel aviv"
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + city + "/" + str(
        start_date) + "/" + str(week_ahead) + "?key=" + API_Key
    response = requests.get(url)
    data = response.json()
    result = {"location": {"resolvedAddress": data['resolvedAddress']}, "forecast": []}
    for day in data['days']:
        cut = {
            "date": day['datetime'],
            "max day": int((day['tempmax']-32)*5/9),
            "min night": int((day['tempmin']-32)*5/9),
            "humidity": day['humidity'],
        }
        result['forecast'].append(cut)
    return result
