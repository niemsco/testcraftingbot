Commands

  Cat Game crafting
    $add floor [min] [max] - add decos to list
      if neither min/max - add whole floor
      if min given but no max - add one deco
      if min and max given - add range of decos
    $remove floor [min] [max] - remove decos
    $clear - clear all decos from list
    $show - show decos in list and crafts needed
    $recipe [floor] [deco] - get one recipe
    optional flags for all commands: 
      -u user - update list for user other than msg author

  Dog Game crafting - same as CG but with word "Dog"
    $dogadd floor [min] [max]
    $dogremove floor [min] [max]
    $dogclear
    $dogshow
    $dogrecipe

  CE crafting
    $starsmax tokens gems hours multiplier [-flags]
      optional flags:
        -a or -aggressive - start crafts early, 1 extra cycle
        -r or -room - add crafting CE room to plan
    $starsgoal goal tokens hours multiplier [-flags]
      optional flags:
        -a or -aggressive - start crafts early, 1 extra cycle  

  Hoard tracking (for TCC)
    $hoard - add lines
    $hoardremove - subtract lines
    $hoardshow - show total and your own lines
    $hoardall - show everyone's hoard contributions (secret command)
    $hoardclear - clear all hoard lines, reset count to 0 (secret command)

  CE crafting (for TCC)
    $room
    $stars3k
  
  TCC admin
    $multiplier - set crafting multiplier
    $pot - add mats to community pot
    $potshow
    $potclear

  Help Commands
    $help - show main help text
    $helpstars - info on $starsmax and $starsgoal
    $helptcc - show TCC CE crafting help
    $helpbadge - for badge admins, list badge categories and nums
    $dm - bot opens a dm
    $calendar - prints event/day for CG and DG
    $hello - check if bot is online

  Badges
    Badge categories (for users to see their badges)
      $easter
      $catlorette
      $mybadges
      $holiday
      $fitness
    Admin
      $badgeadd @user category badgenum - supports multi (comma delim, no spaces)
      $badgeclear @user category
      

DB structure 
(userIDorN specifies it might be a one-word string name if using -u flag)
  crafting~[userIDorN]~cat = list of Cat Game decos
  crafting~[userIDorN]~dog = list of Dog Game decos
  hoard = hoard total
  hoard~[userIDorN] = the user's hoard total
  hoarddisp~[userIDorN] = the user's display name 
  badge~[userID]~category = list of badges
  multiplier = TCC crafting multiplier
  community pot = mats in community pot

ID dictionary
  Channels:
    870785964413452318 - Fearless Revival crafting-bot
    874430786428882944 - Fearless Retrievers crafting-bot
    814911496231845904 - TCC Sweetling's CE bot
    814346827938660354 - Sweetling Sandserver general
    783900285436559360 - Orange's testing channel
  Users:
    721843920404742205 - Sweetling
    179430266895466506 - Orange
    655087300140597268 - Akat
