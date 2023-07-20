age = "My name is John"

print(len(age)) #length of the whole string
print(age[3:6]) #print the character between the given position
print(age[3:9:2]) #print the character bettween the given position while skipping 
print(age.upper()) #Uppercase
print(age.count("n")) #counting the number of n appear
print(age.index("n")) #first position of the apperance of n
print(age.startswith("My")) #boolean of how the string start
print(age.endswith("John")) #boolean of how the string end
print(age.split("  "))

astrring = [2,4,6,2,6,8]
print(astrring.index(4))
print(astrring[::-1]) #reverse the string, the number how many skipped
print(astrring[3:]) #start counting from the given position
