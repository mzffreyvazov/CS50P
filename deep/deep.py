answer = input("What's the answer to the Great Question of Life, the Universe and Everything? ")
answer = answer.strip(" .,-_").lower().replace("-", "").replace("_", "").replace(" ", "")
if answer == "42" or answer == "fortytwo":
    print("YES")
else:
    print("NO")