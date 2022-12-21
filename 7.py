direction = input("file direction")

try:
    with open(direction, encoding="utf8") as fp:
        text = fp.readlines()
        if len(text) == 0:
            raise Exception("The .txt file is empty.\ndirection: "+direction)
except:
    raise Exception("wrong file direction.\ndirection: "+direction)

    
fin = []

def new():
    D = {}
    D["BANK"] = ""
    D["START_PRICE"] = ""
    D["STOP_PRICE"] = ""
    D["PAIR"] = ""
    D["TARGETS"] = []

    return D

def target(id, t, og, b, n):
    p = "%.3f" % ((float(og)-float(t))/float(og)*-100)
    return [str(id)+" target: "+str(t)+" FTT", "Percent: "+str(p)+"%", "Bank: "+str("%.2f" % (float(b)*(float(p)/100)+float(b)))+" FTT", "Target size: "+str("%.2f" % (float(b)/float(og)/float(n)))+" * "+str(t)+" = "+str("%.3f" % (float(b)/float(og)/float(n)*float(t)))+" FTT"]
    
target_counter = 1

c = new()
for i in text:
    if not (i == "\n"):
        if i[0] == "-":
            fin.append("BANK: "+c["BANK"]+"\n")
            fin.append("PAIR: "+c["PAIR"]+"\n")
            fin.append("START_PRICE: "+c["START_PRICE"]+"\n")
            fin.append("STOP_PRICE: "+c["STOP_PRICE"]+"\n")
            fin.append("\n")
            for a in c["TARGETS"]:
                fin.append("\n".join(a))
                fin.append("\n")
                fin.append("\n")
            fin.append("\n")
            fin.append("Strategy income: sum() - 1000 = ???; percent: ???")
            fin.append("\n")
            fin.append("\n")
            fin.append("----------------------------------------------\n\n")
            c = new()


        elif i[:5] == "BANK:":
            c["BANK"] = i[6:].replace("\n", "")
        elif i[3] == "-":
            c["PAIR"] = i.replace("\n", "")
        elif i[:5] == "Вход:":
            c["START_PRICE"] = i[6:].replace("\n", "")
        elif i[:6] == "Выход:":
            c["STOP_PRICE"] = i[7:].replace("\n", "")

        elif i[:7] == "Таргет:":
            targets = i[8:].split(";")
            counter = 1
            for a in targets:
                c["TARGETS"].append(target(counter, a.replace("\n", ""), c["START_PRICE"], c["BANK"], len(targets)))
                counter += 1

open(direction[:-9]+"output.txt", "w", encoding="utf8").write("".join(fin[:-1]))
fin