import time


def arr_to_str(input_arrs):
    output_str = ""
    for arr in input_arrs:
        output_str += "^".join(arr) + "\n"
    return output_str


movie_options_tests = [
    [
        ["action", "disaster", "violence"],
        ["Clint Eastwood", "Judy Dench", "Cher"],
        ["great", "good", "ok"]
    ],
    [
        ["passion", "heart break", "romance", "love"]
    ],
    [
        ["one genre"],
        ["One Actor"],
        ["the BEST"],
        ["something else"]
    ],
]

for i, movie_options in enumerate(movie_options_tests):
    print(f"\nRunning Test Number {i+1}")
    print(f"movie options: {movie_options}")

    with open("random_attributes.txt", "w") as file:
        file.write(f"run\n{arr_to_str(movie_options)}")

    time.sleep(2)

    with open("random_attributes.txt", "r") as file:
        line = file.readline()[:-1]
        random_selections = []
        while line:
            random_selections.append(line)
            line = file.readline()[:-1]

    print(f"choices: {random_selections}")

    time.sleep(5)

