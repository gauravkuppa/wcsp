import itertools
from datetime import date
import os
toulbar2Path = '/home/gauravkuppa24/toulbar2/build/bin/Linux/toulbar2'

class NQueens:

    n = 0

    def __init__(self, n):
        self.n = n

    def header(self):
        title = str(self.n) + "QueensProblem " + str(self.n) + " " + str(self.n) + " " + str(self.n ** 2) + " 1000000"
        domain = ((str(self.n) + " ") * n)
        return title +  "\n" + domain
    
    def constraint(self, possibleColumnCombinations, row_i, row_j):
        rowDifference = abs(row_i - row_j)
        strArray = list()
        for a, b in possibleColumnCombinations:
            # make sure that the two are not equal
            if a == b:
                strArray.append(str(a) + " " + str(b) + " 100")

            # make sure diagonals are not crossing
            if abs(a - b) == rowDifference:
                strArray.append(str(a) + " " + str(b) + " 100")
            
        
        strArray.insert(0, "2 " + str(row_i) + " " + str(row_j) + " 0 " + str(len(strArray)))
        return strArray


    def soft_constraint(self, row_i):
        strArray = list()
        #distinguish when n is even
        
        
        if self.n % 2 == 0:
            for i in range(n):
                if (n * row_i + i + row_i) % 2 == 1: #black
                    strArray.append(str(i) + " 20")


        #distinguish when n is odd
        else:
            for i in range(n):
                if (n * row_i + i % 2) == 1:
                    strArray.append(str(i) + " 20") # cost
                
        strArray.insert(0, "1 " + str(row_i) + " 0 " + str(len(strArray)))

        return strArray

while True:
    try:
        n = int(input("Enter a value for N:"))
    except ValueError:
        n = input("Please enter only an integer.")
        continue
    else:
        break


today = date.today()
d1 = today.strftime("%d_%m_%Y")
fName = str(n) + "Queens" + str(d1) + ".wcsp"
f = open(fName,"w+")
possibleColumnCombinations= list(itertools.product(list(range(0, n)), list(range(0, n))))
possibleRowCombinations = possibleColumnCombinations.copy()
for row_i, row_j in possibleRowCombinations:
    if row_i == row_j:
        possibleRowCombinations.remove((row_i, row_j))
test = NQueens(n)
f.write(test.header() + '\n')

for row_i in range(n):
    for string in test.soft_constraint(row_i):
        f.write(string + '\n')

for row_i, row_j in possibleRowCombinations:
    for string in test.constraint(possibleColumnCombinations, row_i, row_j):
        f.write(string +'\n')
print("Done")
f.close()
print(fName)


os.system("python main.py -f " + fName + " -t -K 3 -p" + toulbar2Path + " -O solution.sol")
