import re

# Your code goes here
find_members = []
Target = "find"
for i in dir(re):
    if Target in i:
        find_members.append(i)
print(sorted(find_members))