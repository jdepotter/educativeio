def printDiag(input, rows, columns):
    i = 0
    j = 0
    while i < rows and j < columns:
        line = ''
        x = i
        y = j
        while x != -1 and y < columns:
            line += str(input[x][y]) + " "
            x -= 1
            y += 1
        
        print(line)
        
        if i < rows:
            i += 1

        if i == rows:
            j += 1
            i = rows - 1
        

printDiag([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]], 5, 4)
        