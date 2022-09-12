from datetime import timezone
import datetime
import random

#main help text with crafting commands
def mainHelpText():
  outmsg="\n**Welcome to CG crafting assistant!**\n"
  outmsg=outmsg+"This bot will remember the decos you are planning for and calculate the crafts you need in your inventory. It works both in a channel or in private message."

  outmsg=outmsg+"\n\n"
  outmsg=outmsg+"**"+"Commands"+"**"
  outmsg=outmsg+"\n\n"

  outmsg=outmsg+"**$dm**: open a DM with Crafting Bot.\n"
  outmsg=outmsg+"**$add**: adds a craft to your Cat Game crafting list.\n"
  outmsg=outmsg+"\tEnter *$add [floor] [deco]* to add a single deco, for example, *$add basic 1*.\n"
  outmsg=outmsg+"\tEnter *$add [floor] [first] [last]* to add a range of decos, for example, *$add basic 5 7* will add basic 5, basic 6, and basic 7 to your list.\n"
  outmsg=outmsg+"\tEnter *$add [floor]* to add all decos on the floor, for example, *$add basic* to add all seven decos from the basic floor."
  outmsg=outmsg+"\n"
  outmsg=outmsg+"**$remove**: removes a craft from your Cat Game list.\n"
  outmsg=outmsg+"\tJust like with $add, you can enter *$remove [floor] [deco]* to remove a single deco, or *$remove [floor] [first] [last]* to remove a range, or *$remove [floor]* to remove a whole floor."
  outmsg=outmsg+"\n"
  outmsg=outmsg+"**$show**: displays everything in your Cat Game list, along with the crafts and coins you need in your inventory to craft that list."
  outmsg=outmsg+"\n"
  outmsg=outmsg+"**$clear**: removes everything from your Cat Game list."
  outmsg=outmsg+"\n"
  outmsg=outmsg+"**$recipe**: Enter *$recipe [floor] [deco]* to see a single Cat Game crafting recipe."
  outmsg=outmsg+"\n"
  outmsg=outmsg+"**$dogadd, $dogremove, $dogshow, $dogclear, $dogrecipe**: The same commands, but for Dog Game."
  outmsg=outmsg+"\n"
  outmsg=outmsg+"**$hoard, $hoardremove, $hoardshow**: Track hoard line counts, for example *$hoard 5* to add 5 lines. Using *$hoardshow* will show club and your own total."
  outmsg=outmsg+"\n"
  outmsg=outmsg+"**$calendar**: see what event/day today is in CG and DG.\n"
  outmsg=outmsg+"**$starsmax** and **$starsgoal**: CE crafting planners, type *$helpstars* for details.\n"
  outmsg=outmsg+"**$mybadges, $easter, $catlorette, $holiday, $fitness**: Use these commands to see your badges. Some badges are for playing in specific events."
  #outmsg=outmsg+"\n\n"
  outmsg2="**Notes:**\n"
  outmsg2=outmsg2+"-Use single word floor names, such as *mysterymansion* instead of *mystery mansion*.\n"
  outmsg2=outmsg2+"-Crafting coin costs are guesses on some floors: levels 43+ in CG, levels 11+ in DG. Crafting recipes on purchase floors in DG are mostly guesses.\n"
  outmsg2=outmsg2+"-**The Garfield floor has been disabled for adding to your list** because I couldn't find the recipes online. If you know the recipes, please DM me. Thank you!"

  outmsg2=outmsg2+"\n\n"
  outmsg2=outmsg2+"**"+"Flags"+"**"
  outmsg2=outmsg2+"\n\n"
  outmsg2=outmsg2+"**-user** or **-u**: specify the user to plan decos for.\n"
  outmsg2=outmsg2+"\tThis flag is for players with alts, who want to keep separate lists. You can apply this flag to any tag, for example *$add basic 1 -user MyAlt* will add the deco to MyAlt's list. Similarly, *$show -user MyAlt* will show MyAlt's list.\n"  
  outmsg2=outmsg2+"\tThis flag can NOT be used to add decos to another person based on their Discord username." 

  outmsg2=outmsg2+"\n\n"
  outmsg2=outmsg2+"Questions or comments, compliments or complaints? Open up a private chat with me (Sweetling) and let me know!\n"

  return [outmsg,outmsg2]

def starsmaxDetail():
  msg="\n"
  msg=msg+"**CE Crafting Features**\n"
  msg=msg+"**$starsmax**: Maximizes stars from gems and tokens during CE.\n"
  msg=msg+"\tEnter *$starsmax [tokens] [gems] [hours] [multiplier] [flags]* to come up with a crafting plan, for example *$starsmax 500000 1000 5 300 -r*.\n"
  msg=msg+"\tThe flags are optional. Available flags are:\n" 
  msg=msg+"\t**-room** or **-r** to include crafing the CE room.\n"
  msg=msg+"\t**-aggressive** or **-a** to signify that you will start your first round of crafts early, getting an extra crafting cycle in.\n"
  msg=msg+"**$starsgoal**: Gives a plan for if you have a star goal in mind.\n"
  msg=msg+"\tEnter *$starsgoal [goal] [tokens] [hours] [multiplier] [flags]* to come up with a crafting plan, for example *$starsgoal 3000 1000000 5 300 -a*.\n"
  msg=msg+"\tThe flags are optional. Available flags are:\n" 
  msg=msg+"\t**-aggressive** or **-a** to signify that you will start your first round of crafts early, getting an extra crafting cycle in.\n"

  msg=msg+"\n"
  msg=msg+"**Instructions:**\n"
  msg=msg+"-Do not craft any D in the last 15 minutes of boost, unless you plan to speedup. You won't have time to collect and craft it into E. This crafting plan assumes you will stop crafting D at that time.\n"
  msg=msg+"-In contrast, you can keep crafing ABC all the way to the end. The ABC will be used for stars recipes.\n"
  msg=msg+"-Keep the other crafts going in the background while doing speedups. For example if you are speeding up A, keep BCDE going.\n"
  msg=msg+"-These values are rounded. That difference can add up. You may need to craft a few extra ABC near the end, or slow-craft a few.\n"
  msg=msg+"-If readjusting during the middle of a crafting session, leave some wiggle room in tokens. The bot starts with a clean slate. If you have backlogged DE, meaning you need to turn your most recent round of ABC into DE, that will cost tokens that the bot doesn't factor in.\n"

  msg2="\n"
  msg2=msg2+"**Speedups:**\n"
  msg2=msg2+"-The bot adjusts for time spent doing speedups. It will automatically decrease the free crafting cycles of that craft, and give you extra speedups. It factors that into gem use.\n"
  msg2=msg2+"-For example, in a 5 hour crafting session, you will not be told to do 120 total cycles and speed up 100. The bot knows that speeding up 100 cycles takes time, and you will not have time to do 20 free cycles.\n"
  msg2=msg2+"-Instead, it will guess at how much time it takes. 100 speedups might take 30 to 40 minutes to do, and you will lose 3 crafting cycles. So it will tell you to do 120 total cycles and speed up 103.\n"
  msg2=msg2+"-The guesses might be off depending on lag.\n"
  msg2=msg2+"-However, be wary if your speedups gets close to total cycles. For example, if you are told to craft 100 rounds of A and speedup 100, then the bot thinks you have NO FREE TIME. In other words, you will NOT HAVE TIME to carry out this crafting plan.\n"
  msg2=msg2+"-Look out for your free cycles of ABC. Each should take no more than 1/3 of the total time. In other words, in a 5-hour crafting session, if your free cycles of ABC drop below 13 or so, that's trouble!\n"

  msg2=msg2+"\n"
  msg2=msg2+"**Aggressive:**\n"
  msg2=msg2+"-To get an extra crafting cycle, start 1 each of ABC about 10 minutes before the crafting boost starts.\n"
  msg2=msg2+"-After the crafting boost, hurry to get the numbers up to the stack sizes you want.\n"
  msg2=msg2+"-You may have to start closer to the boost time if you are frequently unable to get the numbers up before the crafts complete.\n"

  return [msg,msg2]

def helpbadge():
  msg="\n"
  msg=msg+"**Badge List (for admins)**\n"
  msg=msg+"Supports multiple badge numbers (comma-delimited, no spaces)"
  msg=msg+"\n"
  msg=msg+"**$badgeadd [@username] mybadges [num]**: 1-beetle, 3-orange FR gem, 4-blue FR gem, 5-50k silver medal, 6-100k gold medal\n"
  msg=msg+"**$badgeadd [@username] fitness [num]**: 1-jan2022\n"
  msg=msg+"\n"  
  msg=msg+"**$badgeclear [@username] [category]**: clear all badges in a category for a user (categories: mybadges, fitness)\n"
  return msg

#returns the CG and DG event and day
def calendar():
  dt = datetime.datetime.now(timezone.utc)
  utc_time = dt.replace(tzinfo=timezone.utc)
  utc_timestamp = utc_time.timestamp()
  today = utc_timestamp//86400
  dayCat = (today-18848)%28 #18848 = 2021/08/08 day before start of a CG cycle
  dayDog = (today-18834)%28 #18834 = 2021/07/25 day before start of a DG cycle
  msg="**Cat Game:** "+getCatDay(dayCat)+"\n"
  msg=msg+"**Dog Game:** "+getDogDay(dayDog)+"\n"
  return msg

#these next two tags are identical but separate intentionally
#in case CG and DG ever use different schedules

#what CG event/day it is based on day of cycle
def getCatDay(day):
  switcher = {
    0: "EB1 begins at next reset",
    1: "Day 1 of EB1",
    2: "Day 2 of EB1",
    3: "Day 3 of EB1",
    4: "Day 4 of EB1",
    5: "Day 5 of EB1",
    6: "Day 6 of EB1",
    7: "Last day of EB1",
    8: "EB2 begins at next reset",
    9: "Day 1 of EB2",
    10: "Day 2 of EB2",
    11: "Day 3 of EB2",
    12: "Day 4 of EB2",
    13: "Day 5 of EB2",
    14: "Day 6 of EB2",
    15: "Day 7 of EB2",
    16: "EB3 begins at next reset",
    17: "Day 1 of EB3",
    18: "Day 2 of EB3",
    19: "Day 3 of EB3",
    20: "Day 4 of EB3",
    21: "Day 5 of EB3",
    22: "Day 6 of EB3",
    23: "Day 7 of EB3",
    24: "CE begins at next reset",
    25: "Day 1 of CE",
    26: "Day 2 of CE",
    27: "Day 3 of CE"
  }
  return switcher.get(day,"")

#what DG event/day it is based on day of cycle
def getDogDay(day):
  switcher = {
    0: "EB1 begins at next reset",
    1: "Day 1 of EB1",
    2: "Day 2 of EB1",
    3: "Day 3 of EB1",
    4: "Day 4 of EB1",
    5: "Day 5 of EB1",
    6: "Day 6 of EB1",
    7: "Last day of EB1",
    8: "EB2 begins at next reset",
    9: "Day 1 of EB2",
    10: "Day 2 of EB2",
    11: "Day 3 of EB2",
    12: "Day 4 of EB2",
    13: "Day 5 of EB2",
    14: "Day 6 of EB2",
    15: "Day 7 of EB2",
    16: "EB3 begins at next reset",
    17: "Day 1 of EB3",
    18: "Day 2 of EB3",
    19: "Day 3 of EB3",
    20: "Day 4 of EB3",
    21: "Day 5 of EB3",
    22: "Day 6 of EB3",
    23: "Day 7 of EB3",
    24: "CE begins at next reset",
    25: "Day 1 of CE",
    26: "Day 2 of CE",
    27: "Day 3 of CE"
  }
  return switcher.get(day,"")

def randQuote():
  quoteAry = [
    "and the sheen of their spears was like stars on the sea", #The Destruction of Sennecherib, Byron
    "even the weakest, all life strives", #Victory Condition, astolat
    "what's waited 'til tomorrow starts tonight", #From Now On, The Greatest Showman
    "do you remember when we were eleven?", #Running on Air, eleventy7
    "they're all right, but none of them is correct", #The Correct Way, VIII of XIII
    "the anger and the despair, the regret and the affection, the longing and the loathing all boiling till the kettle is dry" #observational skills, ghostcatamount
  ]
  return random.choice(quoteAry)