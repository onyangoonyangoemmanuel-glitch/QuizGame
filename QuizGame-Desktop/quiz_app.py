import tkinter as tk
from tkinter import messagebox

# -------------------------------
# QUIZ DATA
# -------------------------------
questions = [
    ("What is the capital city of Kenya?", ["Nairobi"]),
    ("Who is the current president of Kenya?", ["William Ruto", "Ruto", "Dr. William Ruto"]),
    ("How many counties does Kenya have?", ["47"]),
    ("In what year did Kenya gain independence?", ["1963"]),
    ("What is the staple food in Kenya?", ["Ugali", "Sembe", "Maize meal"]),
    ("What draws tourists to Kenya?", ["Wildlife", "Wild animals", "Safari"]),
    ("Which woman won a Nobel Prize from Kenya?", ["Wangari Maathai", "Prof. Wangari Maathai"]),
    ("Which rebels from Central Kenya fought for independence?", ["Mau Mau"]),
    ("Which Olympic activity does Kenya dominate in?", ["Athletics", "Running", "Marathon"]),
    ("Who are the top Kenyan street hip-hop artistes?", ["Wakadinali"]),
]

# -------------------------------
# QUIZ LOGIC
# -------------------------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🇰🇪 Kenyan Quiz Game")
        self.root.geometry("600x400")
        self.root.config(bg="#f2f2f2")

        self.score = 0
        self.q_index = 0

        self.title_label = tk.Label(
            root, text="Kenyan Quiz Game 🇰🇪", font=("Helvetica", 18, "bold"), bg="#f2f2f2"
        )
        self.title_label.pack(pady=20)

        self.question_label = tk.Label(
            root, text="", font=("Helvetica", 14), wraplength=500, justify="center", bg="#f2f2f2"
        )
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
        self.answer_entry.pack(pady=10)

        self.submit_btn = tk.Button(
            root, text="Submit", command=self.check_answer, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white"
        )
        self.submit_btn.pack(pady=10)

        self.status_label = tk.Label(
            root, text="", font=("Helvetica", 12), bg="#f2f2f2"
        )
        self.status_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.q_index < len(questions):
            q_text = questions[self.q_index][0]
            self.question_label.config(text=q_text)
            self.answer_entry.delete(0, tk.END)
            self.status_label.config(text=f"Question {self.q_index + 1} of {len(questions)}")
        else:
            self.end_game()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answers = [a.lower() for a in questions[self.q_index][1]]

        if user_answer in correct_answers:
            self.score += 1
            messagebox.showinfo("Correct!", "✅ Correct answer!")
        else:
            messagebox.showerror("Wrong!", f"❌ Wrong! Correct answer: {questions[self.q_index][1][0]}")

        self.q_index += 1
        self.load_question()

    def end_game(self):
        percentage = round((self.score / len(questions)) * 100, 2)
        messagebox.showinfo(
            "Quiz Complete",
            f"You scored {self.score}/{len(questions)} ({percentage}%)"
        )
        self.root.destroy()

# -------------------------------
# RUN THE APP
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
