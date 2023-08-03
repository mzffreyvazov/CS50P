import random


def main():
    level = get_level()
    score = rounds(level)
    print("Score: ", score)

def get_level():
    global n
    while True:
        try:
            n = int(input("Level: "))
            if n not in range(1, 4):
                continue
            else:
                return n
        except ValueError:
            continue

def generate_integer(level):
    global x, y
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    else:
        x = random.randint(10**(level-1), (10**level - 1))
        y = random.randint(10**(level-1), (10**level - 1))

    return x, y

def check_point(x, y):
    j = 1
    while j<4:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                j += 1
                print("EEE")
        except:
            j += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False



def rounds(level):
    b = 1
    score = 0
    while b < 11:
        x, y = generate_integer(level)
        response = check_point(x, y)
        if response == True:
            score += 1
        b += 1
    return score




if __name__ == "__main__":
    main()
