
print ("What is 1+1?")
print ("")


q1 = False
q2 = False
q3 = False
q4 = False
score = 0
rage = 0
ppq = 25 #points per question

print("(1) 4")
print("(2) 3")
print("(3) 2")
print("(4) 1")
while q1 == False:
    try:
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

print("(1) 4")
print("(2) 8")
print("(3) 3")
print("(4) 2")
while q2 == False:
    try:
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
print("What is the meaning to life, the universe, and everything?")
print(" ")

print("(1) To love")
print("(2) 69")
print("(3) 42")
print("(4) To live")
while q3 == False:
    try:
        a3 = int(input("Your answer >"))
        if 0 < a3 < 5:
            q3 = True
            if a3 == 3:
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
print("John has 4 apples and his train is 5 minutes early.")
print("Calcuate the mass of the sun")
print(" ")

print("(1) 1.989 × 10^30 kg")
print("(2) 1.98 × 10^50 kg")
print("(3) .435 × 10^30 g")
print("(4) .435 × 10^50 g")
while q4 == False:
    try:
        a4 = int(input("Your answer >"))
        if 0 < a4 < 5:
            q4 = True
            if a4 == 1:
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
