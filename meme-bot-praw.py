import discord
import asyncpraw
import random

# Replace with your bot token
TOKEN = 'MTQwMjQ1Nzc1NjIxMjEzNzk5NA.GMtRfw.NkHLgcFb96hmtkSA9wnDc1dva8pcLxKDRqR_DA'

# Reddit API credentials (replace with your own)
REDDIT_CLIENT_ID = 'Ne7TwTrNBcb05Uh7133ZvQ'
REDDIT_CLIENT_SECRET = 'ID-HmLMGOlo5sMrPXK57Q2IZinC_-A'
REDDIT_USER_AGENT = 'discord-meme-bot/0.1 by hello-world123456789'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



# Lazy initialization for asyncpraw Reddit instance
reddit = None

async def get_relevant_meme(query):
    global reddit
    if reddit is None:
        import asyncpraw
        reddit = asyncpraw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
    # Search for memes in popular meme subreddits
    subreddits = ['memes', 'dankmemes', 'funny', 'wholesomememes']
    subreddit = await reddit.subreddit('+'.join(subreddits))
    memes = []
    async for post in subreddit.search(query, sort='relevance', time_filter='month', limit=20):
        if not post.stickied and post.url.endswith(('jpg', 'jpeg', 'png', 'gif')):
            memes.append(post)
    if memes:
        meme = random.choice(memes)
        return meme.title, meme.url
    else:
        return None, None

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    query = message.content.strip()
    meme_title, meme_url = await get_relevant_meme(query)
    if meme_url:
        await message.channel.send(f"**{meme_title}**\n{meme_url}")
    else:
        await message.channel.send("Couldn't find a relevant meme. Try another message!")

client.run(TOKEN)
