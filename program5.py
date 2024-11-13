import random

def main():
    aa = titleScreen()
    aDarkForest(aa)    

def aDarkForest(aa):
    print("\n----------------------------------------------------------------------------------------------------------")
    print("\n* you wake up on a dirt path, dark trees swaying all around you *")
    print("\n* you attempt to stand up and double over, what happened? *")
    print("\n* blood stains your clothes, scratch marks run down your legs and arms *")
    if aa[8] == 1:
        print("\n* looking behind you, you find a wooden sword, nearly broken *")
    print("\n* you check your pockets,", aa[7], "gold pieces and", aa[9], "cake *")
    print("\n* your name is all you remember,", aa[0])
    print("\n* you gather your belongings and start down the path, the moon glistening above *")
    path(aa)

def path(aa):
    aa[12] += 1
    print("\n* | (n)orth | (e)ast | (s)outh | (w)est | *")
    print("\n* | (q)uit  | (d)isplay stats  | (g)old | *")
    pathChoice = str(input("\n--> "))
    while pathChoice != 'n' and pathChoice != 'e' and pathChoice != 's' and pathChoice != 'w' and pathChoice != 'q' and pathChoice != 'd' and pathChoice != 'g':
        pathChoice = str(input("\n--> "))
    if pathChoice == 'q':
        quit()
    elif pathChoice == 'g':
        print("\n| *",aa[7], "shiny gold pieces * |") ; aa[12] -= 1 ; path(aa)
    elif pathChoice == 'd':
        aa[12] -= 1 ; stats(aa)
    elif pathChoice == 'n' or pathChoice == 's' or pathChoice == 'e' or pathChoice == 'w':
        pathChance(aa)

def pathChance(aa):
    pathOptions = ['easyEnemy', 'easyEnemy','easyEnemy','nothing','nothing','nothing','nothing']
    if aa[12] >= 1:
        pathOptions.append('alter')
    if aa[12] >= 5:
        pathOptions.append('shop')
    if aa[12] >= 40:
        pathOptions.append('secret')
    if aa[12] >= 10:
        pathOptions.append('hardEnemy')
    if aa[12] >= 20:
        pathOptions.append('hardEnemy')
    if aa[12] >= 30:
        pathOptions.remove('easyEnemy')
    if aa[12] >=40:
        pathOptions.remove('easyEnemy')
        pathOptions.append('alter')
    if aa[12] >=45:
        pathOptions.append('hardEnemy')
    if aa[12] >= 55:
        pathOptions.remove('easyEnemy')

    if aa[4] == 1:
        pathOptions.append('difficultPath')
    pathIs = random.choice(pathOptions)
    if pathIs == 'easyEnemy':
        hardCombatVariable = 0
        easyCombat(aa,hardCombatVariable)
    elif pathIs == 'hardEnemy':
        hardCombatVariable = 1
        easyCombat(aa,hardCombatVariable)
    elif pathIs == 'alter':
        alter(aa)
    elif pathIs == 'shop':
        shop(aa)
    elif pathIs == 'nothing':
        nothing(aa)
    elif pathIs == 'difficultPath':
        difficultPath(aa)
    elif pathIs == 'secret':
        secret(aa)

def difficultPath(aa):
    goldPieces = random.randrange(30,50)
    print('* you make your way through a difficult path using your agility skills and find',goldPieces,'gold pieces')
    path(aa)

def secret(aa):
    print('* while walking you stumble upon a huge rock wall and 5 empty slots inside the wall *')
    print('* the voice behind the trees whispers... spell the word *')
    word = str(input('--> '))
    lowerWord = word.lower()
    if lowerWord == 'exile':
        print('* you slot the tablets into the wall...exile...suddenly a section of the wall crumbles to dust and you stand in front of a black gaping hole... *')
        print('* you enter the cave and light a torch... unfortunately by doing so you accidentally woke the gigantic sleeping dragon directly in front of you *')
        print('* before you even have time to react it opens its eyes and swings its tail, swatting you against the cave wall and breaking some of your bones *')
        print('* you stand and face the Dragon *')
        hardCombatVariable = 2
        easyCombat(aa,hardCombatVariable)
    else:
        print('* you spell',word,'but nothing happens... *')
        path(aa)

def shop(aa):
    print('* you overhear a man talking to himself just behind a row of bushes *')
    print('* as to not be spotted you peer over the bush and see an old man, or possibly human-watcher hybrid, sitting under an artificial light *')
    print('* he appears to be friendly and its clear he\' selling various items which are propped up on tables with prices on next to them *')
    print('* you walk through the bushes and the man greets you with a somewhat cautious smile, "hello traveler - purchase something won\'t you" *')
    print('* you take a look at what he\'s selling... *')
    print('* |---|SHOP|---| *')
    realShop(aa)

def realShop(aa):
    print('* |Gold Pieces: ',aa[7],'| *') 
    cakePrice = 15
    wandPrice = 250
    if aa[5] == 2:
        cakePrice -=2
        wandPrice -=10
    if aa[5] == 3:
        cakePrice -=3
        wandPrice -=20
    if aa[5] == 4:
        cakePrice -=4
        wandPrice -= 30
    if aa[5] == 5:
        cakePrice -=5
        wandPrice -=40
    if aa[13] == 0:
        wand = '(w)and'
    if aa[13] == 1:
        wand = 'Wand Purchased'
    if aa[13] == 0:
        print("* Items Available: |(c)ake <",cakePrice,'g >|',wand,wandPrice,'|(e)xit the shop| *')
    else:
        print("* Items Available: |(c)ake <",cakePrice,'g >|',wand,'|(e)xit the shop| *')
    purchase = str(input('--> '))
    while purchase != 'c' and purchase != 'e' and purchase != 'E' and purchase != 'C' and purchase != 'w' and purchase != 'W':
        purchase = str(input('--> '))
    if purchase == 'c' or purchase == 'C':
        if aa[7] >= cakePrice:
            print('* you bought 1 slice of cake for',cakePrice,'gold pieces *')
            aa[9] += 1
            aa[7] -= cakePrice
        else:
            print('* you cannot afford that *')
            realShop(aa)
    if purchase == 'e' or purchase == 'E':
        print('* you thank the man and continue down the trail again... *')
        path(aa)
    if purchase == 'W' or purchase == 'w':
        if aa[13] == 0:
            if aa[7] >= wandPrice:
                aa[13] = 1
                aa[7] -= wandPrice
        else:
            print('* you already purchased the wand *')
            realShop(aa)

    print('* do you want to purchase more stuff? (y/n) *')
    moreStuff = str(input('--> '))
    while moreStuff != 'y' and moreStuff != 'Y' and moreStuff != 'n' and moreStuff != 'N':
        moreStuff = str(input('--> '))
    if moreStuff == 'y' or moreStuff == 'Y':
        realShop(aa)
    else:
        print('* you thank the man for the goods and set down the trail once more... *')
        path(aa)

def alter(aa):
    print('* as you carefully walk through the woods you notice a strange stone obelisk in the middle of the forest... *')
    print('* you reach out to touch it and it sends a shock through your whole body... *')
    print('* you hear a voice somewhere in the woods... choose *')
    realAlter(aa)
def realAlter(aa):    
    statOptions = ['strength','health','speed','intelligence','luck','mana']
    option1 = random.choice(statOptions)
    option2 = random.choice(statOptions)
    option3 = random.choice(statOptions)
    while option1 == option2 or option1 == option3 or option2 == option3:
        option1 = random.choice(statOptions)
        option2 = random.choice(statOptions)
        option3 = random.choice(statOptions)
    print('* |',option1,'|',option2,'|',option3,'| *')
    chosenStat = str(input('--> '))
    while chosenStat != option1 and chosenStat != option2 and chosenStat != option3:
        chosenStat = str(input('--> '))
    if chosenStat == 'strength':
        print('* you feel power course through your veins *') ; aa[2] += 1
    if chosenStat == 'health':
        print('* you feel the iron in your blood solidify *')
        hI = [1,1,1,1,2,2,2,2,2,3,3,3,4,4,5] ; t = random.choice(hI) ; aa[1] += t ; aa[11] += t
    if chosenStat == 'speed':
        if aa[3] <= 4:
            print('* you feel quicker and lighter on your feet *')
            aa[3] += 1
        else:
            print('* you already are as quick as they come *')
            print('* suddenly the alter glows white and youre blinded by the light... when you regain sight, the alter has changed... *')
            realAlter(aa)
    if chosenStat == 'intelligence':
        if aa[5] <= 4:
            print('* you feel smarter and more savvy *')
            aa[5] += 1
        else:
            print('* you already are as smart as they come *')
            print('* suddenly the alter glows white and youre blinded by the light... when you regain sight, the alter has changed... *')
            realAlter(aa)
    if chosenStat == 'luck':
        if aa[6] <= 4:
            print('* you feel the urge to go buy a lottery ticket *')
            aa[6] += 1
        else:
            print('* you already are as lucky as they come... *')
            print('* suddenly the alter glows white and youre blinded by the light... when you regain sight, the alter has changed... *')
            realAlter(aa)
    if chosenStat == 'mana':
        aa[15] += 3
    print('* although you are not sure what just happened you press forward... *') ; path(aa)

def nothing(aa):
    nothingOptions = [1,2,3,4,5,6,7]
    nothingChosen = random.choice(nothingOptions)
    if nothingChosen == 1:
        print('\n* you trudge forward, trees in every direction... *')
        path(aa)
    elif nothingChosen == 2:
        if aa[10] <= 4:
            print('\n* stumbling through the foliage you spot something laying in a bush... you pick up a stone tablet, a red glow emitting from it... *')
            print('\n* you added the tablet to your inventory (stats) *')
            aa[10] += 1
        else:
            randomGoldAmount = random.randrange(1,30)
            print('\n* as you make your way through a bush you notice something shiny and pickup',randomGoldAmount,'gold pieces')
            aa[7] += randomGoldAmount
        path(aa)
    elif nothingChosen == 3:
        print('\n* walking down the path you spot some cake laying in a ditch beside you... *')
        print('\n* you added 1 cake to your inventory (stats) *')
        aa[9] += 1 ; path(aa)
    elif nothingChosen == 4:
        print('\n* you move forward, ducking between the low hanging branches... *') ; path(aa)
    elif nothingChosen == 5:
        print('\n* you look up at the moon and contemplate how you ended up here, unfortunately you hit a tree branch and took 1 damage *')
        aa[1] = aa[1] - 1
        if aa[1] <= 0:
            print('* somehow that tree branch managed to kill you and you die on the forest floor... *')
            quit()
        path(aa)
    elif nothingChosen == 6:
        print('\n* you notice a creature in the woods but it has yet to notice you... *')
        print('\n* do you want to attack the monster? (y/n) *')
        yesMonster = str(input('--> '))
        while yesMonster != 'y' and yesMonster != 'n' and yesMonster != 'Y' and yesMonster != 'N':
            yesMonster = str(input('--> '))
        hardOrEasy = [0,0,0,0,1] ; hardOrEasySelection = random.choice(hardOrEasy)
        if hardOrEasy == 1:
            hardCombatVariable == 1
        else:
            hardCombatVariable = 0
        if yesMonster == 'y' or yesMonster == 'Y':
            easyCombat(aa,hardCombatVariable)
        if yesMonster == 'n' or yesMonster == 'N':
            print('* probably a smart decision... *') ; path(aa)
    elif nothingChosen == 7:
        print('* you come across a stream in the forest, you plunge your hands in and feel your wounds close... *')
        print('* HP Restored *') ; aa[1] = aa[11] ; path(aa)

def easyCombat(aa,hardCombatVariable):
    aa[14] = aa[15] 
    atk = aa[2]
    speed = aa[3]
    luck = aa[6]
    sword = aa[8]
    
    easyMonster = {'Zombie':[10,1,3,0,1,5,10],'Skeleton':[8,2,3,1,2,8,14],'Jelly':[6,1,3,0,3,10,20],'Wanderer':[3,3,4,2,3,20,30]}
    if hardCombatVariable == 1: 
        easyMonster = {'Silent':[10,3,6,2,3,20,30],'Watcher':[8,4,7,3,5,30,50],'Evoker':[5,6,8,2,6,30,60],'Defect':[1,20,30,2,3,100,200]}
    preWords = ['terrifying','horrific','insane','grotesque','mad','wild']
    preWord = random.choice(preWords)
    if hardCombatVariable == 2:
        easyMonster = {'Dragon':[10,100,120,5,15,1000,2000]}

#296-308 is the function for mob encounter probability
    allMonsters = []
    for key in easyMonster:
        allMonsters.append([key, easyMonster[key][0]])
    total = 0
    for m in allMonsters:
        total = total + m[1]
    selection = random.randint(0, total-1)
    highpoint = 0
    for m in allMonsters:
        highpoint = highpoint + m[1]
        if selection < highpoint:
            enemy = m[0]
            break

    minHealth = easyMonster[enemy][1]
    maxHealth = easyMonster[enemy][2]
    mobHealth = random.randrange(minHealth, maxHealth)
    maxMobHealth = mobHealth

    minGold = easyMonster[enemy][5]
    maxGold = easyMonster[enemy][6]
    goldDrop = random.randrange(minGold,maxGold)
    if aa[6] == 2:
        goldDrop += 10
    if aa[6] == 3:
        goldDrop += 20
    if aa[6] == 4:
        goldDrop += 30
    if aa[6] == 5:
        goldDrop += 50
    
    if hardCombatVariable == 0 or hardCombatVariable == 1:
        print("\n* stumbling along you run into a",preWord, enemy," *")
    while aa[1] >= 1 and mobHealth >= 1:
        
        swordPower = 0
        if sword == 0:
            swordPower = atk
        elif sword == 1:
            swordPower = atk + 1
        elif sword == 2:
            swordPower = atk + 2
        elif sword == 3:
            swordPower = atk + 4
        elif sword == 4:
            swordPower = atk * 2
        elif sword == 5:
            swordPower = atk * 3
        variableAttack = [swordPower - 1, swordPower, swordPower + 1]
        newDamage = random.choice(variableAttack)
        
        minDamage = easyMonster[enemy][3]
        maxDamage = easyMonster[enemy][4]

        print("\n* health: ",aa[1],"/",aa[11],"| attack: <",variableAttack[0],"-",variableAttack[2],"> | mana: ",aa[14], "| " ,enemy, "health: ",mobHealth,"/",maxMobHealth,"| attack: <",minDamage,"-",maxDamage,"> *")
        print("\n* what do you do? |(f)ight|(r)un away|(c)ast spell|(e)at cake| *")
        choice = str(input("--> "))
        
        while choice != 'f' and choice != 'r' and choice != 'c' and choice != 'e':
            choice = str(input("\n--> "))
        if choice == 'f':
            print("\n* you swing at the", enemy,"dealing",newDamage,"damage *")
            mobHealth -= newDamage
            if mobHealth <= 0:
                if hardCombatVariable == 1 or hardCombatVariable == 0:
                    print("\n* you defeated the",enemy,"and gained",goldDrop,"gold pieces *")
                    aa[7] = aa[7] + goldDrop
                    path(aa)
                else:
                    print("* you defeated the dragon...as his head hits the floor the stone wall behind it opens up revelealing sunlight... you step out into the fresh air...not a tree in sight *")
                    print("THANK YOU FOR PLAYING")
                    quit()
            mobAttack = random.randrange(minDamage,maxDamage)
            print("\n* the",enemy,"swings at you dealing", mobAttack,"damage *")
            aa[1] = aa[1] - mobAttack
        elif choice  == 'r':
            if hardCombatVariable != 2:
                chancetorun = ['1','2']
                if speed == 1:
                    chancetorun += '3'
                    chancetorun += '4'
                    chancetorun += '5'
                    chancetorun += '6'
                elif speed == 2:
                    chancetorun += '3'
                    chancetorun += '4'
                    chancetorun += '5'
                elif speed == 3:
                    chancetorun += '3'
                    chancetorun += '4'
                elif speed == 4:
                    chancetorun += '3'
                ran = random.choice(chancetorun)
                if ran == '1':
                    print("\n* you escaped the fight and gained nothing * ")
                    path(aa)
                elif ran == '2' or ran == '3' or ran == '4' or ran == '5' or ran == '6':
                    print("\n* you failed to escape and the",enemy,"swings at you *")
                    mobAttack = random.randrange(minDamage,maxDamage)
                    aa[1] = aa[1] - mobAttack
            else:
                print('* you cannot escape the dragon *')
        elif choice == 'c':
            spellDamage = (atk * 2) - 1
            if aa[13] == 1:
                if aa[14] >= 3:
                    aa[14] -= 3
                    print("\n* you cast a spell and dealt ", spellDamage,"damage *")
                    mobHealth = mobHealth - spellDamage
                    if mobHealth <= 0:
                        if hardCombatVariable == 2:
                            print("* You defeat the dragon and notice light shining behind where the dragon was standing... *")
                            print("* You step out into the light and look around... not a tree in sight *")
                            print("* THANK YOU FOR PLAYING *")
                            quit()
                        print("\n* you defeated the",enemy," and gained", goldDrop,"gold pieces *")
                        aa[7] += goldDrop
                        path(aa)
                    mobAttack = random.randrange(minDamage,maxDamage)
                    print("\n* the ",enemy," swings at you dealing ", mobAttack," damage *")
                    aa[1] = aa[1] - mobAttack
                else:
                    print('* you are all out of mana *')
            else:
                print("* you have no idea how to use a spell or how you would even cast one *")
        elif choice == 'e':
            if aa[9] <= 0:
                print("\n* you are all out of cake *")
            elif aa[1] == aa[11]:
                print("\n* you already have the maximum amount of health *")
            elif aa[1] < aa[11]:
                print("\n* you stop for a second to have a nice slice of cake *")
                aa[1] = aa[1] + 5
                aa[9] = aa[9] - 1
                if aa[1] > aa[11]:
                    aa[1] = aa[11]
    if aa[1] <= 0:
        print("\n* you succombed to the",enemy,"and died *") ; quit()
    else:
        if hardCombatVariable != 2:
            print(hardCombatVariable)
            print("\n* you defeated the",enemy,"and gained", goldDrop,"gold pieces *")
        if hardCombatVariable == 2:
            print('\n* you slay the dragon and collect your spoils...a section of the wall collapses behind the dragon and you step out of the cave into the sunlight... not a tree in sight *')
            print('\nTHANK YOU FOR PLAYING')
            quit()
    aa[7] = aa[7] + goldDrop
    path(aa)

def stats(aa):
    perks = []
    if aa[4] == 1:
        perks.append('Agility (Allows different path traversal in certain areas)')
    if aa[16] == 1:
        perks.append('Bludgeon (Deals massive damage one time, doesn\'t end your turn')
    if perks == []:
        perks = 'No Perks'
    if aa[8] ==  0:
        displaySword = 'No Sword'
    elif aa[8] == 1:
        displaySword = 'Wooden Sword'
    
    print("\n ---- |",aa[0],"| ---- ")
    print("\n|Health       <",aa[1], "/", aa[11],">")
    print("\n|Attack       <",aa[2],">")
    print("\n|Mana         <",aa[15],">")
    print("\n|Speed        <",aa[3],"/ 5>")
    print("\n|Intelligence <",aa[5],"/ 5>")
    print("\n|Luck         <",aa[6],"/ 5>")
    print("\n|Sword        <",displaySword,">")
    print("\n|Gold         <",aa[7],">")
    print("\n|Cake         <",aa[9],">")
    print("\n|Perks:       <",perks,">")
    if aa[13] == 1:
        print("\n|Wand         < Yes >")
    if aa[10] == 1:
        print("\n|Your 1 tablet reads a single letter...'E'|")
    if aa[10] == 2:
        print("\n|You look at both your tablets...'EX'|")
    if aa[10] == 3:
        print("\n|Your three tablets spell the letters...'EXI'|")
    if aa[10] == 4:
        print("\n|The tablets begin to form a word...'EXIL'|")
    if aa[10] == 5:
        print("\n|Having collected five tablets you read the word they spell...'EXILE'|")
    path(aa)

def titleScreen():
    print("\n* welcome to a dark forest *")
    print("\n* enter the name of your character *")
    name = str(input("\n--> "))
    print("\n* pick one: strength, health, speed *")
    attribute1 = str(input("\n--> "))
    while attribute1 != 'strength' and attribute1 != 'health' and attribute1 != 'speed':
        print("\n* pick one: strength, health, speed *")
        attribute1 = str(input("\n--> "))
    print("\n* pick another: intelligence, luck, agility *")
    attribute2 = str(input("\n--> "))
    while attribute2 != 'intelligence' and attribute2 != 'luck' and attribute2 != 'agility':
        print("\n* pick another: intelligence, luck, agility *")
        attribute2 = str(input("\n--> "))
    print("\n* choose an item: sword, gold, cake *")
    iItem = str(input("\n--> "))
    while iItem != 'sword' and iItem != 'gold' and iItem != 'cake':
        print("\n* choose an item: sword, gold, cake *")
        iItem = str(input("\n--> "))
    
    hp = 10 #health
    atk = 1 #attack
    speed = 1 #1 / 10 chance to escape fights, if speed is chosen add 1 to make it 2/10(1/5 chance to escape)
    agility = 0 # Whether or not the player can go down certain paths, if attribute1 == agility then agility == 1, allowing them to choose those paths
    intell = 1 #Intelligence is on a scale of 1-5 starting at 0, can go up through selecting it at ts or at alters, LOWERS SHOP PRICES
    luck = 1 #Luck gives more gold after defeating mobs, on a scale of 1-5 
    gold = 10 #currency
    sword = 0 #0 is no sword, 1 is wooden, 2 is bronze, 3 is iron, 4 is blackstone,  5 is magical
    cake = 3 #healing item
    
    if attribute1 == 'health':
        hp += 3
    elif attribute1 == 'strength':
        atk += 1
    elif attribute1 == 'speed':
        speed += 1
    if attribute2 == 'agility':
        agility += 1
    elif attribute2 == 'intelligence':
        intell += 1
    elif attribute2 == 'luck':
        luck += 1
    if iItem == 'gold':
        gold += 10
    elif iItem == 'sword':
        sword +=1
    elif iItem == 'cake':
        cake += 3
    tablet = 0
    maxHP = hp
    prog = 0
    wand = 0
    mana = 10
    maxMana = mana
    bludgeon = 0
    aa = [name, hp, atk, speed, agility, intell, luck, gold, sword, cake, tablet, maxHP,prog,wand,mana,maxMana,bludgeon]
    return aa
main()
