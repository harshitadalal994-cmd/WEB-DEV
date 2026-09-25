from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/analytics/<int:student_id>")
def analytics(student_id):

    # Example analytics
    attendance = 72

    if attendance < 75:
        status = "Attendance Warning"
    else:
        status = "Attendance Normal"

    return jsonify({
        "student_id": student_id,
        "attendance": attendance,
        "status": status
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
