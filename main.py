def print_data(data):
    for student in data:
        print(f"Name: {student[0]} - Height: {student[1]}cm")
    print()


def add_student(data):
    name = input("Zadaj meno studenta: ")
    height = int(input("zadaj vyšku v cm: "))
    data.append((name, height))


def print_menu():
    print("""
    ------MAIN MENU-----
    [1] - vypis data
    [2] - pridat data
    [0] - exit
    """)

def run():
    data = [("Adam", 134), ("Eva", 130), ("Karol", 145)]

    while True:
        print_menu()
        user_choice = input("zadaj volbu: ")

        if user_choice == "1":
            print_data(data)

        elif user_choice == "2":
            add_student(data)

        elif user_choice == "0":
            break

        else:
            print("zadal si zlu volbu")



run()