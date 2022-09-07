# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
import os
import random
from discord.utils import *
import discord.utils
import asyncio

TOKEN = os.environ.get('TOKEN')

a = "db!"

bot = commands.Bot(command_prefix="simbo!", intents=discord.Intents.all())
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    print("Я запущен!")

@bot.command()
async def hello(ctx):
    await ctx.message.delete()
    await ctx.send(embed=discord.Embed(title=ctx.author.name + " пришёл.", colour=discord.Color.green()))

@bot.command()
async def say(ctx,*,message=None):
    if message == None:
        await ctx.send("**Ошибка выполнения команды!**\nИспользование: simbo!say <текст>")
    await ctx.message.delete()
    await ctx.send(message)

@bot.command()
async def dm(ctx,*,message=None):
    await user.send(message)

@bot.command()
async def cat(ctx):
    d = random.choice(["https://cdn.discordapp.com/attachments/1016692299922677832/1016693709552762940/lolcats42.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693709867319327/lolcats43-728x532.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693710139961404/lolcats45-728x546.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693710483882075/lolcats46.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693710915915776/lolcats37.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693711318548480/lolcats38.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693711700250695/lolcats39-728x546.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693711977054218/lolcats40-728x546.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693711977054218/lolcats40-728x546.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693712220344401/lolcats41-728x660.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693053681041408/lolcats08-728x716.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693053362282597/lolcats07-728x741.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693053114810418/lolcats06-728x546.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693052804452452/lolcats05.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693052124966922/lolcats13-728x546.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016693052124966922/lolcats13-728x546.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016692856129327184/lolcats04.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016692855835734056/lolcats03-728x546.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016692855600861194/lolcats02.jpg", "https://cdn.discordapp.com/attachments/1016692299922677832/1016692642488266842/lolcats05.jpg", "https://bigpicture.ru/wp-content/uploads/2014/06/lolcats47.jpg"])

    await ctx.send(d)
@bot.command()
async def mute( ctx, member: discord.Member, time: int, *, reason="нарушение правил"):
    try:
        muted_role = discord.utils.get(ctx.message.guild.roles, name="Заглушен by Simbo")
    except:
        ctx.send("Пожалуйста, создайте мьют-роль с названием Заглушен by Simbo, и заберите у неё все права во всех каналах.")
    emb = discord.Embed(title=f":boom: Заглушено {member.name}!", description=f"По причине: {reason}\nЗаглушил: {ctx.author.mention}\nВремя: {time} минут", colour=discord.Color.green())
    await ctx.send(embed=emb)
    await member.send(embed=emb)
    await ctx.message.delete()
    muted_role = discord.utils.get(ctx.message.guild.roles, name="Заглушен by Simbo")
    await member.add_roles(muted_role)
    # Спим X секунд, перед тем как снять роль.
    await asyncio.sleep(time * 60) 
    # Снимаем роль замученного.
    await member.remove_roles(muted_role)
@bot.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, user: discord.Member, time="1", *, reason="невиновен"):
    muted_role = discord.utils.get(ctx.message.guild.roles, name="Заглушен by Simbo")
    ban = discord.Embed(title=f":boom: Разглушено {user.name}!", description=f"По причине: {reason}\nРазглушил: {ctx.author.mention}", colour=discord.Color.green())
    await ctx.channel.send(embed=ban)
    await user.send(embed=ban)
    await ctx.message.delete()
    await user.remove_roles(muted_role)
@bot.command()
async def custom(ctx,*,message=None):
    if message == None:
        await ctx.send("**Ошибка выполнения команды!**\nИспользование: simbo!custom <действие>")
    if message != None:
        await ctx.message.delete()
        await ctx.send(ctx.author.mention + " " + message)
    
@bot.command()
async def embed(ctx,*,message=None):
    if message == None:
        await ctx.send("**Ошибка выполнения команды!**\nИспользование: simbo!embed <текст>")
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(description = f"" + message,colour = discord.Color.blue()))

@bot.command()
async def user(ctx,member:discord.Member = None, guild: discord.Guild = None):
    d = False
    d2 = False
    if member == None:
        d = True
    else:
        d2 = True
    if d or d2 != True:
        await ctx.send("**Ошибка выполнения команды!**\nИспользование: ``simbo!user <@пользователь>``")

    if member == None:
        emb = discord.Embed(title="Информация о пользователе", color=ctx.message.author.color)
        emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)
        t = ctx.message.author.status
        if t == discord.Status.online:
            d = " В сети"

        t = ctx.message.author.status
        if t == discord.Status.offline:
            d = " Не в сети"

        t = ctx.message.author.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = ctx.message.author.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"

        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=ctx.message.author.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{ctx.message.author.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="Информация о пользователе", color=member.color)
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
        t = member.status
        if t == discord.Status.online:
            d = " В сети"

        t = member.status
        if t == discord.Status.offline:
            d = " Не в сети"

        t = member.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = member.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"
        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=member.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        await ctx.send(embed = emb)

@bot.command()
async def goodbye(ctx):
    await ctx.message.delete()
    await ctx.send(embed=discord.Embed(title=ctx.author.name + " ушёл.", colour=discord.Color.red()))

@bot.command()
async def help(ctx): 
    help1 = discord.Embed(title=f"Доступные команды:", description=f"\n**__:shield: Модерирование__**\n``simbo!ban <@пользователь>`` - забанить пользователя\n``simbo!mute <@пользователь> <время> <причина>`` - заглушить пользователя\n``simbo!unmute <@пользователь> <причина>`` - разглушить пользователя\n``simbo!kick <@пользователь>`` - кикнуть пользователя\n``simbo!warn <@пользователь>`` - выдать варн пользователю\n__(если бот не отвечает - у вас нету прав, либо он не смог найти пользователя)__\n\n**__:wrench: Утилиты__ **\n``simbo!addrole <@пользователь> <имя роли>`` - выдать роль пользователю\n``simbo!removerole <@пользователь> <имя роли>`` - забрать роль у пользователя\n``simbo!user <@пользователь>`` - информация об учаснике\n``simbo!clear <кол-во сообщений>`` - очистить чат\n\n**__:smile: Весёлое__**\n``simbo!cat`` - рандомное фото котика\n``simbo!popit`` - виртуальный поп-ит\n``simbo!hello`` - вывести сообщения о вашем появлении\n``simbo!goodbye`` - вывести сообщения о вашем уходе\n``simbo!custom <действие>`` - РП действие\n\n**__:art: Дизайн__**\n``simbo!embed <текст>`` - выводит красивое сообщения в 'коробочке'\n``simbo!say <текст>`` - сказать что-то от имени бота\n\n**__:information_source: Информация__**\n``simbo!info`` - информация о боте\n``simbo!link`` - получить ссылку-приглашение бота себе на сервер",colour=discord.Color.blue())
    await ctx.channel.send(embed=help1)

@bot.command()
async def stop(ctx):
    await ctx.send("Отключаюсь...")
    exit()

@bot.command()
async def привет(ctx):
    await ctx.send("Привет! Кстати, ты нашёл секретную команду))) Поздравляю!")

@bot.command()
async def addrole(ctx, member: discord.Member, *, role):
    role2 = discord.utils.get(ctx.message.guild.roles, name=role)
    await member.add_roles(role2)
    await ctx.send(embed=discord.Embed(title=f"Роли", description=f"Роль успешно выдана!", colour=discord.Color.green()))

@bot.command()
async def removerole(ctx, member: discord.Member, *, role):
    role2 = discord.utils.get(ctx.message.guild.roles, name=role)
    await member.remove_roles(role2)
    await ctx.send(embed=discord.Embed(title=f"Роли", description=f"Роль успешно забрана!", colour=discord.Color.green()))
member = discord.Member

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason="нарушения правил"):
    ban = discord.Embed(title=f":boom: Забанено {user.name}!", description=f"По причине: {reason}\nЗабанил: {ctx.author.mention}", colour=discord.Color.green())
    await ctx.message.delete()
    await ctx.channel.send(embed=ban)
    await user.send(embed=ban)
    await user.ban(reason=reason)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="нарушения правил"):
    kick = discord.Embed(title=f":boom: Кикнуто {user.name}!", description=f"По причине: {reason}\nКикнул: {ctx.author.mention}", colour=discord.Color.green())
    await ctx.message.delete()
    await ctx.channel.send(embed=kick)
    await user.send(embed=kick)
    await user.kick(reason=reason)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=None):
    if amount == None:
        await ctx.send("**Ошибка выполнения команды!**\nИспользование: simbo!clear <кол-во сообщений>")
    amountint = int(amount)
    await ctx.channel.purge(limit = amountint)
    await ctx.send(embed=discord.Embed(description="Удалено " + amount + " сообщений", colour=discord.Color.green()))

@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, user: discord.Member, *, reason="нарушения правил"):
        warn = discord.Embed(title=f":boom: Выдано предуприждение пользователю {user.name}!", description=f"По причине: {reason}\nВыдал предуприждения: {ctx.author.mention}", colour=discord.Color.green())
        await ctx.message.delete()
        await ctx.channel.send(embed=warn)
        await user.send(embed=warn)

@bot.command()
async def popit(ctx):
        await ctx.send("||:red_square:||||:green_square:||||:yellow_square:||||:purple_square:||||:orange_square:||\n||:red_square:||||:green_square:||||:yellow_square:||||:purple_square:||||:orange_square:||\n||:red_square:||||:green_square:||||:yellow_square:||||:purple_square:||||:orange_square:||\n||:red_square:||||:green_square:||||:yellow_square:||||:purple_square:||||:orange_square:||\n||:red_square:||||:green_square:||||:yellow_square:||||:purple_square:||||:orange_square:||")

@bot.command()
async def restart_MWWLA(ctx):
    await ctx.send("222 OK, RESTART FUNCTION = 221 START")
    os.system("python main.py")

@bot.command()
async def link(ctx):
    await ctx.send(embed = discord.Embed(title = f"Ссылка на бота:", description = f"https://discord.com/api/oauth2/authorize?client_id=867723875458744330&permissions=8&scope=bot"))

@bot.command()
async def info(ctx):
    await ctx.send(embed = discord.Embed(title=f"Информация об Simbo:", description=f"Офф.сервер бота - **https://discord.gg/mBJnQZgg85**\nРазработчик - " + "" + "**MrWoonWorld#8808**\nВсе команды - **simbo!help**"))

@bot.command()
async def гдеТвойДруг(ctx):
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(description="Мой старый друг... (ммммммм)... Его со мной нет много лет... Но память вдруг... (ммммммм)... Ударом в бок напомнит как - он мог летать... (ммммм)... Когда смотел на монитор.. Любил мечтать..."))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed = discord.Embed(description = f'{ctx.author.mention}, команда не найдена или введена неправильно!', colour = discord.Color.red()))
bot.run(TOKEN)
