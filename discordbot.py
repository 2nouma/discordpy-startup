from discord.ext import commands
import os
import traceback
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

#役職系
ID_CHANNEL_README = 687874762399023133 # 該当のチャンネルのID
ID_Message = 688714255260057605 #MessageID
ID_ROLE_DES = 687871101908418638 # デストロンID
ID_ROLE_SAI = 687871258788102164 # サイバトロンID
ID_EMOJI_DES = 688714255260057605 #デストロン絵文字ID
ID_EMOJI_SAI = 688714255260057605 #サイバトロン絵文字ID

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

@bot.event
async def on_raw_reaction_add(payload):
    # channel_id から Channel オブジェクトを取得
    channel = client.get_channel(payload.channel_id)
    
    # message_id から message オブジェクトを取得
    messagel = client.get_messagel(payload.message_id)
    
    # emoji_id から emoji オブジェクトを取得
    emoji1 = client.get_emoji(payload.emoji)
    
    # 該当のチャンネル以外はスルー
    if channel.id != ID_CHANNEL_README:
        return
    
    # 該当のメッセージ以外はスルー
    if messagel.id != ID_Message:
        return

    # guild_id から Guild オブジェクトを取得
    guild = client.get_guild(payload.guild_id)

    # user_id から Member オブジェクトを取得
    member = guild.get_member(payload.user_id)

    # 用意した役職IDから Role オブジェクトを取得
    role1 = guild.get_role(ID_ROLE_DES)
    role2 = guild.get_role(ID_ROLE_SAI)

    # リアクションを付けたメンバーに役職を付与
    if emoji1.id != ID_EMOJI_DES:
       await member.add_roles(role1)
    elif emoji1.id != ID_EMOJI_DES:
       await member.add_roles(role2)
    else: return
    
    # 分かりやすいように歓迎のメッセージを送る
    #await channel.send('いらっしゃいませ！')
    
    bot.run(token)
