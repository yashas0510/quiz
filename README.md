# Phishing Awareness Quiz
The Phishing Awareness Quiz is an interactive web application designed to educate users about phishing attempts and improve their ability to recognize malicious emails, messages, and links. The application provides a dynamic set of questions based on real-world phishing scenarios, historical attacks, and general cybersecurity knowledge.


## Overview
The **Phishing Awareness Quiz** is an interactive web application designed to educate users about phishing attempts and improve their ability to recognize malicious emails, messages, and links. The application provides a dynamic set of questions based on real-world phishing scenarios, historical attacks, and general cybersecurity knowledge. Users receive detailed feedback on their answers to enhance their learning experience.

---

## Features
- A versatile question bank with scenarios based on:
  - Real phishing attacks (e.g., Yahoo breach, WHO COVID-19 attack).
  - General cybersecurity principles (e.g., HTTPS vs HTTP, urgency tactics).
- Interactive feedback for each question, showing correct answers and explanations.
- Dynamically rendered quiz interface.
- Simple, user-friendly UI for accessibility.
- Backend powered by Flask for easy deployment and extensibility.

---

## Technologies Used
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Custom CSS
- **Data Handling**: JSON-based communication between frontend and backend

---

## Project Structure
```
phishing-quiz/
├── app.py           # Main Flask application
├── templates/       # HTML templates for the frontend
│   └── quiz.html    # Main quiz interface
├── static/          # Static files for styling and interactivity
│   ├── style.css    # CSS styles
│   └── script.js    # JavaScript for quiz submission and feedback
```

---

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/phishing-awareness-quiz.git
   cd phishing-awareness-quiz
   ```

2. **Set Up Python Environment**:
   - Ensure Python is installed (`python --version` to check).
   - Install pip (`pip install --upgrade pip`).

3. **Install Dependencies**:
   ```bash
   pip install flask
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Quiz**:
   Open your browser and go to `http://127.0.0.1:5000`.

---

## How It Works
1. Users are presented with multiple-choice questions based on phishing scenarios.
2. Upon submission, the backend processes their answers and returns:
   - Whether each answer was correct.
   - Detailed explanations for incorrect answers.
3. The frontend dynamically displays feedback for each question.

---

## Sample Questions
1. **Scenario**: "An email claims to be from PayPal and asks you to log in using a link. The email contains grammatical errors."
   - **Options**: Yes, No
   - **Correct Answer**: Yes

2. **Scenario**: "The URL for your bank's login page starts with `http://` instead of `https://`. Should you proceed?"
   - **Options**: Yes, No
   - **Correct Answer**: No

3. **Historical Attack**: "Which phishing campaign in 2020 targeted users pretending to be emails from the World Health Organization (WHO)?"
   - **Options**: Operation COVID Shield, WHO COVID-19 Phishing Attack, Pandemic Mail Breach
   - **Correct Answer**: WHO COVID-19 Phishing Attack

---

## Customization
- Add more questions by editing the `questions` array in `app.py`.
- Update the styling by modifying `static/style.css`.
- Enhance interactivity in `static/script.js`.

---

## Deployment
1. **Deploy Locally**: Follow the steps in the installation section.
2. **Deploy Online**:
   - Use platforms like **Heroku**, **Render**, or **PythonAnywhere**.
   - Example Heroku Deployment:
     ```bash
     heroku create phishing-awareness-quiz
     git push heroku main
     ```

---

## Future Enhancements
- Add images of phishing emails for better visual understanding.
- Include real-time scoring and leaderboards.
- Localize the quiz for multiple languages.
- Integrate additional cybersecurity scenarios (e.g., smishing, vishing).

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Contribution
Feel free to contribute by:
- Adding new phishing scenarios.
- Enhancing the UI/UX.
- Reporting bugs or suggesting improvements via [GitHub Issues](https://github.com/yourusername/phishing-awareness-quiz/issues).

---

## Acknowledgements
- Inspired by real-world phishing awareness initiatives.
- Special thanks to the cybersecurity community for sharing knowledge and resources.

