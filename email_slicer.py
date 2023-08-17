#collect email from user
#split the email using the @, the first part as th user name, the second part is gonna be saves as domain
#split domain using the .,

def main():
    print("Welcome to the email slicer ")
    print("")

    email_input = input("Input your email address:")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print ("Username : ", username)
    print("Domain : _", domain)
    print ("Extension:", extension)


while True
    main()