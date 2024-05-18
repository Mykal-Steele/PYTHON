# (a4, Task_3) #

import time
import sys
load = False
def star(k):
    if k == 0:
        print("N/A")
    asterisk = "*"
    hash_char = '#'
    n = ((k - 1) * 2) + 1  # Get the number of * at the bottom
    last = n  # Save the value of 'n' to the variable 'last' because we are going to change the 'n' value but want to use its value before changing it later on
    first = True  # This is used to assign the number of '#' in the first line, and we remove '#' again and again after this to get the triangle shape

    n = 1  # to set the start of the loop

    while n != last:
        if first:
            hash_str = int(((last - 1) / 2)) * hash_char  # This calculation makes the '#' pattern for the first line
            print(hash_str + (asterisk * n) + hash_str)  # This prints the first line of the triangle
        else:  # This will loop until complete
            hash_str = hash_str[:-1]  # remove a '#'
            print(hash_str + (asterisk * n) + hash_str)

        first = False
        n += 2 # Increment by 2 because the number of asterisks increases by 2 after each line
    if extra == False:
        print(asterisk * last)  # Printing the last line, which will never include a '#'. This is the easiest part :D
    else:
        pass

def upside_down_star(k):
    asterisk = "*"
    hash_char = '#'
    n = (((k*(-1)) - 1) * 2) + 1  # Get the number of * at the top
    last = n  # Save the value of 'n' to the variable 'last' because we are going to change the 'n' value but want to use its value before changing it later on
    first = True  # This is used to assign the number of '#' in the first line, and we remove '#' again and again after this to get the triangle shape

    n = 1  # to set the start of the loop
    if extra == False:
        print(asterisk * last)  # Printing the first line, which will never include a '#'. This is the easiest part :D
    else:
        pass

    while n != last:
        if first:
            afterFull = (asterisk * last)[:-2]  # This remove two * 
            print(hash_char + (afterFull) + hash_char) 
            
        else:  # This will loop until complete
            
            hash_char = hash_char + '#' # add a '#'
            afterFull = afterFull[:-2] # remove two # after each line
            print(hash_char + (afterFull) + hash_char)  
            
        first = False # checking
        n += 2 # Increment by 2 because the number of asterisks increases by 2 after each line

prompt = """-------------------------------------------------------------

--- Type the k value [OR] Switch to Diamond Mode ---

Positive 'k' generates the top part of the triangle.
Negative 'k' generates the bottom part of the triangle.

[OR]

Type 'dia' for the Diamond Pattern. It combines both the top and bottom parts of the triangle

-------------------------------------------------------------
Type... """   
while True:
    k = input(prompt)

    def loading_animation(duration=2):
        start_time = time.time()
        while True:
            for char in '|/-\\':
                sys.stdout.write('\r' + 'Loading ' + char)
                sys.stdout.flush()
                time.sleep(0.1)
                # Check if the duration has elapsed
                if time.time() - start_time >= duration:
                    return


    try:
        k = int(k)
        extra = False
        if int(k) >= 0:
            
            loading_animation(duration=0.5)
            print("\n")
            
            star(int(k))  # Calling the function with the input of k
        elif int(k) < 0:    
            loading_animation(duration=0.5)
            print("\n")
            upside_down_star(int(k))

    except ValueError:
        while True:
            up = int(input("\n-------------------------------------------------------------\n\nType the size of the Diamond will have\nNegative numbers won't work here\n\n -------------------------------------------------------------\nType... "))
            if up >= 0:
                up = up + 1
                k = up
                extra = True
                loading_animation(duration=0.5)
                print("\n")
                if k >= 0:
                    star(int(k))
                    
                    upside_down_star(int(-k))
                else:
                    print("The value has to be greater than 0")
                break
            else:
                print("\nXX#The value can't be lower than 1XX\n")

