import math

def maxstarshelper(args,flagAry):
  argAry = args.split()
  errStr = "Expected syntax: $starsmax tokens gems hours multiplier [-room] [-aggressive]" #[-debug]
  if len(argAry)<4: return errStr
  tokens = int(argAry[0])
  gems = int(argAry[1])
  hours = float(argAry[2])
  multiplier = float(argAry[3])
  
  if "-room" in flagAry: room = 1
  else: room = 0
  if "-aggressive" in flagAry: aggressive = 1
  else: aggressive = 0

  if tokens<=0: return errStr
  if hours<=0: return errStr
  if gems<0: gems = 0
  if multiplier<=1: multiplier = 1

  return maxstars(tokens,gems,hours,multiplier,room,aggressive,0)

def goalstarshelper(args,flagAry):
  argAry = args.split()
  errStr = "Expected syntax: $starsgoal goal tokens hours multiplier [-aggressive]" #[-debug]
  if len(argAry)<4: return errStr
  goal = int(argAry[0])
  tokens = int(argAry[1])
  hours = float(argAry[2])
  multiplier = float(argAry[3])
  
  if "-aggressive" in flagAry: aggressive = 1
  else: aggressive = 0

  if tokens<=0: return errStr
  if hours<=0: return errStr
  if multiplier<=1: multiplier = 1

  return goalstars(goal,tokens,hours,multiplier,aggressive)


def maxstars(tokens,gems,hours,mult,room,aggressive,debug):
  startingcycles=getstartingfreecycles(hours,aggressive)
  curcost=0
  curgoal=0
  for increment in (6000,1200,150,30,6):
    curcost=mintokencost(curgoal,gems,mult,room,startingcycles,0)[5]
    while curcost<tokens:
      tempary = mintokencost(curgoal+increment,gems,mult,room,startingcycles,0)
      curcost = tempary[5]
      if debug == 1:
        print("Goal: " + str(curgoal+increment))
        print(tempary[0])
        print(tempary[1])
        print(tempary[2])
        print(tempary[3])
        print("Gems: " + str(tempary[4]))
        print("Tokens: " + str(tempary[5]))
        print()
      if curcost>tokens: continue

      curgoal=curgoal+increment
      
  resultary = mintokencost(curgoal,gems,mult,room,startingcycles,0)
  totalcycles = aryadd(resultary[0],resultary[1])
  stacksrounded = aryround(resultary[2])
  speedups = resultary[1]
  totalcrafts = aryround(resultary[3])

  msg = getmessage(curgoal,stacksrounded,totalcycles,speedups,room,totalcrafts,resultary[4],resultary[5])
  return msg

def getmessage(curgoal,stacksrounded,totalcycles,speedups,room,totalcrafts,gems,tokens):
  msg="" #outmsg=outmsg+"**$dm**: open a DM with Crafting Bot.\n"
  if room==1: msg = msg + "**FINAL:** " + str(curgoal) + "+178\n"
  else: msg = msg + "**FINAL:** " + str(curgoal) + "\n"
  
  msg = msg + "\n"
  msg = msg + "**How many to make of each craft**\n"
  msg = msg + msgstr("A",stacksrounded[0],totalcycles[0],speedups[0])
  msg = msg + msgstr("B",stacksrounded[1],totalcycles[1],speedups[1])
  msg = msg + msgstr("C",stacksrounded[2],totalcycles[2],speedups[2])
  msg = msg + msgstr("D",stacksrounded[3],totalcycles[3],speedups[3])
  msg = msg + msgstr("E",stacksrounded[4],totalcycles[4],speedups[4])
  if room==1: msg = msg + msgstr("F",11,1,0)

  msg = msg + "\n"
  msg = msg + "**Total crafts**\n"
  msg = msg + "A: " + str(totalcrafts[0]) + "\n"
  msg = msg + "B: " + str(totalcrafts[1]) + "\n"
  msg = msg + "C: " + str(totalcrafts[2]) + "\n"
  msg = msg + "D: " + str(totalcrafts[3]) + "\n"
  msg = msg + "E: " + str(totalcrafts[4]) + "\n"
  if room==1: msg = msg + "F: 11\n"

  msg = msg + "\n"
  msg = msg + "**Gems:** " + str(gems) + "\n"
  msg = msg + "**Tokens:** " + str(round(tokens))  + "\n"
  msg = msg + "\n"
  return msg

def goalstars(goal,tokens,hours,mult,aggressive):
  startingcycles=getstartingfreecycles(hours,aggressive)
  resultary=mintokencost(goal,0,mult,0,startingcycles,tokens)
  #resultary format: [freecycles,speedups,finalary[1],totalcrafts,usedgems,finalary[0]]
  totalcycles = aryadd(resultary[0],resultary[1])
  stacksrounded = aryround(resultary[2])
  speedups = resultary[1]
  totalcrafts = aryround(resultary[3])

  msg = getmessage(goal,stacksrounded,totalcycles,speedups,0,totalcrafts,resultary[4],resultary[5])

  return msg

def mintokencost(goal,gems,mult,room,startingcraftcycles,tokencap):
  baseary=[10,10,10,75,100]
  speedupcostary=[30,30,30,30,40]
  roomary=[513,504,503,140,54]
  totalE=goal/3
  totalcrafts=[7*totalE,9*totalE,9*totalE,2*totalE,totalE]
  if room==1: 
    totalcrafts = aryadd(totalcrafts,roomary)
    roomcost = getstackcost(200,11,mult) + 6430
  else: roomcost = 0
  if tokencap>0: gems=999999 #essentially infinite gems

  speedups=[0,0,0,0,0]
  freecycles=arycopy(startingcraftcycles)
  usedgems=0
  curCost=gettotalcost(baseary,freecycles,speedups,totalcrafts,mult,roomcost)[0]

  while usedgems<(gems-29):
    if (tokencap>0) and (curCost<tokencap): break 
    testtotals=[]
    savingspergem = []
    
    for i in range(5): #add 1 speedups to each craft and see what it would cost
      testspeedups = arycopy(speedups)
      testspeedups[i]=testspeedups[i]+1
      resultary=gettotalcost(baseary,freecycles,testspeedups,totalcrafts,mult,roomcost)
      testtotals.append(resultary[0]) #array of hypothetical new costs
      savingspergem.append((curCost-resultary[0])/speedupcostary[i]) #savings per gem

    maxsavings = max(savingspergem) #the most effective craft to spend gems on
    minindex = savingspergem.index(maxsavings)
    speedups[minindex] = speedups[minindex]+1
    curCost = testtotals[minindex]

    #increment totals for whichever craft we decided to speed up
    mintotalcycles = freecycles[minindex]+speedups[minindex]
    minstacksize = totalcrafts[minindex]/mintotalcycles
    minspeeduptotal = speedups[minindex]*minstacksize

    #this section handles the time it takes to speed crafts - lost free cycles
    if minindex==4: lostfreecycles = math.ceil(minspeeduptotal/90000)
    else: lostfreecycles = math.ceil(minspeeduptotal/45000)
    if lostfreecycles>startingcraftcycles[minindex]: lostfreecycles = startingcraftcycles[minindex]

    #get worried if this line shows up - if free cycles is 0 on any craft - time crunch!
    freecycles[minindex] = startingcraftcycles[minindex] - lostfreecycles
    speedups[minindex] = mintotalcycles - freecycles[minindex]

    usedgems=gettotalgems(speedups)


    #print("Incremented: " + str(minindex))
    #print(freecycles)
    #print(speedups)
    #print(testtotals)
    #print("Gems: " + str(usedgems))
    #print("Tokens: " + str(minval))
    #print()

  finalary = gettotalcost(baseary,freecycles,speedups,totalcrafts,mult,roomcost)
  return [freecycles,speedups,finalary[1],totalcrafts,usedgems,finalary[0]]

def gettotalcost(baseary,freestacks,speedups,totalcrafts,mult,roomcost):
  totalstacks=aryadd(freestacks,speedups)
  stacksizes=arydivide(totalcrafts,totalstacks)

  stackcosts = [0,0,0,0,0]
  for i in range(5):
    stackcosts[i]=getstackcost(baseary[i],stacksizes[i],mult)

  totalcosts = arymultiply(stackcosts,totalstacks)
  overallcost = sum(totalcosts) + (300*totalcrafts[4])
  overallcost = overallcost + roomcost

  return [overallcost,stacksizes]

def getstackcost(base,stack,mult):
  return (stack+3)*stack*base/(2*mult)

def getstartingfreecycles(hours,aggressive):
  if aggressive==1: hours=hours+.25
  freeABC = math.ceil(hours*4)
  unroundedE = (hours-.5)*2
  freeE = math.ceil(unroundedE)
  if freeE==unroundedE: freeD = freeABC-3
  else: freeD = freeABC-2
  return [freeABC,freeABC,freeABC,freeD,freeE]

def gettotalgems(speedups):
  costary=[30,30,30,30,40]
  return sum(arymultiply(costary,speedups))

def arydivide(a, b):
  arylength = len(a)
  result = []
  for i in range(arylength):
    result.append(a[i]/b[i])
  return result

def arymultiply(a, b):
  arylength = len(a)
  result = []
  for i in range(arylength):
    result.append(a[i]*b[i])
  return result

def aryadd(a, b):
  arylength = len(a)
  result = []
  for i in range(arylength):
    result.append(a[i]+b[i])
  return result

def arysubtract(a, b):
  arylength = len(a)
  result = []
  for i in range(arylength):
    result.append(a[i]-b[i])
  return result

def arycopy(a):
  arylength = len(a)
  result = []
  for i in range(arylength):
    result.append(a[i])
  return result

def aryround(a):
  arylength = len(a)
  result = []
  for i in range(arylength):
    result.append(round(a[i]))
  return result 

def msgstr(label,stack,totalcycles,freecycles):
  return label + ": " + str(stack) + ", " + str(totalcycles) + " times (speedups: " + str(freecycles) + ")\n"