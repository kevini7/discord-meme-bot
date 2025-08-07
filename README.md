# Discord Meme Bot

A simple Discord bot that sends random memes when trigger words are detected in chat. Built with Python and deployable on Railway.

## Features
- Responds to messages containing trigger words (e.g., meme, lol, joke)
- Fetches memes from [meme-api.com](https://meme-api.com/)
- Easy deployment to Railway

## Setup

### 1. Requirements
- Python 3.8+
- Railway account
- Discord bot token

### 2. Installation

Install dependencies:
```
pip install discord.py requests
```

### 3. Environment Variables
Set your Discord bot token as an environment variable named `TOKEN` in Railway's dashboard.

### 4. Files
- `meme-bot.py`: Main bot code
- `requirements.txt`: Python dependencies
- `Procfile`: Tells Railway how to start the bot

### 5. Deployment (Railway)
1. Push your code to Railway
2. Add the `TOKEN` environment variable
3. Railway will install dependencies and start your bot automatically

## Example Usage
Send a message like `meme` or `lol` in your Discord server. The bot will reply with a random meme.

## Contributing
Pull requests are welcome!

## License
MIT
