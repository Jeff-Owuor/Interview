import csv

 
# opening the CSV file
with open('interview.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
  result = []
  array = []
  # displaying the contents of the CSV file
  for lines in csvFile:
       result.append(lines[-1])
       for i in lines:
            if result.count(i)>0:
               array.append(result.count(i))
        
print(result)
print(array[::-1])