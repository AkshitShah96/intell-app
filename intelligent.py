import discord
from discord.ui import Button, View
from discord.utils import get
import os
from dotenv import load_dotenv
import wikipedia
import smtplib
import datetime
import webbrowser
import youtube_dl


client = discord.Client()

@client.event
async def on_ready():
    general_channel = client.get_channel(936524570888925189)
    await general_channel.send("* Bot just landed on the server!")

@client.event
async def on_error(error):
    general_channel = client.get_channel(936524570888925189)
    await general_channel.send(error)
    
@client.event
async def on_member_join(member):
    myEmbed = discord.Embed(title = "INTELLIJE", description="Welcome to Virtuality!", color=0xffff00)
    myEmbed.add_field(name="Welocome to our Discord Server! " + str(member) ,value="🤖", inline=False)
    myEmbed.add_field(name="Hope you will have a great time here...", inline=False)
    myEmbed.set_footer(text="Study!, Play!, Sleep!")
    myEmbed.set_author(name="AMUL INTELLIGENT BOT")
    await member.send(embed=myEmbed)

@client.event
async def on_message(message):
    #Sends a private message to the user.
    if message.content =="#private":
        await message.author.send("* Hello there, in private!\nI'm AMUL INTELLIGENT Bot!\n How may I help you?") 
        
    #Gives information about the concerned topic.    
    elif "#wiki" in message.content:
        await message.channel.send("* Searching Google!")
        try:
            message.content = message.content.replace("#wiki", "")
            results = wikipedia.summary (message.content,sentences = 10)
            await message.channel.send("* According to Google, "+ results)
        except Exception as e:
            await message.channel.send("* Something went wrong\n" + str(e))
    
    #Gives a option of roles to the members in the Noobpook server.
    elif message.content == "#roles":
        button = Button(label="AMUL", style=discord.ButtonStyle.green, emoji="🍼")
        button2 = Button(label="Rishi The Piro", style=discord.ButtonStyle.danger, emoji="🕹")
        button3 = Button(label="The DJ GUY", style=discord.ButtonStyle.grey, emoji="🎧")
        button4 = Button(label="Server Owner", style=discord.ButtonStyle.grey)
        view = View()
        view.add_item(button)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        async def button_callback(interaction):
            author = interaction.user
            role = get(author.guild.roles, name='Noobpook')
            await interaction.user.add_roles(role)
        button.callback = button_callback 
        async def button_callback(interaction):
            author = interaction.user
            role = get(author.guild.roles, name='UkiNoobda')
            await interaction.user.add_roles(role)
        button2.callback = button_callback 
        async def button_callback(interaction):
            author = interaction.user
            role = get(author.guild.roles, name='The Dj wala Babu')
            await interaction.user.add_roles(role)
        button3.callback = button_callback 
        async def button_callback(interaction):
            author = interaction.user
            role = get(author.guild.roles, name='the yoyo guy')
            await interaction.user.add_roles(role)
        button4.callback = button_callback 
        await message.channel.send("hi", view=view)
    
    #A user can make custom buutons with the help of this command.
    elif "!makebut" in message.content:
            msg = message.content.split("~")
            mg = len(msg)
            if mg==4:
               b1 = msg[3].split(",")
               button = Button(label=str(b1[0]), emoji=str(b1[1]))
               view=View(timeout=10)
               view.add_item(button)
               async def button_callback(interaction):
                    await interaction.response.send_message(str(b1[2]))
               button.callback = button_callback
            elif mg==5:
               b1 = msg[3].split(",")
               button = Button(label=str(b1[0]), emoji=str(b1[1]))
               b2 = msg[4].split(",")
               button2 = Button(label=str(b2[0]), emoji=str(b2[1]))
               view=View(timeout=10)
               view.add_item(button)
               view.add_item(button2)
               async def button_callback(interaction):
                    await interaction.response.send_message(str(b1[2]))
               button.callback = button_callback
               async def button_callback(interaction):
                    await interaction.response.send_message(str(b2[2]))
               button2.callback = button_callback
            elif mg==6:
               b1 = msg[3].split(",")
               button = Button(label=str(b1[0]), emoji=str(b1[1]))
               b2 = msg[4].split(",")
               button2 = Button(label=str(b2[0]), emoji=str(b2[1]))
               b3 = msg[5].split(",")
               button3 = Button(label=str(b3[0]), emoji=str(b3[1]))
               view=View(timeout=10)
               view.add_item(button)
               view.add_item(button2)
               view.add_item(button3)
               async def button_callback(interaction):
                    await interaction.response.send_message(str(b1[2]))
               button.callback = button_callback
               async def button_callback(interaction):
                    await interaction.response.send_message(str(b2[2]))
               button2.callback = button_callback
               async def button_callback(interaction):
                    await interaction.response.send_message(str(b3[2]))
               button3.callback = button_callback
            elif mg==7:
               b1 = msg[3].split(",")
               button = Button(label=str(b1[0]), emoji=str(b1[1]))
               b2 = msg[4].split(",")
               button2 = Button(label=str(b2[0]), emoji=str(b2[1]))
               b3 = msg[5].split(",")
               button3 = Button(label=str(b3[0]), emoji=str(b3[1]))
               b4 = msg[6].split(",")
               button4 = Button(label=str(b4[0]), emoji=str(b4[1]))
               view=View(timeout=10)
               view.add_item(button)
               view.add_item(button2)
               view.add_item(button3)
               view.add_item(button4)
               async def button_callback(interaction):
                    await interaction.response.send_message(str(b1[2]))
               button.callback = button_callback
               async def button_callback(interaction):
                    await interaction.response.send_message(str(b2[2]))
               button2.callback = button_callback
               async def button_callback(interaction):
                    await interaction.response.send_message(str(b3[2]))
               button3.callback = button_callback
               async def button_callback(interaction):
                    await interaction.response.send_message(str(b4[2]))
               button4.callback = button_callback
            message_channel = client.get_channel(int(msg[2]))
            await message_channel.send(str(msg[1]), view=view)
            await message.channel.send("Custom Button sent to the desired channel!")        
   
    #Enables the user to send emails through discord.
    #Broken though.
    elif "#email" in message.content:
        try:
            mail = message.content.split("~")
            to = mail[3]
            content = mail[4]
            email= mail[1]
            epas= mail[2]           
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(email, epas)
            server.sendmail(email, to, content)
            server.close()
            await message.author.send("* Email sent!")           
        except Exception as e:
            await message.author.send("* Something went wrong! \n"+str(e))
           
    #actually doesn't work
    elif '#time' in message.content:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        await message.channel.send("* The time is "+strTime)
     
    #troll someone using this command by sending a custom message to certain channel
    elif '#troll13579 ' in message.content:
        try:
            message.content = message.content.replace("#troll795453 ", "")
            ok = message.content.split(" ")
            ol = int(ok[0])
            message.content = message.content.replace(ok[0] , "")
            message_channel = client.get_channel(ol)
            await message_channel.send(message.content)
            await message.author.send("The troll command has been successfully send to the desired channel!")
        except Exception as e:
            await message.author.send(str(e))
     
    #troll someone presonnally using his ID and sending him message through the bot.
    elif "#troll2468" in message.content:
        try:
            msg = message.content.split("~")
            message_author = await client.fetch_user(int(msg[1]))
            await message_author.send(str(msg[2]))
            await message.author.send("The troll command has been successfully send to the desired user!" + str(message_author))
        except Exception as e:
            await message.author.send("We encountered a problem \n" + str(e))
    
    #Funny Easter egg for my friend.
    elif message.content == "akshit is milkman, right?":         
        await message.channel.send("That's true!")
        await message.content.add_reaction("🌚")
    
    #Gives you the exact count of letters in your paragraph.
    elif "#countl" in message.content:
        while True:
            pas = message.content
            count=0
            for x in pas:
                count+=1
            await message.channel.send("*"+str(count-6)+ " letters")
            break
    
    #Gives you the version of the discord bot.
    elif "#version" in message.content:
        myEmbed = discord.Embed(title ="The Intelligents", description="So called Intelligents...", color=0xffff00)
        myEmbed.add_field(name="Total Participants:",value="7", inline=False)
        myEmbed.add_field(name="Total Bots:",value="3", inline=False)
        myEmbed.add_field(name="Date released:",value="7TH FEBRUARY 2021", inline=False)
        myEmbed.set_footer(text="Study!, Play!, Sleep!")
        myEmbed.set_author(name=str(message.author)  )
        await message.channel.send(embed=myEmbed)
    
    #Gives you the exact count of words in your paragraph.
    elif "#countw" in message.content:
        while True:
            pas = message.content
            count=0
            for x in pas:
                if x == " ":
                    count+=1
            await message.channel.send("*"+str(count+2)+" words")
    
    #Gives you the exact count of the word you mentioned in the command.
    elif "#countcus" in message.content:
        while True:
            pas = message.content
            list=pas.split(" ")
            un=list[1]
            p = list.count(un)
            #un =list.count([1])
            #count=0
            #for x in pas:
                #if x == str(un):
                    #count+=1
            await message.channel.send("*"+str(p-1))
            break
    
    #Proceeds you towards the calculator part.
    elif "#cal" in message.content:    
        op=message.content.split(" ")
        if op[1] == "a":
            o = int(op[2])
            t = int(op[3])
            a = (o+t)
            await message.channel.send("* The sum is " + str(a))
        elif op[1] == "s":
            o = int(op[2])
            t = int(op[3])
            a = (o-t)
            await message.channel.send("* The reduction is " + str(a))
        elif op[1] == "m":
            o = int(op[2])
            t = int(op[3])
            a = (o*t)
            await message.channel.send("* he product is " + str(a))
        elif op[1] == "d":
            o = int(op[2])
            t = int(op[3])
            a = (o/t)
            await message.channel.send("* The division is " + str(a))
        elif op[1] == "exp":
            o = int(op[2])
            t = int(op[3])
            a = (o**t)
            await message.channel.send("* The exponent is " + str(a))
        elif op[1] == "root":
            o = int(op[2])
            t = int(op[3])
            a = (o**(1/t))
            await message.channel.send("* The root is " + str(a))
        elif op[1] == "log":
            o = int(op[2])
            t = int(op[3])
            total=0
            while True:
                i=(o/(t**2))
                if i==1:
                    total+=2
                    break
                elif i<1:
                    total+=1
                    break
                elif i>1:
                    total+=2
                    o = i
                    continue
            await message.channel.send("*The approximate answer to the given Logarith is "+str(total))
            
    elif message.content == "#commands":
        await message.channel.send("* Thanks for using NOOBPOOK Bot🤖 \nHere are the commands you can use with this bot. \n1. #*wiki ex.Minecraft: Gives you information about the desired topic you want.\n\n2. #*private: Connects with you in private chat.\n\n3. #*time: Gives you the current time.\n\n4. #*version: Gives you the version of the bot.\n\n5. #*countl ...: Gives you the exact number of letters in your paragraph.\n\n6. #*countw ...: Gives you the exact number of words in your paragraph.\n\n7. #*countcus...: Gives you the exact number of words you mention in your paragraph.\n\n8. #*cal a 57 75: Add both the numbers and gives you the required answer. \n\n9.#*cal s 90 75: Subtarct the numbers and gives you the required answer.\n\n10. #*cal m 57 75: Multiply both the numbers and gives you the required product.\n\n11. #*cal d 999999 11: Divide the numbers and gives you the required answer.\n\n12. #*cal exp 10 3: Can perform exponentation and gives you the required answer.\n\n13. #*cal root 1000 3: Can perform under root operations and gives you the required answer.\n\n14. #*cal log 3 1000: Perform log operations and gives you the required answer.")
    
    #manager for the music-commands section:
    elif str(message.channel) == client.get_channel(939541391569211483):
        if ";" not in message.content or message.author != "FredBoat♪♪#7284":
            await message.channel.purge(limit=1)
            botEmbed = discord.Embed(title ="Intelligent Bot", description="That message is not allowed here!", color=0xffff00)
            botEmbed.add_field(name=str(message.author),value="❌", inline=False)
            botEmbed.add_field(name="Only FredBoat commands are allowed in this channel!")
            await message.author.send(embed=botEmbed)
            pass                   
    
    #manager for the meeting and general channel.
    elif message.channel==client.get_channel(936524570888925190) and message.channel==client.get_channel(936524570888925189):
        if ";" in message.content:
            message_channel=client.get_channel(939541391569211483)
            await message.channel.purge(limit=1)
            musicEmbed = discord.Embed(title ="Intelligent Bot", description="That message is not allowed here!", color=0xffff00)
            musicEmbed.add_field(name=str(message.author),value="❌", inline=False)
            musicEmbed.add_field(name="What to do then?", value="To use commands ,head onto the the "+str(message_channel), inline=False)
            musicEmbed.set_footer(text="Study!, Play!, Sleep!")     
            await message.author.send(embed=musicEmbed)
            pass
    
    #manager for the botcommand channel.
    elif message.channel == client.get_channel(939414218149605396):
        if "/" not in message.content or message.author != "MEE6#4876" :
            await message.channel.purge(limit=1)
            message_channel = client.get_channel(936524570888925189)
            musicEmbed = discord.Embed(title ="Intelligent Bot", description="That message is not allowed here!", color=0xffff00)
            musicEmbed.add_field(name=str(message.author),value="❌", inline=False)
            musicEmbed.add_field(name="What to do then?", value="To do normal messages ,head onto the the "+str(message_channel), inline=False)
            musicEmbed.set_footer(text="Study!, Play!, Sleep!")     
            await message.author.send(embed=musicEmbed)
            pass
            pass 
    
    elif "hello" in message.content:
        await message.add_reaction("😃")
        pass
    
    elif str(message.author) == "NOOB#9812":
        await message.add_reaction("👽")
        pass

    elif str(message.channel) == "youtube":
        await message.add_reaction("👍")
        pass

    elif str(message.author) == "BeastBoyKrish#5783":
        await message.add_reaction("💀")
        pass
    
    elif str(message.author) == "Minecraftsmp#2089":
        await message.add_reaction("😮")
        pass

client.run("OTQwMTk5NzkzNTEzMzM2ODMy.YgD7Sg.IXCU3ieABBJk3kSVE0jXpG55ex0")
