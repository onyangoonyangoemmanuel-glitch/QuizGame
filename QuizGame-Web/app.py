import os
import random
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
# Change this for production (use an env var or proper secret management)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "replace-this-with-a-secret-key")

# ---------------------------
# QUIZ DATA: question, options, correct
# ---------------------------
QUESTIONS = [
    {
        "q": "What is the capital city of Kenya?",
        "options": ["Nairobi", "Mombasa", "Kisumu", "Eldoret"],
        "answer": "Nairobi",
    },
    {
        "q": "Who is the current president of Kenya?",
        "options": ["Uhuru Kenyatta", "William Ruto", "Raila Odinga", "Musalia Mudavadi"],
        "answer": "William Ruto",
    },
    {
        "q": "How many counties does Kenya have?",
        "options": ["42", "45", "47", "50"],
        "answer": "47",
    },
    {
        "q": "In what year did Kenya gain independence?",
        "options": ["1963", "1978", "1952", "1980"],
        "answer": "1963",
    },
    {
        "q": "What is the staple food in Kenya?",
        "options": ["Rice", "Chapati", "Ugali", "Potatoes"],
        "answer": "Ugali",
    },
    {
        "q": "What draws tourists to Kenya?",
        "options": ["Mountains", "Wildlife", "Lakes", "Caves"],
        "answer": "Wildlife",
    },
    {
        "q": "Which woman won a Nobel Prize from Kenya?",
        "options": ["Grace Onyango", "Charity Ngilu", "Wangari Maathai", "Martha Karua"],
        "answer": "Wangari Maathai",
    },
    {
        "q": "Which rebels from Central Kenya fought for independence?",
        "options": ["Kikuyu Council", "Mau Mau", "Freedom Front", "Kamba Warriors"],
        "answer": "Mau Mau",
    },
    {
        "q": "Which Olympic activity does Kenya dominate in?",
        "options": ["Swimming", "Athletics", "Boxing", "Cycling"],
        "answer": "Athletics",
    },
    {
        "q": "Who are the top Kenyan street hip-hop artistes?",
        "options": ["Khaligraph Jones", "Wakadinali", "Octopizzo", "Nyashinski"],
        "answer": "Wakadinali",
    },
]

# ---------------------------
# Helpers
# ---------------------------
def init_quiz():
    """Initialize session state for a new quiz."""
    chosen = random.sample(QUESTIONS, len(QUESTIONS))  # shuffle and copy
    # Ensure options are shuffled per question
    for q in chosen:
        random.shuffle(q["options"])
    session["questions"] = chosen
    session["q_index"] = 0
    session["score"] = 0
    session["wrong"] = []  # list of dicts: {q, chosen, correct}

# ---------------------------
# Routes
# ---------------------------
@app.route("/")
def index():
    return render_template("index.html", total=len(QUESTIONS))


@app.route("/start", methods=["POST"])
def start():
    init_quiz()
    return redirect(url_for("question"))


@app.route("/question", methods=["GET"])
def question():
    if "questions" not in session:
        return redirect(url_for("index"))

    q_index = session.get("q_index", 0)
    questions = session["questions"]

    if q_index >= len(questions):
        return redirect(url_for("result"))

    current = questions[q_index]
    total = len(questions)
    return render_template(
        "question.html",
        q_index=q_index,
        total=total,
        question=current["q"],
        options=current["options"],
    )


@app.route("/answer", methods=["POST"])
def answer():
    if "questions" not in session:
        return redirect(url_for("index"))

    chosen = request.form.get("option")
    if chosen is None:
        flash("Please select an option before submitting.", "warning")
        return redirect(url_for("question"))

    q_index = session.get("q_index", 0)
    questions = session["questions"]

    if q_index >= len(questions):
        return redirect(url_for("result"))

    current = questions[q_index]
    correct = current["answer"]

    if chosen == correct:
        session["score"] = session.get("score", 0) + 1
    else:
        wrong = session.get("wrong", [])
        wrong.append({"q": current["q"], "chosen": chosen, "correct": correct})
        session["wrong"] = wrong

    # next question
    session["q_index"] = q_index + 1

    if session["q_index"] >= len(questions):
        return redirect(url_for("result"))
    else:
        return redirect(url_for("question"))


@app.route("/result")
def result():
    if "questions" not in session:
        return redirect(url_for("index"))

    total = len(session["questions"])
    score = session.get("score", 0)
    wrong = session.get("wrong", [])
    percentage = round((score / total) * 100, 2) if total else 0
    return render_template(
        "result.html", score=score, total=total, percentage=percentage, wrong=wrong
    )


@app.route("/restart", methods=["POST"])
def restart():
    init_quiz()
    return redirect(url_for("question"))


if __name__ == "__main__":
    # Use debug=True only in development
    app.run(host="0.0.0.0", port=5000, debug=True)
