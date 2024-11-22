import asyncio
from twitchio.client import Client
from dotenv import load_dotenv
'''

"/Users/mikress/tokens_nov_21/.env"'''
import sys
from dotenv import load_dotenv
import os

# Allow user to pass a custom path or use a default path
token_file_path = sys.argv[1] if len(sys.argv) > 1 else "./.env"

# Load environment variables
try:
    load_dotenv(token_file_path)
    print("Tokens loaded successfully.")
except Exception as e:
    print(f"Error loading tokens: {e}")
    exit()

# Retrieve the access token
TWITCH_TOKEN = os.getenv("TWITCH_ACCESS_TOKEN")
if not TWITCH_TOKEN:
    print("Error: Missing Twitch access token.")
    exit()

# Validate environment variables
if not TWITCH_TOKEN:
    print("Error: Missing Twitch access token.")
    exit()

class TwitchAPI(Client):
    async def get_software_and_dev_titles(self):
        """Fetch live stream titles for the 'Software and Game Development' category."""
        try:
            # Search for the 'Software and Game Development' category
            categories = await self.search_categories("Software and Game Development")

            if not categories:
                print("No categories found.")
                return

            category_id = categories[0].id
            print(f"Category found: {categories[0].name} (ID: {category_id})")

            # Fetch streams under the category
     
            streams = await self.fetch_streams(game_ids=[category_id])
  
            if not streams:
                print("No live streams found.")
                return

            # Print titles of live streams
            print("Live streams in 'Software and Game Development':")
            for stream in streams:
                print(f"- {stream.title} by {stream.user}")

        except Exception as e:
            print(f"An error occurred: {e}")

async def main():
    client = TwitchAPI(token=TWITCH_TOKEN)
    await client.get_software_and_dev_titles()

if __name__ == "__main__":
    asyncio.run(main())
