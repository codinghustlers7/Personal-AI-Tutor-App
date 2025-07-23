from flask import Flask, render_template, request, session, jsonify
import traceback

# real app
app = Flask(__name__)
app.secret_key = "your_secret_key_here"

from controllers.tutor_controller import TutorController
tutor_controller = TutorController()
@app.route("/", methods=["GET"])
def index():
    tutor_controller.ensure_user_session(session)
    return render_template("tutor.html")

@app.route("/api/create_session", methods=["POST"])
def create_session():
    return tutor_controller.create_session(session)

@app.route("/api/send_question", methods=["POST"])
def send_question():
    data = request.get_json(force=True)
    app.logger.debug(f"🔍 payload: {data!r}")
    try:
        return tutor_controller.send_query(session, data)
    except Exception as e:
        traceback.print_exc()
        app.logger.exception("🔥 error in send_query")
        return jsonify({"error": str(e)}), 500

# … your other routes …

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)


# Initialize Flask app
