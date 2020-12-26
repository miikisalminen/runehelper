import os
import discord
import scraper as sc

TOKEN = "SECRET TOKEN"

client = discord.Client()

@client.event

async def on_message(message):

# wiki linker
	if message.content.startswith ("!wiki"):
		response = sc.wiki(message.content.replace("!wiki ",""))
		print(response)
		await message.channel.send(response)

# GE Price check
	if message.content.startswith ("!price"):
		response = sc.price(message.content.replace("!price ",""))
		await message.channel.send(response)

# HiScore check




#NeededToLevel

#!ranks



client.run(TOKEN)