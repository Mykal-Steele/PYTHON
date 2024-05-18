# (a4, Task_6) #

import time 
import sys

# Calculate sum of the squared digits of a number
def sumOfDigitsSquared(n: int) -> int:
    result = []  # Stores squared digits
    for i in str(n):  # Loops through each digit of the number
        output = int(i) ** 2  # Squares the digit
        result.append(output)  # Adds squared digit to result
    return sum(result)  # Returns sum of squared digits

# Checks if a number is happy
def isHappy(n: int) -> bool:
    while n != 1 and n != 4:  # Loops until number becomes 1 (happy) or 4 (unhappy)
        n = sumOfDigitsSquared(n)  # Computes sum of squared digits
    return n == 1  # Returns True if number is happy

# Generates list of happy numbers up to given index
def listOfHappy(index: int) -> list:
    num = 1  # Starts with number 1
    numList = []  # Stores happy numbers
    while len(numList) < index:  # Loops until desired number of happy numbers is reached
        if isHappy(num):  # Checks if current number is happy
            numList.append(num)  # Adds happy number to list
        num += 1  # Moves to next number
    return numList  # Returns list of happy numbers
def quit_script():
    print("Exiting the script. Goodbye!👋")
    time.sleep(1)
    sys.exit()

# Infinite loop to prompt user for input
while True:
    ui = input("Press 'K' to find the kth\nPress 'H' to check if a number is a Happy Number\nPress 'Q' to quit the script\n\nType...")  # Asking for user input
    if ui.lower() == 'k':  # Checks if user wants to find the kth happy number
        time.sleep(0.5)
        while True:
            k = int(input("Enter the k-th index for the Happy Number: "))  # Asking for the index of the happy number
            if k <= 0:  # Checking if index is valid
                print("\n$$❌ Invalid input. The Value Can't be Lower than 1.$$\n")  # Printing an error message for invalid input
            else:
                break
        kth = listOfHappy(k)  # Generating list of happy numbers up to specified index
        print("- The happy number at index", ui, "is:", int(kth[-1]))  # Printing the kth happy number
        time.sleep(1.4)  # Pausing execution for 1.4 seconds
        
    elif ui.lower() == 'h':  # Checks if user wants to check if a number is happy
        time.sleep(0.5)
        while True:
            num = int(input("Enter a number to check if it's a Happy Number: "))  # Asking for the number to check
            if num <= 0:  # Checking if number is valid
                print("\n$$❌ Invalid input. The Value Can't be Lower than 1.$$\n")  # Printing an error message for invalid input
            else:
                break
        n = sumOfDigitsSquared(num)  # Computing sum of squared digits of the input number
        print(isHappy(n))  # Printing whether the number is happy or not
        time.sleep(1.4)  # Pausing execution for 1.4 seconds
        
    elif ui.lower() == 'q':  # Checks if user wants to quit the script
        quit_script()  # Calling the function to quit the script

    else:  # Handles invalid input
        print("\n$$❌ Invalid input. Please try again. $$\n")  # Printing an error message for invalid input
        time.sleep(1)  # Pausing execution for 1 second