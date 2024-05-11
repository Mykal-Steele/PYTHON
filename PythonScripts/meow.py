hour: int = int(input())
minute: int = int(input())
meowing:bool = input().lower() == 'true'

trouble = (hour > 21 and meowing) or (hour <= 6 and minute < 30 and meowing) 
print(trouble)
