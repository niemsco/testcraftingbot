import math

def room(multiplier):
  outmsg="\n**Craft the room in 2 hours**"
  outmsg=outmsg+"\nTimes given as minutes after start of boost" 

  outmsg=outmsg+"\n"
  outmsg=outmsg+"\n0:00 - 75/75/75 ABC"
  outmsg=outmsg+"\n0:15 - 75/75/75 ABC, 20D"
  outmsg=outmsg+"\n0:30 - 75/75/75 ABC, 20D"
  outmsg=outmsg+"\n0:45 - 75/75/75 ABC, 20D, 18E"
  outmsg=outmsg+"\n1:00 - 75/75/75 ABC, 20D"
  outmsg=outmsg+"\n1:15 - 75/75/75 ABC, 20D, 18E"
  outmsg=outmsg+"\n1:30 - 75/75/75 ABC, 20D"
  outmsg=outmsg+"\n1:45 - 20D, 18E, 11F"
  
  outmsg=outmsg+"\n"
  outmsg=outmsg+"\nTotal crafted - 525/525/525 ABC, 140D, 54E, 11F"
  outmsg=outmsg+"\nInventory - 17/29/29 ABC, 32D, 21E, 11F"
  outmsg=outmsg+"\nMultiplier: " + str(multiplier)
  outmsg=outmsg+"\nCost: " + str(getRoomCost(multiplier))

  return outmsg


def stars3k (multiplier):
  outmsg="\n**Craft 3000 stars (1000E) in 5 hours**"
  outmsg=outmsg+"\nTimes given as minutes after start of boost" 

  outmsg=outmsg+"\n"
  outmsg=outmsg+"\n0:00 - 392/504/504 ABC"
  outmsg=outmsg+"\n0:15 - 392/504/504 ABC, 112D"
  outmsg=outmsg+"\n0:30 - 392/504/504 ABC, 112D"
  outmsg=outmsg+"\n0:45 - 392/504/504 ABC, 112D, 112E"
  outmsg=outmsg+"\n"
  outmsg=outmsg+"\n1:00 - 392/504/504 ABC, 112D"
  outmsg=outmsg+"\n1:15 - 392/504/504 ABC, 112D, 112E"
  outmsg=outmsg+"\n1:30 - 392/504/504 ABC, 112D"
  outmsg=outmsg+"\n1:45 - 392/504/504 ABC, 112D, 112E"
  outmsg=outmsg+"\n"
  outmsg=outmsg+"\n2:00 - 392/504/504 ABC, 112D"
  outmsg=outmsg+"\n2:15 - 392/504/504 ABC, 112D, 112E"
  outmsg=outmsg+"\n2:30 - 392/504/504 ABC, 112D"
  outmsg=outmsg+"\n2:45 - 392/504/504 ABC, 112D, 112E"
  outmsg=outmsg+"\n"
  outmsg=outmsg+"\n3:00 - 392/504/504 ABC, 112D"
  outmsg=outmsg+"\n3:15 - 392/504/504 ABC, 112D, 112E"
  outmsg=outmsg+"\n3:30 - 392/504/504 ABC, 112D"
  outmsg=outmsg+"\n3:45 - 392/504/504 ABC, 112D, 112E"
  outmsg=outmsg+"\n"
  outmsg=outmsg+"\n4:00 - 392/504/504 ABC, 112D"
  outmsg=outmsg+"\n4:15 - 392/504/504 ABC, 112D, 112E"
  outmsg=outmsg+"\n4:30 - 10/10/10 ABC, 112D"
  outmsg=outmsg+"\n4:45 - 112E"
  
  outmsg=outmsg+"\n"
  outmsg=outmsg+"\nTotal crafted - 7066/9082/9082 ABC, 2016D, 1008E"
  outmsg=outmsg+"\nInventory - 1018/1018/1018 ABC, 1008E"
  outmsg=outmsg+"\nMultiplier: " + str(multiplier)
  outmsg=outmsg+"\nCost: " + f'{get3kCost(multiplier):,}'

  return outmsg

def getRoomCost(multiplier):
  base = 807100
  recipes = 6430
  return int((base/multiplier) + recipes)

def get3kCost(multiplier):
  base = 74420640 + 1950 #1950 is the 3 stacks of 10 for ABC buffer
  starRecipe = 300*1008
  return int((base/multiplier) + starRecipe)

def baseCost(craft):
  switcher = {
    "A": 10,
    "B": 10,
    "C": 10,
    "D": 75,
    "E": 100,
    "F": 200
  }
  return switcher.get(craft,0)
  
def stackCost(craft, stack):
  base=baseCost(craft)
  return int((stack+3)*base*stack/2)

def getStacks(stackEper30min):
  stackA=math.ceil(7*stackEper30min/2)
  stackB=math.ceil(9*stackEper30min/2)
  stackC=math.ceil(9*stackEper30min/2)
  return [stackA,stackB,stackC]

def costPer15min(stackEper30min, multiplier):
  # base crafting cost per 30 min
  aryABC=getStacks(stackEper30min)
  cost=2*stackCost("A",aryABC[0])
  cost=cost+2*stackCost("B",aryABC[1])
  cost=cost+2*stackCost("C",aryABC[2])
  cost=cost+2*stackCost("D",stackEper30min)
  cost=cost+stackCost("E",stackEper30min)

  # adjust for multiplier and stars recipe
  cost = int(cost/multiplier)+(300*stackEper30min)
  return int(cost/2)

def findEper30min(tokensPerRound,multiplier):
  mult20exceed = 20

  while costPer15min(mult20exceed,multiplier)<tokensPerRound:
    mult20exceed=mult20exceed+20
  stackEper30min = mult20exceed-20

  mult5exceed=stackEper30min
  while costPer15min(mult5exceed,multiplier)<tokensPerRound:
    mult5exceed=mult5exceed+5
  stackEper30min = mult5exceed-5

  return stackEper30min

def starsmax(args,multiplier):
  argStr=args.strip()
  if len(argStr)==0: return "Expected syntax: $starsmax [tokens] or $starsmax [tokens] [multiplier]"

  argAry=argStr.split(" ")
  try: tokens=int(argAry[0].replace(',', ''))
  except: return errtcc()
  
  if len(argAry)>1: mult=float(argAry[1])
  else: mult=multiplier
  outmsg="\n**Maximize token use in 5 hours**"
  outmsg=outmsg+"\nTimes given as minutes after start of boost" 

  tokensPerRound=int(tokens/18)
  stackEper30min=findEper30min(tokensPerRound,mult)
  aryABC=getStacks(stackEper30min)
  stackA=aryABC[0];stackB=aryABC[1];stackC=aryABC[2]
  stackD=stackEper30min

  strABC=str(stackA)+"/"+str(stackB)+"/"+str(stackC)+" ABC"
  strD=str(stackD)+"D";strE=str(stackEper30min)+"E"

  outmsg=outmsg+"\n"
  outmsg=outmsg+"\n0:00 - " + strABC
  outmsg=outmsg+"\n0:15 - " + strABC + ", " + strD 
  outmsg=outmsg+"\n0:30 - " + strABC + ", " + strD 
  outmsg=outmsg+"\n0:45 - " + strABC + ", " + strD + ", " + strE 
  outmsg=outmsg+"\n"
  outmsg=outmsg+"\n1:00 - " + strABC + ", " + strD 
  outmsg=outmsg+"\n1:15 - " + strABC + ", " + strD + ", " + strE 
  outmsg=outmsg+"\n1:30 - " + strABC + ", " + strD 
  outmsg=outmsg+"\n1:45 - " + strABC + ", " + strD + ", " + strE 
  outmsg=outmsg+"\n"
  outmsg=outmsg+"\n2:00 - " + strABC + ", " + strD 
  outmsg=outmsg+"\n2:15 - " + strABC + ", " + strD + ", " + strE 
  outmsg=outmsg+"\n2:30 - " + strABC + ", " + strD 
  outmsg=outmsg+"\n2:45 - " + strABC + ", " + strD + ", " + strE 
  outmsg=outmsg+"\n"
  outmsg=outmsg+"\n3:00 - " + strABC + ", " + strD 
  outmsg=outmsg+"\n3:15 - " + strABC + ", " + strD + ", " + strE 
  outmsg=outmsg+"\n3:30 - " + strABC + ", " + strD 
  outmsg=outmsg+"\n3:45 - " + strABC + ", " + strD + ", " + strE 
  outmsg=outmsg+"\n"
  outmsg=outmsg+"\n4:00 - " + strABC + ", " + strD 
  outmsg=outmsg+"\n4:15 - " + strABC + ", " + strD + ", " + strE 
  outmsg=outmsg+"\n4:30 - 10/10/10 ABC, " + strD
  outmsg=outmsg+"\n4:45 - " + strE
  
  totalA=18*stackA+10;totalB=18*stackB+10;totalC=18*stackC+10
  totalD=18*stackD;totalE=9*stackEper30min
  strABC=str(totalA)+"/"+str(totalB)+"/"+str(totalC)+" ABC"
  strD=str(totalD)+"D";strE=str(totalE)+"E"
  outmsg=outmsg+"\n"
  outmsg=outmsg+"\nTotal crafted - " + strABC + ", " + strD + ", " + strE

  invA=totalA-(6*totalE);invB=totalB-(8*totalE);invC=totalC-(8*totalE)
  invD=totalD-(2*totalE);invE=totalE
  strABC=str(invA)+"/"+str(invB)+"/"+str(invC)+" ABC"
  strD=str(invD)+"D";strE=str(invE)+"E"
  outmsg=outmsg+"\nInventory - " + strABC + ", " + strD + ", " + strE
  outmsg=outmsg+"\nMultiplier: " + str(mult)

  totalCost = 18*costPer15min(stackEper30min,mult)
  extraCostBase = stackCost("A",10) + stackCost("B",10) + stackCost("C",10)
  totalCost = totalCost + int(extraCostBase/mult)
  outmsg=outmsg+"\nCost: " + f'{totalCost:,}'

  return outmsg

def helptcc():
  outmsg="\n**TCC Commands**\n"
  outmsg=outmsg+"These commands are for use in the TCC server."

  outmsg=outmsg+"\n\n"
  outmsg=outmsg+"**"+"Commands"+"**"
  outmsg=outmsg+"\n"

  outmsg=outmsg+"**$room**: Step-by-step instructions to craft the room in 2 hours.\n"
  outmsg=outmsg+"**$stars3k**: Step-by-step instructions to craft 3000 stars (1000E) in 5 hours.\n"
  outmsg=outmsg+"**$starsmax**: Step-by-step instructions to craft as many E as you have tokens and gems for. The cost of the star recipe is included in these calculations. Enter $helpstars for more info.\n"

  outmsg=outmsg+"\n\n"
  outmsg=outmsg+"**"+"Admin Commands"+"**"
  outmsg=outmsg+"\n"

  outmsg=outmsg+"**$multiplier**: Enter *$multiplier [x]* to set the multiplier for the server, for example *$multiplier 30.1*.\n"
  outmsg=outmsg+"**$pot**: Enter *$pot [x]* to add x mats to the community pot, for example *$pot 100*.\n"
  outmsg=outmsg+"**$potshow**: Show what's in the community pot.\n"
  outmsg=outmsg+"**$potclear**: Clear the community pot.\n"

  return outmsg

def errtcc():
  return "Something went wrong. Enter *$helptcc* for instructions."