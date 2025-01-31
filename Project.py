import time
print("Please fill out this form. \n")
time.sleep(1)
print("Hit RETURN to continue or CTRL-C (^C) to abort")
input('')
time.sleep(1)

print("NOTICE: ALL ENTRIES ARE CASE SENSITIVE!")
time.sleep(2)

name = input("\nWhat is your name? \n>> ")  
while name == "":
    time.sleep(1)
    name = input("\nPlease enter your name. \n>> ")
time.sleep(1)


gender = input("\nPlease enter your Gender. (Male/Female) \n>> ")
while gender == "":
    time.sleep(1)
    gender = input("\nPlease enter your Gender. (Male/Female) \n>> ")
time.sleep(1)

status = input("\nWhat is your Marital Status? (Single/Married/Divorced)\n>> ")
while status == "":
    time.sleep(1)
    status = input("\nPlease state your Marital Status? (Single/Married/Divorced)\n>> ")

if gender == ('Male'):
    time.sleep(1)
    print(f"Hello Mr {name}. \n")
elif gender == ('Female') and status == ('Married'):
    time.sleep(1)
    print(f"Hello Mrs {name}. \n")
elif gender == ('Female'):
    time.sleep(1)
    print(f"Hello Ms {name}. \n")
time.sleep(2)



while True:
    age_input = input("How old are you? \n>> ").strip()

    if age_input.isdigit():
        age = int(age_input)
        break

    else:
        print("Plese enter your age \n")
time.sleep(1)
    


if age in range (13, 20):
    print("Still a teenager, cool. \n")
elif age < 13:
    print("You're quite young")
elif age in range (20, 49):
    print("Thats amazing")
elif age >= 70:
    print(f"You are {age} years old, wow!!")
time.sleep(2)

home = input("\nWhat country do you live in? \n>> ")
while home == "":
    home = input("\nWhat country do you live in? \n>> ")
if home == ('Uganda'):
    time.sleep(2)
    print(f"{home}, the pearl of Africa")
else:
    time.sleep(2)
    print(f"{home} is a lovely Country")
time.sleep(2)

email = input("\nPlease Enter you Email: \n>> ")
while email == "":
    email = input("\nPlease Enter you Email: \n>> ")
time.sleep(2)

phone = int(input("\nPlease Enter your phone number: \n>> "))
time.sleep(2)

school = input("\nAre you in a Learning Institute? (Yes/No)\n>> ")
while school == "":
    school = input("\nAre you in a Learning Institute? (Yes/No)\n>> ")
time.sleep(1)

if school == ('Yes'):
    school_name = input("\nWhat is it called? \n>> ")
    while school_name == "":
        school_name = input("\nWhat is it called? \n>> ")
    time.sleep(2)
    print(f"{school_name}, Nice name")
    time.sleep(1)
    location = input("\nWhere is it Located? \n>> ")
    while location == "":
        location = input("\nWhere is it Located? \n>> ")
    time.sleep(2)
    print("\nThats a nice place")
    time.sleep(1)
    studies = input("\nWhat are you learning? \n>> ")
    while studies == "":
        studies = input("\nWhat are you learning? \n>> ")
    time.sleep(2)
    print("Sound's Interesting")
    time.sleep(2)

if school == ('No'):
    employed = input("\nAre you employed? (Yes/No)\n>> ")
    while employed == "":
        employed = input("\nAre you employed? (Yes/No)\n>> ")
    time.sleep(1)
    if employed == ('Yes'):
        where = input("\nWhere are you employed? \n>> ")
        while where == "":
            where = input("\nWhere are you employed? \n>> ")
        time.sleep(2)
        print("Wonderful")
    if employed == ('No'):
        print("No worries")

time.sleep(2)
if gender == ('Male'):
    print(f"\nThank you for your time Mr {name}.")
elif gender == ('Female') and status == ('Married'):
    print(f"\nThank you for time Mrs {name}.")
elif gender == ('Female'):
    print(f"\nThank you for your time Ms {name}.")
time.sleep(2)
print("\nHave a lovely day")