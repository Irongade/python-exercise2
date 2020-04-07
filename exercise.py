import random
import string

# creating empty container
container = {}

runProgram = True
i = 0

while (runProgram == True):  # a while statement is used to ensure comtinuity of the program
    fName = input("insert your First name:")
    lName = input("insert your Last name:")
    email = input("insert your email:")

    # this function generates a password of both string and digit type and returns the randomly generated passoword
    def generatePassword(stringLength=5):
        randomPassword = string.ascii_letters + string.digits
        return "".join(random.choice(randomPassword) for i in range(stringLength))

    # the randomly generated password is returned here
    generatedPassword = generatePassword()

    # this combines first two letters of the first name and last two letters of last name and then combines everythng with the password
    createdPassword = fName[0:2] + lName[-1:-3:-1] + generatedPassword

    # this gets user preferred password and checks to see if the length of the password is longer than 7 and if it is, returns the password
    def checkPasswordLength():
        createPersonalPassword = input(
            "kindly input your desired password:")
        # while the length is longer than 7 keep asking for correct password
        while (len(createPersonalPassword) <= 7):
            createPersonalPassword = input(
                "your desired password should be longer than 7 characters:")

        userPassword = createPersonalPassword
        print(
            f"First Name: {fName} \n Last Name: {lName} \n Email: {email} \n Password: {userPassword}")
        return userPassword

    # this asks if user is fine the generated password and if yes displays the user details and if not asks for desired password from user
    def displayPassword():
        print(
            f" This is the password created specifically for you: {createdPassword} ")
        answer = input("Are you satisfied with this Password, Yes/No:")

        if (answer.lower() == "yes"):
            userPassword = createdPassword
            print(
                f"First Name: {fName} \n Last Name: {lName} \n Email: {email} \n Password: {userPassword}")
        elif (answer.lower() == "no"):
            userPassword = checkPasswordLength()
        return userPassword

# storing the returned userpassword so it can be passed to storedetails function
    userPassword = displayPassword()

    # this stores the user info and returns a dictionary that can be passed into the container dictionary
    def storeDetails(fName, lName, email, userPassword):
        userDetails = {
            "Name": fName + " " + lName,
            "Email": email,
            "Password": userPassword
        }
        return userDetails

    userDetails = storeDetails(fName, lName, email, userPassword)

# this updates the container such that it keeps adding user details as long as program doesnt end
    container[i] = userDetails

# this function keeps track of users and increments when there is a new user and increments i so a new entry to the container can be created
    def increment(i):
        i += 1
        return i

    def restartProgram():  # this checks to see if the user would like to run the program again
        answer = input("would you like to restart the program? Yes/No:")
        if (answer.lower() == "yes"):
            return runProgram == True
        elif (answer.lower() == "no"):
            return runProgram == False

    # prints current container dictionary before restarting program
    print(container)

    i = increment(i)  # storing new value of function increment in i

    # this stores the value from the restart program function and stops the program if false
    runProgram = restartProgram()
