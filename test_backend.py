
import httpx
import asyncio

async def test_backend():
    print("Testing Backend Connectivity...")
    
    # 1. Health check
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            r = await client.get("http://127.0.0.1:8000/health")
            print(f"Health Check: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"Health Check Failed: {e}")
        return

    # 2. TMDB Proxy check (Home feed)
    try:
        print("\nTesting Home Feed (TMDB Proxy)...")
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.get("http://127.0.0.1:8000/home?category=popular&limit=5")
            print(f"Home Feed Status: {r.status_code}")
            if r.status_code == 200:
                print("Success! Backend can reach TMDB.")
                print(f"Items: {len(r.json())}")
            else:
                print(f"Error: {r.text}")
    except Exception as e:
        print(f"Home Feed Test Failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_backend())
