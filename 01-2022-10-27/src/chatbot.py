import time

print("Hi, my name is Vincent.")
time.sleep(1)
print("What is your name?")
user = input()
if user.lower() == "joachim":
    print("Good afternoon my creator!")
    print("")
elif user.lower() in ["alex", "leo", "martha"]:
    print("Oh, what a pleasure! It feels great to have you in the house.")
    time.sleep(1)
    print("Is Joachim somewhere around too?")
    answer = input()
    if answer.lower() == "yes":
        print("Great, a strong team!")
    elif answer.lower() == "no":
        print("OK, if you see him make sure he knows that we miss him.")
    else:
        print("Well, did not get that, but thats's fine. See you buddy!")
    print("")
else:
    print(f"Nice to meet you {user}.")
    print("")
time.sleep(1)
