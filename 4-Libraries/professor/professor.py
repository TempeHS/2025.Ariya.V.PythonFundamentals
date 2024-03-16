import random


def main():
    get_level()
    generate_integer()


def get_level():
    while True:
        level = input("Level: ")
        if level not in ["1", "2", "3"]:
            continue
        else:
            return


def generate_integer():
    score = 0
    for i in range(10):
        trials = 1
        x = random.randint(1, 9)
        y = random.randint(1, 9)

        while True:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                score += 1
                break
            elif answer != x + y and trials < 3:
                trials += 1
                print("EEE")
                continue
            else:
                print("x + y = ", (x + y))
                break
    print("Score: ", score)


if __name__ == "__main__":
    main()
