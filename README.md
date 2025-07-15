# 📢 tg-freepost-bot — Turn Your Telegram Channel into a Public Imageboard

A Telegram bot script designed to transform a channel into a lightweight imageboard. Users can post content via the bot, and each post links to a discussion thread for community interaction.

> ⚠️ **Warning:** Telegram flagged this project as "malicious" and deleted the test bot during development. See [Important Note](#️-important-note) below for details.

---

## 📚 Table of Contents

- [📢 tg-freepost-bot — Turn Your Telegram Channel into a Public Imageboard](#-tg-freepost-bot--turn-your-telegram-channel-into-a-public-imageboard)
  - [📚 Table of Contents](#-table-of-contents)
  - [🧠 Project Overview](#-project-overview)
    - [Key Features:](#key-features)
  - [⚠️ Important Note](#️-important-note)
  - [🐍 Installation](#-installation)
    - [Requirements](#requirements)
    - [1. Clone the repo](#1-clone-the-repo)
    - [2. Install dependencies](#2-install-dependencies)
    - [3. Set up environment](#3-set-up-environment)
    - [4. Run the bot](#4-run-the-bot)
  - [🐳 Docker (Optional)](#-docker-optional)
  - [💬 Usage](#-usage)
  - [🛠️ Contributing](#️-contributing)
  - [📜 License](#-license)
  - [🙏 Acknowledgments](#-acknowledgments)

---

## 🧠 Project Overview

**tg-freepost-bot** is a Python-based backend that lets Telegram subscribers submit posts (text, images, files) to a channel via a bot. Posts appear in the channel along with a reply link, enabling discussion in an associated group — similar in spirit to imageboards or anonymous forums.

### Key Features:
- ✅ Post text, photos, or documents through the bot  
- ✅ Automatically forwards user submissions to a channel  
- ✅ Bilingual tag selection system (English + Russian)  
- ✅ Supports inline tag-based categorization of content  
- ✅ Sends a welcome message explaining the rules and usage  
- 🐳 Docker-ready (files prepared, but not tested in deployment)

---

## ⚠️ Important Note

> This project was **only tested locally** and never deployed to a production cloud server.  
>  
> Unfortunately, Telegram permanently banned the test bot and issued the following warning:

> _“You have created a malicious bot that was banned on Telegram. Please note that creating abusive bots (for example, bots for spamming and interfering with communication in groups) may lead to your account being terminated...”_

This bot is **not malicious**, does not send unsolicited messages, and was only used for controlled testing. However, it seems Telegram is highly sensitive to automated posting bots that allow public input.  
Use this project **at your own risk**.

---

## 🐍 Installation

### Requirements
- Python 3.11+
- `python-telegram-bot==20.8`
- `python-dotenv`
- Docker (optional, for containerized deployment)

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/tg-freepost-bot.git
cd tg-freepost-bot
````

### 2. Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Set up environment

Create a `.env` file in the root directory:

```env
BOT_TOKEN=your_bot_token_here
CHANNEL_USERNAME=@your_channel_name
```

### 4. Run the bot

```bash
python bot.py
```

---

## 🐳 Docker (Optional)

The repo includes a `Dockerfile` and `docker-compose.yml` for future deployment.
Although untested, this setup aims to make it easy to run the bot on a cloud instance or a Raspberry Pi:

```bash
docker-compose up -d
```

> Note: The container is stateless — no user uploads are stored on disk. Logs go to stdout.

---

## 💬 Usage

1. Create a Telegram channel and link a discussion group to it.
2. Create a bot via [@BotFather](https://t.me/BotFather) and get the token.
3. Invite the bot to the discussion group and give it permission to read messages.
4. Share the bot with subscribers. When they message the bot:

   * A bilingual welcome message explains how it works.
   * They select a tag (e.g., “📰 News / Новости”).
   * Their message is posted to the channel with the appropriate tags.
   * A reply thread opens in the discussion group.

---

## 🛠️ Contributing

This project is a rough prototype with lots of potential directions. Feel free to fork, improve, or use it as a base for your own experiments.

If you manage to successfully deploy or improve it, **let me know** — message me at `[your contact info here]`.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

This bot was developed using a combination of human effort and **AI assistance via ChatGPT**.
Some of the code was refined or generated with help from OpenAI tools.


> *Built as an experiment. Use responsibly.*



[def]: #key-features
[def2]: #-table-of-contents