def loveTri(n: int) -> list[list[int]]:
    line = 0
    output = []
    filled = 0
    if n >0:
        output.append(1)
        line +=1
        filled += 1
        up = output
        print(output)
    while line < n:
        line +=1
        output = []
        output.append(up[-1])
        l= 1

 
loveTri(3)