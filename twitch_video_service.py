# services/twitch_video_service.py
import os
import sys
import asyncio
from twitchio.http import TwitchHTTP
from datetime import datetime, timezone

# Set up the correct path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

# Absolute imports
from models.user import User
from config.database import connect_mongodb

class TwitchVideoService:
    def __init__(self, user_model, token_file_path):
        self.user_model = user_model
        self.token_file_path = token_file_path
        self.twitch_http = None

    async def init_twitch(self):
        self.twitch_http = TwitchHTTP(
            client=None,
            api_token=os.getenv("TWITCH_ACCESS_TOKEN"),
            client_id=os.getenv("TWITCH_CLIENT_ID"),
            client_secret=os.getenv("TWITCH_CLIENT_SECRET"),
        )

    async def get_user_videos(self, user_id):
        """Retrieve videos for a specific user"""
        try:
            response = await self.twitch_http.get_videos(user_id=user_id)
            return [
                {
                    "vod_titles": video.get("title"),
                    "published_at": video.get("published_at"),
                    "vod_ids": video.get("id")
                }
                for video in response
            ]
        except Exception as e:
            print(f"Error getting videos for user {user_id}: {e}")
            return []

    async def get_sd_streamers(self):
        """Retrieve Software & Development streamers"""
        try:
            response = await self.twitch_http.get_streams(game_ids=["1469308723"])
            return response
        except Exception as e:
            print(f"Error getting Software & Development streamers: {e}")
            return []

    async def update_db(self):
        """Update MongoDB with streamer and video data"""
        await self.init_twitch()

        try:
            streamers = await self.get_sd_streamers()
            for streamer in streamers:
                user_id = streamer.get("user_id")

                if self.user_model.get_user(user_id):
                    print(f"User {user_id} exists, skipping...")
                    continue

                videos = await self.get_user_videos(user_id)

                user_data = {
                    "user_id": user_id,
                    "username": streamer.get("user_name"),
                    "title": streamer.get("title"),
                    "videos": videos,
                    "stream_status": "live",
                    "date_entered": datetime.now(timezone.utc)
                }

                self.user_model.create_user(user_data)
                print(f"Added user: {streamer.get('user_name')}")

            if self.twitch_http.session:
                await self.twitch_http.session.close()
        except Exception as e:
            print(f"Error in update_db: {e}")
            if self.twitch_http.session:
                await self.twitch_http.session.close()

    def show_users(self):
        """Display users and their videos in a formatted table"""
        users = self.user_model.get_all_users()
        print("\nSoftware & Development Streamers and Their Videos:")
        for user in users:
            print(f"\nUsername: {user['username']}")
            print(f"Stream Status: {user['stream_status']}")
            print("Recent Videos:")
            for video in user.get('videos', []):
                print(f"  • {video['vod_titles']}")
                print(f"    Published: {video['published_at']}")
            print("-" * 50)

if __name__ == "__main__":
    import asyncio
    from config.database import connect_mongodb

    async def main():
        # Connect to MongoDB
        db = connect_mongodb()
        if db is None:
            print("Failed to connect to database.")
            return

        # Initialize models and services
        user_model = User(db)
        token_file_path = os.getenv("TWITCH_TOKEN_FILE", "./tokens.env")
        video_service = TwitchVideoService(user_model, token_file_path)

        # Update database
        await video_service.update_db()

        # Show results
        video_service.show_users()

    asyncio.run(main())
