mydict = {}
while True:
    try:
        item = input().lower()
        if item in mydict:
            mydict[item] += 1
        else:
            mydict[item] = 1
    except EOFError:
        for key in sorted(mydict.keys()):
            print(mydict[key], key.upper())
        break

