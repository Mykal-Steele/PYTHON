# (a4, Task_2)

# It takes an integer called upto and prints numbers and their remainders.
def powerLoop(upto: int) -> None:
    # Go through numbers from 0 to upto (inclusive).
    for i in range(upto + 1):  
        # Print the current number (i) and its remainder when 7 is raised to that power and divided by 97.
        print(i, (7**i) % 97)

# Ask the user for a number and run the powerLoop function with it.
powerLoop(int(input("Give me a number: ")))
