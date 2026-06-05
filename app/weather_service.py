import httpx

async def get_weather(city:str):
    async with httpx.AsyncClient() as client:
        geo_url = (
            f"https://geocoding-api.open-meteo.com/v1/search"
            f"?name={city}&count=1"
        )
        geo_response= await client.get(geo_url)
        geo = geo_response.json()
        if "results" not in geo:
            return None
        latitude = geo["results"][0]["latitude"]
        longitude = geo["results"][0]["longitude"]
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            f"&current_weather=true"
        )
        weather_respounse = await client.get(weather_url)
        weather = weather_respounse.json()

        return {
            "city": city.title(),
            "temperature": weather["current_weather"]["temperature"],
            "windspeed": weather["current_weather"]["windspeed"]
        }
