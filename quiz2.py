# Kenyan Quiz Game

print("Welcome to the Kenyan Quiz Game!")

answer = input("Do you wanna play? (yes/no): ").lower()
if answer != "yes":
    print("Okay, maybe next time!")
    quit()

print("Welcome, Player! Let's begin 🎯")

score = 0

questions = [
    ("What is the capital city of Kenya?", "nairobi"),
    ("Who is the current president of Kenya?", "zakayo"),
    ("How many counties does Kenya have?", "47"),
    ("In what year did Kenya gain independence?", "1963"),
    ("What is the staple food in Kenya?", "sembe"),
    ("What draws tourists to Kenya?", "wild animals"),
    ("Which woman won a Nobel Prize from Kenya?", "wangari maathai"),
    ("Which rebels from Central Kenya fought for independence?", "mau mau"),
    ("Which Olympic activity does Kenya dominate in?", "athletics"),
    ("Who are the top Kenyan street hip-hop artistes?", "wakadinali"),
]

for q, correct in questions:
    answer = input(q + " ").lower()
    if answer == correct:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect!")

print("\n🎯 You scored " + str(score) + " out of " + str(len(questions)))
print("Your percentage: " + str(round((score / len(questions)) * 100, 2)) + "%")
