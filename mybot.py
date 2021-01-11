import os
import praw
import random
import tweepy
import discord
from dotenv import load_dotenv
from discord.ext import commands

#loads the .env file
load_dotenv()


"""
You can use any prefix instead of '#'
just make the required changes , for now I'm using '#'
"""

#the prefix of the bot is '#'
client = commands.Bot(command_prefix = "#")         

#removing the default help command so that we can make our own custom help command
client.remove_command("help")


#Rules for Your server

rules = [":one: <rule 1>",                          #write 1st rule in <rule1 1>
         ":two: <rule 2>", 
         ":three: <rule 3>",
         "",                                        # write rules 4, 5 , 6 also here
         "",
         "",
         ":seven:  <your institute> >>> any other college ." ]


filtered_words = ["fuck"]                           # you can add more words to filter
                                                    # suggestions for words to filter are welcome :)


# prints bot is ready on the terminal when it is online
@client.event
async def on_ready():
    print("Bot is ready")


# executed whenever a message is ent on your server
@client.event
async def on_message(msg):
    """
    prevent the filtered words from being used in your server
    warns the person who uses these words in dm and deltes the message containing filtered words
    """
    
    for word in filtered_words:
        if word in msg.content.lower():
            await msg.delete()
            await msg.author.send("Don't use bad words")

    # adds the reaction 😂 if someone says lol
    if "lol" in msg.content.lower():
        await msg.add_reaction("😂")

    # adds the reaction 🤣 is someone says lmao
    if "lmao" in msg.content.lower():
        await msg.add_reaction("🤣")

    # adds the reaction 🆒 if someone says cool
    if "cool" in msg.content.lower():
        await msg.add_reaction("🆒")

    try:
        if msg.mentions[0] == client.user:
            await msg.channel.send("My prefix is '#'") #sends this when someone mentions @YOUR_BOT
    except:
        pass
    
    await client.process_commands(msg)


#  for exception handling
@client.event
async def on_command_error(ctx, exception):
    exception = getattr(exception, "original", exception)
    if isinstance(exception, commands.MissingPermissions):
        await ctx.send("You can't do that 😂")
    elif isinstance(exception, commands.MissingRequiredArgument):
        await ctx.send("Please enter all the required arguments 🤦🏻‍♂️")
    else:
        raise exception


# help command

@client.group(invoke_without_command = True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Use #help <command> for extended information of a command.", colour = ctx.author.colour)
    em.add_field(name = "Rules", value = "#rule rule_no.", inline = True)
    em.add_field(name = "info", value = "#whois or #info or #user", inline = True)
    em.add_field(name = "Moderation", value = "kick,ban,unban,mute,unmute,clear", inline = True)
    em.add_field(name = "Poll" , value = "#poll <option1> or <option2>", inline = True)
    em.add_field(name = "fun", value ="hello, meme, lol, lmao", inline = True)
    await ctx.send(embed = em)


# subcommands of help command

@help.command()
async def kick(ctx):
    em = discord.Embed(title = "kick", description = "kicks a member from the guild", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#kick <member> [reason]")
    await ctx.send(embed=em)

@help.command()
async def ban(ctx):
    em = discord.Embed(title = "ban", description = "bans a member from the guild", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#ban <member> [reason]")
    await ctx.send(embed=em)

@help.command()
async def unban(ctx):
    em = discord.Embed(title = "unban", description = "unbans a member who was banned from the guild", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#unban <member> ")
    await ctx.send(embed=em)

@help.command()
async def mute(ctx):
    em = discord.Embed(title = "mute", description = "prevents a member from sending messages", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#mute <member> ")
    await ctx.send(embed=em)

@help.command()
async def unmute(ctx):
    em = discord.Embed(title = "unmute", description = "unmutes a muted member", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#unmute <member> ")
    await ctx.send(embed=em)

@help.command()
async def clear(ctx):
    em = discord.Embed(title = "clear", description = "deltes the last <n> messages from the channel", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#clear <no. of messages to be deleted>")
    em.add_field(name = "Note", value = "use #clear to delete the last message")
    em.add_field(name = "Also" , value = "you can delete max. 20 messages, bcoz ishaan fixed the upper limit")
    await ctx.send(embed=em)

@help.command()
async def rule(ctx):
    em = discord.Embed(title = "rule", description = "send the rules of the server", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#rule <rule no.> ")
    await ctx.send(embed=em)

@help.command()
async def whois(ctx):
    em = discord.Embed(title = "whois", description = "send the user info of mentioned user", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#whois <member> ")
    await ctx.send(embed=em)

@help.command()
async def poll(ctx):
    em = discord.Embed(title = "poll", description = "sends a poll consisting of two options", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#poll <option 1> or <option 2> ")
    await ctx.send(embed=em)

@help.command()
async def meme(ctx):
    em = discord.Embed(title = "meme", description = "sends a random meme", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#meme")
    await ctx.send(embed=em)

@help.command()
async def hello(ctx):
    em = discord.Embed(title = "hello", description = "try it out", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#hello")
    await ctx.send(embed=em)

#todo
"""
@help.command()
async def fire(ctx):
    em = discord.Embed(title = "fire", description = "try it out", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#fire")
    await ctx.send(embed=em)
"""


@help.command()
async def lol(ctx):
    em = discord.Embed(title = "lol", description = "try it out", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#lol")
    await ctx.send(embed=em)

@help.command()
async def lmao(ctx):
    em = discord.Embed(title = "lmao", description = "try it out", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#lmao")
    await ctx.send(embed=em)

@help.command()
async def cool(ctx):
    em = discord.Embed(title = "cool", description = "try it out", colour = ctx.author.colour)
    em.add_field(name = "**Syntax**", value = "#cool")
    await ctx.send(embed=em)



# the commands

@client.command()
async def hello(ctx):
    await ctx.send("Hi")


@client.command()
async def rule(ctx,*,number):
    await ctx.send(rules[int(number) - 1])


clr_max = 20
@client.command(aliases=['clr'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 1):
    if amount <= clr_max:
        await ctx.channel.purge(limit = amount + 1)
    else:
        await ctx.send("You can't delete so many messages")


@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member,*,reason = "No Reason Provided"):
    await member.send('You have been kicked from "freshers tech club", because : ' + reason)
    await ctx.send('You have been kicked from "freshers tech club", because : ' + reason)
    await member.kick(reason = reason)


@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member,*,reason = "No Reason Provided"):
    try:
        await ctx.send(member.name + ' have been banned from "freshers tech club", because : ' + reason)
    except:
        await ctx.send("The member has their dms closed.")

    await member.ban(reason = reason)


@client.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx,*,member : discord.Member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):

            await ctx.guild.unban(user)
            await ctx.send(member_name + "has been unbanned!")
            return

    await ctx.send(member+" was not found")

MUTED = int(os.getenv('MUTED_ROLE_ID'))


@client.command(aliases=['m'])
@commands.has_permissions(kick_members = True)
async def mute(ctx, *, member : discord.Member):
    muted_role = ctx.guild.get_role(MUTED)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " has been muted")


@client.command(aliases=['um'])
@commands.has_permissions(kick_members = True)
async def unmute(ctx, *, member : discord.Member):
    muted_role = ctx.guild.get_role(MUTED)

    await member.remove_roles(muted_role)

    await ctx.send(member.mention + " has been unmuted")


@client.command()
async def lol(ctx):
    await msg.delete()
    await ctx.send("😂")


@client.command()
async def lmao(ctx):
    await msg.delete()
    await ctx.send("🤣")


@client.command()
async def cool(ctx):
    await ctx.send("🆒")


#todo issue here

"""
@client.command()
async def fire(ctx:
    await msg.delete()
    await ctx.send("🔥")
"""


# sends information about the mentioned user
@client.command(aliases=['user', 'info'])
async def whois(ctx, member : discord.Member):
    embed = discord.Embed(title = member.name, description = member.mention, colour  = discord.Colour.green())
    embed.add_field(name = "ID", value = member.id, inline = True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed = embed)





# meme command using reddit

reddit_client_id = os.getenv('CLIENT_ID')
reddit_client_secret = os.getenv('CLIENT_SECRET')
reddit_user_agent = os.getenv('USER_AGENT')

reddit = praw.Reddit(client_id = reddit_client_id,
                     client_secret = reddit_client_secret,
                     user_agent = reddit_user_agent)

"""
This command sends a random meme from the top 10 memes tredending on reddit
"""

@client.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)


#poll command
# sends a poll consisting of two options seperated by 'or'
@client.command(aliases = ['pl'])
async def poll(ctx,*,msg):
    channel = ctx.channel
    try:
        op1, op2 = msg.split("or")
        txt = f"React with ✅ for {op1} or ❎ for {op2}"
    except:
        await channel.send("Correct Syntax: [Choice1] or [Choice2]")
        return


    embed = discord.Embed(title = "Poll", description = txt, colour = discord.Colour.red() )
    message_ = await channel.send(embed=embed)
    await message_.add_reaction("✅")
    await message_.add_reaction("❎")
    await ctx.message.delete()



# twitter commands

#personal information
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCES_TOKEN_SECRET')

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth)

# twitter client_id
twitter_client_id = api.me().id



# tweet command
@client.command()
async def tweet(ctx, *, msg):
    api.update_status(status = msg)

    tweet = api.user_timeline(id = twitter_client_id, count = 1)[0]
    tweet_text = tweet.text   
        #print(tweet.text)
    
    tweet_url = "https://twitter.com/<your_twitter_tagname>/status/" + str(tweet.id)

    for DGuild in client.guilds:
                for DChannel in DGuild.text_channels:
                    if DChannel.name == 'testing':

                        embed = discord.Embed(title = tweet.user.screen_name, description = tweet_text, colour  = discord.Colour.blue())
                        embed.add_field(name = "TWEET ID", value = tweet.id, inline = True)
                        embed.add_field(name = "TWEET URL", value = tweet_url, inline = True)
                        embed.set_thumbnail(url = tweet_url)

                        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Posted by {ctx.author.name}")
                        embed.set_author(name='@your_twitter_tagname', icon_url=client.user.default_avatar_url)
                        await DChannel.send(embed = embed)


#todo  wip

"""
@client.command()
async def TWEET(ctx, *, amount = 2):
    messages = await ctx.channel.history(limit=amount).flatten()
    TWEET_text = messages[0]
    await ctx.send(TWEET_text)
"""



TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)