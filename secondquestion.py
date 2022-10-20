import csv
from collections import Counter
 
# opening the CSV file
with open('interview.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
  result = []
  
  # displaying the contents of the CSV file
  
  for lines in csvFile:
       result.append(lines[-1])            
print(list(Counter(result).keys())[0:11])