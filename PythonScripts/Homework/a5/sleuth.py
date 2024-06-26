words = ["bog", "moon", "rabbit", "the", "bit", "raw"]
grid = [["r","a","w","b","i","t"],
["x","a","y","z","c","h"],
["p","q","b","e","i","e"],
["t","r","s","b","o","g"],
["u","w","x","v","i","t"],
["n","m","r","w","o","t"]]


def word_sleuth(grid: list[list[str]], w: list[str]):
    contain = []
    first = []
    xi=0
    containx, grid_size = stright(grid, w, contain)
    output = vertical(grid, w, grid_size, xi, first, containx)
    print(output)


    



def stright(grid: list[list[str]], w: list[str], contain) -> bool:
    for i in w:
        for y in grid:  
            concentrated = "".join(y)
            grid_size = len(concentrated)
            if i in concentrated:
                contain.append(i)   
            else:
                "no"
                
    return contain, grid_size


def vertical(grid: list[list[str]], w: list[str], grid_size, xi, first, contain) -> bool:
    for i in w:
        while  xi < grid_size:
            for z in grid:
                first.append(z[xi])
            ztrated = "".join(first)
            
            xi += 1
        if i in ztrated:
                contain.append(i)
    return contain

def diagonal(matrix, word):
    directions = [[1, 1], [-1, 1]]  # Right diagonal and left diagonal directions   
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    for i in range(rows):
        for j in range(cols):
            for direction in directions:
                found = True
                x, y = i, j
                for char in word:
                    if not (0 <= x < rows and 0 <= y < cols and matrix[x][y] == char):
                        found = False
                        break
                    x += direction[0]
                    y += direction[1]
                
                if found:
                    # Calculate starting row and column based on direction
                    start_row = i
                    start_col = j
                    if direction == [1, 1]:  # Right diagonal
                        end_row = x - 1
                        end_col = y - 1
                    elif direction == [-1, 1]:  # Left diagonal
                        end_row = x + 1
                        end_col = y - 1
                    
                    return (start_row, start_col, end_row, end_col)
    
    return None

def make_unique(lst: list[str]) -> list[str]:
    pass


word_sleuth(grid, words)