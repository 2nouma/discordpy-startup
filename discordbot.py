from discord.ext import commands
import os
import traceback
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

#役職系
ID_CHANNEL_README = 687874762399023133 # 該当のチャンネルのID
ID_ROLE_DES = 687871101908418638 # デストロンID

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def neko(ctx):
    await ctx.send('にゃ～ん')
    
    bot.run(token)
    
import discord
token = os.environ['DISCORD_BOT_TOKEN']
# 接続に必要なオブジェクトを生成
client = discord.Client()    

@client.event
async def on_raw_reaction_add(payload):
    # channel_id から Channel オブジェクトを取得
    channel = client.get_channel(payload.channel_id)
    # 該当のチャンネル以外はスルー
    if channel.id != ID_CHANNEL_README:
        return
    # guild_id から Guild オブジェクトを取得
    guild = client.get_guild(payload.guild_id)
    # user_id から Member オブジェクトを取得
    member = guild.get_member(payload.user_id)
    # 用意した役職IDから Role オブジェクトを取得
    role1 = guild.get_role(ID_ROLE_DES)
    # リアクションを付けたメンバーに役職を付与
    await member.add_roles(role1)
    
client.run(token)
