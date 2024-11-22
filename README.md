# Twitch Software and Game Development Stream Fetcher

This project fetches and lists live stream titles for the "Software and Game Development" category on Twitch. It uses the Twitch API and `twitchio` library for interacting with the Twitch platform.

## Prerequisites

Before running this application, ensure you have the following:

- Python 3.8 or later
- [Pixi](https://pypi.org/project/pixi/) for environment management
- A Twitch Developer account and an access token
- `.env` file containing your Twitch API access token

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a Pixi environment:

    ```bash
    pixi new twitch-fetcher-env
    pixi activate twitch-fetcher-env
    ```

3. Install the required dependencies:

    ```bash
    pip install twitchio python-dotenv
    ```

4. Create an `.env` file to securely store your Twitch API access token. Place the file in the specified directory:

    ```bash
    echo "TWITCH_ACCESS_TOKEN=<your-twitch-access-token>" > /Users/mikress/tokens_nov_21/.env
    ```

## Usage

1. Update the `token_file_path` variable in the script to point to the location of your `.env` file:

    ```python
    token_file_path = "/Users/mikress/tokens_nov_21/.env"
    ```

2. Run the script:

    ```bash
    python <script-name>.py
    ```

3. The script will fetch live streams in the "Software an
# joker_twitch_api
This repo is used to build the llm with joker's IP. SSHHH DONT TELL 🤐
