import random

user_tries = 0
playing = True
cpu_input = random.randint(-100,100)

while True:
    user_input = input("Would you like to guess what number I am thinking? (y/n) ")
    if user_input in ["n", "no"]:
        print("FINE THEN!")
        quit()
    if user_input not in ["y", "n", "yes", "no"]:
        continue
    
    while True:
        if playing == False:
            quit()
        try:
            if(user_tries == 0):
                user_input = int(input("What's your first guess? "))
                user_tries+=1
            else:
                user_input = int(input("Next guess? "))
            
            if user_input == cpu_input:
                if user_tries == 0:
                    print("You got it first try!")
                    playing = False
                    quit()
                else:
                    print("Well done, it took " + str(user_tries) + " tries.")
                    playing = False
                    quit()
            elif user_input < cpu_input:
                print("Higher...")
                user_tries+=1
            elif user_input > cpu_input:
                print("Lower...")
                user_tries+=1
        except:
            if playing == True:
                print("Type a number!")
    
            
    
    
        
    
    