import discord
import os
import redis

from os import environ
#environ["REPLIT_DB_URL"] = "https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2NjMxOTk1MzAsImlhdCI6MTY2MzA4NzkzMCwiZGF0YWJhc2VfaWQiOiI5NWI0MjhiNy04NGE3LTQ5ODktYmZiZC01NDNhMzcxYWQzNmIiLCJ1c2VyIjoiU2NvdHROaWVtYW5uIiwic2x1ZyI6IlN3ZWV0Qm90In0.PqKEYwiSkGuYswO7NhMV5utCgk8PAhNoV81OcJCIv6FaZe7emOOG9M1KutF-n9GV_nvRLO6ordKFMq9sQdm37A"
#environ["REPLIT_DB_URL"] = "https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2NjMzMjIyNzIsImlhdCI6MTY2MzIxMDY3MiwiZGF0YWJhc2VfaWQiOiI5NWI0MjhiNy04NGE3LTQ5ODktYmZiZC01NDNhMzcxYWQzNmIiLCJ1c2VyIjoiU2NvdHROaWVtYW5uIiwic2x1ZyI6IlN3ZWV0Qm90In0.FSoG-qK70XAq837M-rHcL63XxGi5dVGpngvjsYbTBQOHBLkUQePCcDdkCByRQpz8zxSsM80gsk_79VyXwwOt-g"
#from replit import db
from messages import mainHelpText, calendar, starsmaxDetail, randQuote, helpbadge
from recipes import getCraftsCat, getRecipeCat, floorSpellcheckCat
from recipesdog import getCraftsDog, getRecipeDog, floorSpellcheckDog
from tcc import room, stars3k, helptcc, errtcc
from clubevent import maxstarshelper,goalstarshelper
from badges import badgeAddMulti, badgeClear, getBadges
from keep_alive import keep_alive
r = redis.from_url(os.environ.get("REDIS_URL"))

def Convert(string):
    li = list(string.split(" "))
    return li
  


def add_decos(user,decos,category):
  if category=="": category='cat'
  argAry=interpretArgs(decos,category)
  if len(argAry)==0: return "Something went wrong. Expected syntax: $add floorname [startingdeco] [endingdeco]\nEnter floor name as one word"

  floor=argAry[0]
  if getRecipe(category,floor,1)=="Invalid floor": return "Floor name not recognized. Check spelling, and enter the floor name as one word."
  minDeco=int(argAry[1])
  maxDeco=int(argAry[2])

  alreadypresent=""
  userkey=getUserKey(user,category)
  if r.exists(userkey):
    decoslist = Convert(r.get(userkey).decode())
  else:
    decoslist = []
  
  for x in range (minDeco, maxDeco+1):
    hash=floor+"/"+str(x)
    if hash not in decoslist:
      decoslist.append(hash)
    else:
      alreadypresent=alreadypresent+", "+hash
  #decoslist.sort()
  #it was required to move to sorted per heroku recommendation
  #sorted(decoslist);
  decoslist.sort()
  r.set(userkey, ' '.join(decoslist))
  #print(r.get(userkey))

  if len(alreadypresent)==0:
    return "Decos added. Happy crafting!"
  return "Decos added. Happy crafting! Decos already in your list:"+alreadypresent.split(",",1)[1]

def remove_decos(user,decos,category):
  if category=="": category='cat'
  userkey=getUserKey(user,category)
  if not r.exists(userkey): return "You do not have any decos in your list."
 
  decoslist = Convert(r.get(userkey).decode())
  #decoslist = db[userkey]
  
  argAry=interpretArgs(decos,category)
  if len(argAry)==0: return "Expected syntax: $remove floorname [startingdeco] [endingdeco]"
  floor=argAry[0]
  if getRecipe(category,floor,1)=="Invalid floor": return "Floor name not recognized. Make sure to enter the floor name as one word."
  minDeco=int(argAry[1])
  maxDeco=int(argAry[2])

  for x in range (minDeco, maxDeco+1):
    hash=floor+"/"+str(x)
    if hash in decoslist:
      decoslist.remove(hash)
  
  #db[userkey] = decoslist
  r.set(userkey, ' '.join(decoslist))
  return "Decos removed. Yeet!"

def clear_decos(user, category):
  if category=="": category='cat'
  userkey=getUserKey(user, category)
  if r.exists(userkey): r.delete(userkey)
  #if userkey in db.keys(): del db[userkey]
  return "Decos cleared."

def show_msg(user,category):
  if category=="": category='cat'
  userkey=getUserKey(user, category)
  if not r.exists(userkey): return ["Planned decos: none"]
  
  decoslist = Convert(r.get(userkey).decode())
  total=len(decoslist)
  if total==0: return ["Planned decos: none"]
    
  msg1 = "Planned decos: "+str(total)+" total"
  msg3 = getCrafts(decoslist,category)

  if total<101:
    crafts = ""
    for x in decoslist: crafts=crafts+", "+str(x)
    crafts = crafts[2:]
    return [msg1 + "\n" + crafts + "\n\n" + msg3]

  else: # split of message as main message first, then list of crafts
    crafts = ""
    returnary=[msg1 + "\n\n" + msg3]
    for x in decoslist: 
      crafts=crafts+", "+str(x)
      if len(crafts)>1970: 
        returnary.append(crafts[2:])
        crafts = ""
    if len(crafts)>0: returnary.append(crafts[2:])
    return returnary
    

def getCrafts(decoslist,category):
  if category=='dog': return getCraftsDog(decoslist)
  return getCraftsCat(decoslist)

def printRecipe(decoStr,category):
  decoAry=decoStr.strip().split()
  if len(decoAry)<2: outmsg="Enter a floor and deco number."
  outmsg=getRecipe(category,decoAry[0], decoAry[1])
  if outmsg=="": outmsg="No recipe found."
  return outmsg

def getRecipe(category,floor,deco):
  if category=='dog': return getRecipeDog(floor,deco)
  return getRecipeCat(floor,deco)

def interpretArgs(decos,category):
  if category=="": category='cat'
  decosAry = decos.split()
  floor=floorSpellcheck(decosAry[0].lower(),category)
  length = len(decosAry)
  if length==1:
    minDeco=1
    maxDeco=7
  elif length==2:   #checks that the deco num is between 1 and 7. Does NOT take a guess.
    try: minDeco=int(decosAry[1])
    except: return []
    if minDeco<1: return []
    if minDeco>7: return []
    maxDeco=minDeco
  elif length==3:   #checks that range is between 1 and 7. Does take guesses.
    try: minDeco=max(int(decosAry[1]),1)   # if min is -5 or something, changes to 1
    except: return []
    try: maxDeco=min(int(decosAry[2]),7)   # if max is 99 or something, changes to 7
    except: return []
  else:
    return []
  return [floor,str(minDeco),str(maxDeco)]

def floorSpellcheck(floor,category):
  if category=='dog': return floorSpellcheckDog(floor)
  return floorSpellcheckCat(floor)

def parseFlags(flagStr):
  tokenAry = flagStr.split()
  tokenCount = len(tokenAry)
  if tokenCount==0: return [[],[]]
  flagAry = ["" for i in range(tokenCount)]
  valAry = ["" for i in range(tokenCount)]
  for i in range(tokenCount):
    token = getAlias(tokenAry[i].strip().lower())
    if token=="-user": #deco craftin - flag is -user and next word is username
      if i+1 < tokenCount: 
        flagAry[i] = token
        valAry[i] = tokenAry[i+1].strip()
    if token in ["-room","-aggressive","-debug"]: #CE options
      flagAry[i] = token
  return [flagAry,valAry]

def getUserKey(user,category):
  if category=="": category='cat'
  return 'crafting~'+str(user)+"~"+category

def getAlias(flag):
  switcher = {
    "-u": "-user",
    "-a": "-aggressive", "-ag": "-aggressive", "-aggr": "-aggressive",
    "-r": "-room", "-rm": "-room"
  }
  return switcher.get(flag,flag) #swaps the flag if it's found, otherwise unchanged

def showBadges(user,category):
  badgeary=getBadges(user,category)
  if badgeary[0]!="": return ["No "+badgeary[0]+" found. Keep collecting!", "", ""]

  embedmsg = discord.Embed(
    title=badgeary[2])
  #file = discord.File("images/egg1.png", filename="image.png")
  file = discord.File(badgeary[1], filename="image.png")
  embedmsg.set_image(url="attachment://image.png")
  return ["", file, embedmsg]

# it was necessary to delcare message intent (appropriate discord bot also need to be set in developer portal
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  if message.author == client.user: 
    return
  
  msg = message.content
  print(message.author)
  print(message.content)

  
  if not msg.startswith('$'):
    return

    
  if msg.startswith('$hello'):
    await message.channel.send('Hello, world!')
    return

  if msg.startswith('$dm'):
    channel = await message.author.create_dm()
    await channel.send('Welcome to Crafting Bot! Enter *$help* for instructions!')
    
  # $help: prints instructions
  msg = message.content
  if msg.startswith('$help'):
    if msg.startswith('$helptcc'): 
      await message.channel.send(helptcc()) 
      return
    if msg.startswith('$helpstar'): 
      ary=starsmaxDetail()
      await message.channel.send(ary[0]) 
      await message.channel.send(ary[1]) 
      return
    if msg.startswith('$helpbadge'): 
      await message.channel.send(helpbadge()) 
      return

    ary=mainHelpText()
    await message.channel.send(ary[0]) 
    await message.channel.send(ary[1]) 
    return

  if msg.startswith('$calendar'):
    await message.channel.send(calendar()) 
    return

  #tcc commands - not user specific
  if msg.startswith('$multiplier'):
    try: mult = (float)(msg.split("$multiplier",1)[1])
    except: 
      await message.channel.send(errtcc())
    #db["multiplier"] = mult
    r.set("multiplier", ' '.join(mult))
    await message.channel.send("Multiplier set")
    return

  if msg.startswith('$room'):
    await message.channel.send(room(r.get("multiplier").decode()))
    return

  if msg.startswith('$stars3k'):
    await message.channel.send(stars3k(r.get("multiplier").decode()))
    return

  if msg.startswith('$pot'):
    if msg.startswith('$potclear'):
      db["community pot"] = 0
      r.set("community pot", 0)
      await message.channel.send("Community pot cleared.")
      return
    if msg.startswith('$potshow'):
      await message.channel.send("Community pot: "+ str(r.get("community pot").decode()))
      return
    mats = msg.split("$pot",1)[1]
    #db["community pot"] = int(db["community pot"])+int(mats)
    await message.channel.send("Mats added to community pot.")
    return

  #
  user=str(message.author.id)
  userflag=0
  flagAry = []
  if "-" in msg:
    msgAry = msg.split("-",1)
    msg=msgAry[0].strip()
    flagStr="-"+msgAry[1]
    parseAry=parseFlags(flagStr)
    flagAry=parseAry[0]
    valAry=parseAry[1]
    
    try: 
      userIndex=flagAry.index("-user")
      user=valAry[userIndex].lower()
      userflag=1
    except: userIndex=-1 

  # $starsmax tokens gems hours multiplier [-room] [-aggressive]
  if msg.startswith('$starsmax'):
    if (1==1): #now allowed in all channels
      args = msg.split("$starsmax",1)[1]
      await message.channel.send(maxstarshelper(args,flagAry))
      return

    #the original starsmax in tcc.py was deprecated
    #await message.channel.send(starsmax(args,db["multiplier"]))
    await message.channel.send(randQuote()) # if it's in a non-allowed channel
    return

  # $starsgoal goal tokens hours multiplier [-aggressive]
  if msg.startswith('$starsgoal'):
    args = msg.split("$starsgoal",1)[1]
    await message.channel.send(goalstarshelper(args,flagAry))
    return

  # $add: add decos to cat game crafting list
  # syntax:
  #   $add floorname      - adds whole floor e.g. $add waterpark
  #   $add floorname deco - adds one deco e.g. $add waterpark 1
  #   $add floorname start end - adds the range of decos from that floor
  # notes: floorname must be all one word e.g. hairsalon not hair salon
  if msg.startswith('$add'):
    decos = msg.split("$add",1)[1]
    await message.channel.send(add_decos(user,decos,'cat'))
    return
  
  # $remove: removes one deco from your cat game list
  # syntax: $remove floorname deco - e.g. $remove waterpark 5
  if msg.startswith('$remove'):
    decos = msg.split("$remove",1)[1]
    await message.channel.send(remove_decos(user,decos,'cat'))
    return

  # $clear: remove all decos from your cat game list
  if msg.startswith('$clear'):
    await message.channel.send(clear_decos(user,'cat'))
    return

  # $show: shows the decos on your cat game list, then a list of crafts required in inventory
  if msg.startswith('$show'):
    returnary = show_msg(user,'cat')
    for msg in returnary: await message.channel.send(msg)
    return
  
  # $recipe: recipe of one specific deco in cat game
  if msg.startswith('$recipe'):
    decoStr = msg.split("$recipe",1)[1]
    await message.channel.send(printRecipe(decoStr,'cat'))
    return

  #the equivalents for dog game
  if msg.startswith('$dogadd'):
    decos = msg.split("$dogadd",1)[1]
    await message.channel.send(add_decos(user,decos,'dog'))
    return
  if msg.startswith('$dogremove'):
    decos = msg.split("$dogremove",1)[1]
    await message.channel.send(remove_decos(user,decos,'dog'))
    return
  if msg.startswith('$dogclear'):
    await message.channel.send(clear_decos(user,'dog'))
    return
  if msg.startswith('$dogshow'):
    returnary = show_msg(user,'dog')
    for msg in returnary: await message.channel.send(msg)
    return
  if msg.startswith('$dogrecipe'):
    decoStr = msg.split("$dogrecipe",1)[1]
    await message.channel.send(printRecipe(decoStr,'dog'))
    return
  #end of dog game section
    


  #Sweetling crafting bot badges :)
  if msg.startswith('$badge'):
    if message.author.id not in [721843920404742205,655087300140597268]: #Only some users can add/remove badges
      await message.channel.send(randQuote())
      return
    if msg.startswith('$badgeadd'):
      params=msg.split("$badgeadd",1)[1].strip()
      paramAry=params.split(" ")
      badgeAddMulti(paramAry[0],paramAry[1],paramAry[2])
      await message.channel.send("Badge added.")
      return
    if msg.startswith('$badgeclear'): 
      params=msg.split("$badgeclear",1)[1].strip()
      paramAry=params.split(" ")
      badgeClear(paramAry[0],paramAry[1])
      await message.channel.send("Badges cleared.")
      return
    if msg.startswith('$badgehelp'):
      await message.channel.send(helpbadge())
    return

  keyword=msg.split()[0][1:]
  badgewords=['mybadges','easter','catlorette','holiday','fitness']
  if keyword in badgewords:
    getuser=msg.split(keyword,1)[1].strip()
    if not getuser: getuser=user
    ary=showBadges(getuser,keyword)
    if ary[0]=="":
      await message.channel.send(file=ary[1],embed=ary[2])
      return
    await message.channel.send(ary[0])
    return

# not necessary on heroku, also remove call to server object
#keep_alive()

# DISCORD_TOKEN defined in heroku env_variables 
client.run(os.environ['DISCORD_TOKEN'])

# the code to check for server, for functions that have to be run from a server
#try:      #checking for server ID
#  serverID=message.guild.id
#except:
#  await message.channel.send('Please use from a server, thanks!')
#  return
#user = str(serverID) + "---" + str(message.author.id)
