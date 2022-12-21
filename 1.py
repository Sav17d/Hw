direction = input("file direction")[:-3]

try:
    with open(direction+".py", encoding="utf8") as fp:
        text = fp.readlines()
except:
    raise Exception("wrong file direction.\ndirection: "+direction+".py")

ttl = []

try:
    with open(direction+".md", encoding="utf8") as fp:
        l1 = []

        for i in fp.readlines():
            if i[:3] == "+ [":
                ttl.append(i)
            else:
                l1.append(i)
        if not (l1[-1][-1] == "\n"):
            l1.append("\n")
except:
    mdpresent = False
    l1 = []
    
l2 = []
mdcheck = True

for i in text:
    if mdcheck:
        if i[:7] == "# ttl":
            ttl.append("+ ["+i[8:-1]+"](#"+i[8:-1].lower().replace(" ", "-")+")\n")
            l2.append("## "+i[8:-1]+"\n")
            l2.append("\n")
        elif i[:13] == "# description":
            l2.append(i[14:])
            l2.append("\n")
        elif i == "# ---end----\n":
            l2.append("```python\n")
            mdcheck = False
    else:
        l2.append(i)
if not (l2[-1][-1] == "\n"):
    l2.append("\n")
l2.append("```\n")

out = ttl + l1 + l2


open(direction+".md", "w", encoding="utf8").write("".join(out))