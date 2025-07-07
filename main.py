import httpx

cities = {
    "chicago": {"lat": 41.8781, "lon": -87.6298},
    "new york": {"lat": 40.7128, "lon": -74.0060},
    "los angeles": {"lat": 34.0522, "lon": -118.2437}
}
select_city = input("Select a city (Chicago, New York, Los Angeles): ").lower()

weather_check_url = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")
geocode_url = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")

if select_city in cities:
    lat = cities[select_city]["lat"]
    lon = cities[select_city]["lon"]
    response = httpx.get(weather_check_url)
    weather = response.json()
    temperature = weather["current_weather"]["temperature"]
    windspeed = weather["current_weather"]["windspeed"]
    print(f"The temperature in {select_city} is {temperature}°C")
    print(f"The windspeed in {select_city} is {windspeed} m/s")
else:
    print("Invalid city")