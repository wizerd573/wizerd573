from discord.ext import commands
# from discord.ext.commands import bot
# from discord.ext.commands import bot
from discord import FFmpegPCMAudio, channel, guild
from youtube_dl import YoutubeDL
from discord.utils import get

TOKEN = "OTAwMDgxMjcwNjQ0Njc0NjAx.YW8IAQ.c7dHcCGvRe1_poHQjRqk6wbKESaw"

robot = commands.Bot(command_prefix="//")

@robot.event
async def on_ready():
   print(f"{robot.user} Bot is Ready")

@robot.command()
async def Gaan(ctx, url):
   YTDL_OPTIONS = {
      "format" : "bestaudio/best",
      "quit" : True,
      "noplaylist" : True
   }

   FFMPEG_OPTIONS = {
      'before_options' : '-reconnect 1 -reconnect_stream 1 -reconnect_deley_max 5',
      'options' : "-vn"
   }

   channel = ctx.message.author.voice.channel
   voice = get(robot.voice_clients, guild=ctx.guild)

   if voice and voice.is_connected():
      await voice.move_to(channel)
   else:
      voice = await channel.connect()

   if not voice.is_playing():
      with YoutubeDL(YTDL_OPTIONS) as ydl:
         info = ydl.extract_info(url, download=False)
      URL = info.get("url")
      voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
      voice.is_playing()
      await ctx.send("Music Playing")
   else:
      await ctx.send("Music already Playing")
      return

robot.run(TOKEN)
