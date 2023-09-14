import csv 

filename = "aapl.csv"

fields=[]
rows=[]

with open(filename,'r') as csvfile:
    # creando un lector de csv 
    csvreader = csv.reader(csvfile)
    # extrayendo nombres de archivos 
    fields= next(csvreader)

    for row in csvreader:
        rows.append(row)


    print("Total no. of rows: %d"%(csvreader.line_num))

print('Field names are:' + ','.join(field for field in fields))


print('\nFirst  rows are:\n')
for row in rows[:5]:

    for col in row:
        print("%10s"%col,end=""),
    print('\n')
