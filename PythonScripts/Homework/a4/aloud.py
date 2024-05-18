# (a4, Task_4) #
# FUNCTION #
def readAloud(lst: list[int]) -> list[int]:
    index = 0
    output = []
    k = lst[0]
    while index < len(lst): # Loop until the end of the list
        count = 1 # first enconder
        while index + 1 < len(lst) and lst[index] == lst[index +1]: # While the list still has more numbers and the next number in the list is the same as the current number...
            count += 1
            index += 1
        output.extend([count, lst[index]])
        index += 1
    return output
        

# INPUT #

lsts = []
w = True
while True:
    if w == True:
        i = input("You could type multiple numbers. \nType your first number (or 'Done' to stop): ")
        w = False
    else:
        i = input("Type your Next numbers (or 'Done' to stop): ")

    if i.lower() == "done":
        break
    try:
        lsts.append(int(i))
    except ValueError:
        print("Please enter a valid number or 'Done' to stop.")

print(readAloud(lsts))
