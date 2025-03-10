import os

def task1(file_name, threshold=6):
    f = open(f"data/{file_name}", "r", encoding="utf-8")
    data = f.read()
    f.close()

    lines = data.split("\n")
    new_data = []

    for line in lines:
        words = line.split()
        for word in words:
            if len(word) > threshold:
                #new_data.append(word)
                new_data.append(f"{word}\n")

    f = open(f"filtered-{file_name}", "w")
    #f.write(", ".join(new_data))
    f.writelines(new_data)
    f.close()

"""task1("data.txt")
"""
with open("data.txt", "r") as f:
    for row in f:
        print(row.strip())


with open("data.txt", "r") as f:
    rows = f.readlines()
    print(rows)"""

with open("data/data.txt", "rb") as f:
    rows = f.read()
    print(rows)

if os.path.exists("data/filtered-data.txt"):
    os.remove("data/filtered-data.txt")
else:
    print("Súbor neexistuje")"""

    def task2