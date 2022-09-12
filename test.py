from replit import db
keys = db.keys()

for key in keys:
  break
  if 1==0: #key.startswith("badges~") and ("catlorette" in key):
    #msg = str(key) + "---" + str(db[key]) + "\n"
    #print(msg)
    badgeAry = db[key]
    for i in range(len(badgeAry)):
      pieceAry = badgeAry[i].split("/")
      if len(pieceAry)==2:
        badgeAry[i]='images/catlorette/'+pieceAry[1]
    #print(badgeAry)
    db[key] = badgeAry

for key in keys:
  if key.startswith("badges~") and ("general" in key):
    if "#" in key: continue
    del db[key]
    continue
    #msg = str(key) + "---" + str(db[key]) + "\n"
    #print(msg)
    keypieces = key.split("~")
    newkey = "badges~"+str(keypieces[1])+"~mybadges"
    db[newkey] = db[key]

print("done")