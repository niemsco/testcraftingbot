def getCraftsCat(decolist):
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
  recipe = getRecipeCat(floor,deco)  #e.g. "2 Metal, 1 Needle, 320 Coins"
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

def getRecipeCat(floor,deco):
  switcher = {
    # regular floors - ordered by level
    "basic":basic,    #1 - level where the floor is unlocked
    "fancy":fancy,
    "posh":posh,
    "mayhem":mayhem,
    "beach":beach,    #5
    "farm":farm,
    "plant":plant,
    "forest":forest,
    "dessert":dessert,
    "dream":dream,    #10
    "woods":woods,
    "galactic":galactic,
    "eighties":eighties,
    "oasis":oasis,
    "reef":reef,      #15
    "garden":garden,
    "nightmare":nightmare,
    "ocean":ocean,
    "pyramid":pyramid,
    "cake":cake,      #20
    "interstellar":interstellar,      
    "punk":punk,      
    "african":african,     
    "profession":profession,     
    "bugs":bugs,       #25
    "winter":winter,
    "spring":spring,
    "autumn":autumn,
    "school":school,
    "dogs":dogs,       #30
    "diner":diner,
    "sports":sports,
    "desert":desert,
    "dinosaurs":dinosaurs,
    "hairsalon":hairsalon, #35
    "heavymetal":heavymetal,
    "western":western,
    "racing":racing,
    "mysterymansion":mysterymansion,
    "stationery":stationery,  #40
    "magicshow":magicshow,
    "camping":camping,
    "plush":plush,
    "roleplay":roleplay,
    "bathroom":bathroom,   #45
    "jungle":jungle,
    "skatepark":skatepark,
    "arctic":arctic,
    "detective":detective,
    "catgamedev":catgamedev,   #50
    "cruise":cruise,
    "birthday":birthday,
    "arcade":arcade,
    "tattooshop":tattooshop,
    "airport":airport,   #55
    "smallpets":smallpets,
    "hippie":hippie,
    "pirates":pirates,
    "hospital":hospital,
    "playground":playground,   #60
    "shipwreck":shipwreck,
    "gnomes":gnomes,
    "deconstructivism":deconstructivism,
    "caveman":caveman,
    "miniature":miniature,   #65
    "wrestling":wrestling,
    "laundromat":laundromat,
    "infant":infant,
    "tropicalfruits":tropicalfruits,
    "gelatin":gelatin,      #70
    "baking":baking, "bakingprestige":bakingprestige,
    "yardsale":yardsale, "yardsaleprestige":yardsaleprestige,
    "deli":deli, "deliprestige":deliprestige,
    "rainy":rainy, "rainyprestige":rainyprestige,
    "minigolf":minigolf, "minigolfprestige":minigolfprestige,

    # for-purchase floors - alphabetical
    "aquarium":aquarium,
    "archery":archery,
    "asianfood":asianfood, "asianfoodprestige":asianfoodprestige,
    "atlantis":atlantis, "atlantisprestige":atlantisprestige,
    "autumnwalk":autumnwalk, "autumnwalkprestige":autumnwalkprestige,
    "balconygarden":balconygarden, "balconygardenprestige":balconygardenprestige,
    "bread":bread, "breadprestige":breadprestige,
    "carousel":carousel,
    "catcafe":catcafe,
    "corn":corn,
    "duck":duck,
    "freshfruit":freshfruit,
    #"garfield":garfield,
    "hatcats":hatcats, "hatcatsprestige":hatcatsprestige,
    "minobeach":minobeach, "minobeachprestige":minobeachprestige,
    "minoforest":minoforest, "minoforestprestige":minoforestprestige,
    "outdoorpool":outdoorpool, "outdoorpoolprestige":outdoorpoolprestige,
    "supercatsquad":supercatsquad, "supercatsquadprestige":supercatsquadprestige,
    "waterfight":waterfight,
    "waterpark":waterpark

  }
  func = switcher.get(floorSpellcheckCat(floor), lambda1)
  try: decoInt = int(deco)
  except: return "Invalid deco number"
  return func(decoInt)

def lambda1(x): return "Invalid floor"

def floorSpellcheckCat(floor):
  floor=floor.strip().lower()
  if floor.startswith("decon"): floor="deconstructivism"
  return floor



###### below is the dictionary of all crafting recipes ######

### regular floors ###

#basic - level 1
def basic(deco):
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

#fancy - level 2
def fancy(deco):
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

#posh - level 3
def posh(deco):
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

#mayhem - level 4
def mayhem(deco):
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

#beach - level 5
def beach(deco):
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

#farm - level 6
def farm(deco):
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

#plant - level 7
def plant(deco):
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

#forest - level 8
def forest(deco):
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

#dessert - level 9
def dessert(deco):
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

#dream - level 10
def dream(deco):
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

#woods - level 11
def woods(deco):
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

#galactic - level 12
def galactic(deco):
  switcher = {
    1: "6 Wood, 11 String, 120 Coins", #WENDY check?
    2: "8 String, 7 Bronze, 120 Coins",
    3: "8 Ribbon, 1 Sparkles, 390 Coins",
    4: "1 Sparkles, 1 Silver, 390 Coins",
    5: "3 Sparkles, 1 Silver, 630 Coins",
    6: "8 Ribbons, 7 Needles, 630 Coins",
    7: "4 Needles, 3 Sparkles, 3 Silver, 1200 Coins"
  }
  return switcher.get(deco,"")

#eighties - level 13
def eighties(deco):
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

#oasis - level 14
def oasis(deco):
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

#reef - level 15
def reef(deco):
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

#garden - level 16
def garden(deco):
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

#nightmare - level 17
def nightmare(deco):
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

#ocean - level 18
def ocean(deco):
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

#pyramid - level 19
def pyramid(deco):
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

#cake - level 20
def cake(deco):
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

#interstellar - level 21
def interstellar(deco):
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

#punk - level 22
def punk(deco):
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

#african - level 23
def african(deco):
  switcher = {
    1: "1 Water, 5 Amethyst, 230 Coins",
    2: "1 Water, 5 Amethyst, 230 Coins",
    3: "2 Water, 3 Silver, 740 Coins",
    4: "1 Gold, 1 Pendant, 740 Coins",
    5: "2 Water, 2 Gold, 1200 Coins",
    6: "3 Water, 5 Sparkles, 1200 Coins", #WENDY check?
    7: "4 Sparkles, 4 Gold, 4 Silver, 2400 Coins"
  }
  return switcher.get(deco,"")

#profession - level 24
def profession(deco):
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

#bugs - level 25
def bugs(deco):
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

#winter - level 26
def winter(deco):
  switcher = {
    1: "8 Orb , 9 Amethyst, 260 Coins",
    2: "5 Needles, 7 Ribbon, 260 Coins",
    3: "6 Sparkles, 6 Needles, 840 Coins",
    4: "1 Waterstone, 2 Water, 840 Coins",
    5: "1 Waterstone, 3 Pendants, 1300 Coins",
    6: "1 Firestone, 6 Silver, 1300 Coins", #WENDY check?
    7: "3 Waterstone, 3 Water, 2 Fire, 2700 Coins"
  }
  return switcher.get(deco,"")

#spring - level 27
def spring(deco):
  switcher = {
    1: "8 Orb, 10 Amethyst, 270 Coins",
    2: "1 Water, 3 Needles, 270 Coins",
    3: "2 Water, 1 Gold, 870 Coins",
    4: "1 Gold, 2 Pendants, 870 Coins",
    5: "5 Water, 1 Fire, 1400 Coins",
    6: "2 Gold, 2 Pendants, 1400 Coins",
    7: "2 Waterstone, 1 Elementstone, 2 Firestone, 2800 Coins" #WENDY check
  }
  return switcher.get(deco,"")

#autumn - level 28
def autumn(deco):
  switcher = {
    1: "2 Sparkles, 7 Amethyst, 280 Coins",
    2: "1 Water, 2 Sparkles, 280 Coins",
    3: "1 Waterstone, 1 Fire, 910 Coins",
    4: "2 Water, 1 Fire, 910 Coins",
    5: "6 Sparkles, 1 Firestone, 1400 Coins",
    6: "1 Firestone, 5 Silver, 1400 Coins",
    7: "3 Waterstones, 1 Elementstone, 2 Firestones, 2900 Coins" #WENDY check
  }
  return switcher.get(deco,"")

#school - level 29
def school(deco):
  switcher = {
    1: "1 Water, 6 Orb, 290 Coins",
    2: "7 Orb, 5 Needles, 290 Coins",
    3: "1 Fire, 9 Needles, 940 Coins",
    4: "1 Waterstone, 3 Water, 940 Coins",
    5: "1 Pendant, 1 Elementstone, 1500 Coins",
    6: "7 Sparkles, 1 Firestone, 1500 Coins",
    7: "3 Waterstone, 1 Elementstone, 2 Firestone, 3000 Coins" #WENDY check
  }
  return switcher.get(deco,"")

#dogs - level 30
def dogs(deco):
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

#diner - level 31
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

#sports - level 32
def sports(deco):
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

#desert - level 33
def desert(deco):
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

#dinosaurs - level 34
def dinosaurs(deco):
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

#hairsalon - level 35
def hairsalon(deco):
  switcher = {
    1: "1 Water, 10 Orbs, 350 Coins",
    2: "8 Ribbon, 2 Silver, 350 Coins",
    3: "3 Water, 5 Silver, 1100 Coins",
    4: "2 Pendants, 1 Fire, 1100 Coins",
    5: "6 Water, 8 Sparkles, 1800 Coins",
    6: "1 Fire, 1 Elementstone, 1800 Coins",
    7: "6 Water, 4 Pendant, 1 Necklace, 3600 Coins" #WENDY wiki said 1800 but this is my best guess
  }
  return switcher.get(deco,"")

#heavymetal - level 36
def heavymetal(deco):
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

#western - level 37
def western(deco):
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

#racing - level 38
def racing(deco):
  switcher = {
    1: "3 Sparkles, 8 Ribbon, 380 Coins",
    2: "1 Water, 3 Sparkles, 380 Coins",
    3: "2 Waterstone, 2 Silver, 1200 Coins",
    4: "1 Fire, 5 Silver, 1200 Coins",
    5: "9 Sparkles, 9 Silver, 1900 Coins",
    6: "2 Pendant, 1 Elementstone, 1900 Coins",
    7: "4 Waterstone, 1 Elementstone, 2 Firestone, 3900 Coins"
  }
  return switcher.get(deco,"")

#mysterymansion - level 39
def mysterymansion(deco):
  switcher = {
    1: "1 Pendant, 4 Orb, 390 Coins",
    2: "2 Water, 3 Orb, 390 Coins",
    3: "1 Gold, 3 Pendant, 1200 Coins",
    4: "2 Gold, 1 Fire, 1200 Coins",
    5: "2 Pendant, 2 Firestone, 2000 Coins",
    6: "7 Sparkles, 3 Gold, 2000 Coins",
    7: "3 Waterstone, 3 Fire, 2 Firestone, 4000 Coins"
  }
  return switcher.get(deco,"")

#stationery - level 40
def stationery(deco):
  switcher = {
    1: "1 Water, 3 Sparkles, 400 Coins",
    2: "1 Water, 2 Silver, 400 Coins",
    3: "2 Gold, 2 Pendants, 1300 Coins",
    4: "1 Gold, 1 Firestone, 1300 Coins",
    5: "3 Gold, 2 Fire, 2100 Coins",
    6: "4 Water, 1 Elementstone, 2100 Coins",
    7: "4 Waterstone, 3 Fire, 2 Firestone, 4200 Coins"
  }
  return switcher.get(deco,"")

#magicshow - level 41
def magicshow(deco):
  switcher = {
    1: "9 Orb, 8 Needle, 410 Coins",
    2: "9 Orb, 8 Needle, 410 Coins",
    3: "4 Water, 1 Fire, 1300 Coins",
    4: "1 Fire, 1 Firestone, 1300 Coins",
    5: "1 Pendant, 1 Firestone, 2100 Coins",
    6: "2 Fire, 1 Elementstone, 2100 Coins",
    7: "4 Waterstone, 3 Fire, 2 Firestone, 4300 Coins"
  }
  return switcher.get(deco,"")

#camping - level 42
def camping(deco):
  switcher = {
    1: "3 Sparkle, 8 Orbs, 420 Coins",
    2: "1 Pendant, 3 Needle, 420 Coins",
    3: "1 Waterstone, 1 Firestone, 1300 Coins",
    4: "1 Firestone, 5 Metal, 1300 Coins",
    5: "2 Firestone, 5 Metal, 2200 Coins",
    6: "2 Waterstone, 2 Fire, 2200 Coins",
    7: "2 Waterstone, 2 Elementstone, 2 Firestone, 4400 Coins"
  }
  return switcher.get(deco,"")

#WENDY from here on, most coin costs are guesses. I used these guesses:
#commons: 10*level
#legendary: +100 each level except +200 on levels that are multipls of20
#epics: legendary/2, rounded down to multiple of 100
#rares: (common+common+legendary)/4 e.g. (430+430+4500)/4 rounded to nearest 100

#plush - level 43
def plush(deco): #WENDY coins
  switcher = {
    1: "9 Orb, 9 Needle, 430 coins",
    2: "2 Water, 6 Orb, 430 coins",
    3: "2 Gold, 1 Fire, 1300 Coins",
    4: "4 Water, 6 Silver, 1300 Coins",
    5: "4 Water, 2 Firestone, 2200 Coins",
    6: "3 Waterstone, 6 Silver, 2200 Coins",
    7: "3 Waterstone, 3 Fire, 3 Firestone, 4500 Coins"
  }
  return switcher.get(deco,"")

#roleplay - level 44 #WENDY coins
def roleplay(deco):
  switcher = {
    1: "1 Pendant, 7 Orb, 440 coins",
    2: "5 Orb, 3 Silver, 440 coins",
    3: "2 Fire, 2 Silver, 1400 Coins",
    4: "4 Water, 1 Firestone, 1400 Coins",
    5: "3 Pendant, 1 Elementstone, 2300 Coins",
    6: "2 Gold, 1 Elementstone, 2300 Coins",
    7: "2 Waterstone, 2 Elementstone, 2 Firestone, 4600 Coins"
  }
  return switcher.get(deco,"")

#bathroom - level 45 #WENDY coins
def bathroom(deco):
  switcher = {
    1: "2 Water, 7 Orb, 450 coins",
    2: "1 Pendant, 7 Orb, 450 coins",
    3: "2 Waterstone, 3 Water, 1400 Coins",
    4: "2 Waterstone, 3 Water, 1400 Coins",
    5: "2 Waterstone, 2 Firestone, 2300 Coins",
    6: "2 Fire, 2 Firestone, 2300 Coins",
    7: "2 Waterstone, 2 Fire, 2 Necklace, 4700 Coins"
  }
  return switcher.get(deco,"") 

#jungle - level 46 #WENDY coins
def jungle(deco):
  switcher = {
    1: "1 Gold, 1 Pendant, 460 coins",
    2: "1 Gold, 1 Pendant, 460 coins",
    3: "2 Water, 2 Fire, 1400 Coins",
    4: "2 Water, 2 Fire, 1400 Coins",
    5: "1 Elementstone, 2 Firestone, 2400 Coins",
    6: "3 Waterstone, 2 Fire, 2400 Coins",
    7: "4 Waterstone, 3 Fire, 3 Firestone, 4800 Coins"
  }
  return switcher.get(deco,"") 

#skatepark - level 47 #WENDY coins
def skatepark(deco):
  switcher = {
    1: "1 Pendant, 8 Orb, 470 coins",
    2: "1 Pendant, 8 Orb, 470 coins",
    3: "2 Waterstone, 1 Fire, 1500 Coins",
    4: "2 Waterstone, 1 Fire, 1500 Coins",
    5: "1 Elementstone, 2 Firestone, 2400 Coins",
    6: "2 Waterstone, 2 Firestone, 2400 Coins",
    7: "3 Waterstone, 2 Elementstone, 2 Firestone, 4900 Coins"
  }
  return switcher.get(deco,"") 

#arctic - level 48 #WENDY coins
def arctic(deco):
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

#detective - level 49 #WENDY coins
def detective(deco):
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

#catgamedev - level 50 #WENDY coins
def catgamedev(deco):
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

#cruise - level 51 #WENDY coins
def cruise(deco):
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

#birthday - level 52 #WENDY coins
def birthday(deco):
  switcher = {
    1: "2 Water, 1 Pendant, 520 coins",
    2: "2 Water, 1 Pendant, 520 coins",
    3: "5 Water, 2 Fire, 1600 Coins",
    4: "5 Water, 2 Fire, 1600 Coins",
    5: "4 Gold, 5 Pendant, 2700 Coins",
    6: "4 Pendant, 1 Necklace, 2700 Coins",
    7: "3 Pendant, 3 Fire, 2 Necklace, 5400 Coins"
  }
  return switcher.get(deco,"") 

#arcade - level 53 #WENDY coins
def arcade(deco):
  switcher = {
    1: "4 Sparkles, 3 Silver, 530 coins",
    2: "4 Sparkles, 3 Silver, 530 coins",
    3: "2 Gold, 4 Pendant, 1600 Coins",
    4: "2 Gold, 4 Pendant, 1600 Coins",
    5: "5 Pendant, 1 Necklace, 2700 Coins",
    6: "4 Gold, 5 Pendant, 2700 Coins",
    7: "3 Gold, 5 Pendant, 2 Necklace, 5500 Coins"
  }
  return switcher.get(deco,"") 

#tattooshop - level 54 #WENDY coins
def tattooshop(deco):
  switcher = {
    1: "5 Sparkles, 7 Needles, 540 coins",
    2: "5 Sparkles, 7 Needles, 540 coins",
    3: "3 Gold, 6 Silver, 1700 Coins",
    4: "3 Gold, 6 Silver, 1700 Coins",
    5: "9 Water, 1 Necklace, 2800 Coins",
    6: "4 Waterstone, 2 Firestone, 2800 Coins",
    7: "1 Artifact, 1 Elementstone, 3 Firestone, 5600 Coins" #WENDY check on this recipe
  }
  return switcher.get(deco,"") 

#airport - level 55 #WENDY coins
def airport(deco):
  switcher = {
    1: "1 Water, 1 Fire, 550 coins",
    2: "1 Water, 1 Fire, 550 coins",
    3: "3 Waterstone, 1 Firestone, 1700 Coins",
    4: "3 Waterstone, 1 Firestone, 1700 Coins",
    5: "6 Gold, 7 Silver, 2800 Coins",
    6: "9 Water, 1 Necklace, 2800 Coins",
    7: "4 Waterstone, 4 Fire, 3 Firestone, 5700 Coins"
  }
  return switcher.get(deco,"") 

#smallpets - level 56 #WENDY coins
def smallpets(deco):
  switcher = {
    1: "1 Gold, 3 Silver, 560 coins",
    2: "1 Gold, 3 Silver, 560 coins",
    3: "1 Pendant, 1 Necklace, 1700 Coins",
    4: "1 Pendant, 1 Necklace, 1700 Coins",
    5: "4 Waterstone, 3 Fire, 2900 Coins",
    6: "10 Water, 1 Necklace, 2900 Coins",
    7: "4 Waterstone, 4 Fire, 3 Firestone, 5800 Coins"
  }
  return switcher.get(deco,"") 

#hippie - level 57 #WENDY coins
def hippie(deco):
  switcher = {
    1: "1 Gold, 3 Silver, 570 coins",
    2: "1 Gold, 3 Silver, 570 coins",
    3: "2 Water, 1 Necklace, 1800 Coins",
    4: "2 Water, 1 Necklace, 1800 Coins",
    5: "5 Water, 5 Fire, 2900 Coins",
    6: "1 Elementstone, 3 Firestone, 2900 Coins",
    7: "1 Artifact, 1 Elementstone, 3 Firestone, 5900 Coins"
  }
  return switcher.get(deco,"") 

#pirates - level 58 #WENDY coins
def pirates(deco):
  switcher = {
    1: "1 Waterstone, 1 Fire, 580 coins",
    2: "1 Waterstone, 1 Fire, 580 coins",
    3: "1 Elementstone, 1 Firestone, 1800 Coins",
    4: "1 Elementstone, 1 Firestone, 1800 Coins",
    5: "4 Waterstone, 3 Fire, 3000 Coins",
    6: "6 Pendant, 1 Necklace, 3000 Coins",
    7: "4 Gold, 6 Pendant, 2 Necklace, 6000 Coins"
  }
  return switcher.get(deco,"") 

#hospital - level 59 #WENDY coins
def hospital(deco):
  switcher = {
    1: "6 Sparkles, 6 Needles, 590 coins",
    2: "6 Sparkles, 6 Needles, 590 coins",
    3: "4 Gold, 4 Silver, 1800 Coins",
    4: "4 Gold, 4 Silver, 1800 Coins",
    5: "6 Water, 5 Fire, 3000 Coins",
    6: "3 Waterstone, 3 Firestone, 3000 Coins",
    7: "5 Waterstone, 2 Elementstone, 3 Firestone, 6100 Coins"
  }
  return switcher.get(deco,"") 

#playground - level 60 #WENDY coins
def playground(deco):
  switcher = {
    1: "2 Water, 1 Fire, 600 coins",
    2: "2 Water, 1 Fire, 600 coins",
    3: "3 Waterstone, 2 Fire, 1900 Coins",
    4: "3 Waterstone, 2 Fire, 1900 Coins",
    5: "2 Elementstone, 2 Firestone, 3100 Coins",
    6: "6 Water, 5 Fire, 3100 Coins",
    7: "4 Waterstone, 3 Fire, 2 Necklace, 6300 Coins"
  }
  return switcher.get(deco,"") 

#shipwreck - level 61 #WENDY coins
def shipwreck(deco):
  switcher = {
    1: "1 Gold, 3 Silver, 610 coins",
    2: "1 Gold, 3 Silver, 610 coins",
    3: "2 Pendant, 1 Necklace, 1900 Coins",
    4: "2 Pendant, 1 Necklace, 1900 Coins",
    5: "3 Waterstone, 3 Firestone, 3200 Coins",
    6: "1 Artifact, 1 Elementstone, 3200 Coins",
    7: "1 Artifact, 2 Elementstone, 2 Firestone, 6400 Coins"
  }
  return switcher.get(deco,"") 

#gnomes - level 62 #WENDY coins
def gnomes(deco):
  switcher = {
    1: "1 Waterstone, 1 Fire, 620 coins",
    2: "1 Waterstone, 1 Fire, 620 coins",
    3: "1 Elementstone, 2 Firestone, 1900 Coins",
    4: "1 Elementstone, 2 Firestone, 1900 Coins",
    5: "6 Pendant, 1 Necklace, 3200 Coins",
    6: "4 Waterstone, 4 Fire, 3200 Coins",
    7: "5 Waterstone, 4 Fire, 4 Firestone, 6500 Coins"
  }
  return switcher.get(deco,"") 

#deconstructivism - level 63 #WENDY coins except I'm sure of 7
def deconstructivism(deco):
  switcher = {
    1: "1 Waterstone, 1 Fire, 630 coins",
    2: "1 Waterstone, 1 Fire, 630 coins",
    3: "1 Elementstone, 2 Firestone, 2000 Coins",
    4: "1 Elementstone, 2 Firestone, 2000 Coins",
    5: "6 Pendant, 1 Necklace, 3300 Coins",
    6: "4 Waterstone, 4 Fire, 3300 Coins",
    7: "5 Waterstone, 4 Fire, 4 Firestone, 6600 coins"
  }
  return switcher.get(deco,"") 

#caveman - level 64 
def caveman(deco):
  switcher = {
    1: "1 Waterstone, 1 Fire, 640 coins",
    2: "1 Waterstone, 1 Fire, 640 coins",
    3: "1 Elementstone, 2 Firestone, 2000 coins",
    4: "1 Elementstone, 2 Firestone, 2000 coins",
    5: "6 Pendant, 1 Necklace, 3300 coins",
    6: "4 Waterstone, 4 Fire, 3300 coins",
    7: "5 Waterstone, 4 Fire, 4 Firestone, 6700 coins"
  }
  return switcher.get(deco,"") 

#miniature - level 65  
def miniature(deco): #WENDY coins
  switcher = {
    1: "1 Waterstone, 1 Fire, 650 coins",
    2: "1 Waterstone, 1 Fire, 650 coins",
    3: "1 Elementstone, 2 Firestone, 2000 Coins",
    4: "1 Elementstone, 2 Firestone, 2000 Coins",
    5: "6 Pendant, 1 Necklace, 3400 Coins",
    6: "4 Waterstone, 4 Fire, 3400 Coins",
    7: "5 Waterstone, 4 Fire, 4 Firestone, 6800 Coins"
  }
  return switcher.get(deco,"") 

#wrestling - level 66  
def wrestling(deco): #WENDY coins
  switcher = {
    1: "1 Waterstone, 1 Fire, 660 coins",
    2: "1 Waterstone, 1 Fire, 660 coins",
    3: "1 Elementstone, 2 Firestone, 2100 Coins",
    4: "1 Elementstone, 2 Firestone, 2100 Coins",
    5: "6 Pendant, 1 Necklace, 3400 Coins",
    6: "4 Waterstone, 4 Fire, 3400 Coins",
    7: "5 Waterstone, 4 Fire, 4 Firestone, 6900 Coins"
  }
  return switcher.get(deco,"") 

#laundromat - level 67 
def laundromat(deco): #WENDY coins except I'm sure of 5-7
  switcher = {
    1: "1 Waterstone, 1 Fire, 670 coins",
    2: "1 Waterstone, 1 Fire, 670 coins",
    3: "1 Elementstone, 2 Firestone, 2100 Coins",
    4: "1 Elementstone, 2 Firestone, 2100 Coins",
    5: "6 Pendant, 1 Necklace, 3500 Coins",
    6: "4 Waterstone, 4 Fire, 3500 Coins",
    7: "5 Waterstone, 4 Fire, 4 Firestone, 7000 Coins"
  }
  return switcher.get(deco,"") 

#infant - level 68 
def infant(deco): #WENDY coins only unsure of 1,2
  switcher = {
    1: "1 Waterstone, 1 Fire, 680 coins",
    2: "1 Waterstone, 1 Fire, 680 coins",
    3: "1 Elementstone, 2 Firestone, 2200 Coins",
    4: "1 Elementstone, 2 Firestone, 2200 Coins",
    5: "6 Pendant, 1 Necklace, 3500 Coins",
    6: "4 Waterstone, 4 Fire, 3500 Coins",
    7: "5 Waterstone, 4 Fire, 4 Firestone, 7100 Coins"
  }
  return switcher.get(deco,"") 

#tropicalfruits - level 69 
def tropicalfruits(deco): 
  switcher = {
    1: "1 firestone, 1 pendant, 690 coins",
    2: "1 firestone, 1 pendant, 690 coins",
    3: "1 Elementstone, 3 gold, 15 orb, 2200 Coins",
    4: "1 Elementstone, 3 gold, 15 orb, 2200 Coins",
    5: "1 Necklace, 4 waterstone, 3600 Coins",
    6: "1 artifact, 1 fire, 15 orb, 3600 Coins",
    7: "1 artifact, 4 waterstone, 4 firestone, 7200 Coins"
  }
  return switcher.get(deco,"") 

#gelatin - level 70 
def gelatin(deco):
  switcher = {
    1: "2 firestone, 2 pendant, 700 coins",
    2: "2 firestone, 2 pendant, 700 coins",
    3: "2 Elementstone, 5 gold, 20 orb, 2200 Coins",
    4: "2 Elementstone, 5 gold, 20 orb, 2200 Coins",
    5: "2 Necklace, 6 waterstone, 3600 Coins",
    6: "2 artifact, 2 fire, 20 orb, 3600 Coins",
    7: "2 artifact, 6 waterstone, 6 firestone, 7300 Coins"
  }
  return switcher.get(deco,"") 

#baking - level 71
def baking(deco):
  switcher = {
    1: "3 firestone, 3 pendant, 710 coins",
    2: "3 firestone, 3 pendant, 710 coins",
    3: "3 Elementstone, 7 gold, 25 orb, 2300 Coins",
    4: "3 Elementstone, 7 gold, 25 orb, 2300 Coins",
    5: "3 Necklace, 8 waterstone, 3700 Coins",
    6: "3 artifact, 3 fire, 25 orb, 3700 Coins",
    7: "3 artifact, 8 waterstone, 8 firestone, 7400 Coins"
  }
  return switcher.get(deco,"") 
def bakingprestige(deco): #bakingprestige
  switcher = {
    1: "6 firestone, 6 pendant, 710 coins",
    2: "6 firestone, 6 pendant, 710 coins",
    3: "6 Elementstone, 14 gold, 50 orb, 2300 Coins",
    4: "6 Elementstone, 14 gold, 50 orb, 2300 Coins",
    5: "6 Necklace, 16 waterstone, 3700 Coins",
    6: "6 artifact, 6 fire, 50 orb, 3700 Coins",
    7: "6 artifact, 16 waterstone, 16 firestone, 7400 Coins"
  }
  return switcher.get(deco,"") 

#yardsale - level 72
def yardsale(deco):
  switcher = {
    1: "3 firestone, 3 pendant, 720 coins",
    2: "3 firestone, 3 pendant, 720 coins",
    3: "3 Elementstone, 7 gold, 25 orb, 2300 Coins",
    4: "3 Elementstone, 7 gold, 25 orb, 2300 Coins",
    5: "3 Necklace, 8 waterstone, 3700 Coins",
    6: "3 artifact, 3 fire, 25 orb, 3700 Coins",
    7: "3 artifact, 8 waterstone, 8 firestone, 7500 Coins"
  }
  return switcher.get(deco,"") 
def yardsaleprestige(deco): #yardsaleprestige
  switcher = {
    1: "6 firestone, 6 pendant, 720 coins",
    2: "6 firestone, 6 pendant, 720 coins",
    3: "6 Elementstone, 14 gold, 50 orb, 2300 Coins",
    4: "6 Elementstone, 14 gold, 50 orb, 2300 Coins",
    5: "6 Necklace, 16 waterstone, 3700 Coins",
    6: "6 artifact, 6 fire, 50 orb, 3700 Coins",
    7: "6 artifact, 16 waterstone, 16 firestone, 7500 Coins"
  }
  return switcher.get(deco,"") 

#deli - level 73
def deli(deco):
  switcher = {
    1: "3 firestone, 3 pendant, 730 coins",
    2: "3 firestone, 3 pendant, 730 coins",
    3: "3 Elementstone, 7 gold, 25 orb, 2300 Coins",
    4: "3 Elementstone, 7 gold, 25 orb, 2300 Coins",
    5: "3 Necklace, 8 waterstone, 3800 Coins",
    6: "3 artifact, 3 fire, 25 orb, 3800 Coins",
    7: "3 artifact, 8 waterstone, 8 firestone, 7600 Coins"
  }
  return switcher.get(deco,"") 
def deliprestige(deco): #deliprestige
  switcher = {
    1: "6 firestone, 6 pendant, 730 coins",
    2: "6 firestone, 6 pendant, 730 coins",
    3: "6 Elementstone, 14 gold, 50 orb, 2300 Coins",
    4: "6 Elementstone, 14 gold, 50 orb, 2300 Coins",
    5: "6 Necklace, 16 waterstone, 3800 Coins",
    6: "6 artifact, 6 fire, 50 orb, 3800 Coins",
    7: "6 artifact, 16 waterstone, 16 firestone, 7600 Coins"
  }
  return switcher.get(deco,"") 

#rainy - level 74
def rainy(deco):
  switcher = {
    1: "3 firestone, 3 pendant, 740 coins",
    2: "3 firestone, 3 pendant, 740 coins",
    3: "3 Elementstone, 7 gold, 25 orb, 2400 Coins",
    4: "3 Elementstone, 7 gold, 25 orb, 2400 Coins",
    5: "3 Necklace, 8 waterstone, 3800 Coins",
    6: "3 artifact, 3 fire, 25 orb, 3800 Coins",
    7: "3 artifact, 8 waterstone, 8 firestone, 7700 Coins"
  }
  return switcher.get(deco,"") 
def rainyprestige(deco): #rainyprestige
  switcher = {
    1: "6 firestone, 6 pendant, 740 coins",
    2: "6 firestone, 6 pendant, 740 coins",
    3: "6 Elementstone, 14 gold, 50 orb, 2400 Coins",
    4: "6 Elementstone, 14 gold, 50 orb, 2400 Coins",
    5: "6 Necklace, 16 waterstone, 3800 Coins",
    6: "6 artifact, 6 fire, 50 orb, 3800 Coins",
    7: "6 artifact, 16 waterstone, 16 firestone, 7700 Coins"
  }
  return switcher.get(deco,"") 

#minigolf - level 75
def minigolf(deco):
  switcher = {
    1: "3 firestone, 3 pendant, 750 coins",
    2: "3 firestone, 3 pendant, 750 coins",
    3: "3 Elementstone, 7 gold, 25 orb, 2400 Coins",
    4: "3 Elementstone, 7 gold, 25 orb, 2400 Coins",
    5: "3 Necklace, 8 waterstone, 3900 Coins",
    6: "3 artifact, 3 fire, 25 orb, 3900 Coins",
    7: "3 artifact, 8 waterstone, 8 firestone, 7800 Coins"
  }
  return switcher.get(deco,"") 
def minigolfprestige(deco): #minigolfprestige
  switcher = {
    1: "6 firestone, 6 pendant, 750 coins",
    2: "6 firestone, 6 pendant, 750 coins",
    3: "6 Elementstone, 14 gold, 50 orb, 2400 Coins",
    4: "6 Elementstone, 14 gold, 50 orb, 2400 Coins",
    5: "6 Necklace, 16 waterstone, 3900 Coins",
    6: "6 artifact, 6 fire, 50 orb, 3900 Coins",
    7: "6 artifact, 16 waterstone, 16 firestone, 7800 Coins"
  }
  return switcher.get(deco,"") 


### purchased floors ###

#aquarium #WENDY not sure about recipes OR costs
def aquarium(deco):
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

#archery
def archery(deco): #WENDY recipes unconfirmed
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

#asianfood
def asianfood(deco):
  switcher = {
    1: "1 Needle, 1 Bronze, 100 Coins",
    2: "1 Needle, 1 Bronze, 100 Coins",
    3: "1 Sparkles, 2 Bronze, 320 Coins",
    4: "1 Sparkles, 2 Bronze, 320 Coins",
    5: "3 Needles, 1 Sparkles, 520 Coins",
    6: "1 Sparkles, 13 Bronze, 520 Coins",
    7: "2 Sparkles, 1 Silver, 1 Gold, 1000 Coins"
  }
  return switcher.get(deco,"")
def asianfoodprestige(deco): #asianfoodprestige
  switcher = {
    1: "2 Needle, 2 Bronze, 100 Coins",
    2: "2 Needle, 2 Bronze, 100 Coins",
    3: "2 Sparkles, 4 Bronze, 320 Coins",
    4: "2 Sparkles, 4 Bronze, 320 Coins",
    5: "6 Needles, 2 Sparkles, 520 Coins",
    6: "2 Sparkles, 26 Bronze, 520 Coins",
    7: "4 Sparkles, 2 Silver, 2 Gold, 1000 Coins"
  }
  return switcher.get(deco,"")

#atlantis
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
def atlantisprestige(deco): #atlantisprestige
  switcher = {
    1: "10 Wood, 100 Coins",
    2: "10 String, 100 Coins",
    3: "4 Metal, 2 Needle, 320 Coins",
    4: "4 Metal, 2 Needle, 320 Coins",
    5: "14 String, 6 Ribbon, 520 Coins",
    6: "16 Metal, 2 Needle, 520 Coins",
    7: "8 Ribbon, 6 Needles, 2 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#autumnwalk
def autumnwalk(deco): #WENDY not sure for most (confirmed for deco 7)
  switcher = {
    1: "5 Wood, 100 Coins", #WENDY unconfirmed
    2: "5 String, 100 Coins", #WENDY unconfirmed
    3: "2 Metal, 1 Needle, 320 Coins", #WENDY unconfirmed
    4: "2 Metal, 1 Needle, 320 Coins", #WENDY unconfirmed
    5: "7 String, 3 Ribbon, 520 Coins", #WENDY unconfirmed
    6: "8 Metal, 1 Needle, 520 Coins", #WENDY unconfirmed
    7: "4 Ribbon, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"") 
def autumnwalkprestige(deco): #autumnwalkprestige
  switcher = {
    1: "10 Wood, 100 Coins",
    2: "10 String, 100 Coins",
    3: "4 Metal, 2 Needle, 320 Coins",
    4: "4 Metal, 2 Needle, 320 Coins",
    5: "14 String, 6 Ribbon, 520 Coins",
    6: "16 Metal, 2 Needle, 520 Coins",
    7: "8 Ribbon, 6 Needles, 2 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#balconygarden
def balconygarden(deco): #WENDY recipes unconfirmed
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
def balconygardenprestige(deco): #balconygardenprestige
  switcher = {
    1: "10 Wood, 100 Coins",
    2: "10 String, 100 Coins",
    3: "4 Metal, 2 Needle, 320 Coins",
    4: "4 Metal, 2 Needle, 320 Coins",
    5: "14 String, 6 Ribbon, 520 Coins",
    6: "16 Metal, 2 Needle, 520 Coins",
    7: "8 Ribbon, 6 Needles, 2 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#bread #WENDY not sure about recipes OR costs
def bread(deco):
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
def breadprestige(deco): #breadprestige
  switcher = {
    1: "10 Wood, 100 Coins",
    2: "10 String, 100 Coins",
    3: "4 Metal, 2 Needle, 320 Coins",
    4: "4 Metal, 2 Needle, 320 Coins",
    5: "14 String, 6 Ribbon, 520 Coins",
    6: "16 Metal, 2 Needle, 520 Coins",
    7: "8 Ribbon, 6 Needles, 2 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#carousel
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

#catcafe
def catcafe(deco): 
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

#corn
def corn(deco): #WENDY recipes unconfirmed
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
  
#duck
def duck(deco): #WENDY recipes unconfirmed
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

#freshfruit #WENDY not sure about recipes OR costs
def freshfruit(deco):
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

#garfield #WENDY
def garfield(deco):
  switcher = {
    1: ""
  }
  return switcher.get(deco,"")
  
#hatcats 
def hatcats(deco): #WENDY not sure about recipes OR costs
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
def hatcatsprestige(deco): #hatcatsprestige
  switcher = {
    1: "10 Wood, 100 Coins",
    2: "10 String, 100 Coins",
    3: "4 Metal, 2 Needle, 320 Coins",
    4: "4 Metal, 2 Needle, 320 Coins",
    5: "14 String, 6 Ribbon, 520 Coins",
    6: "16 Metal, 2 Needle, 520 Coins",
    7: "8 Ribbon, 6 Needles, 2 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#minobeach
def minobeach(deco):
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
def minobeachprestige(deco): #minobeachprestige
  switcher = {
    1: "10 Wood, 100 Coins",
    2: "10 String, 100 Coins",
    3: "4 Metal, 2 Needle, 320 Coins",
    4: "4 Metal, 2 Needle, 320 Coins",
    5: "14 String, 6 Ribbon, 520 Coins",
    6: "16 Metal, 2 Needle, 520 Coins",
    7: "8 Ribbon, 6 Needles, 2 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#minoforest
def minoforest(deco):
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
def minoforestprestige(deco): #minoforestprestige
  switcher = {
    1: "10 Wood, 100 Coins",
    2: "10 String, 100 Coins",
    3: "4 Metal, 2 Needle, 320 Coins",
    4: "4 Metal, 2 Needle, 320 Coins",
    5: "14 String, 6 Ribbon, 520 Coins",
    6: "16 Metal, 2 Needle, 520 Coins",
    7: "8 Ribbon, 6 Needles, 2 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#outdoorpool
def outdoorpool(deco): #WENDY recipes unconfirmed
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
def outdoorpoolprestige(deco): #outdoorpoolprestige
  switcher = {
    1: "10 Wood, 100 Coins",
    2: "10 String, 100 Coins",
    3: "4 Metal, 2 Needle, 320 Coins",
    4: "4 Metal, 2 Needle, 320 Coins",
    5: "14 String, 6 Ribbon, 520 Coins",
    6: "16 Metal, 2 Needle, 520 Coins",
    7: "8 Ribbon, 6 Needles, 2 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#supercatsquad
def supercatsquad(deco): #WENDY not sure for most (confirmed for deco 7)
  switcher = {
    1: "5 Wood, 100 Coins", #WENDY unconfirmed
    2: "5 String, 100 Coins", #WENDY unconfirmed
    3: "2 Metal, 1 Needle, 320 Coins", #WENDY unconfirmed
    4: "2 Metal, 1 Needle, 320 Coins", #WENDY unconfirmed
    5: "7 String, 3 Ribbons, 520 Coins", #WENDY unconfirmed
    6: "8 Metal, 1 Needle, 520 Coins", #WENDY unconfirmed
    7: "4 Ribbons, 3 Needles, 1 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")
def supercatsquadprestige(deco): #supercatsquadprestige
  switcher = {
    1: "10 Wood, 100 Coins",
    2: "10 String, 100 Coins",
    3: "4 Metal, 2 Needle, 320 Coins",
    4: "4 Metal, 2 Needle, 320 Coins",
    5: "14 String, 6 Ribbon, 520 Coins",
    6: "16 Metal, 2 Needle, 520 Coins",
    7: "8 Ribbon, 6 Needles, 2 Sparkles, 1000 Coins"
  }
  return switcher.get(deco,"")

#waterfight
def waterfight(deco): #WENDY recipes unconfirmed
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

#waterpark
def waterpark(deco):
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
