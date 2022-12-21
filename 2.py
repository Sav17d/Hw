direction = input("file direction")
try:
    with open(direction, encoding="utf8") as fp:
        text = fp.readlines()
        if len(text) == 0:
            raise Exception("wrong .csv file.\ndirection: "+direction)
except:
    raise Exception("wrong file direction.\ndirection: "+direction)



fin = []
fin.append("[\n")
tab = 1

values = text[0].replace("\n", "").split(",")

for i in text[1:]:
    tab = 1
    fin.append((tab*"    ") + "{\n")
    count = 0
    for val in i.replace("\n", "").split(","):
        tab += 1
        if val == "":
            val = "null"

        try:
            fin.append((tab*"    ")+values[count]+": "+val+",\n")
        except:
            raise Exception("wrong attributes.\numbers when accured: "+str(count+1))

        count += 1
        tab -= 1
    fin.append((tab*"    ") + "}\n")

fin.append("]\n")

open(direction[:-4]+".json", "w", encoding="utf8").write("".join(fin))

direction = input("file direction")

import csv
import json

try:
    with open(direction, newline='', encoding="utf8") as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        text = []
        for row in file:
            text.append(','.join(row))
except:
    raise Exception("wrong file direction.\ndirection: "+direction)

fin = []    

values = text[0].split(",")

for i in text[1:]:
    count = 0
    a = {}
    for val in i.split(","):
        if val == "":
            val = "null"

        try:
            a[values[count]] = val
        except:
            raise Exception("wring attributes.\nnumber when occured: "+str(count+1))

        count += 1
    fin.append(a)

open(direction[:-4]+".json", "w", encoding="utf8").write(json.dumps(fin,indent=4))

S, [21 дек. 2022 г., 15:38:28]:
Так, а какая из них 3?