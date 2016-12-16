
var total;
var activePlayer = 1;
var gameGoing = true;
var players = 4; 
var player =[];
var isDubs = 0;
var houses = [0]*40;
var price = [0,60,0,60,0,200,100,0,100,120,0,140,150,140,160,200,180,0,180,200,0,220,0,220,240,200,260,260,150,280,0,300,300,0,320,200,350,0,400];
var rent0 =[0,2,0,4,0,98, 6,0,6,8,0,10,99,10,12,98,14,0,14,16,0,18,0,18,20,98,22,22,99,24,0,26,26,0,28,98,0,35,0,50];
var rent1 = [0,10,0,20,0,99,30,0,30,40,0,50,98,50,60,99,70,0,70,80,0,90,0,90,100,99,110,110,98,120,0,130,130,0,150,99,0,175,0,200];
var rent2 = [0,30, 0,60,0,99,90,0,90,100,0,150,98,150,180,99,200,0,200,220,0, 250,0,250, 300,99,330,330,98,360,0,390,390,0,450,99,0,500,0,600];
var rent3 = [0,90,0,180,0,99,270,0,270,300,0,450,98,450,500,99,550,0,550,600,0,700,0,700,750,99,800,800,98,850,0,900,900,0,1000,99,0,1100,0,1400];
var rent4 = [0,160,0,320,0,99,400,0,400,450,0,625,98,625,700,99,750,0,750,800,0,875,0,875,925,99,975,975,98,1025,0,1100,1100,0,1200,99,0,1300,0,1700];
var rent5 = [0,250,0,450,0,99,550,0,550,600,0,750,98,750,900,99,950,0,950,1000,0,1050,0,1050,1100,99,1150,1150,98,1200,0,1275,1275,0,1400,99,0,1500,0,2000];
var housePrice = [50,50,50,50,50,50,50,50,50,50,100,100,100,100,100, 100,100,100,100,100, 150,150,150,150,150, 150,150,150,150,150, 200,200,200,200,200, 200,200,200,200,200];
var propID = ['Go', 'BrP1', 'Community Chest', 'BrP2', 'Income Tax 2.0M', 'RR1', 'LbP1', 'Chance', 'LbP2', 'LbP3', 'Just Visiting', 'PP1', 'Utility - Piedmont Natural Gas', 'PP2', 'PP3', 'RR2', 'OP1', 'Community Chest', 'OP2', 'OP3', 'Free Parking', 'RP1', 'Chance', 'RP2', 'RP3', 'RR3', 'YP1', 'YP2', 'Utility - Duke Power', 'YP3', 'Go to jail', 'GP1', 'GP2', 'Community Chest', 'GP3', 'RR4', 'Chance', 'DBP1', 'Luxury Tax 1.0M', 'DBP2'];
var isProperty = [false, true, false, true, false, true, true, false, true, true, false, true, true, true, true, true, true, false, true, true, false, true, false, true, true, true, true, true, true, true, false, true, true, false, true, true, false, true, false, true];
var isOwned = [false]*40;
var ownedOutright = [true]*40;
var monopolized = [false]*40;
var chestCards = ['Advance to Go (Collect $200)','Bank error in your favor: collect $200','Doctor\'s fees: Pay $50',
              'Get Out of Jail Free: this card may be kept until needed, or sold',
              'Go to Jail: go directly to jail, Do not pass Go, do not collect $200',
              'It is your birthday: Collect $10 from each player',
              'Grand Opera Night: collect $50 from every player for opening night seats',
              'Income Tax refund: collect $20','Life Insurance Matures: collect $100','Pay Hospital Fees of $100',
              'Pay School Fees of $50','Receive $25 Consultancy Fee',
              'You are assessed for street repairs: $40 per house, $115 per hotel',
              'You have won second prize in a beauty contest: collect $10','You inherit $100',
              'From sale of stock you get $50','Holiday Fund matures: Receive $100'];
var chanceCards = ['Advance to Go (Collect $200)','Advance to Illinois Ave:  if you pass Go, collect $200',
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
               'Your building loan matures:  collect $150','You have won a crossword competition: collect $100'];

//shuffles chance and community chest
function shuffleCards(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;
  // While there remain elements to shuffle...
  while (0 !== currentIndex) {
    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;
    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }
  return array;
}


function next(){
  isDubs = 0;
  if (players > activePlayer) {
    activePlayer += 1
  }
  else {
    activePlayer = 1
  }
}

function throwDice(){
  // mupdate(p1Props)
  // mupdate(p2Props)
  // mupdate(p3Props)
  // mupdate(p4Props)
  var dice1 = Math.floor((Math.random() * 6) + 1);
  var dice2 = Math.floor((Math.random() * 6) + 1);
  total = dice1 + dice2

  $('.dice').html('Player ' + activePlayer + " rolled: <br>" + dice1 + " and " + dice2 + " Which is: " + total);

  if (isDoubles(dice1, dice2)){
      $('.dice').append('Doubles!');
      isDubs += 1;
    }

  if (isDubs < 3) {
    
  }

//build option first

  // if (isDubs < 3):
  //     movePos(total)
  //     if activePlayer == 1:
  //       option(p1Pos) 
  //     if activePlayer == 2:
  //       option(p2Pos)
  //     if activePlayer == 3:
  //       option(p3Pos)
  //     if activePlayer == 4:
  //       option(p4Pos)
             
  //     if not isDoubles(dice1,dice2):
  //       next()
  //           #option to buy property 
                    
  // if isDubs > 2:
  //     movePos(999)
  //     print 'YOU\'RE IN JAIL! YOU ROLLED DUBS THRICE!'
  //     afterOption()          
  //     next()  
}

function chest(){
  console.log("chest");
}

function chance(){
  console.log("chance");
}

function luxTax(){
  console.log("lux tax");
}

function incomeTax(){
  console.log("income tax")
}

//labels properties that are part of monopolies as such
function mupdate(){

}

function jailAnnouncement(){
  console.log("in jail");
}

function parkingAnnouncement(){
  console.log("free parking");
}

function isDoubles(one, two){
	if (one === two){
		return true
	}
	else return false;
}

function createPlayers(){
  for (i = 1; i <= players; i++) {
    var newPlayer = new Player(i);
    player.push(newPlayer);
  }
}

function updateDebug(){
  for(i in player) {
    $('#debug').append(player[i].playerDetails());
  }
}

//player constructor
function Player(id) {
	this.id = id;
	this.cash = 1500;
	this.pos = 0;
	this.props = [];
	this.jRolls = 0;
	this.hasGOJcard = false;
	this.rrsOwned = 0;
	this.utsOwned = 0;
  this.jailed = false;
}

Player.prototype.playerDetails = function() {
    return ('Player ' + this.id + '<br>' + 'Cash: ' + this.cash + '<br>' + 'Position: ' + this.pos + '<br>' + 'Properties: ' + this.props + '<br>' + '<br>');
};

Player.prototype.option = function() {
    //pay your taxes
    switch(this.pos) {
      case 4:
        //pay your taxes
        incomeTax();
        break;
      case 48:
        luxTax();
        break;
      case 2:
      case 17:
      case 33:
        //draw Community Chest card
        chest();
        break;
      case 7:
      case 22:
      case 36:
        //draw Chance Card
        chance();
        break;
      case 30:
        this.jailed = true;
        this.pos = 999;
        jailAnnouncement();
        break;
      case 20:
        //Free parking awards $100
        this.cash += 100;
        parkingAnnouncement();
        break;
    }
    //checks if property owns and pays rent or prompts to buy
    if (isProperty[this.pos]){
      if (isOwned[this.pos]){
        payRent(this.pos);
      }
      else {
        buyIt(this.pos);
      }
    }
    this.afterOption();
}

Player.prototype.afterOption = function() {

};

  

// Player.prototype.playerDetails = function() {

// var player1 = new Player(1);
// $('#debug').html(player1.playerDetails());

//run game code (debug)
createPlayers();
updateDebug();
chanceCards = shuffleCards(chanceCards);
chestCards = shuffleCards(chestCards);