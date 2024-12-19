from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample phishing data
questions = [
    {
        "id": 1,
        "text": "An email claims to be from PayPal and asks you to 'log in to confirm your account' by clicking on a link. The email has grammatical errors. Is this phishing?",
        "options": ["Yes", "No"],
        "answer": "Yes",
    },
    {
        "id": 2,
        "text": "You receive an email from 'security@amazon-support.com' warning you about a login attempt. The sender's email domain looks slightly unusual. Is this phishing?",
        "options": ["Yes", "No"],
        "answer": "Yes",
    },
    {
        "id": 3,
        "text": "A friend sends you a message on social media with only a link and no context. What should you do?",
        "options": [
            "Click the link immediately",
            "Ask your friend if they sent it",
            "Ignore the message",
        ],
        "answer": "Ask your friend if they sent it",
    },
    {
        "id": 4,
        "text": "The URL for your bank's login page starts with 'http://' instead of 'https://'. Should you proceed?",
        "options": ["Yes", "No"],
        "answer": "No",
    },
    {
        "id": 5,
        "text": "In 2016, which phishing attack compromised over 500 million Yahoo accounts by tricking users into clicking malicious links?",
        "options": ["Operation Aurora", "The Yahoo Breach", "Cloud Hopper"],
        "answer": "The Yahoo Breach",
    },
    {
        "id": 6,
        "text": "A pop-up on a website claims your computer is infected and urges you to download antivirus software immediately. Is this likely phishing?",
        "options": ["Yes", "No"],
        "answer": "Yes",
    },
    {
        "id": 7,
        "text": "What is a common tactic used in phishing attacks to trick users into acting quickly?",
        "options": [
            "Offering a discount",
            "Creating a sense of urgency",
            "Providing free software",
        ],
        "answer": "Creating a sense of urgency",
    },
    {
        "id": 8,
        "text": "You receive an unexpected email from a popular brand offering a $100 gift card if you fill out a survey. Is this phishing?",
        "options": ["Yes", "No"],
        "answer": "Yes",
    },
    {
        "id": 9,
        "text": "Which of these is a red flag for identifying phishing links?",
        "options": [
            "Misspelled domains (e.g., 'goggle.com')",
            "Shortened URLs (e.g., bit.ly links)",
            "Both of the above",
        ],
        "answer": "Both of the above",
    },
    {
        "id": 10,
        "text": "Which real-world phishing campaign in 2020 targeted users by pretending to be emails from the World Health Organization (WHO)?",
        "options": [
            "Operation COVID Shield",
            "WHO COVID-19 Phishing Attack",
            "Pandemic Mail Breach",
        ],
        "answer": "WHO COVID-19 Phishing Attack",
    },
]

@app.route("/")
def index():
    return render_template("quiz.html", questions=questions)


@app.route("/check", methods=["POST"])
def check():
    user_answers = request.json.get("answers", {})
    results = {}
    feedback = []

    for question in questions:
        qid = str(question["id"])
        correct = question["answer"]
        user_response = user_answers.get(qid, "")
        results[qid] = (user_response == correct)
        feedback.append({
            "question": question["text"],
            "your_answer": user_response,
            "correct_answer": correct,
            "is_correct": user_response == correct,
            "explanation": "Correct!" if user_response == correct else f"The correct answer is '{correct}'."
        })
    
    return jsonify(feedback)
if __name__ == "__main__":
    app.run(debug=True)
