# Importing discord.py thing
# also taking the discord.ext from that as well
# logging is a normal python thing - dotenv is to keep stuff secure not hardcoded
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import google.generativeai as genai
import os

#dotenv is secure to keep stuff private
load_dotenv()
discordToken = os.getenv("DISCORD_TOKEN")
geminiToken = os.getenv("GEMINI_TOKEN")


#creating handler for files. File name discord log mode w means writing
handler = logging.FileHandler(filename="Discord Bot\discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default() #discord intents refer to discord.py
intents.message_content = True
intents.members = True

#genai for token to work and establish model
genai.configure(api_key=geminiToken)
model = genai.GenerativeModel("gemini-2.5-flash")

#make bot and have a command prefix with intents
bot = commands.Bot(command_prefix="^", intents=intents)

stinky_role = "stinky"

#bot will respond to these events
#bot is ready to use will print in terminal
@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

#when a member joins send msg
@bot.event
async def on_member_join(member):
    await member.send(f"You stink {member.name}")

#when certain word spotted delete | Filter system
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "poo" in message.content.lower().split():
        await message.delete()
        await message.channel.send(f"{message.author.mention} don't do that.")
        
    await bot.process_commands(message) #you need this for the bot to 
    #process the rest of the commands since we override it when doing this message event

#this will make commands
@bot.command()
#ctx = context
async def hello(ctx): #^hello
    await ctx.send(f"Hello {ctx.author.mention}!")

#this is how to assign roles but with a role variable in code
@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=stinky_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} is now assigned to {stinky_role}")
    else:
        await ctx.send("Role doesn't exist")

#command to add designated role
@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=stinky_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} is now removed from {stinky_role}")
    else:
        await ctx.send("Role doesn't exist")

#Examples of commands that need a role to use
@bot.command()
@commands.has_role(stinky_role)
async def secret(ctx):
    await ctx.send("Welcome to the club!")
    
@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You do not have perms")

#MAKE BOT DM USER WITH YOUR MSG
@bot.command()
async def dm(ctx, member: discord.Member, *, msg):
    try:
        await member.send(msg)
        await ctx.reply("DM'ed User!")
    except discord.Forbidden:
        await ctx.reply("Failed to DM user.")
    
#DM USING PROMPT AND AI    
@bot.command()
async def aidm(ctx, member: discord.Member, *, prompt):
    response = model.generate_content(f"Make a message using this prompt. Make sure you are under 2000 characters. {prompt}")
    answer = response.text
    try:
        await member.send(answer)
        await ctx.reply("Sent it!")
    except discord.Forbidden:
        await ctx.reply("Failed to send...")
    
#POLL COMMAND
@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="POLL", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")

# ASK COMMAND TAKE QUESTION OUTPUT ANSWER
@bot.command()
async def ask(ctx, *, question):
    thinking_message = await ctx.send("Thinking! 🤔 This might take a few moments...")
    response = model.generate_content(f"Respond in less than 2000 Characters. {question}")
    answer = response.text
    await thinking_message.edit(content=answer)
        
    
bot.run(discordToken, log_handler=handler, log_level=logging.DEBUG)