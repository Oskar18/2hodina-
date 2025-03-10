import os #as something

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

#task1("data.txt")
"""
with open("data.txt", "r") as f:
    for row in f:
        print(row.strip())


with open("data.txt", "r") as f:
    rows = f.readlines()
    print(rows)"""
"""
with open("data/data.txt", "rb") as f:
    rows = f.read()
    print(rows)

if os.path.exists("data/filtered-data.txt"):
    os.remove("data/filtered-data.txt")
else:
    print("Súbor neexistuje")"""



def task2(file_name):
    with (open(f"data/{file_name}", "r") as f_old,
          open(f"data/copy-{file_name}", "w") as f_new):
        data = f_old.read()
        f_new.write(data)

#task2("data.txt")

def task3(file_name):
    f = open(f"data/{file_name}", "r", encoding="utf-8")
    data = f.readlines()
    f.close()

    print(data)
    data.reverse()
    print(data)
    new_data = [f"{line.strip()}\n" for line in data]

    f = open(f"reverse-{file_name}", "w")
    f.writelines(new_data)
    f.close()


task3("data.txt")