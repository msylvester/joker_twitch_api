import asyncio
from twitchio.http import TwitchHTTP
from token_setup import load_tokens

# Path to the .env file
TOKEN_FILE_PATH = "/Users/mikress/tokens_nov_21/.env"

async def fetch_user_videos(twitch_http, user_id):
    """
    Fetch video information for a given user ID.

    :param twitch_http: Instance of TwitchHTTP.
    :param user_id: The ID of the user to fetch videos for.
    :return: A list of dictionaries containing video titles and published dates.
    """
    try:
        # Fetch videos for the user
        response = await twitch_http.get_videos(user_id=user_id)
        videos = [
            {"title": video.get("title"), "published_at": video.get("published_at")}
            for video in response
        ]

        print(f"Total videos fetched: {len(videos)}")
        return videos
    except Exception as e:
        print(f"Error fetching videos: {e}")
        return []


async def main():
    """
    Main function to initialize the TwitchHTTP client and fetch user videos.
    """
    # Load tokens
    tokens = load_tokens(TOKEN_FILE_PATH)

    # Initialize the TwitchHTTP client
    twitch_http = TwitchHTTP(
        client=None,  # Replace with a TwitchIO Client instance if available
        api_token=tokens["TWITCH_ACCESS_TOKEN"],
        client_id=tokens["TWITCH_CLIENT_ID"],
        client_secret=tokens["TWITCH_CLIENT_SECRET"],
    )

    # User ID to fetch videos for
    user_id = 655726077

    # Fetch and display video info
    videos = await fetch_user_videos(twitch_http, user_id)
    print("Videos:", videos)

    # Ensure the session is closed
    if twitch_http.session:
        await twitch_http.session.close()


if __name__ == "__main__":
    asyncio.run(main())
