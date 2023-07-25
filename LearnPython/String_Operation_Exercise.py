s = "Perk et ath cafe, AS"
# Length should be 20
print("The length of the string is: %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first a index is: %d" % s.index("a"))

# Number of a's should be 2
print("The number of a is: %d" % s.count("a"))

# Slicing the string into bits
# Start to 5
print("index 4 to end is: %s" % s[4:])
# 5 to 10
print("index 4 to 9 is: %s" % s[4:9])
# Just number 12
print("index 11 is: %s" % s[11])
#(only odd index)
print("char at odd index are: %s" % s[1::2])

# 5th-from-last to end
print("start from 5 from last to end index is: %s" % s[-5:])
# Convert everything to uppercase
print(s.upper())

# Convert everything to lowercase
print(s.lower())

# Check how a string starts
if s.startswith("Perk"):
    print("The string start with Perk")

# Check how a string ends
if s.endswith("ome!"):
    pass
# Split the string into three separate strings, each containing only a word
#No way i am not change my string s again to mkae this thing work, string s already doesnt make sense :)