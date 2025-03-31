from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load JSON data from a file
with open("list.json", "r") as file:
    students = json.load(file)

def get_student_by_id(student_id):
    return next((student for student in students if student.get("id") == student_id), None)

@app.route('/student', methods=['GET'])
def get_student():
    student_id = request.args.get('id', type=int)
    student = get_student_by_id(student_id)
    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
