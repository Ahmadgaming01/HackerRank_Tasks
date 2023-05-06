'''
String s = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

'''


def minion_game(string):
    s = 'BANRNA'
    Vowels = ["A","E","I","O","U"]
    StuartScoreCons = 0
    KevinScoreVowels = 0
    
    for x in range(len(s)):
        
        if s[x] in Vowels:
            KevinScoreVowels+=len(s)-x

        else:
            StuartScoreCons+=len(s)-x
  
    if KevinScoreVowels> StuartScoreCons:
        print("Kevin",KevinScoreVowels)
    elif KevinScoreVowels<StuartScoreCons:
        print("Stuart",StuartScoreCons)
    else:
        print("Draw")

        return


    
    minion_game(s)


