def check_username(username, valid_domains): # This function checks if username is valid or not
    is_valid = False
    if username.count("@") == 1:
        record = username.split("@")
        domain = record[1]
        if domain in valid_domains:
            is_valid = True
            print("Username is valid.")
    if not is_valid:
        print("Username is invalid!")



def main():
    username = input("Enter username: ")
    valid_domains = ("gmail.com", "ualberta.ca")
    check_username(username, valid_domains)


main()


