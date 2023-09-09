import random 
import csv

filename = "randomNumbers.csv"
fields=[]
rows=[]


with open(filename,'w', newline='') as csvfile:
        
    writer=csv.writer(csvfile,delimiter='|')

    for _ in range(5):

        numbers=random.uniform(0,1)
        print(numbers)
        writer.writerow([numbers])

with open(filename,'r') as csvfile1:
    csvreader = csv.reader(csvfile1)


    for fila in csvreader:
        print(f"Numero por fila: {fila}")

