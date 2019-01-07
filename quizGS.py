print ("What is 1+1?")
print ("")


q1 = False
q2 = False
score = 0
rage = 0
ppq = 50 #points per question

while q1 == False:
    try:
        print("(1) 4")
        print("(2) 3")
        print("(3) 2")
        print("(4) 1")
        a1 = int(input("Your answer >"))
        if 0 < a1 < 5:
            q1 = True
            if a1 == 3:
                score += ppq
                rage = 0
            else:
                score += 0
                rage = 0
        else:
             rage += 1
        if 0 < rage < 4:
            print("Oh come on. You had one job. Answer 1,2,3, or 4. Try again")
        if 3 < rage < 5:
            print ("Oh come on! FFS! 1, 2, 3, or 4! Its not rocket science!")
        if rage == 5:
            print("Im done with you. Go do something else. You are clearly incapable of ansering a simple multiple chice question.")
        if rage >= 6:
            print("Stop. Please, PLEASE stop!")
            
    except ValueError:
        print("Hey. Its a number. 1, 2, 3, or 4. Try again")
#-------------------------------------------------------------------------------
print("Ok, that was easy. Not for long.")
print("Whats 2+2?")
print(" ")

while q2 == False:
    try:
        print("(1) 4")
        print("(2) 8")
        print("(3) 3")
        print("(4) 2")
        a2 = int(input("Your answer >"))
        if 0 < a2 < 5:
            q2 = True
            if a2 == 1:
                score += ppq
                rage = 0
            else:
                score += 0
                rage = 0
        else:
             rage += 1
        if 0 < rage < 4:
            print("Oh come on. You had one job. Answer 1,2,3, or 4. Try again")
        if 3 < rage < 5:
            print ("Oh come on! FFS! 1, 2, 3, or 4! Its not rocket science!")
        if rage == 5:
            print("Im done with you. Go do something else. You are clearly incapable of ansering a simple multiple chice question.")
        if rage >= 6:
            print("Stop. Please, PLEASE stop!")
            
    except ValueError:
        print("Hey. Its a number. 1, 2, 3, or 4. Try again")
#---------------------------------------------------------------------------------
print ("Nice job completing this super HARD test! Your score is", score,"%") 
