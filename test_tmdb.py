
import os
import httpx
from dotenv import load_dotenv
import asyncio

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

async def test():
    print(f"Testing API Key with httpx: {API_KEY}")
    try:
        url = "https://api.themoviedb.org/3/configuration"
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(url, params={"api_key": API_KEY})
        print(f"Status Code: {r.status_code}")
        if r.status_code == 200:
            print("Success! API Key is valid.")
        else:
            print(f"Error: {r.text}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    asyncio.run(test())
