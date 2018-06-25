import os

def main():
    f_pw = open("passwordlist", "r")
    f_user = open("userlist", "r")

    passwords = f_pw.read().splitlines()
    users = f_user.read().splitlines()

    f_pw.close()
    f_user.close()

    try:
        os.remove("userdb.txt")
    except OSError:
        pass

    with open("userdb.txt", "w") as f_userdb:
        for user in users:
            for password in passwords:
                f_userdb.write(user + ":x:" + password + "\n")

if __name__ == "__main__":
    main()