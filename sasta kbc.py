n = input("Are you ready to play??(yes/no)")
prize=0
if(n=='yes'):
    x = int(input('''QUESTION 1. World literacy day is observed on:
    1. Sep 8
    2. Nov 28
    3. May 2
    4. Sept 22'''))
    if(x==1):
        print("Sep 8 is correct answer")
        prize = prize+5000
        print("Till now, you've won", prize)
        t = input("Do you want to continue? (yes/no)")
        if(t=='yes'):
            y = int(input('''QUESTION 2: The langauge of Lakshadweep, a Union Territory of India is:
            1. Tamil
            2. Hindi
            3. Malayalam
            4. Telugu'''))
            if(y==3):
                print("Malayalam is correct answer")
                prize = prize+15000
                print("Till now, you've won", prize)
                t = input("Do you want to continue? (yes/no)")
                if(t=='yes'):
                    z = int(input('''QUESTION 3: Bahubali festival is related to:
                    1. Islam
                    2. Hindiuism
                    3. Buddhism
                    4. Jainism'''))
                    if(z==4):
                        print("Jainism is the correct answer!!")
                        prize = prize+80000
                        print("Till now, you've won", prize)
                        t = input("Do you want to continue? (yes/no)")
                        if(t=='yes'):
                            a = int(input('''QUESTION 4. Who is the author of Manas Ka Hans:
                            1. Kushwant Singh
                            2. Prem Chand
                            3. Jayshankar Prasad
                            4. Amrit Lal Nagar'''))
                            if(a==4):
                                print("Amrit Lal Nagar is the correct answer!!")
                                print("5 CRORE")
                                prize= 50000000
                                print("Congratulations, you've won", prize)
                            else:
                                print("Sorry, wrong answer, you've lost all your winnings")
                        else:
                            print("congrtulations, you've successfully exited the game with Rs",prize)
                    else:
                        print("Wrong answer, you've bveen eliminated")
                else:
                    print("congrtulations, you've successfully exited the game with Rs",prize)


            else:
                print("Wrong answer, you've been eliminated")
        
        else:
            print("congrtulations, you've successfully exited the game with Rs.5000")


    else    :
            print("wrong answer, you're eliminated")