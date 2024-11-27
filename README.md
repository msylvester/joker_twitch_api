

# 🎥 Twitch Software and Game Development Stream Fetcher

This project fetches all the streamers in the software and dev category who are live and populates a mongodb database.


## 🛠️ Prerequisites

Before running this application, ensure you have the following:

- 🐍 Python 3.12 or later
- ⚙️ [Pixi](https://pypi.org/project/pixi/) for environment management
- 🎮 A Twitch Developer account and an access token
- 📄 A `.env` file containing your Twitch API access token

## 📦 Installation

1. Create and activate a Pixi environment:

    ```bash
    pixi new twitch-fetcher-env
    pixi activate twitch-fetcher-env
    ```:x:x
    

2. Install the required dependencies from the `.toml` file:

    ```bash
    pixi install
    ```

3. Create an `.env` file to securely store your Twitch API access token:

    ```bash
    echo "TWITCH_TOKEN=<your-twitch-access-token>" > .env
    ```

## 🚀 Usage

1. Run the script:

    ```bash
    python twitch_video_service.py
    ```

2. The script will fetch live streams in the "Software and Game Development" category and display their titles.

---
## Follow me on twitch [krystal_mess323](https://www.twitch.tv/krystal_mess323)  💯
<!-- 
# 🃏 Joker Twitch API

This repository is used to build LLMs leveraging Joker's intellectual property. 🤐 **Please handle with confidentiality.** -->
