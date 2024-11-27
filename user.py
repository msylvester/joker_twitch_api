# models/user.py
from datetime import datetime, timezone

class User:
    def __init__(self, db):
        self.db = db
        self.collection = db.users

    def create_user(self, user_data):
        vod_titles = [video['vod_titles'] for video in user_data.get('videos', [])]
        vod_ids = [video['vod_ids'] for video in user_data.get('videos', [])]

        document = {
            'user_id': user_data.get('user_id'),
            'title': user_data.get('title'),
            'vod_titles': vod_titles,
            'date_entered': datetime.now(timezone.utc),
            'vod_ids': vod_ids,
        }
        return self.collection.insert_one(document)

    def get_user(self, user_id):
        return self.collection.find_one({'user_id': user_id})

    def update_user_videos(self, user_id, video_id):
        return self.collection.update_one(
            {'user_id': user_id},
            {'$push': {'video_ids': video_id}}
        )

    def get_all_users(self):
        """Retrieve all users from the database"""
        try:
            users = list(self.collection.find({}))
            print(f"Retrieved {len(users)} users from database")
            return users
        except Exception as e:
            print(f"Error retrieving users: {e}")
            return []