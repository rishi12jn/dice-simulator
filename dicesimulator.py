import random

def roll_dice():
    return random.randint(1,6)

def main():
    while True:
        input("Press enter to roll the dice...")
        result=roll_dice()
        print(f"you rolled a {result}")
        
        play_again=input("Do you want to roll again(y/n)").lower()
        if play_again!='y':
            print("thnaks")
            break
        
if __name__=="__main__" :
    main()