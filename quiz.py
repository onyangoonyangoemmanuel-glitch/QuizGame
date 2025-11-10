
answer = input("Do you wanna play a Kenyan Quiz Game ? ").lower()

if answer == "yes" :
    print("Welcome Player! ")
else:
    close()

score = 0
answer = input("What is the capital city of Kenya ? ").lower()
if answer == "nairobi":
    print(True)
    score += 1
else:
    print(False)

answer = input("Who is the current president of Kenya ? ").lower()
if answer == "zakayo" :
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

answer = input("How many counties does Kenya have ? ").lower()
if answer == "47" :
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

answer = input("In what year did Kenya gain independence ? ").lower()
if answer == "1963" :
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

answer = input("What is the staple food in Kenya ? ").lower()
if answer == "sembe" :
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

answer = input("What draws tourists to Kenya ? ").lower()
if answer == "wild animals" :
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

answer = input("Which woman won a nobel prize from Kenya ? ").lower()
if answer == "wangari maathaai" :
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

answer = input("Which Rebels from Central Kenya fought for Kenyan independence ? ").lower()
if answer == "mau mau" :
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

answer = input("Which Olympic activity does Kenya dominate in ? ").lower()
if answer == "Athletics" :
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

answer = input("Who are the top kenyan street hiphop artistes ? ").lower()
if answer == "wakadinali" :
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

    print("You have scored a total of : " + str(score) + " Correct answers.")
    print("You got " + str((score/8 * 100 )) + "%")