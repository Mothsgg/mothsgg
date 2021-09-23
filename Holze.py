import discord
from discord.ext import commands
import datetime
from asyncio import sleep
import asyncio
from discord_components import DiscordComponents, Button, ButtonStyle
import youtube_dl
import os

client = commands.Bot( command_prefix = 'h.' )
client.remove_command("help")

@client.event

async def on_ready():
	print( 'Hozle - mothsgg connect' )

	await client.change_presence( status = discord.Status.online, activity = discord.Game( 'h.hozle - Odinoshka' ) )
	await sleep(15)
	await client.change_presence( status = discord.Status.online, activity = discord.Game( 'h.new - mothsgg' ) )

# Clear message
@client.command(aliases=['clear'])
async def purge(ctx, amount=11):
    if(not ctx.author.guild_permissions.manage_messages):
        await ctx.send('**Cannot run command! Requires:** ``Manage Messages``')
        return
    amount = amount+1
    if amount > 501:
        await ctx.send('**<:nom_869681325173526578:869681343519412265>:x: Можно удалить только до 500 сообщений, но не 1000 и выше..**')
    else: 
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'**<:Animeshka:873293654180126721> Очистка прошла успешла, удалено {amount} сообщений!**')

# embed

async def hozle( ctx ):
	emb = discord.Embed( title = '> Информация', description = '<a:omgtyanos:872913096866398279> Доброго времени суток, спасибо что вы выбрали нашего бота **Hozle**ᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ<:lovetyanoshka:872916813179125780> Наш бот преобладает очень много различных команд и функционала.ᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠᅠ <a:create_tyanoshka:872926311885209681> Наш сервер по общению: **[Вступить](https://discord.gg/FhZuyhDQAE)**ᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠ<a:create_tyanoshka:872926311885209681> Бот используется только на сервере **Odinoshka!**', colour = discord.Color.blue() )
	emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
	emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
	emb.set_image( url = 'https://share.creavite.co/jgIVK042z2RSX9uH.gif' )

	await ctx.send( embed = emb  )

# embed2

@client.command( pass_context = True )

async def new( ctx ):
	emb = discord.Embed( title = '> Новое о боте', description = 'Доброго времени суток, этот бот сделан для сервера ``Odinoshka`` больше ни к какому, на нем проводяться обновления раз в месяц как в неделю, из-за того что начались школьные поры я попытаюсь обновлять его чаще, добавлю: Экономику, мини игры, и другие плюшки. ', colour = discord.Color.orange() )
	emb.set_image( url = 'https://share.creavite.co/iYFPCtm5UaIUF2Gh.gif' )

	await ctx.send( embed = emb  )

# embed 3
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def test( ctx ):
	emb = discord.Embed( title = '> Новая функция бота', description = 'Добавил новую функцию для бота и сервера за одно, чтобы вы отслеживали обновления, хотя кому это надо?...))', colour = discord.Color.orange() )
	emb.set_image( url = 'http://images.vfl.ru/ii/1632232848/f5c53406/35949567.png' )

	await ctx.send( embed = emb  )

# embed 3
@client.command( pass_context = True )

async def Connection( ctx ):
	emb = discord.Embed( title = '> Связи с владельцем', description = 'Доброго времени суток, скорее всего вы ввели эту команду для того чтобы связаться с владельцем сервера, и так вот связи:', colour = discord.Color.orange() )
	emb.set_image( url = 'https://data.whicdn.com/images/250572398/original.gif' )
	emb.add_field(name='Telegram', value=f'[**₊˚Перейти₊˚**](https://t.me/m0thss)')
	emb.add_field(name='instagram', value=f'[**₊˚Перейти₊˚**](https://www.instagram.com/m0thsssy/?hl=ru)')
	emb.add_field(name=':D', value=f'**:chocolate_bar: Соблюдайте наши правила сервера, чтобы не получать наказания на нашем сервере.**')
	emb.add_field(name='Заметка', value=f'**Посмотреть такую же панельку вы можете в <#870365601619664996>**')
	await ctx.send( embed = emb  )

# music bot

import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl

from random import choice

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}!  Ready to jam out? See `?help` command for details!')

@client.command(name='ping', help='This command returns the latency')
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency: {round(client.latency * 1000)}ms')

@client.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
    responses = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
    await ctx.send(choice(responses))

@client.command(name='die', help='This command returns a random last words')
async def die(ctx):
    responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
    await ctx.send(choice(responses))

@client.command(name='credits', help='This command returns the credits')
async def credits(ctx):
    await ctx.send('Made by `RK Coding`')
    await ctx.send('Thanks to `DiamondSlasher` for coming up with the idea')
    await ctx.send('Thanks to `KingSticky` for helping with the `?die` and `?creditz` command')

@client.command(name='creditz', help='This command returns the TRUE credits')
async def creditz(ctx):
    await ctx.send('**No one but me, lozer!**')

@client.command(name='play', help='This command plays music')
async def play(ctx, url):
    if not ctx.message.author.voice:
        await ctx.send("**❌ Вы не подключены к войс каналу!**")
        return

    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**:notes:** {}'.format(player.title))

@client.command(name='stop', help='This command stops the music and makes the bot leave the voice channel')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

# reactik
@client.command( pass_context = True )

async def hug( ctx ):
    emb = discord.Embed( title = '> Обнимашки :3', description = 'Доброго времени суток, этот бот сделан для сервера ``Odinoshka`` больше ни к какому, на нем проводяться обновления раз в месяц как в неделю, из-за того что начались школьные поры я попытаюсь обновлять его чаще, добавлю: Экономику, мини игры, и другие плюшки. ', colour = discord.Color.orange() )
    emb.set_image( url = 'https://i.gifer.com/UxvR.gif' )

# avatar
@client.command()
async def avatar(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author
    
    icon_url = member.avatar_url 
 
    avatarEmbed = discord.Embed(title = f"Аватар {member.name}", color = 0xFFA500)
 
    avatarEmbed.set_image(url = f"{icon_url}")
 
    avatarEmbed.timestamp = ctx.message.created_at 
 
    await ctx.send(embed = avatarEmbed)

# say
@client.command(case_insensitive=True)
async def say(ctx, saymsg=None):
    if saymsg==None:
        return await ctx.send("**Вы не написали аргументы. Пример: h.say ТыКрутой**")
     
    sayEmbed = discord.Embed(title=f"Сообщение от бота", color = discord.Color.orange(), description=f"{saymsg}")
    sayEmbed.timestamp = ctx.message.created_at
    
    await ctx.send(embed = sayEmbed)

# token
token = open( 'Token.txt', 'r' ).readline()

client.run( token )