#import discord
import os
import redis

from os import environ

#from discord.ext import commands
from PIL import Image
r = redis.from_url(os.environ.get("REDIS_URL"))

def Convert(string):
    li = list(string.split(" "))
    return li

def badgeCategories(): # category names can't contain tilda '~', lowercase preferred
  return ['easter','catlorette','mybadges','holiday','fitness']

def stripUserId(memberStr):
  memberStr=memberStr.strip()
  if memberStr.startswith('<@'):
    memberStr=memberStr.split("<@",1)[1]
  if memberStr.startswith('!'):
    memberStr=memberStr.split("!",1)[1]
  if memberStr.endswith('>'):
    memberStr=memberStr.split(">")[0]
  return memberStr

def badgeAddMulti(userId,category,badgeIdList):
  badgeIdAry=badgeIdList.split(",")
  for badgeId in badgeIdAry:
    badgeAdd(userId,category,badgeId)

def badgeAdd(userId,category,badgeId):
  user=stripUserId(userId)
  hash='badges~'+str(user)+"~"+category

  badgefile = getFile(category,badgeId)
  if not badgefile: return

  if r.exists(hash):
    badgelist = Convert(r.get(hash).decode())
  else:
    badgelist = []

  if badgefile not in badgelist:
    badgelist.append(badgefile)
  
  #db[hash]=badgelist
  r.set(hash, ' '.join(badgelist))

  return

def badgeClear(userId,category):
  user=stripUserId(userId)
  hash='badges~'+str(user)+"~"+category
  #db[hash]=[]
  r.delete(hash)
  return

def combineImg(list_im): #pass in array of images
  #list_im = ['images/egg1.png','images/egg1.png']
  if len(list_im)==0: return ""
  images = [Image.open(x) for x in list_im]
  widths, heights = zip(*(i.size for i in images))
  total_width = sum(widths)
  max_height = max(heights)

  # creates a new empty image, RGB mode, and size 444 by 95
  new_im = Image.new('RGB', (total_width, max_height))

  x_offset = 0
  for im in images:
    new_im.paste(im, (x_offset,0))
    x_offset += im.size[0]

  path='images/temp.png'
  new_im.save(path)

  return path

def getBadges(userId,category):
  user=stripUserId(userId)
  hash="badges~"+str(user)+"~"+category
  #print(hash)
  if r.exists(hash):
    badgeAry = Convert(r.get(hash).decode())
    return ["",combineImg(badgeAry),getEmbedTitle(category)]
  else: 
    return [getNoun(category),"",""]
  
def getFile(category,badgeId):
  switcher = {
    "easter":easter,
    "catlorette":catlorette,
    "mybadges":mybadges,
    "holiday":holiday,
    "fitness":fitness
  }
  func = switcher.get(category, lambda1)
  return func(int(badgeId))

#
def lambda1(x): return ""

def getNoun(category):
  switcher = {
    "easter":"Easter eggs",
    "catlorette":"roses"
  }
  return switcher.get(category,"badges")

def getEmbedTitle(category):
  switcher = {
    "easter":"My Collected Eggs",
    "catlorette":"My Roses",
    "holiday":"My Holiday Collection",
    "fitness":"My Fitness Badges"
  }
  return switcher.get(category,"My Badges")

def easter(badgeId):
  switcher = {
    0: "images/bunny.png",
    1: "images/egg1.png", #red
    2: "images/egg2.png", #blue
    3: "images/egg3.png", #green
    4: "images/egg4.png", #purple
    5: "images/egg5.png", #yellow
    6: "images/egg6.png", #red, gold spots
    7: "images/egg7.png", #blue, bronze spots
    8: "images/egg8.png", #green, silver spots
    9: "images/egg9.png", #yellow, black spots
    10: "images/egg10.png", #pastel pink
    11: "images/egg11.png", #orange, white swirl, fearless revival
    99: "images/chick.png"
  }
  return switcher.get(badgeId,"")

def catlorette(badgeId):
  switcher = {
    #May 2021 badges
    1: "images/catlorette/rose.png", #simple red rose
    2: "images/catlorette/ring.png", #ring
    3: "images/catlorette/rose2.png", #simple purple rose
    4: "images/catlorette/night.png", #pink cat on moon
    5: "images/catlorette/poppy.png", #red poppy flower
    6: "images/catlorette/bigring.png", #obnoxiously large diamond
    7: "images/catlorette/fancyrose.png", #dark rose with FR swirl
    11: "images/catlorette/rose11.png", #first impression rose - rainbow
    12: "images/catlorette/rose12.png", #black tie mud rose - black/white
    13: "images/catlorette/rose13.png", #can i steal you rose - snake
    14: "images/catlorette/rose14.png", #the right reasons rose - gold
    #Jul 2022 badges
    21: "images/catlorette/rose21.png", #first impression (good) - red
    22: "images/catlorette/rose22.png", #mud wrestle - black/red/blue
    23: "images/catlorette/rose23.png", #can i steal you - blue
    24: "images/catlorette/rose24.png", #right reasons - gold/sparkle
    25: "images/catlorette/rose25.png", #first impression (great) - rainbow
    26: "images/catlorette/ring21.png", #normal ring
    27: "images/catlorette/ring22.png", #big ring - crafted extra sparkles
    28: "images/catlorette/ring23.png" #red gem ring - consolation
  }
  return switcher.get(badgeId,"")

def mybadges(badgeId):
  switcher = {
    1: "images/bug.png", #beetle for making a bug report
    2: "images/phoenixruff.png", #black/white husky - minigame participation
    3: "images/frgem.png", #orange heart gem - 1yr anniversary
    4: "images/frgem2.png", #blue heart gem - original members
    5: "images/50k.png", #silver medal - 50k in a CE
    6: "images/100k.png" #gold medal - 100k in CE
  }
  return switcher.get(badgeId,"")

def holiday(badgeId):
  switcher = {
    1: "images/christmas.png", #christmas tree
    2: "images/hannukah.png", #dreidel
    3: "images/kwanzaa.png", #seven kwanzaa candles
    4: "images/diwali.png", #rangoli
    5: "images/eid.png", #moon/star/lantern
    6: "images/lasposadas.png", #7-point pinata
    7: "images/soyal.png", #sun with plumed snake
    8: "images/yule.png", #snowflake
    9: "images/festivus.png", #festivus pole
    10: "images/lunarnewyear.png", #dao fu
    11: "images/fearlessiversary.png" #FR symbol with laurel
  }
  return switcher.get(badgeId,"")

def fitness(badgeId):
  switcher = {
    1: "images/fitness/jan2022.png" #blue snow boot/jan 2022
  }
  return switcher.get(badgeId,"")
