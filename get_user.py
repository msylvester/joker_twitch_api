import asyncio
from twitchio.http import TwitchHTTP
from token_setup import load_tokens

# Path to the .env file
TOKEN_FILE_PATH = "/Users/mikress/tokens_nov_21/.env"

async def fetch_user_info(twitch_http, user_id):
    """
    Fetch user information given a user ID.
    
    :param twitch_http: Instance of TwitchHTTP.
    :param user_id: The ID of the user to fetch.
    :return: User information as a dictionary.
    """
    try:
        response = await twitch_http.get_users(ids=[user_id], logins=[])
        #response = await twitch_http.get_videos(user_id='655726077')
        return response
    except Exception as e:
        print(f"Error fetching user info: {e}")
        return None


async def main():
    # Load tokens
    tokens = load_tokens(TOKEN_FILE_PATH)

    # Initialize the TwitchHTTP client
    twitch_http = TwitchHTTP(
        client=None,  # Replace with a TwitchIO Client instance if available
        api_token=tokens["TWITCH_ACCESS_TOKEN"],
        client_id=tokens["TWITCH_CLIENT_ID"],
        client_secret=tokens["TWITCH_CLIENT_SECRET"],
    )

    # The ID of the user to fetch
    user_id = 28254552

    # Fetch and display user info
    user_info = await fetch_user_info(twitch_http, user_id)
    print("User Info:", user_info)

    # Ensure the session is closed
    if twitch_http.session:
        await twitch_http.session.close()


if __name__ == "__main__":
    asyncio.run(main())
