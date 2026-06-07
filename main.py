from auth import register_user, login_user

while True:

    print("\n===== DEAD MAN SWITCH =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Name: ")
        email = input("Email: ")
        password = input("Password: ")

        register_user(
            name,
            email,
            password
        )

    elif choice == "2":

        email = input("Email: ")
        password = input("Password: ")

        user = login_user(
            email,
            password
        )

        if user:
            print(f"Welcome {user[1]}")

    elif choice == "3":
        break