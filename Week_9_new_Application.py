
user_ids = []

def open_text():
    with open("user.txt", "r+") as file:
        for line in file:
            record = line.split('|')
            user_ids.append(record[0])
    file.close()

def user_input():
    while True:
        flagId = False
        while not flagId:
            user_id = input("Input user id : ")
            if (user_id == "End."):
                return
            for id in user_ids:
                if(id == user_id):
                    print("User id has already registered")
                    break
                flagId = True


        password = input("Input user password : ")

        flagCode = False

        while not flagCode:
            code = input("Input authorization code : ")
            if(code == "Admin" or code == "User"):
                flagCode = True
            else:
                print("The authorization code must be 'Admin' or 'User' !")

        #append the user_ids after validation
        user_ids.append(user_id)

        with open("user.txt", "a+") as file:
            file.write(user_id)
            file.write('|')
            file.write(password)
            file.write('|')
            file.write(code)
            file.write('\n')
            file.close()

def display():
    with open("user.txt",'r+') as file:
        for line in file:
            record = line.split('|')
            print("User id : ", record[0])
            print("Password : ", record[1])
            print("Authorization code : ", record[2])
        file.close()


open_text()
user_input()
display()

