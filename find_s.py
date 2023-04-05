import csv
def updatehypothesis(x, h):
    if h == []:
        return x
    for i in range( 0, len(h)):
        if x[i].upper() != h[i].upper():
            h[i] == "?"
    return h
if __name__ == "_main_":
    data = []
    h = []
    with open ('C:\Users\user\Desktop\database.csv', 'r') as file:
        reader =csv.reader(file)
        print("Data:")
        for row in reader:
            data.append(row)
            print(row)
        if data:
            for x in data:
                if x[-1].upper() == "YES":x.pop()
                updatehypothesis(x,h)
                printf ("lnHypothesis:", h)
