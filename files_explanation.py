def read_data(path):
    f = open(path, "r")
    data = f.read()
    f.close()
    return data


def write_data(path, data):
    f = open(path, "a")
    f.write(data)
    f.close()

FILE_PATH = "test1.turtle"

#data = read_data(FILE_PATH)
#print(data)
user_data = input("zadaj data: ")
write_data(FILE_PATH, user_data)
data = read_data(FILE_PATH)
print(data)