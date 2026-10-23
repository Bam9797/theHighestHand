import random


class Enemy():
    def __init__(self, personality):
        self.personality = personality
        # self.victory = victory
        # self.losses = losses
        # self.Round = 0
    def personality(self):
        return self.personality
    def Introduction(self, result):
        print(f"\n\nyour next opponent is... {self.personality['Name']}.\n")
        if result == 0:
            print(f"{self.personality['introductionN']}\n")
        elif result <0:
            print(f"{self.personality['introductionL']}\n")
        elif result >0:
            print(f"{self.personality['introductionW']}\n")
    def Round(self, win):
        if win == 0:
            print(f"\n{self.personality['RoundN'][random.randint(0,len(self.personality['RoundN'])-1)]}\n")
        elif win <0:
            print(f"\n{self.personality['RoundL'][random.randint(0,len(self.personality['RoundL'])-1)]}\n")
        elif win >0:
            print(f"\n{self.personality['RoundW'][random.randint(0,len(self.personality['RoundW'])-1)]}\n")
        
    def Win(self):
        self.personality["wins"] += 1
        print(f"\n{self.personality['Victory'][random.randint(0,len(self.personality['Victory'])-1)]}\n")
    def Lost(self):
        self.personality["losses"] += 1
        print(f"\n{self.personality['Defeat'][random.randint(0,len(self.personality['Defeat'])-1)]}\n")

CaptainBlackhawk={
    "Name": "Captain Johnathan Blackhawk",
    "introductionN": "Ye Dare match wits with me? \n Prepare ye self!",
    "introductionL": "Ye want rematch?\n Yar Har Har! Bring it!",
    "introductionW": "Ye be a worthy opponent, but Aye will not lose again!",
    "wins": 0,
    "losses": 0,
    "RoundN": ["Get out me Head","We be in lockstep","luck we aren't we...","knock it off the mental","Cheap trick is all you got!"],
    "RoundL": ["Yar Har Har!","Ye gettin' seasick","keep your wits up","the fool's fallen over","keep yer wits about ye!"],
    "RoundW": ["Strong move...","Don't underestimate me, it ain't over yet!","ye be a worthy opponent, but Aye will not lose again!","aye may have misjudged the situation..."],
    "Victory": ["I may have lost this time, maybe next time will be different","strong player but don't let it go to your head","aye it happens to the best of us...","good game, hope to see ye again!"],
    "Defeat": ["Yar Har Har!","Ye need more practice","Ye need more practice","Keep yer wits about ye!","Hope to see ye again... after ye've had more practice!"]
}

BanditKing={
    "Name": "Bandit King Yazif",
    "introductionN": "a little worm challenging me?\n I will crush you like the bug you are!",
    "introductionL": "you want rematch?\n you should've just quit...",
    "introductionW": "you dare challenge me again?\n I will crush you and your huge ego!",
    "wins": 0,
    "losses": 0,
    "RoundN": ["your little!","get out my head twerp!","your mind tricks won't work on me!","knock it off!","Cheap trick is all you got!"],
    "RoundL": ["Ha Ha Ha!"," ...","your pathetic!","you fool!","...Just like a bug..."],
    "RoundW": ["I will not lose again!","Don't underestimate me!","I am the superior warrior!"],
    "Victory": ["I may have lost this time, but I will return and crush you like the bug you are!","I may have misjudged you this time... but won't make that mistake again!","..."],
    "Defeat": ["Ha Ha Ha!"," Loser!"," your pathetic!","you fool!","...Just like a bug..."]
}

SirMerick={
    "Name": "Sir Merick",
    "introductionN": "you wish to match wits with me? let's see if you can...",
    "introductionL": "you want rematch? i needed a new training dummy anyway...",
    "introductionW": "...I won't lose again...",
    "wins": 0,
    "losses": 0,
    "RoundN": ["Great Minds, Eh.","cute parlor trick but that won't help you.","Did you think wouldn't notice","How?!"],
    "RoundL": ["Success!"," ..."," naivete at its finest","you fool!","you leave much to be desired..."],
    "RoundW": ["I will not lose again!","Don't underestimate me!","your lucky one aren't you...",""],
    "Victory": ["HOW COULD I LOSE?","I tire of playing scum like you!","...","your luck will run out...SCUM!!"],
    "Defeat": ["I guess you were as dumb as you look..."," And here I thought you would be a challenge..."," your pathetic!","pity you weren't good enough for training","Fool is a fool"]
}

randomEnemies=[CaptainBlackhawk,BanditKing,SirMerick]
