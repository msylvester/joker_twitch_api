import asyncio
from twitchio.client import Client
from dotenv import load_dotenv
import sys
from load_env import load_tokens
import os

token_file_path = sys.argv[1] if len(sys.argv) > 1 else "./.env"

try:
    load_dotenv(token_file_path)
except Exception:
    try:
        load_tokens(token_file_path)
    except Exception as e:
        print(f"Error loading tokens: {e}")
        exit()

TWITCH_TOKEN = os.getenv("TWITCH_ACCESS_TOKEN")
if not TWITCH_TOKEN:
    print("Error: Missing Twitch access token.")
    exit()

class TwitchAPI(Client):
    async def get_software_and_dev_titles(self):
        try:
            categories = await self.search_categories("Software and Game Development")
            if not categories:
                return

            category_id = categories[0].id
            streams = await self.fetch_streams(game_ids=[category_id])
            if not streams:
                return

            for stream in streams:
                print(f"- {stream.title} by {stream.user}")
        except Exception as e:
            print(f"An error occurred: {e}")

async def main():
    client = TwitchAPI(token=TWITCH_TOKEN)
    await client.get_software_and_dev_titles()

if __name__ == "__main__":
    asyncio.run(main())
