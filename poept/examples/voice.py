from poept import PoePT

bot = PoePT()
bot.login("<email>@gmail.com")

# speech from mic
prompt = bot.livevoice(10)
response = bot.ask("Sage", prompt)
print("Answer:", response)


# speech from recorded file
prompt = bot.filevoice("speech.wav")
response = bot.ask("Sage", prompt)
print("Answer:", response)


bot.close()
