
def isItThree(num):
    sum = 0
    while num > 0:
        reg = num %10
        sum += reg
        num = num // 10
    return(sum % 3 == 0)

num = 664577685556758577351325135135315325251323324399911523233333333333333333333333333333333
print(isItThree(num))
print(num %  3== 0)