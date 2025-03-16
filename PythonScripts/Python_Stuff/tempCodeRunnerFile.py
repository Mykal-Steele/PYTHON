
def isItThree(num):
    sum = 0
    while num >=0:
        reg = num %10
        sum += reg
        num = num // 10
    return(sum % 3 == 0)

isItThree(241)