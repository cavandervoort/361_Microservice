import time
import random


while True:
    time.sleep(1)

    with open("random_attributes.txt", "r") as file:
        line = file.readline()[:-1]
        if line != "run":
            continue
        line = file.readline()[:-1]
        random_selections = []
        while line:
            options_arr = line.split("^")
            choice = options_arr[random.randrange(len(options_arr))]
            random_selections.append(choice)
            line = file.readline()[:-1]

    print(f"choices: {random_selections}")

    with open("random_attributes.txt", "w") as file:
        output_str = "\n".join(random_selections) + "\n"
        file.write(output_str)
