from flask import Flask, render_template, request

app = Flask(__name__)

feedbacks = []


@app.route("/", methods=["GET", "POST"])
def home():

    message = None
    error = None

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        erp = request.form.get("erp", "").strip()
        course = request.form.get("course", "").strip()
        feedback = request.form.get("feedback", "").strip()

        # Basic validation
        if not name or not email or not erp or not course or not feedback:
            error = "All fields are required."

        # Email validation
        elif not email.endswith("@niet.co.in"):
            error = "Please use your NIET email ID ending with @niet.co.in."

        else:
            feedbacks.append({
                "name": name,
                "email": email,
                "erp": erp,
                "course": course,
                "feedback": feedback
            })

            message = "Feedback submitted successfully!"

    return render_template(
        "index.html",
        feedbacks=feedbacks,
        message=message,
        error=error
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
