import math
import csv
with open ("data.csv",newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

finaldata = data[0]
def mean(finaldata):
    total = 0
    n = len(finaldata)
    for x in finaldata:
        total = total + int(x)
    mean = total / n
    return mean

squaredlist = []
for Number in finaldata:
    A = int(Number)- mean(finaldata)
    A = A**2 
    squaredlist.append(A) 

sum = 0
for I in squaredlist:
    sum = sum + I

n = len(finaldata)
result = sum / (n - 1)    
standarddivation = math.sqrt(result)

print(standarddivation)
