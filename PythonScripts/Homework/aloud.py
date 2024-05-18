def readAloud(lst: list[int]) -> list[int]:
    index = 0
    output = []
    k = lst[0]
    while index < len(lst): # Loop until the end of the list
        count = 1 # first enconder
        while index + 1 < len(lst) and lst[index] == lst[index +1]: # while the list still have more number and the next number in the list is the same as current number
            count += 1
            index += 1
        output.extend([count, lst[index]])
        index += 1
    return output
        



lsts = []
while True:
    i = input("Type a number (or 'Done' to stop): ")
    if i.lower() == "done":
        break
    try:
        lsts.append(int(i))
    except ValueError:
        print("Please enter a valid number or 'Done' to stop.")

print(readAloud(lsts))
