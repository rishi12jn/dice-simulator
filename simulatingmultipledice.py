import random

def roll_dice(num_dice,num_sides):
    return[random.randint(1,num_sides) for _ in range(num_dice)]
    
def main():
    while True:
        try:
            num_dice=int(input("enter the number of dice to roll"))
            num_sides=int(input("enter number of sides:"))
        except ValueError:
            print("please enter valid number")
            continue
        
        input("press enter to roll the dice...")
        results=roll_dice(num_dice,num_sides)
        print(f"you rolled:{results}")
        
        play_again=input("do you want to roll again(y/n):").lower()
        if play_again!="y":
            print("thanks")
            break
        if __name__=="__main__":
            main()