import random

while True:
    choice = input("Roll the dice (Y/N): ").lower()
    if choice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(4,8)
        print(f"{dice1} {dice2}")
    elif choice == "n":
            print("Thanks! Not a problem")
            break
    else:
        print("Invalid choice! Try again! ")





