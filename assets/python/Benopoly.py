import random

# to do: finish chance and community chest
# increment rrsOwned and utsOwned when trading or buying rr or utility
# fix weirdness going on with afterOption

isDubs = 0
p1Pos = 0
p2Pos = 0
p3Pos = 0
p4Pos = 0

activePlayer = 1
gameGoing = True
players = 4

total = 0
p1Cash = 1500
p2Cash = 1500
p3Cash = 1500
p4Cash = 1500

p1JRolls = 0 
p2JRolls = 0
p3JRolls = 0
p4JRolls = 0
hasGOJcard = [False, False, False, False, False, False]
rrsOwned = [0,0,0,0,0,0]
utsOwned = [0,0,0,0,0,0]
houses = [0]*40
price = [0,60,0,60,0,200,100,0,100,120,0,140,150,140,160,200,180,0,180,200,0,220,0,220,240,200,260,260,150,280,0,300,300,0,320,200,350,0,400]
rent0 =[0,2,0,4,0,98, 6,0,6,8,0,10,99,10,12,98,14,0,14,16,0,18,0,18,20,98,22,22,99,24,0,26,26,0,28,98,0,35,0,50]
rent1 = [0,10,0,20,0,99,30,0,30,40,0,50,98,50,60,99,70,0,70,80,0,90,0,90,100,99,110,110,98,120,0,130,130,0,150,99,0,175,0,200]
rent2 = [0,30, 0,60,0,99,90,0,90,100,0,150,98,150,180,99,200,0,200,220,0, 250,0,250, 300,99,330,330,98,360,0,390,390,0,450,99,0,500,0,600]
rent3 = [0,90,0,180,0,99,270,0,270,300,0,450,98,450,500,99,550,0,550,600,0,700,0,700,750,99,800,800,98,850,0,900,900,0,1000,99,0,1100,0,1400]
rent4 = [0,160,0,320,0,99,400,0,400,450,0,625,98,625,700,99,750,0,750,800,0,875,0,875,925,99,975,975,98,1025,0,1100,1100,0,1200,99,0,1300,0,1700]
rent5 = [0,250,0,450,0,99,550,0,550,600,0,750,98,750,900,99,950,0,950,1000,0,1050,0,1050,1100,99,1150,1150,98,1200,0,1275,1275,0,1400,99,0,1500,0,2000]
housePrice = [50,50,50,50,50,50,50,50,50,50,100,100,100,100,100, 100,100,100,100,100, 150,150,150,150,150, 150,150,150,150,150, 200,200,200,200,200, 200,200,200,200,200]
propID = ['Go', 'BrP1', 'Community Chest', 'BrP2', 'Income Tax 2.0M', 'RR1', 'LbP1', 'Chance', 'LbP2', 'LbP3', 'Just Visiting', 'PP1', 'Utility - Piedmont Natural Gas', 'PP2', 'PP3', 'RR2', 'OP1', 'Community Chest', 'OP2', 'OP3', 'Free Parking', 'RP1', 'Chance', 'RP2', 'RP3', 'RR3', 'YP1', 'YP2', 'Utility - Duke Power', 'YP3', 'Go to jail', 'GP1', 'GP2', 'Community Chest', 'GP3', 'RR4', 'Chance', 'DBP1', 'Luxury Tax 1.0M', 'DBP2'] 
isProperty = [False, True, False, True, False, True, True, False, True, True, False, True, True, True, True, True, True, False, True, True, False, True, False, True, True, True, True, True, True, True, False, True, True, False, True, True, False, True, False, True]
isOwned = [False]*40
ownedOutright = [True]*40
monopolized = [False]*40
p1Props=[]
p2Props=[]
p3Props=[]
p4Props=[]


chestCards = ['Advance to Go (Collect $200)','Bank error in your favor: collect $200','Doctor\'s fees: Pay $50',
              'Get Out of Jail Free: this card may be kept until needed, or sold',
              'Go to Jail: go directly to jail, Do not pass Go, do not collect $200',
              'It is your birthday: Collect $10 from each player',
              'Grand Opera Night: collect $50 from every player for opening night seats',
              'Income Tax refund: collect $20','Life Insurance Matures: collect $100','Pay Hospital Fees of $100',
              'Pay School Fees of $50','Receive $25 Consultancy Fee',
              'You are assessed for street repairs: $40 per house, $115 per hotel',
              'You have won second prize in a beauty contest: collect $10','You inherit $100',
              'From sale of stock you get $50','Holiday Fund matures: Receive $100']
chanceCards = ['Advance to Go (Collect $200)','Advance to Illinois Ave:  if you pass Go, collect $200',
               'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown.',
               'Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.',
               'Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.',
               'Advance to St. Charles Place: if you pass Go, collect $200','Bank pays you dividend of $50',
               'Get out of Jail Free:  this card may be kept until needed, or traded/sold','Go back 3 spaces',
               'Go directly to Jail:  do not pass Go, do not collect $200',
               'Make general repairs on all your property: for each house pay $25, for each hotel $100',
               'Pay poor tax of $15','Take a trip to Reading Railroad:  if you pass Go, collect $200',
               'Take a walk on the Boardwalk:  advance token to Boardwalk',
               'You have been elected chairman of the board:  pay each player $50',
               'Your building loan matures:  collect $150','You have won a crossword competition: collect $100']

def unmortgage():
   global p1Cash
   global p2Cash
   global p3Cash
   global p4Cash
   
   if activePlayer == 1:
      print 'These are your properties\' identifying numbers'
      print p1Props
      for i in p1Props:
        print propID[i]
      mortgage = input("Player:  %s  Which one of dem dere properties you wanna unmortgage, Cap'n?" % (activePlayer))
      ownedOutright[mortgage] = True
      interest = price[mortgage] * .10
      p1Cash -= (price[mortgage]/2) + interest
      p1Cash = round(p1Cash)
   if activePlayer == 2:
      print 'These are your properties\' identifying numbers'
      print p1Props
      for i in p1Props:
        print propID[i]
      mortgage = input("Player:  %s  Which one of dem dere properties you wanna unmortgage, Cap'n?" % (activePlayer))
      ownedOutright[mortgage] = True
      interest = price[mortgage] * .10
      p2Cash -= (price[mortgage]/2) + interest
      p2Cash = round(p2Cash)
   if activePlayer == 3:
      print 'These are your properties\' identifying numbers'
      print p3Props
      for i in p3Props:
        print propID[i]
      mortgage = input("Player:  %s  Which one of dem dere properties you wanna unmortgage, Cap'n?" % (activePlayer))
      ownedOutright[mortgage] = True
      interest = price[mortgage] * .10
      p3Cash -= (price[mortgage]/2) + interest
      p3Cash = round(p3Cash)
   if activePlayer == 4:
      print 'These are your properties\' identifying numbers'
      print p4Props
      for i in p4Props:
        print propID[i]
      mortgage = input("Player:  %s  Which one of dem dere properties you wanna unmortgage, Cap'n?" % (activePlayer))
      ownedOutright[mortgage] = True
      interest = price[mortgage] * .10
      p4Cash -= (price[mortgage]/2) + interest
      p4Cash = round(p4Cash)
   afterOption()


def rrRent(paidPlayer):
  if rrsOwned[paidPlayer - 1] == 0:
    print 'Error in processing railroad rent'
  if rrsOwned[paidPlayer - 1] == 1:
    rent = 25
  elif rrsOwned[paidPlayer - 1] == 2:
    rent = 50
  elif rrsOwned[paidPlayer - 1] == 3:
    rent = 100
  elif rrsOwned[paidPlayer - 1] == 4:
    rent = 200
    
  return rent

def utRent(paidPlayer):
  if utsOwned[paidPlayer - 1] == 0:
    print 'Error in processing Utility rent'
  if utsOwned[paidPlayer - 1] == 1:
    rent = total * 4
  elif utsOwned[paidPlayer - 1] == 2:
    rent = total * 10
  return rent

    
    
      
  

def shuffleCards():
  global chestCards
  global chanceCards
  random.shuffle(chestCards)
  random.shuffle(chanceCards)
  
  
        
def next():
  global isDubs 
  global activePlayer
  isDubs = 0
  if players > activePlayer:
    activePlayer += 1
  else: 
    activePlayer = 1
    
def jailcheck():
  if activePlayer == 1 and p1Pos == 999:
    return True
  elif activePlayer == 2 and p2Pos == 999:
    return True
  elif activePlayer == 3 and p3Pos == 999:
    return True
  elif activePlayer == 4 and p4Pos == 999:
    return True
  else:
    return False

def throwDice():
  global isDubs
  global total
  mupdate(p1Props)
  mupdate(p2Props)
  mupdate(p3Props)
  mupdate(p4Props)
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  total = dice1 + dice2
 #total = 12
  print dice1
  print dice2
  print 'Player %s  rolled a' % (activePlayer)
  print total
  if isDoubles(dice1, dice2):
      print 'Doubles!'
      isDubs += 1
  if isDubs < 3:
      movePos(total)
      if activePlayer == 1:
        option(p1Pos) 
      if activePlayer == 2:
        option(p2Pos)
      if activePlayer == 3:
        option(p3Pos)
      if activePlayer == 4:
        option(p4Pos)
             
      if not isDoubles(dice1,dice2):
        next()
            #option to buy property	
                    
  if isDubs > 2:
      movePos(999)
      print 'YOU\'RE IN JAIL! YOU ROLLED DUBS THRICE!'
      afterOption()          
      next()  

def roll():
  global total
  global gameGoing
  global isDubs
  global p1Cash
  global p2Cash
  global p1Props
  global p2Props
  global ownedOutright
  print ("P1 Cash:")
  print p1Cash
  print ("P2 Cash")
  print p2Cash
  gameGoing = True
  
  while gameGoing:
    print '---------------------------------------------------------------------------------------'
    if jailcheck():
      jailroll()
    else:
      letter1 = raw_input("Player:  %s  R to Roll, B to Build, M to Mortgage, I to Implode your precious buildings, U to Unmortgage, Q to quit" % (activePlayer))
      if letter1.upper() == "R":
        throwDice()
      if letter1.upper() == "U":
        unmortgage()
      if letter1.upper() == "B":
        mupdate(p1Props)
        mupdate(p2Props)
        mupdate(p3Props)
        mupdate(p4Props)
        monoList = hasMonopoly()

        if not monoList:
          print "You have no monopolies to speak of, good sir."
        else: 
          print 'Here are your monopolies:'
          print monoList
          for i in monoList:
            print propID[i]
            
          construction = input("Player:  %s  Where would you like to build, dear chap?" % (activePlayer))
          constructIt(construction)	
          
          #need to check to see if building evenly
          houses[construction] += 1
        
      if letter1.upper() == "M":
         if activePlayer == 1:
            print 'These are your properties\' identifying numbers'
            print p1Props
            for i in p1Props:
              print propID[i]
            mortgage = input("Player:  %s  Which one of dem dere properties you wanna mortgage, Bubba?" % (activePlayer))
            ownedOutright[mortgage] = False
            mortReturn = price[mortgage] / 2
            p1Cash += mortReturn
         if activePlayer == 2:
            print 'These are your properties\' identifying numbers'
            print p1Props
            for i in p1Props:
              print propID[i]
            mortgage = input("Player:  %s  Which one of dem dere properties you wanna mortgage, Bubba?" % (activePlayer))
            ownedOutright[mortgage] = False
            mortReturn = price[mortgage] / 2
            p1Cash += mortReturn
         if activePlayer == 3:
            print 'These are your properties\' identifying numbers'
            print p3Props
            for i in p3Props:
              print propID[i]
            mortgage = input("Player:  %s  Which one of dem dere properties you wanna mortgage, Bubba?" % (activePlayer))
            ownedOutright[mortgage] = False
            mortReturn = price[mortgage] / 2
            p3Cash += mortReturn
         if activePlayer == 4:
            print 'These are your properties\' identifying numbers'
            print p4Props
            for i in p4Props:
              print propID[i]
            mortgage = input("Player:  %s  Which one of dem dere properties you wanna mortgage, Bubba?" % (activePlayer))
            ownedOutright[mortgage] = False
            mortReturn = price[mortgage] / 2
            p4Cash += mortReturn	
      if letter1.upper() == "I":
         if activePlayer == 1:
            for i in p1Props:
              if houses[i] > 0:
                print i
                print propID[i]
                print 'has ', houses[i], ' buildings'
            implosion = input("Player:  %s  Which one of dem properties\'s buildings you wanna implode, boss?" % (activePlayer))
            if houses[implosion] > 0:
              houses[implosion] -= 1
              mbValue = housePrice[implosion]/2
              p1Cash += mbValue
            else: print 'Nothing there for me to implode.  And I was lookin forward to it too...'
         if activePlayer == 2:
            for i in p2Props:
              if houses[i] > 0:
                print i
                print propID[i]
                print 'has ', houses[i], ' buildings'
            implosion = input("Player:  %s  Which one of dem properties\'s buildings you wanna implode, boss?" % (activePlayer))
            if houses[implosion] > 0:
              houses[implosion] -= 1
              mbValue = housePrice[implosion]/2
              p2Cash += mbValue
            else: print 'Nothing there for me to implode.  And I was lookin forward to it too...'
      if letter1.upper() == 'Q':
        gameGoing = False

def jailroll():
    global p1Cash
    global p2Cash
    global p3Cash
    global p4Cash
    global p1Pos
    global p2Pos
    global p3Pos
    global p4Pos  
    
    letter2 = raw_input("Player:  %s  You're in jail.  R to Roll for Doubles, P to pay your fine of $50." % (activePlayer))
    if letter2.upper()== 'R':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total = dice1 + dice2
        print dice1, " ", dice2
        if dice1 == dice2:
          print 'Congrats, you\'re out of jail with doubles.'
          jailLocation()
          movePos(total)
          if activePlayer == 1:
             option(p1Pos) 
          if activePlayer == 2:
             option(p2Pos)
          if activePlayer == 3:
             option(p3Pos)
          if activePlayer == 4:
             option(p4Pos)
          afterOption()
        else:
          print 'No Doubles for you, jailbird.'
          jailInc()
          next()
        
    if letter2.upper() == 'P':
        jailLocation()
        payYourWayOut()
        throwDice()
           
        

def jailLocation():
  global p1Pos
  global p2Pos
  global p3Pos
  global p4Pos
  if activePlayer == 1:
    p1Pos = 10
  elif activePlayer == 2:
    p2Pos = 10
  elif activePlayer == 3:
    p3Pos = 10
  elif activePlayer == 4:
    p4Pos = 10

def payYourWayOut():
    global p1Cash
    global p2Cash
    global p3Cash
    global p4Cash
    
    if activePlayer == 1:
       p1Cash -= 50
    elif activePlayer == 2:
       p2Cash -= 50
    elif activePlayer == 3:
       p3Cash -= 50
    elif activePlayer == 4:
       p4Cash -= 50

def jailInc():
  global p1JRolls
  global p2JRolls
  global p3JRolls
  global p4JRolls

  if activePlayer == 1: 
    p1JRolls += 1
  if activePlayer == 2:
    p2JRolls += 1
  if activePlayer == 3:
    p3JRolls += 1
  if activePlayer == 4:
    p4JRolls += 1

  if p1JRolls == 3:
    p1JRolls = 0
    payYourWayOut()
  if p2JRolls == 3:
    p2JRolls = 0
    payYourWayOut()
  if p3JRolls == 3:
    p3JRolls = 0
    payYourWayOut()
  if p4JRolls == 3:
    p4JRolls = 0
    payYourWayOut()  

      
def afterOption():
    global gameGoing
    global isDubs
    global p1Cash
    global p2Cash
    global p3Cash
    global p4Cash
    global p1Props
    global p2Props
    global p3Props
    global p4Props
    global ownedOutright

    if activePlayer == 1:
      print 'P1Cash: ', p1Cash
    if activePlayer == 2:
      print 'P2Cash: ', p2Cash
    if activePlayer == 3:
      print 'P3Cash: ', p3Cash
    if activePlayer == 4:
      print 'P4Cash: ', p4Cash

      
    #something is up with this loop, its not working right, i need to fix this
      
    letter2 = raw_input("Player:  %s  R to Roll(If you hit doubles..), B to Build, M to Mortgage, U to Unmortgage, I to Implode your precious buildings, Any Other Key to End Turn" % (activePlayer))
 
    if letter2.upper() == "U":
      unmortgage()
    if letter2.upper() == "B":
      mupdate(p1Props)
      mupdate(p2Props)
      mupdate(p3Props)
      mupdate(p4Props)
      monoList = hasMonopoly()

      if not monoList:
        print "You have no monopolies to speak of, good sir."
      else: 
        print 'Here are your monopolies:'
        print monoList
        for i in monoList:
          print propID[i]
          
        construction = input("Player:  %s  Where would you like to build, dear chap?" % (activePlayer))
        constructIt(construction)	
        
        #need to check to see if building evenly
        houses[construction] += 1
      
      
    if letter2.upper() == "M":
       if activePlayer == 1:
          print 'These are your properties\' identifying numbers'
          print p1Props
          for i in p1Props:
            print propID[i]
          mortgage = input("Player:  %s  Which one of dem dere properties you wanna mortgage, Bubba?" % (activePlayer))
          ownedOutright[mortgage] = False
          mortReturn = price[mortgage] / 2
          p1Cash += mortReturn
       if activePlayer == 2:
          print 'These are your properties\' identifying numbers'
          print p1Props
          for i in p1Props:
            print propID[i]
          mortgage = input("Player:  %s  Which one of dem dere properties you wanna mortgage, Bubba?" % (activePlayer))
          ownedOutright[mortgage] = False
          mortReturn = price[mortgage] / 2
          p1Cash += mortReturn
       if activePlayer == 3:
          print 'These are your properties\' identifying numbers'
          print p3Props
          for i in p3Props:
            print propID[i]
          mortgage = input("Player:  %s  Which one of dem dere properties you wanna mortgage, Bubba?" % (activePlayer))
          ownedOutright[mortgage] = False
          mortReturn = price[mortgage] / 2
          p3Cash += mortReturn
       if activePlayer == 4:
          print 'These are your properties\' identifying numbers'
          print p4Props
          for i in p4Props:
            print propID[i]
          mortgage = input("Player:  %s  Which one of dem dere properties you wanna mortgage, Bubba?" % (activePlayer))
          ownedOutright[mortgage] = False
          mortReturn = price[mortgage] / 2
          p4Cash += mortReturn
       afterOption()
       
    if letter2.upper() == "I":
       if activePlayer == 1:
          for i in p1Props:
            if houses[i] > 0:
              print i
              print propID[i]
              print 'has ', houses[i], ' buildings'
          implosion = input("Player:  %s  Which one of dem properties\'s buildings you wanna implode, boss?" % (activePlayer))
          if houses[implosion] > 0:
            houses[implosion] -= 1
            mbValue = housePrice[implosion]/2
            p1Cash += mbValue
          else: print 'Nothing there for me to implode.  And I was lookin forward to it too...'
       if activePlayer == 2:
          for i in p2Props:
            if houses[i] > 0:
              print i
              print propID[i]
              print 'has ', houses[i], ' buildings'
          implosion = input("Player:  %s  Which one of dem properties\'s buildings you wanna implode, boss?" % (activePlayer))
          if houses[implosion] > 0:
            houses[implosion] -= 1
            mbValue = housePrice[implosion]/2
            p2Cash += mbValue
          else: print 'Nothing there for me to implode.  And I was lookin forward to it too...'    

	   
def constructIt(site):
    global p1Cash
    global p2Cash
    global p3Cash
    global p4Cash
    if activePlayer == 1:    
       p1Cash -= housePrice[site] 
    if activePlayer == 2:
       p2Cash -= housePrice[site]
    if activePlayer == 3:
       p3Cash -= housePrice[site]
    if activePlayer == 4:
       p4Cash -= housePrice[site]

def chest():
    global p1Cash
    global p2Cash
    global p3Cash
    global p4Cash
    global p1Pos
    global p2Pos
    global p3Pos
    global p4Pos
    
    print 'Player %s you landed on Community Chest' % activePlayer
    c = chestCards.pop()
    print c

    if c == 'Advance to Go (Collect $200)':
      if activePlayer == 1:
        p1Cash += 200
        p1Pos = 0
      if activePlayer == 2:
        p2Cash += 200
        p2Pos = 0
      if activePlayer == 3:
        p3Cash += 200
        p3Pos = 0
      if activePlayer == 4:
        p4Cash += 200
        p4Pos = 0
                
    elif c == 'Bank error in your favor: collect $200':
      if activePlayer == 1:
        p1Cash += 200
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash += 200
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash += 200
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash += 200
        print 'P4Cash: ', p4Cash
        
    elif c == 'Doctor\'s fees: Pay $50':
      if activePlayer == 1:
        p1Cash -= 50
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash -= 50
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash -= 50
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash -= 50
        print 'P4Cash: ', p4Cash
        
    elif c == 'Get Out of Jail Free: this card may be kept until needed, or sold':
      hasGOJcard[activePlayer - 1] = True
    elif c == 'Go to Jail: go directly to jail, Do not pass Go, do not collect $200':
      if activePlayer == 1:
        p1Pos = 999
      if activePlayer == 2:
        p2Pos = 999
      if activePlayer == 3:
        p3Pos = 999
      if activePlayer == 4:
        p4Pos = 999
      print 'Player %s is now in Jail.' % activePlayer
        
    elif c == 'It is your birthday: Collect $10 from each player':
      collection = (players - 1) * 10
      if players == 4:
        if activePlayer == 1:
          p1Cash += collection
          p2Cash -= 10
          p3Cash -= 10
          p4Cash -= 10
        if activePlayer == 2:
          p2Cash += collection
          p1Cash -= 10
          p3Cash -= 10
          p4Cash -= 10
        if activePlayer == 3:
          p3Cash += collection
          p2Cash -= 10
          p1Cash -= 10
          p4Cash -= 10
        if activePlayer == 4:
          p4Cash += collection
          p2Cash -= 10
          p3Cash -= 10
          p1Cash -= 10
      if players == 3:
        if activePlayer == 1:
          p1Cash += collection
          p2Cash -= 10
          p3Cash -= 10
        if activePlayer == 2:
          p2Cash += collection
          p1Cash -= 10
          p3Cash -= 10
        if activePlayer == 3:
          p3Cash += collection
          p2Cash -= 10
          p1Cash -= 10
      if players == 2:
        if activePlayer == 1:
          p1Cash += collection
          p2Cash -= 10

    elif c == 'Grand Opera Night: collect $50 from every player for opening night seats':
      collection = (players - 1) * 50
      if players == 4:
        if activePlayer == 1:
          p1Cash += collection
          p2Cash -= 50
          p3Cash -= 50
          p4Cash -= 50
        if activePlayer == 2:
          p2Cash += collection
          p1Cash -= 50
          p3Cash -= 50
          p4Cash -= 50
        if activePlayer == 3:
          p3Cash += collection
          p2Cash -= 50
          p1Cash -= 50
          p4Cash -= 50
        if activePlayer == 4:
          p4Cash += collection
          p2Cash -= 50
          p3Cash -= 50
          p1Cash -= 50
      if players == 3:
        if activePlayer == 1:
          p1Cash += collection
          p2Cash -= 50
          p3Cash -= 50
        if activePlayer == 2:
          p2Cash += collection
          p1Cash -= 50
          p3Cash -= 50
        if activePlayer == 3:
          p3Cash += collection
          p2Cash -= 50
          p1Cash -= 50
      if players == 2:
        if activePlayer == 1:
          p1Cash += collection
          p2Cash -= 50
        if activePlayer == 2:
          p2Cash += collection
          p1Cash -= 50

    elif c == 'Income Tax refund: collect $20':
      if activePlayer == 1:
        p1Cash += 20
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash += 20
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash += 20
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash += 20
        print 'P4Cash: ', p4Cash
        
    elif c == 'Life Insurance Matures: collect $100':
      if activePlayer == 1:
        p1Cash += 100
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash += 100
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash += 100
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash += 100
        print 'P4Cash: ', p4Cash
        
    elif c == 'Pay Hospital Fees of $100':
      if activePlayer == 1:
        p1Cash -= 100
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash -= 100
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash -= 100
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash -= 100
        print 'P4Cash: ', p4Cash
        
    elif c == 'Pay School Fees of $50':
      if activePlayer == 1:
        p1Cash -= 50
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash -= 50
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash -= 50
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash -= 50
        print 'P4Cash: ', p4Cash 

    elif c == 'Receive $25 Consultancy Fee':
      if activePlayer == 1:
        p1Cash += 25
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash += 25
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash += 25
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash += 25
        print 'P4Cash: ', p4Cash 

    elif c == 'You are assessed for street repairs: $40 per house, $115 per hotel':
      print 'todo'
    elif c == 'You have won second prize in a beauty contest: collect $10':
      if activePlayer == 1:
        p1Cash += 10
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash += 10
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash += 10
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash += 10
        print 'P4Cash: ', p4Cash
        
    elif c == 'You inherit $100':
      if activePlayer == 1:
        p1Cash += 100
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash += 100
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash += 100
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash += 100
        print 'P4Cash: ', p4Cash    

    elif c == 'From sale of stock you get $50':
      if activePlayer == 1:
        p1Cash += 50
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash += 50
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash += 50
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash += 50
        print 'P4Cash: ', p4Cash    

    elif c == 'Holiday Fund matures: Receive $100':
      if activePlayer == 1:
        p1Cash += 100
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash += 100
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash += 100
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash += 100
        print 'P4Cash: ', p4Cash

    afterOption()
        
    
        
def chance():
    global p1Cash
    global p2Cash
    global p3Cash
    global p4Cash
    global p1Pos
    global p2Pos
    global p3Pos
    global p4Pos
    
    print 'Player %s you landed on Chance' % activePlayer
    c = chanceCards.pop()
    print c

    if c == 'Advance to Go (Collect $200)':
      if activePlayer == 1:
        p1Cash += 200
        p1Pos = 0
      if activePlayer == 2:
        p2Cash += 200
        p2Pos = 0
      if activePlayer == 3:
        p3Cash += 200
        p3Pos = 0
      if activePlayer == 4:
        p4Cash += 200
        p4Pos = 0

    elif c =='Advance to Illinois Ave:  if you pass Go, collect $200':
      if activePlayer == 1:
        if p1Pos > 24:
          p1Cash += 200
          print '$200 for passing GO'
        p1Pos = 24
        option(p1Pos)
      if activePlayer == 2:
        if p2Pos > 24:
          p2Cash += 200
          print '$200 for passing GO'
        p2Pos = 24
        option(p2Pos)
      if activePlayer == 3:
        if p3Pos > 24:
          p3Cash += 200
          print '$200 for passing GO'          
        p3Pos = 24
        option(p3Pos)
      if activePlayer == 4:
        if p4Pos > 24:
          p4Cash += 200
          print '$200 for passing GO'
        p4Pos = 24
        option(p4Pos)

    elif c =='Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown.':
      dice1 = random.randint(1,6)
      dice2 = random.randint(1,6)
      total = dice1 + dice2
      rent = total * 10
      print 'You rolled', dice1, ' ', dice2
      print 'Rent = ', rent

      if activePlayer == 1:
        if p1Pos > 12 and p1Pos < 28:
          p1Pos = 28
          cPos = 28
        elif p1Pos < 12:
          p1Pos = 12
          cPos = 12
        else:
          #must pass go
          p1Cash += 200
          print '$200 for passing GO'
      if activePlayer == 2:
        if p2Pos > 12 and p2Pos < 28:
          p2Pos = 28
          cPos = 28
        elif p1Pos < 12:
          p2Pos = 12
          cPos = 12
        else:
          #must pass go
          p2Cash += 200
          print '$200 for passing GO'
      if activePlayer == 3:
        if p3Pos > 12 and p3Pos < 28:
          p3Pos = 28
          cPos = 28
        elif p3Pos < 12:
          p3Pos = 12
          cPos = 12
        else:
          #must pass go
          p1Cash += 200
          print '$200 for passing GO'

      if activePlayer == 4:
        if p4Pos > 12 and p4Pos < 28:
          p4Pos = 28
          cPos = 28
        elif p1Pos < 12:
          p4Pos = 12
          cPos = 12
        else:
          #must pass go
          p1Cash += 200
          print '$200 for passing GO'

          
      if isOwned[cPos]:
        #paidPlayer  = owner of the property  
        for x in range(len(p1Props)):
           if pos == p1Props[x]: 
              paidPlayer = 1
        for x in range(len(p2Props)):
           if pos == p2Props[x]: 
              paidPlayer = 2
        for x in range(len(p3Props)):
           if pos == p3Props[x]: 
              paidPlayer = 3
        for x in range(len(p4Props)):
           if pos == p4Props[x]: 
              paidPlayer = 4
        
        
        if activePlayer == 1:
            if ownedOutright[pos]:
               if paidPlayer == 1:
                   print 'You already own this one.'
               elif paidPlayer == 2:
                   p1Cash -= rent
                   p2Cash += rent
               elif paidPlayer == 3:
                   p1Cash -= rent
                   p3Cash += rent	
               elif paidPlayer == 4:
                   p1Cash -= rent
                   p4Cash += rent
            else: print 'Mortgaged'
                   
        elif activePlayer == 2: 
            if ownedOutright[pos]:
               if paidPlayer == 2:
                   print 'You already own this one.'
               elif paidPlayer == 1:
                   p2Cash -= rent
                   p1Cash += rent
               elif paidPlayer == 3:
                   p2Cash -= rent
                   p3Cash += rent	
               elif paidPlayer == 4:
                   p2Cash -= rent
                   p4Cash += rent 
            else: print 'Mortgaged'
            
        elif activePlayer == 3: 
            if ownedOutright[pos]:
               if paidPlayer == 3:
                   print 'You already own this one.'
               elif paidPlayer == 2:
                   p3Cash -= rent
                   p2Cash += rent
               elif paidPlayer == 1:
                   p3Cash -= rent
                   p1Cash += rent	
               elif paidPlayer == 4:
                   p3Cash -= rent
                   p4Cash += rent 
            else: print 'Mortgaged'
            
        elif activePlayer == 4: 
            if ownedOutright[pos]:
               if paidPlayer == 4:
                   print 'You already own this one.'
               elif paidPlayer == 1:
                   p4Cash -= rent
                   p1Cash += rent
               elif paidPlayer == 3:
                   p4Cash -= rent
                   p3Cash += rent	
               elif paidPlayer == 2:
                   p4Cash -= rent
                   p2Cash += rent 
            else: print 'Mortgaged'
        if not paidPlayer == activePlayer:    
            print 'Player ', activePlayer,' just payed Player ', paidPlayer, ' rent in the amount of: ', rent
      else:
        option(cPos)
              

                
          
          
    elif c =='Advance token to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.':
      print 'todo'
    elif c =='Advance to St. Charles Place: if you pass Go, collect $200':
      if activePlayer == 1:
        if p1Pos > 11:
          p1Cash += 200
          print '$200 for passing GO'
        p1Pos = 11
        option(p1Pos)
      if activePlayer == 2:
        if p2Pos > 11:
          p2Cash += 200
          print '$200 for passing GO'
        p2Pos = 11
        option(p2Pos)
      if activePlayer == 3:
        if p3Pos > 11:
          p3Cash += 200
          print '$200 for passing GO'          
        p3Pos = 11
        option(p3Pos)
      if activePlayer == 4:
        if p4Pos > 11:
          p4Cash += 200
          print '$200 for passing GO'
        p4Pos = 11
        option(p4Pos)
        
    elif c =='Bank pays you dividend of $50':
      if activePlayer == 1:
        p1Cash += 50
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash += 50
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash += 50
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash += 50
        print 'P4Cash: ', p4Cash   
    elif c =='Get out of Jail Free:  this card may be kept until needed, or traded/sold':
        hasGOJcard[activePlayer - 1] = True
    elif c =='Go back 3 spaces':
        if activePlayer == 1:
          p1Pos -= 3
          option(p1Pos)
        if activePlayer == 2:
          p2Pos -=3
          option(p2Pos)
        if activePlayer == 3:
          p1Pos -= 3
          option(p3Pos)
        if activePlayer == 4:
          p2Pos -=3
          option(p4Pos)          
    elif c =='Go directly to Jail:  do not pass Go, do not collect $200':
      if activePlayer == 1:
        p1Pos = 999
      if activePlayer == 2:
        p2Pos = 999
      if activePlayer == 3:
        p3Pos = 999
      if activePlayer == 4:
        p4Pos = 999
      print 'Player %s is now in Jail.' % activePlayer
      
    elif c =='Make general repairs on all your property: for each house pay $25, for each hotel $100':
      print 'todo'
    elif c =='Pay poor tax of $15':
      if activePlayer == 1:
        p1Cash -= 15
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash -= 15
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash -= 15
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash -= 15
        print 'P4Cash: ', p4Cash 
    elif c =='Take a trip to Reading Railroad:  if you pass Go, collect $200':
      if activePlayer == 1:
        if p1Pos > 5:
          p1Cash += 200
          print '$200 for passing GO'
        p1Pos = 5
        option(p1Pos)
      if activePlayer == 2:
        if p2Pos > 5:
          p2Cash += 200
          print '$200 for passing GO'
        p2Pos = 5
        option(p2Pos)
      if activePlayer == 3:
        if p3Pos > 5:
          p3Cash += 200
          print '$200 for passing GO'          
        p3Pos = 5
        option(p3Pos)
      if activePlayer == 4:
        if p4Pos > 5:
          p4Cash += 200
          print '$200 for passing GO'
        p4Pos = 5
        option(p4Pos)
    elif c =='Take a walk on the Boardwalk:  advance token to Boardwalk':
      if activePlayer == 1:
        p1Pos = 39
        option(p1Pos)
      if activePlayer == 2:
        p2Pos = 39
        option(p2Pos)
      if activePlayer == 3:
        p3Pos = 39
        option(p3Pos)
      if activePlayer == 4:
        p4Pos = 39
        option(p4Pos)
        
    elif c =='You have been elected chairman of the board:  pay each player $50':
      collection = (players - 1) * 50
      if players == 4:
        if activePlayer == 1:
          p1Cash -= collection
          p2Cash += 50
          p3Cash += 50
          p4Cash += 50
        if activePlayer == 2:
          p2Cash -= collection
          p1Cash += 50
          p3Cash += 50
          p4Cash += 50
        if activePlayer == 3:
          p3Cash -= collection
          p2Cash += 50
          p1Cash += 50
          p4Cash += 50
        if activePlayer == 4:
          p4Cash -= collection
          p2Cash += 50
          p3Cash += 50
          p1Cash += 50
      if players == 3:
        if activePlayer == 1:
          p1Cash -= collection
          p2Cash += 50
          p3Cash += 50
        if activePlayer == 2:
          p2Cash -= collection
          p1Cash += 50
          p3Cash += 50
        if activePlayer == 3:
          p3Cash -= collection
          p2Cash += 50
          p1Cash += 50
      if players == 2:
        if activePlayer == 1:
          p1Cash -= collection
          p2Cash += 50

    elif c =='Your building loan matures:  collect $150':
      if activePlayer == 1:
        p1Cash += 150
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash += 150
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash += 150
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash += 150
        print 'P4Cash: ', p4Cash   
    elif c =='You have won a crossword competition: collect $100':
      if activePlayer == 1:
        p1Cash += 100
        print 'P1Cash: ', p1Cash
      if activePlayer == 2:
        p2Cash += 100
        print 'P2Cash: ', p2Cash
      if activePlayer == 3:
        p3Cash += 100
        print 'P3Cash: ', p3Cash
      if activePlayer == 4:
        p4Cash += 100
        print 'P4Cash: ', p4Cash   
    afterOption()
def incomeTax():
  global p1Cash
  global p2Cash
  global p3Cash
  global p4Cash
  if activePlayer == 1:
    p1Cash -= 200
  if activePlayer == 2:
    p2Cash -= 200
  if activePlayer == 3:
    p3Cash -= 200
  if activePlayer == 4:
    p4Cash -= 200
  print 'Player ', activePlayer, ' landed on Income Tax.  They paid $200 in income tax and are now considering joining the Tea Party.'
  afterOption()

def luxTax():
  global p1Cash
  global p2Cash
  global p3Cash
  global p4Cash
  if activePlayer == 1:
    p1Cash -= 100
  if activePlayer == 2:
    p2Cash -= 100
  if activePlayer == 3:
    p3Cash -= 100
  if activePlayer == 4:
    p4Cash -= 100
  print 'Player ', activePlayer, ' landed on Luxury Tax.  They paid $100 in luxury tax and are now considering joining the Tea Party.'
  afterOption()

	   
def option(pos):
    global p1Pos
    global p2Pos
    global p3Pos
    global p4Pos
    global p1Cash
    global p2Cash
    global p3Cash
    global p4Cash

    if pos == 4:
      incomeTax()
    if pos == 48:
      luxTax()

    #COMMUNITY CHEST SPACES AT: 2,17,33
    if pos == 2 or pos == 17 or pos == 33:
      chest()

    #CHANCE SPACES AT: 7,22,36
    elif pos == 7 or pos == 22 or pos == 36:
      chance()
    
    #Go to Jail space here
    elif pos == 30:
      print 'Player %s just landed in Jail.' % activePlayer
      if activePlayer == 1:
        p1Pos = 999
        print p1Pos
      if activePlayer == 2:
        p2Pos = 999
      if activePlayer == 3:
        p3Pos = 999
      if activePlayer == 4:
        p4Pos = 999
      afterOption()

    #Free Parking
    elif pos == 20:
      print 'Player %s just landed on Free Parking.' % activePlayer
      if activePlayer == 1:
        p1Cash += 50
        print p1Cash
      if activePlayer == 2:
        p2Cash += 50      
      if activePlayer == 3:
        p3Cash += 50
      if activePlayer == 4:
        p4Cash += 50
      afterOption()
      
    elif isProperty[pos]:
        if isOwned[pos]:	    
            payRent(pos)
        else:
            buyIt(pos)
    else:
      afterOption()
      
	    
def payRent(pos):
    global p1Cash
    global p2Cash
    global p3Cash
    global p4Cash
    
    if monopolized[pos] and ownedOutright[pos]:
       if houses[pos] == 0:
           rent = rent0[pos]*2
       elif houses[pos] == 1:
           rent = rent1[pos]
       elif houses[pos] == 2:
           rent = rent2[pos]
       elif houses[pos] == 3:
           rent = rent3[pos]
       elif houses[pos] == 4:
           rent = rent4[pos]
       elif houses[pos] == 5:
	   rent = rent5[pos]
    elif ownedOutright[pos]:
      rent = rent0[pos]
    else:
      rent = 0

     
    #paidPlayer  = owner of the property  
    for x in range(len(p1Props)):
       if pos == p1Props[x]: 
	  paidPlayer = 1
    for x in range(len(p2Props)):
       if pos == p2Props[x]: 
	  paidPlayer = 2
    for x in range(len(p3Props)):
       if pos == p3Props[x]: 
	  paidPlayer = 3
    for x in range(len(p4Props)):
       if pos == p4Props[x]: 
	  paidPlayer = 4

    if rent == 98 and ownedOutright[pos]:
      rent = rrRent(paidPlayer)
      print 'It\'s a railroad'
      print 'Rent is ', rent
    if rent == 99 and ownedOutright[pos]:
      rent = utRent(paidPlayer)
      print 'It\'s a Utility'
      print 'Rent is ', rent
    
    
    if activePlayer == 1:
        if ownedOutright[pos]:
	   if paidPlayer == 1:
	       print 'You already own this one.'
	   elif paidPlayer == 2:
	       p1Cash -= rent
	       p2Cash += rent
	   elif paidPlayer == 3:
	       p1Cash -= rent
	       p3Cash += rent	
	   elif paidPlayer == 4:
	       p1Cash -= rent
	       p4Cash += rent
	else: print 'Mortgaged'
	       
    if activePlayer == 2: 
        if ownedOutright[pos]:
	   if paidPlayer == 2:
	       print 'You already own this one.'
	   elif paidPlayer == 1:
	       p2Cash -= rent
	       p1Cash += rent
	   elif paidPlayer == 3:
	       p2Cash -= rent
	       p3Cash += rent	
	   elif paidPlayer == 4:
	       p2Cash -= rent
	       p4Cash += rent 
        else: print 'Mortgaged'
	
    if activePlayer == 3: 
        if ownedOutright[pos]:
	   if paidPlayer == 3:
	       print 'You already own this one.'
	   elif paidPlayer == 2:
	       p3Cash -= rent
	       p2Cash += rent
	   elif paidPlayer == 1:
	       p3Cash -= rent
	       p1Cash += rent	
	   elif paidPlayer == 4:
	       p3Cash -= rent
	       p4Cash += rent 
        else: print 'Mortgaged'
	
    if activePlayer == 4: 
        if ownedOutright[pos]:
	   if paidPlayer == 4:
	       print 'You already own this one.'
	   elif paidPlayer == 1:
	       p4Cash -= rent
	       p1Cash += rent
	   elif paidPlayer == 3:
	       p4Cash -= rent
	       p3Cash += rent	
	   elif paidPlayer == 2:
	       p4Cash -= rent
	       p2Cash += rent 
        else: print 'Mortgaged'
      
	

               
    if  not paidPlayer == activePlayer:    
	print 'Player ', activePlayer,' just payed Player ', paidPlayer, ' rent in the amount of: ', rent

    afterOption()

    

def hasMonopoly():
   monoList = []
   if activePlayer == 1:
      for i in p1Props:
	if monopolized[i]:
          monoList.append(i)
   if activePlayer == 2:
      for i in p2Props:
	if monopolized[i]:
	  monoList.append(i)
   if activePlayer == 3:
      for i in p3Props:
	if monopolized[i]:
          monoList.append(i)
   if activePlayer == 4:
      for i in p4Props:
	if monopolized[i]:
	  monoList.append(i)
   return monoList
	  

      
    

def mupdate(props):
    br = []
    brx = [1,3]
    lb = []
    lbx = [6,8,9]
    p = []
    px =[11,13,14]
    o = []
    ox =[16,18,19]
    r = []
    rx = [21,23,24]
    y = []
    yx = [26,27,29]
    g = []
    gx = [31,32,34]
    db = []
    dbx = [37,39]
    props = sorted(props)
    
    if props:
       for i in props:
           if i in brx:
              br.append(i)
    
       if br == brx:
          for i in brx:
             monopolized[i] = True
             
       for i in props:
           if i in lbx:
              lb.append(i)
    
       if lb == lbx:
          for i in lbx:
             monopolized[i] = True
             
       for i in props:
           if i in px:
              p.append(i)
    
       if p == px:
          for i in px:
             monopolized[i] = True
             
       for i in props:
           if i in ox:
              o.append(i)
    
       if o == ox:
          for i in ox:
             monopolized[i] = True
             
       for i in props:
           if i in rx:
              r.append(i)
    
       if r == rx:
          for i in rx:
             monopolized[i] = True
             
       for i in props:
           if i in yx:
              y.append(i)
    
       if y == yx:
          for i in yx:
             monopolized[i] = True
             
       for i in props:
           if i in gx:
              g.append(i)
    
       if g == gx:
          for i in gx:
             monopolized[i] = True
             
       for i in props:
           if i in dbx:
              db.append(i)
    
       if db == dbx:
          for i in dbx:
             monopolized[i] = True     
    
def buyIt(pos):
    global isOwned
    global p1Props
    global p2Props
    global p3Props
    global p4Props
    global p1Cash
    global p2Cash
    global p3Cash
    global p4Cash
    
    
    letter1 = raw_input("Unowned. Buy it?  B to buy.")
    if letter1.upper() == "B":
        if rent0[pos] == 98:
            rrsOwned[activePlayer - 1] += 1
        if rent0[pos] == 99:
            utsOwned[activePlayer - 1] += 1
        if activePlayer == 1:
            p1Props.append(pos)
            isOwned[pos] = True
            print ("Player 1 just bought:")
            print propID[pos]
	    p1Cash -= price[pos]
        if activePlayer == 2:
            p2Props.append(pos)
            isOwned[pos] = True
            print ("Player 2 just bought:")
            print propID[pos]
	    p2Cash -= price[pos]
        if activePlayer == 3:
            p3Props.append(pos)
            isOwned[pos] = True
            print ("Player 3 just bought:")
            print propID[pos]
	    p3Cash -= price[pos]
        if activePlayer == 4:
            p4Props.append(pos)
            isOwned[pos] = True
            print ("Player 4 just bought:")
            print propID[pos]
	    p4Cash -= price[pos]
	if pos == 5 or pos == 15 or pos == 25 or pos == 35:
            rrsOwned[activePlayer - 1] += 1
    else: print 'You chose not to buy it. Cheapskate.'
    afterOption()
    


def movePos(roll):   
      global p1Pos
      global p2Pos
      global p3Pos
      global p4Pos
      global p1Cash
      global p2Cash
      global p3Cash
      global p4Cash
      if roll == 999:
        if activePlayer == 1:
           p1Pos = 999
        if activePlayer == 2:
           p2Pos = 999
        if activePlayer == 3:
           p3Pos = 999
        if activePlayer == 4:
           p4Pos = 999
        afterOption()  
      elif activePlayer == 1:
        if p1Pos + roll > 39:
	   print 'Player %s you received $200 for passing go.' %activePlayer
           p1Cash += 200
           print p1Cash
           p1Pos = (p1Pos + roll) - 40
        else:
           p1Pos += roll
        print('Player 1 now at position:')
        print(p1Pos)
        print('Which is:')
        print(propID[p1Pos])
        if isProperty[p1Pos]:
           print 'property'
        else:
           print 'non-property'
      elif activePlayer == 2:
	if p2Pos + roll > 39:
	    #200 for passing go
	   p2Cash += 200
           p2Pos = (p2Pos + roll) - 40
        else:
           p2Pos += roll
        print('Player 2 now at position:')
        print(p2Pos)
        print('Which is:')
        print(propID[p2Pos])
        if isProperty[p2Pos]:
           print 'property'
        else:
           print 'non-property'
      elif activePlayer == 3:
        if p3Pos + roll > 39:
	  #200 for passing go
           p3Cash += 200
           p3Pos = (p3Pos + roll) - 40
        else:
           p3Pos += roll
        print('Player 3 now at position:')
        print(p3Pos)
        print('Which is:')
        print(propID[p3Pos])
        if isProperty[p3Pos]:
           print 'property'
        else:
           print 'non-property'
      elif activePlayer == 4:
	if p4Pos + roll > 39:
	    #200 for passing go
	   p4Cash += 200
           p4Pos = (p4Pos + roll) - 40
        else:
           p4Pos += roll
        print('Player 4 now at position:')
        print(p4Pos)
        print('Which is:')
        print(propID[p4Pos])
        if isProperty[p4Pos]:
           print 'property'
        else:
           print 'non-property'	 
   
 
  
def isDoubles(int1, int2):
    return int1 == int2


def run():
   global isDubs
   global gameGoing
   isDubs = 0
   shuffleCards()
   

   
   
   
   roll()
   
   roll()
   
   print '1 ', p1Cash
   print '2 ', p2Cash
   print '3 ', p3Cash
   print '4 ', p4Cash
   print 'props p1:'
   print p1Props
   print 'props p2:'
   print p2Props
   print 'props p3: ', p3Props
   print 'props p4: ', p4Props
   

run()


