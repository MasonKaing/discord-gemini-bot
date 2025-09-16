# discord-gemini-bot
Learning Project: A Python Discord bot that answers questions and DMs users using Gemini AI

⚠️ Note: This bot uses Google’s Gemini API. You need your own API key to run it.  
Please follow Google’s API Terms of Service when using this project.

Discord Bot with Gemini API

A simple Discord bot built with Python, discord.py, and Google’s Gemini API. \
This project started as an experiment to learn how to create a discord bot, but it evolved into a small AI-powered assistant that can answer questions, write prompts, and send those to private DMS.

Features
- AI responses using Google’s Gemini API
- Custom commands like ^ask for question answering
- Ability to send DMs to other users. (^dm and ^aidm)

Tech Stack
[Python 3.x](https://www.python.org)
[discord.py](https://discordpy.readthedocs.io/en/stable)
[Google Generative AI (Gemini)](https://ai.google.dev)

Getting Started
1. Clone the repo
git clone https://github.com/<your-username>/<your-repo-name>.git \
cd <your-repo-name>

2. Install dependencies
pip install -r requirements.txt

3. Add your tokens
Create a .env file in the root folder: \
This is where if you haven't to get your own API keys. \
DISCORD_TOKEN=your-discord-bot-token-here \
GEMINI_API_KEY=your-gemini-api-key-here

4. Invite the bot to discord server

5. Run the bot
python main.py

Commands

^hello (say hello to the bot.) \
^dm @user "msg" (DM the user mentioned the message) \
^aidm @user "prompt" (DM the user mentioned a AI generated paragraph based off the prompt) \
^ask "question" (Ask Gemini a question and receive an answer) \ 
^poll "question for poll" (Creates a poll using reaction system) \

Hardcoded Commands (won't work for you, mainly for my testing purposes) \
^assign (assigns the author a role called "stinky" if already made in server) \
^remove (removes the "stinky" role) \
^secret (if user has stinky role it will work, if not bot will say no perms.) \

Event reactions

If bot is ready, it will print that it is ready \
If user joins server, it will dm user "You stink @user" \
If message is sent, it will check for the word "poo" and if it occurs it will delete the message \

That's all \
use this for whatever
