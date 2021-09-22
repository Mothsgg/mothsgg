import discord
from discord.ext import commands
import datetime
from asyncio import sleep
import asyncio
from discord_components import DiscordComponents, Button, Button

client = commands.Bot( command_prefix = 'h.' )
client.remove_command("help")

@client.event

async def on_ready():
	print( 'Hozle - mothsgg connect' )

<<<<<<< HEAD
	await client.change_presence( status = discord.Status.online, activity = discord.Game( 'h.hozle - Odinoshka' ) )
	await sleep(15)
	await client.change_presence( status = discord.Status.online, activity = discord.Game( 'h.new - mothsgg' ) )
=======
	await client.change_presence( status = discord.Status.online, activity = discord.Game( '!!Hozle' ) )
>>>>>>> c1ba24bed7df66a45257b135d732babc919de114

# Clear message
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

<<<<<<< HEAD
async def clear( ctx, amount = 10000 ):
=======
async def clear( ctx, amount = 10000000 ):
>>>>>>> c1ba24bed7df66a45257b135d732babc919de114
	await ctx.channel.purge( limit = amount )

# embed

@client.command( pass_context = True )

<<<<<<< HEAD
async def Holze( ctx ):
	emb = discord.Embed( title = '>Информация', description = '', colour = discord.Color.blue() )
=======
async def Hozle( ctx ):
	emb = discord.Embed( title = '> Информация', description = '<a:omgtyanos:872913096866398279> Доброго времени суток, спасибо что вы выбрали нашего бота **Hozle**ᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ<:lovetyanoshka:872916813179125780> Наш бот преобладает очень много различных команд и функционала.ᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠᅠ <a:create_tyanoshka:872926311885209681> Наш сервер по общению: **[Вступить](https://discord.gg/FhZuyhDQAE)**ᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠᅠ ᅠ<a:create_tyanoshka:872926311885209681> Бот используется только на сервере **Odinoshka!**', colour = discord.Color.blue() )
>>>>>>> c1ba24bed7df66a45257b135d732babc919de114
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

# token
token = open( 'Token.txt', 'r' ).readline()

client.run( token )