function submitQuiz() {
    const formData = new FormData(document.getElementById("quiz-form"));
    const answers = {};
    formData.forEach((value, key) => {
        answers[key.replace("q", "")] = value;
    });

    fetch("/check", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ answers }),
    })
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById("results");
            resultsDiv.innerHTML = "<h2>Results:</h2>";

            data.forEach(item => {
                const result = document.createElement("div");
                result.classList.add("result-item");

                result.innerHTML = `
                    <p><strong>Question:</strong> ${item.question}</p>
                    <p><strong>Your Answer:</strong> ${item.your_answer}</p>
                    <p><strong>Correct Answer:</strong> ${item.correct_answer}</p>
                    <p><strong>Feedback:</strong> ${item.explanation}</p>
                    <hr>
                `;
                resultsDiv.appendChild(result);
            });
        })
        .catch(error => console.error("Error:", error));
}
