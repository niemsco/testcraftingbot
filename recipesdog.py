def getCraftsDog(decolist):
  craftAry = [0 for i in range(24)]
  labelAry = ["coins", "log", "cotton", "rock", "quartz", "string", "wood", "ribbon", "metal", "needle", "sparkle", "bronze", "silver", "gold", "amethyst", "pendant", "necklace", "orb", "water", "fire", "waterstone", "firestone", "elementstone", "artifact"]

  for x in decolist:
    xsplit=x.split("/")
    floor=xsplit[0]
    deco=int(xsplit[1])
    craftAry=addCrafts(craftAry,floor,deco)
  
  msg="Crafts to have in inventory:"
  for x in range(len(craftAry)):
    if craftAry[x]>0: msg=msg + "\n" + str(craftAry[x]) + " " + labelAry[x]
  return msg

def addCrafts(craftAry,floor,deco):
  recipe = getRecipeDog(floor,deco)  #e.g. "2 Metal, 1 Needle, 320 Coins"
  if recipe=="Invalid floor": return craftAry
  recipeAry=recipe.split(",")
  for craft in recipeAry:          #e.g. " 1 Needle" (may have extra spaces)
    craftsplit = craft.strip().split(" ")
    num = int(craftsplit[0])      #e.g. 1
    craftName = craftsplit[1].strip().lower() #e.g. "needle" (no whitespace, lowercase)
    index = getIndex(craftName)   #e.g. 5 because needle count is stored in ary[5]
    if index != -1: craftAry[index]=craftAry[index]+num
  return craftAry

def getIndex(craftName):
  switcher = {
    "coin": 0, "coins": 0,
    "log": 1, "logs": 1,
    "cotton": 2,
    "rock": 3, "rocks": 3,
    "quartz": 4,
    "string": 5,
    "wood": 6,
    "ribbon": 7, "ribbons": 7,
    "metal": 8,
    "needle": 9, "needles": 9,
    "sparkle": 10, "sparkles": 10,
    "copper": 11, "bronze": 11,
    "silver": 12,
    "gold": 13,
    "amethyst": 14, "amethysts": 14,
    "pendant": 15, "pendants": 15,
    "necklace": 16, "necklaces": 16,
    "orb": 17, "orbs": 17,
    "water": 18,
    "fire": 19,
    "waterstone": 20, "waterstones": 20,
    "firestone": 21, "firestones": 21,
    "elementstone": 22, "elementstones": 22,
    "artifact": 23, "artifacts": 23
  }
  return switcher.get(craftName,-1)

def getRecipeDog(floor,deco):
  switcher = {
    # regular floors - ordered by level
    "dogpark":dogpark,    #1 - level where the floor is unlocked
    "fancyflat":fancyflat,
    "sleeping":sleeping,
    "backyard":backyard,
    "wolfpack":wolfpack,    #5
    "camping":camping,
    "japanesefood":japanesefood,
    "barbecue":barbecue,
    "arcade":arcade,
    "dimsum":dimsum,    #10
    "dessertshop":dessertshop,
    "gnomes":gnomes,
    "birthday":birthday,
    "underwater":underwater,
    "bookstore":bookstore,      #15
    "plush":plush,
    "mayhem":mayhem,
    "stationery":stationery,
    "mysterymansion":mysterymansion,
    "rainy":rainy,      #20
    "egypt":egypt,      
    "forest":forest,      
    "school":school,     
    "eighties":eighties,     
    "spicerack":spicerack,       #25
    "dream":dream,
    "magicshow":magicshow,
    "garden":garden,
    "farm":farm,
    "influencer":influencer,       #30
    "diner":diner,
    "plants":plants,
    "autumn":autumn,
    "profession":profession,
    "detective":detective, #35
    "jungle":jungle,
    "spy":spy,
    "punk":punk,
    "deconstructivism":deconstructivism,
    "egyptiantomb":egyptiantomb,  #40
    "shipwreck":shipwreck,
    "arctic":arctic,
    "cabin":cabin,
    "train":train,
    "bathroom":bathroom,   #45
    "dinosaurs":dinosaurs,
    "heavymetal":heavymetal,
    "sugarland":sugarland,
    "wrestling":wrestling,   
    "hairsalon":hairsalon,  #50
    "beach":beach,

    # for-purchase floors - alphabetical
    "atlantis":atlantis,
    "carousel":carousel,
    "catfloor":catfloor,
    "cosmicunicorns":cosmicunicorns,
    "doggydaycare":doggydaycare,
    "dogspa":dogspa,
    "donutfloat":donutfloat,
    "gemstone":gemstone,
    "gothic":gothic,
    "gourmet":gourmet,
    "highfashion":highfashion,
    "kpop":kpop,
    "minigolf":minigolf,
    "ocean":ocean,
    "stargazing":stargazing,
    "tarot":tarot,
    "wigs":wigs 
  }
  func = switcher.get(floorSpellcheckDog(floor), lambda1)
  try: decoInt = int(deco)
  except: return "Invalid deco number"
  return func(decoInt)

def lambda1(x): return "Invalid floor"

def floorSpellcheckDog(floor):
  floor=floor.strip().lower()
  if floor.startswith("japanese"): floor="japanesefood"
  elif floor.startswith("decon"): floor="deconstructivism"
  elif floor=="k-pop": floor="kpop"
  return floor



###### below is the dictionary of all crafting recipes ######

### regular floors ###

#dogpark - level 1
def dogpark(deco):
  switcher = {
    1: "2 Log, 20 Coins",
    2: "2 Log, 20 Coins",
    3: "1 Log, 3 Cotton, 50 Coins",
    4: "1 Log, 3 Cotton, 50 Coins",
    5: "4 Log, 2 Cotton, 100 Coins",
    6: "3 Log, 3 Cotton, 100 Coins",
    7: "5 Log, 6 Cotton, 200 Coins"
  }
  return switcher.get(deco,"")

#fancyflat - level 2
def fancyflat(deco):
  switcher = {
    1: "2 Log, 20 Coins",
    2: "2 Cotton, 20 Coins",
    3: "3 Log, 2 Cotton, 50 Coins",
    4: "5 Cotton, 50 Coins",
    5: "3 Log, 5 Cotton, 100 Coins",
    6: "4 Log, 4 Cotton, 100 Coins",
    7: "11 Log, 10 Cotton, 200 Coins"
  }
  return switcher.get(deco,"")

#sleeping - level 3
def sleeping(deco):
  switcher = {
    1: "5 Logs, 20 Coins",
    2: "5 Logs, 20 Coins",
    3: "5 Logs, 8 Cotton, 50 Coins",
    4: "5 Logs, 8 Cotton, 50 Coins",
    5: "10 Logs, 12 Cotton, 100 Coins",
    6: "12 Logs, 10 Cotton, 100 Coins",
    7: "21 Logs, 22 Cotton, 200 Coins"
  }
  return switcher.get(deco,"")

#backyard - level 4
def backyard(deco):
  switcher = {
    1: "2 Wood, 20 Coins",
    2: "2 String, 20 Coins",
    3: "1 Ribbon, 2 String, 50 Coins",
    4: "2 Wood, 1 Ribbon, 50 Coins",
    5: "5 Wood, 5 String, 100 Coins",
    6: "1 Ribbon, 5 String, 100 Coins",
    7: "5 Wood, 3 Ribbon, 4 String, 200 Coins"
  }
  return switcher.get(deco,"")

#wolfpack - level 5
def wolfpack(deco):
  switcher = {
    1: "4 Wood, 50 Coins",
    2: "4 Wood, 50 Coins",
    3: "1 Ribbon, 6 String, 160 Coins",
    4: "1 Ribbon, 6 String, 160 Coins",
    5: "3 Ribbon, 3 String, 260 Coins",
    6: "3 Ribbon, 3 String, 260 Coins",
    7: "9 Ribbon, 520 Coins"
  }
  return switcher.get(deco,"")

#camping - level 6
def camping(deco):
  switcher = {
    1: "5 String, 60 Coins",
    2: "5 Wood, 60 Coins",
    3: "1 Needle, 2 Metal, 190 Coins",
    4: "6 Wood, 5 Metal, 190 Coins",
    5: "1 Needle, 8 Metal, 310 Coins",
    6: "1 Needle, 8 Metal, 310 Coins",
    7: "1 Sparkle, 1 Needle, 1 Ribbon, 630 Coins"
  }
  return switcher.get(deco,"")

#japanesefood - level 7
def japanesefood(deco):
  switcher = {
    1: "2 Ribbon, 70 Coins",
    2: "6 String, 70 Coins",
    3: "7 Wood, 2 Ribbon, 220 Coins",
    4: "7 Wood, 7 Metal, 220 Coins",
    5: "2 Needles, 4 Metal, 360 Coins",
    6: "2 Needles, 4 Metal, 360 Coins",
    7: "1 Sparkle, 2 Needles, 2 Ribbon, 730 Coins"
  }
  return switcher.get(deco,"")

#barbecue - level 8
def barbecue(deco):
  switcher = {
    1: "7 Wood, 80 Coins",
    2: "7 String, 80 Coins",
    3: "2 Ribbons, 1 Needles, 260 Coins",
    4: "2 Ribbons, 1 Needle, 260 Coins",
    5: "1 Needle, 1 Sparkles, 420 Coins",
    6: "9 Metal, 2 Needles, 420 Coins",
    7: "4 Ribbons, 3 Needles, 1 Sparkles, 840 Coins"
  }
  return switcher.get(deco,"")

#arcade - level 9
def arcade(deco):
  switcher = {
    1: "3 Ribbon, 90 Coins",
    2: "8 Metal, 90 Coins",
    3: "6 Metal, 2 Needles, 290 Coins",
    4: "6 Metal, 2 Needles, 290 Coins",
    5: "4 Ribbons, 1 Sparkles, 470 Coins",
    6: "4 Ribbons, 1 Sparkles, 470 Coins",
    7: "3 Ribbon, 3 Needles, 2 Sparkles, 940 Coins"
  }
  return switcher.get(deco,"")

#dimsum - level 10
def dimsum(deco):
  switcher = {
    1: "1 Wood, 1 Needle, 100 Coins",
    2: "1 Wood, 1 Needle, 100 Coins",
    3: "3 Metal, 1 Sparkles, 320 Coins",
    4: "1 Needle, 1 Sparkles, 320 Coins",
    5: "6 Ribbon, 1 Sparkles, 520 Coins",
    6: "4 Needles, 8 Bronze, 520 Coins",
    7: "4 Needles, 2 Sparkles, 1 Silver, 1000 Coins"
  }
  return switcher.get(deco,"")

#WENDY from here on, coin costs are guesses based on CG costs

#dessertshop - level 11 #WENDY coins
def dessertshop(deco):
  switcher = {
    1: "6 Wood, 1 Needle, 110 Coins",
    2: "5 Metal, 5 Bronze, 110 Coins",
    3: "4 Ribbon, 1 Sparkles, 350 Coins",
    4: "4 Bronze, 1 Silver, 350 Coins",
    5: "2 Needles, 2 Sparkles, 570 Coins",
    6: "4 Needles, 1 Silver, 570 Coins",
    7: "1 Sparkles, 1 Silver, 1 Gold, 1100 Coins"
  }
  return switcher.get(deco,"")

#gnomes - level 12 #WENDY coins
def gnomes(deco):
  switcher = {
    1: "11 Wood, 11 String, 120 Coins",
    2: "8 String, 7 Bronze, 120 Coins",
    3: "8 Ribbon, 1 Sparkles, 390 Coins",
    4: "1 Sparkles, 1 Silver, 390 Coins",
    5: "3 Sparkles, 1 Silver, 630 Coins",
    6: "8 Ribbons, 7 Needles, 630 Coins",
    7: "4 Needles, 3 Sparkles, 3 Silver, 1200 Coins"
  }
  return switcher.get(deco,"")

#birthday - level 13 #WENDY coins
def birthday(deco):
  switcher = {
    1: "13 Wood, 12 Metal, 130 Coins",
    2: "5 Wood, 5 Ribbon, 130 Coins",
    3: "2 Sparkles, 1 Silver, 420 Coins",
    4: "10 Ribbon, 1 Silver, 420 Coins",
    5: "4 Needles, 3 Sparkles, 680 Coins",
    6: "6 Needles, 2 Silver, 680 Coins",
    7: "4 Sparkles, 2 Silver, 1 Gold, 1300 Coins"
  }
  return switcher.get(deco,"")

#underwater - level 14 #WENDY coins
def underwater(deco):
  switcher = {
    1: "2 Needles, 3 Ribbons, 140 Coins",
    2: "2 Needles, 3 Ribbons, 140 Coins",
    3: "6 Ribbon, 2 Silver, 450 Coins",
    4: "6 Ribbon, 2 Silver, 450 Coins",
    5: "1 Silver, 1 Gold, 730 Coins",
    6: "6 Needles, 3 Silver, 730 Coins",
    7: "2 Sparkles, 2 Silver, 2 Gold, 1400 Coins"
  }
  return switcher.get(deco,"")

#bookstore - level 15 #WENDY coins
def bookstore(deco):
  switcher = {
    1: "1 Amethyst, 1 Silver, 150 Coins",
    2: "3 Needles, 3 Ribbon, 150 Coins",
    3: "5 Needles, 2 Silver, 480 Coins",
    4: "5 Needles, 2 Silver, 480 Coins",
    5: "2 Silver, 1 Gold, 780 Coins",
    6: "6 Needles, 4 Silver, 780 Coins",
    7: "5 Silver, 1 Gold, 2 Pendant, 1500 Coins"
  }
  return switcher.get(deco,"")

#plush - level 16 #WENDY coins
def plush(deco):
  switcher = {
    1: "1 Sparkles, 4 Amethyst, 160 Coins",
    2: "6 Amethyst, 5 Ribbon, 160 Coins",
    3: "6 Needles, 2 Silver, 520 Coins",
    4: "1 Silver, 1 Pendant, 520 Coins",
    5: "9 Needles, 1 Gold, 840 Coins",
    6: "4 Sparkles, 1 Pendant, 840 Coins",
    7: "2 Silver, 2 Gold, 2 Pendant, 1600 Coins"
  }
  return switcher.get(deco,"")

#mayhem - level 17 #WENDY coins
def mayhem(deco):
  switcher = {
    1: "3 Ribbon, 1 Silver, 170 Coins",
    2: "5 Amethyst, 1 Sparkles, 170 Coins",
    3: "1 Needle, 1 Gold, 550 Coins",
    4: "3 Sparkles, 2 Silver, 550 Coins",
    5: "4 Silver, 1 Pendant, 890 Coins",
    6: "4 Silver, 1 Pendant, 890 Coins",
    7: "3 Silver, 2 Gold, 2 Pendant, 1700 Coins"
  }
  return switcher.get(deco,"")

#stationery - level 18 #WENDY coins
def stationery(deco):
  switcher = {
    1: "3 Needles, 1 Sparkles, 180 Coins",
    2: "4 Ribbon, 1 Silver, 180 Coins",
    3: "4 Needles, 3 Silver, 580 Coins",
    4: "1 Sparkles, 1 Gold, 580 Coins",
    5: "4 Silver, 1 Gold, 940 Coins",
    6: "1 Gold, 2 Pendant, 940 Coins",
    7: "4 Sparkles, 3 Silver, 3 Gold, 1800 Coins"
  }
  return switcher.get(deco,"")

#mysterymansion - level 19 #WENDY coins
def mysterymansion(deco):
  switcher = {
    1: "9 Amethyst, 10 Bronze, 190 Coins",
    2: "9 Amethyst, 10 Bronze, 190 Coins",
    3: "6 Needles, 1 Pendant, 610 Coins",
    4: "2 Sparkles, 1 Pendant, 610 Coins",
    5: "13 Needles, 1 Gold, 990 Coins",
    6: "2 Sparkles, 2 Pendant, 990 Coins",
    7: "3 Gold, 3 Pendant, 1900 Coins"
  }
  return switcher.get(deco,"")

#rainy - level 20 #WENDY coins
def rainy(deco):
  switcher = {
    1: "1 Amethyst, 1 Water, 200 Coins",
    2: "4 Orb, 1 Silver, 200 Coins",
    3: "4 Orb, 4 Silver, 650 Coins",
    4: "7 Needles, 2 Water, 650 Coins",
    5: "1 Gold, 2 Pendants, 1000 Coins",
    6: "1 Pendant, 1 Fire, 1000 Coins",
    7: "4 Water, 3 Fire, 2100 Coins"
  }
  return switcher.get(deco,"")

#egypt - level 21 #WENDY coins
def egypt(deco):
  switcher = {
    1: "3 Needles, 1 Silver, 210 Coins",
    2: "5 Orb, 1 Silver, 210 Coins",
    3: "1 Sparkles, 1 Fire, 680 Coins",
    4: "3 Sparkles, 3 Silver, 680 Coins",
    5: "4 Sparkles, 2 Pendants, 1100 Coins",
    6: "3 Silver, 2 Pendants, 1100 Coins",
    7: "4 Water, 3 Fire, 2200 Coins"
  }
  return switcher.get(deco,"")

#forest - level 22 #WENDY coins
def forest(deco):
  switcher = {
    1: "3 Ribbon, 1 Water, 220 Coins",
    2: "3 Needles, 1 Silver, 220 Coins",
    3: "3 Silver, 2 Water, 710 Coins",
    4: "3 Silver, 2 Water, 710 Coins",
    5: "4 Sparkles, 4 Water, 1100 Coins",
    6: "2 Pendant, 1 Fire, 1100 Coins",
    7: "1 Water, 1 Fire, 1 Necklace, 2300 Coins"
  }
  return switcher.get(deco,"")

#school - level 23 #WENDY coins
def school(deco):
  switcher = {
    1: "1 Water, 5 Amethyst, 230 Coins",
    2: "1 Water, 5 Amethyst, 230 Coins",
    3: "2 Water, 3 Silver, 740 Coins",
    4: "1 Gold, 1 Pendant, 740 Coins",
    5: "2 Water, 2 Gold, 1200 Coins",
    6: "4 Water, 5 Sparkles, 1200 Coins",
    7: "4 Sparkles, 4 Gold, 4 Silver, 2400 Coins"
  }
  return switcher.get(deco,"")

#eighties - level 24 #WENDY coins
def eighties(deco):
  switcher = {
    1: "1 Water, 6 Amethyst, 240 Coins",
    2: "1 Water, 5 Ribbon, 240 Coins",
    3: "3 Sparkles, 1 Gold, 780 Coins",
    4: "1 Waterstone, 2 Water, 780 Coins",
    5: "1 Waterstone, 1 Firestone, 1200 Coins",
    6: "2 Waterstone, 1 Fire, 1200 Coins",
    7: "2 Waterstone, 4 Water, 2 Fire, 2500 Coins"
  }
  return switcher.get(deco,"")

#spicerack - level 25 #WENDY coins
def spicerack(deco):
  switcher = {
    1: "7 Amethyst , 5 Needles, 250 Coins",
    2: "11 Amethyst, 9 Ribbon, 250 Coins",
    3: "1 Waterstone, 1 Pendant, 810 Coins",
    4: "1 Waterstone, 7 Needles, 810 Coins",
    5: "1 Firestone, 4 Silver, 1300 Coins",
    6: "4 Sparkles, 2 Gold, 1300 Coins",
    7: "2 Waterstone, 4 Water, 2 Fire, 2600 Coins"
  }
  return switcher.get(deco,"")

#dream - level 26 #WENDY coins
def dream(deco):
  switcher = {
    1: "8 Orb , 9 Amethyst, 260 Coins",
    2: "5 Needles, 7 Ribbon, 260 Coins",
    3: "6 Sparkles, 6 Needles, 840 Coins",
    4: "1 Waterstone, 2 Water, 840 Coins",
    5: "1 Waterstone, 3 Pendants, 1300 Coins",
    6: "1 Fire, 6 Silver, 1300 Coins",
    7: "3 Waterstone, 3 Water, 2 Fire, 2700 Coins"
  }
  return switcher.get(deco,"")

#magicshow - level 27 #WENDY coins
def magicshow(deco):
  switcher = {
    1: "8 Orb, 10 Amethyst, 270 Coins",
    2: "1 Water, 3 Needles, 270 Coins",
    3: "2 Water, 1 Gold, 870 Coins",
    4: "1 Gold, 2 Pendants, 870 Coins",
    5: "5 Water, 1 Fire, 1400 Coins",
    6: "2 Gold, 2 Pendants, 1400 Coins",
    7: "2 Waterstone, 1 Elementstone, 1 Firestone, 2800 Coins"
  }
  return switcher.get(deco,"")

#garden - level 28 #WENDY coins
def garden(deco):
  switcher = {
    1: "2 Sparkles, 7 Amethyst, 280 Coins",
    2: "1 Water, 2 Sparkles, 280 Coins",
    3: "1 Waterstone, 1 Fire, 910 Coins",
    4: "2 Water, 1 Fire, 910 Coins",
    5: "6 Sparkles, 1 Firestone, 1400 Coins",
    6: "1 Firestone, 5 Silver, 1400 Coins",
    7: "3 Waterstones, 1 Elementstone, 1 Firestones, 2900 Coins"
  }
  return switcher.get(deco,"")

#farm - level 29 #WENDY coins
def farm(deco):
  switcher = {
    1: "1 Water, 6 Orb, 290 Coins",
    2: "7 Orb, 5 Needles, 290 Coins",
    3: "1 Fire, 9 Needles, 940 Coins",
    4: "1 Waterstone, 3 Water, 940 Coins",
    5: "1 Pendant, 1 Elementstone, 1500 Coins",
    6: "7 Sparkles, 1 Firestone, 1500 Coins",
    7: "3 Waterstone, 1 Elementstone, 1 Firestone, 3000 Coins"
  }
  return switcher.get(deco,"")

#influencer - level 30 #WENDY coins
def influencer(deco):
  switcher = {
    1: "1 Water, 7 Orbs, 300 Coins",
    2: "1 Water, 2 Sparkles, 300 Coins",
    3: "1 Fire, 10 Needles, 970 Coins",
    4: "1 Fire, 1 Firestone, 970 Coins",
    5: "1 Sparkle, 1 Elementstone, 1500 Coins",
    6: "2 Waterstone, 1 Fire, 1500 Coins",
    7: "4 Water, 3 Pendants, 1 Necklace, 3100 Coins"
  }
  return switcher.get(deco,"")

#diner - level 31 #WENDY coins
def diner(deco):
  switcher = {
    1: "1 Water, 2 Sparkles, 310 Coins",
    2: "2 Needles, 2 Silver, 310 Coins",
    3: "1 Firestone, 1 Silver, 990 Coins",
    4: "1 Waterstone, 3 Water, 990 Coins",
    5: "3 Pendants, 1 Firestone, 1600 Coins",
    6: "2 Sparkles, 1 Elementstone, 1600 Coins",
    7: "2 Waterstone, 1 Elementstone, 2 Firestone, 3200 Coins"
  }
  return switcher.get(deco,"")

#plants - level 32 #WENDY coins
def plants(deco):
  switcher = {
    1: "1 Water, 2 Sparkles, 320 Coins",
    2: "1 Water, 5 Needles, 320 Coins",
    3: "1 Pendant, 1 Firestone, 1000 Coins",
    4: "4 Sparkles, 1 Fire, 1000 Coins",
    5: "2 Waterstone, 6 Sparkles, 1600 Coins",
    6: "1 Fire, 1 Elementstone, 1600 Coins",
    7: "5 Water, 2 Fire, 1 Necklace, 3300 Coins"
  }
  return switcher.get(deco,"")

#autumn - level 33 #WENDY coins
def autumn(deco):
  switcher = {
    1: "1 Water, 2 Silver, 330 Coins",
    2: "8 Orbs, 6 Needles, 330 Coins",
    3: "3 Water, 5 Sparkles, 1000 Coins",
    4: "4 Water, 1 Gold, 1000 Coins",
    5: "1 Gold, 1 Elementstone, 1700 Coins",
    6: "4 Sparkles, 4 Pendants, 1700 Coins",
    7: "2 Waterstone, 1 Elementstone, 2 Firestone, 3400 Coins"
  }
  return switcher.get(deco,"")

#profession - level 34 #WENDY coins
def profession(deco):
  switcher = {
    1: "2 Sparkles, 5 Needles, 340 Coins",
    2: "1 Pendant, 1 Orb, 340 Coins",
    3: "5 Sparkles, 5 Silver, 1100 Coins",
    4: "5 Sparkles, 1 Fire, 1100 Coins",
    5: "4 Water, 2 Fire, 1700 Coins",
    6: "1 Elementstone, 3 Silver, 1700 Coins",
    7: "3 Waterstone, 2 Fire, 2 Firestone, 3500 Coins"
  }
  return switcher.get(deco,"")

#detective - level 35 #WENDY coins
def detective(deco):
  switcher = {
    1: "1 Water, 10 Orbs, 350 Coins",
    2: "8 Ribbon, 2 Silver, 350 Coins",
    3: "3 Water, 5 Silver, 1100 Coins",
    4: "2 Pendants, 1 Fire, 1100 Coins",
    5: "6 Water, 8 Sparkles, 1800 Coins",
    6: "1 Fire, 1 Elementstone, 1800 Coins",
    7: "6 Water, 4 Pendant, 1 Necklace, 3600 Coins"
  }
  return switcher.get(deco,"")

#jungle - level 36 #WENDY coins
def jungle(deco):
  switcher = {
    1: "7 Orb, 2 Silver, 360 Coins",
    2: "7 Orb, 2 Silver, 360 Coins",
    3: "4 Water, 4 Sparkles, 1200 Coins",
    4: "2 Pendants, 1 Fire, 1200 Coins",
    5: "2 Pendants, 1 Elementstone, 1800 Coins",
    6: "2 Water, 2 Firestone, 1800 Coins",
    7: "3 Waterstone, 1 Elementstone, 2 Firestone, 3700 Coins"
  }
  return switcher.get(deco,"")

#spy - level 37 #WENDY coins
def spy(deco):
  switcher = {
    1: "4 Needles, 2 Silver, 370 Coins",
    2: "1 Water, 2 Sparkles, 370 Coins",
    3: "4 Water, 1 Fire, 1200 Coins",
    4: "1 Waterstone, 1 Firestone, 1200 Coins",
    5: "4 Water, 2 Fire, 1900 Coins",
    6: "2 Water, 2 Firestone, 1900 Coins",
    7: "3 Waterstone, 1 Elementstone, 2 Firestone, 3800 Coins"
  }
  return switcher.get(deco,"")

#WENDY from this point on, the recipes diverge from CG
#punk - level 38 #WENDY coins
def punk(deco):
  switcher = {
    1: "1 Water, 2 Silver, 380 Coins",
    2: "1 Water, 3 Sparkles, 380 Coins",
    3: "1 Waterstone, 2 Pendant, 1200 Coins",
    4: "1 Fire, 5 Silver, 1200 Coins",
    5: "3 Waterstone, 1 Firestone, 1900 Coins",
    6: "2 Gold, 1 Elementstone, 1900 Coins",
    7: "3 Pendant, 2 Fire, 2 Firestone, 3900 Coins"
  }
  return switcher.get(deco,"")

#deconstructivism - level 39 #WENDY coins
def deconstructivism(deco):
  switcher = {
    1: "3 Sparkles, 8 Ribbon, 390 Coins",
    2: "1 Water, 3 Sparkles, 390 Coins",
    3: "2 Waterstone, 2 Silver, 1200 Coins",
    4: "5 Silver, 1 Fire, 1200 Coins",
    5: "9 Sparkles, 9 Silver, 2000 Coins",
    6: "2 Pendants, 1 Elementstone, 2000 Coins",
    7: "4 Waterstone, 1 Elementstone, 2 Firestone, 4000 Coins"
  }
  return switcher.get(deco,"")

#egyptiantomb - level 40 #WENDY coins
def egyptiantomb(deco):
  switcher = {
    1: "1 Pendant, 4 Orbs, 400 Coins",
    2: "2 Water, 3 Orbs, 400 Coins",
    3: "1 Gold, 3 Pendants, 1300 Coins",
    4: "2 Gold, 1 Fire, 1300 Coins",
    5: "2 Pendants, 2 Firestone, 2100 Coins",
    6: "7 Sparkles, 3 Gold, 2100 Coins",
    7: "3 Waterstone, 3 Fire, 2 Firestone, 4200 Coins"
  }
  return switcher.get(deco,"")

#shipwreck - level 41 #WENDY coins
def shipwreck(deco):
  switcher = {
    1: "1 Water, 3 Sparkles, 410 Coins",
    2: "1 Water, 2 Silver, 410 Coins",
    3: "2 Gold, 2 Pendants, 1300 Coins",
    4: "1 Gold, 1 Firestone, 1300 Coins",
    5: "3 Gold, 2 Fire, 2100 Coins",
    6: "4 Water, 1 Elementstone, 2100 Coins",
    7: "4 Waterstone, 3 Fire, 2 Firestone, 4300 Coins"
  }
  return switcher.get(deco,"")

#arctic - level 42 #WENDY coins
def arctic(deco):
  switcher = {
    1: "8 Needles, 9 Orbs, 420 Coins",
    2: "8 Needles, 9 Orbs, 420 Coins",
    3: "4 Water, 1 Fire, 1300 Coins",
    4: "1 Firestone, 1 Fire, 1300 Coins",
    5: "1 Firestone, 1 Necklace, 2200 Coins",
    6: "1 Elementstone, 2 Fire, 2200 Coins",
    7: "4 Waterstone, 3 Fire, 2 Firestone, 4400 Coins"
  }
  return switcher.get(deco,"")

#cabin - level 43 #WENDY coins
def cabin(deco):
  switcher = {
    1: "8 Orb, 3 Sparkles, 430 coins",
    2: "1 Pendant, 3 Needles, 430 coins",
    3: "1 Waterstone, 1 Firestone, 1300 Coins",
    4: "1 Firestone, 5 Silver, 1300 Coins",
    5: "2 Firestone, 5 Silver, 2200 Coins",
    6: "2 Waterstone, 2 Fire, 2200 Coins",
    7: "2 Waterstone, 2 Elementstone, 2 Firestone, 4500 Coins"
  }
  return switcher.get(deco,"")

#train - level 44 #WENDY coins
def train(deco):
  switcher = {
    1: "9 Needles, 9 Orb, 440 coins",
    2: "6 Orb, 2 Water, 440 coins",
    3: "1 Fire, 2 Gold, 1400 Coins",
    4: "4 Water, 6 Silver, 1400 Coins",
    5: "4 Water, 2 Firestone, 2300 Coins",
    6: "3 Waterstone, 6 Silver, 2300 Coins",
    7: "3 Waterstone, 3 Fire, 3 Firestone, 4600 Coins"
  }
  return switcher.get(deco,"")

#bathroom - level 45 #WENDY coins
def bathroom(deco):
  switcher = {
    1: "1 Pendant, 7 Orb, 450 coins",
    2: "5 Orb, 3 Silver, 450 coins",
    3: "2 Fire, 2 Silver, 1400 Coins",
    4: "4 Water, 1 Firestone, 1400 Coins",
    5: "3 Pendant, 1 Elementstone, 2300 Coins",
    6: "2 Gold, 1 Elementstone, 2300 Coins",
    7: "2 Waterstone, 2 Elementstone, 2 Firestone, 4700 Coins"
  }
  return switcher.get(deco,"") 

#dinosaurs - level 46 #WENDY coins
def dinosaurs(deco):
  switcher = {
    1: "1 Pendant, 1 gold, 460 coins",
    2: "1 Pendant, 1 gold, 460 coins",
    3: "2 Fire, 2 water, 1400 Coins",
    4: "2 Fire, 2 water, 1400 Coins",
    5: "2 firestone, 1 Elementstone, 2400 Coins",
    6: "3 waterstone, 2 fire, 2400 Coins",
    7: "4 Waterstone, 3 fire, 3 Firestone, 4800 Coins"
  }
  return switcher.get(deco,"") 

#heavymetal - level 47 #WENDY coins
def heavymetal(deco):
  switcher = {
    1: "1 Pendant, 8 Orb, 470 coins",
    2: "1 Pendant, 8 Orb, 470 coins",
    3: "1 Fire, 2 waterstone, 1500 Coins",
    4: "1 Fire, 2 waterstone, 1500 Coins",
    5: "2 firestone, 1 Elementstone, 2400 Coins",
    6: "2 firestone, 2 waterstone, 2400 Coins",
    7: "3 Waterstone, 2 Elementstone, 2 Firestone, 4900 Coins"
  }
  return switcher.get(deco,"") 

#sugarland - level 48 #WENDY coins
def sugarland(deco):
  switcher = {
    1: "1 Pendant, 8 Orb, 480 coins",
    2: "1 Pendant, 8 Orb, 480 coins",
    3: "2 Waterstone, 1 Firestone, 1500 Coins",
    4: "2 Waterstone, 1 Firestone, 1500 Coins",
    5: "2 Pendant, 1 Necklace, 2500 Coins",
    6: "3 Water, 1 Necklace, 2500 Coins",
    7: "1 Artifact, 1 Elementstone, 2 Firestone, 5000 Coins"
  }
  return switcher.get(deco,"") 

#wrestling - level 49 #WENDY coins
def wrestling(deco):
  switcher = {
    1: "1 Gold, 1 Silver, 490 coins",
    2: "1 Gold, 1 Silver, 490 coins",
    3: "3 Water, 3 Pendant, 1500 Coins",
    4: "3 Water, 3 Pendant, 1500 Coins",
    5: "3 Gold, 4 Pendant, 2500 Coins",
    6: "3 Waterstone, 2 Fire, 2500 Coins",
    7: "3 Waterstone, 2 Fire, 2 Necklace, 5100 Coins"
  }
  return switcher.get(deco,"") 

#hairsalon - level 50 #WENDY coins
def hairsalon(deco):
  switcher = {
    1: "1 Pendant, 9 Orb, 500 coins",
    2: "1 Pendant, 9 Orb, 500 coins",
    3: "2 Waterstone, 1 Fire, 1600 Coins",
    4: "2 Waterstone, 1 Fire, 1600 Coins",
    5: "2 Pendant, 1 Necklace, 2600 Coins",
    6: "5 Water, 3 Fire, 2600 Coins",
    7: "3 Waterstone, 2 Elementstone, 3 Firestone, 5200 Coins"
  }
  return switcher.get(deco,"") 

#beach - level 51 #WENDY coins
def beach(deco):
  switcher = {
    1: "2 Water, 1 Pendant, 510 coins",
    2: "2 Water, 1 Pendant, 510 coins",
    3: "2 Waterstone, 2 Fire, 1600 Coins",
    4: "2 Waterstone, 2 Fire, 1600 Coins",
    5: "8 Water, 1 Necklace, 2600 Coins",
    6: "6 Water, 4 Fire, 2600 Coins",
    7: "4 Waterstone, 4 Fire, 3 Firestone, 5300 Coins"
  }
  return switcher.get(deco,"") 


### purchased floors ###

#atlantis #WENDY all guess
def atlantis(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbons, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbons, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#carousel #WENDY guessed on 2 through 7, sure of 1
def carousel(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbons, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbons, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#catfloor #WENDY all guess
def catfloor(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbons, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbons, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")
  
#cosmicunicorns
def cosmicunicorns(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbons, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbons, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#doggydaycare #WENDY unsure of all recipes
def doggydaycare(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbons, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbons, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#dogspa #WENDY unsure of all recipes
def dogspa(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbons, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbons, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#donutfloat #WENDY unsure of all recipes
def donutfloat(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbons, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbons, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#gemstone #WENDY all guessed
def gemstone(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbons, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbons, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#gothic #WENDY I am sure of 3 through 7
def gothic(deco):
  switcher = {
    1: "5 Wood, 100 Coins", #WENDY recipe and cost guess
    2: "5 String, 100 Coins", #WENDY recipe and cost guess
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbons, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbons, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#gourmet #WENDY all guess
def gourmet(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbons, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbons, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")
  
#highfashion #WENDY all guess
def highfashion(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbon, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbon, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")
  
#kpop #WENDY all guess
def kpop(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbon, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbon, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#minigolf #WENDY all guess
def minigolf(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbon, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbon, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#ocean #WENDY all guess
def ocean(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbon, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbon, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#stargazing #WENDY all guess
def stargazing(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbon, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbon, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#tarot #WENDY all guess
def tarot(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbon, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbon, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#wigs #WENDY all guess
def wigs(deco):
  switcher = {
    1: "5 Wood, 100 Coins",
    2: "5 String, 100 Coins",
    3: "2 Metal, 1 Needle, 320 Coins",
    4: "2 Metal, 1 Needle, 320 Coins",
    5: "7 String, 3 Ribbon, 520 Coins",
    6: "8 Metal, 1 Needle, 520 Coins",
    7: "4 Ribbon, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

