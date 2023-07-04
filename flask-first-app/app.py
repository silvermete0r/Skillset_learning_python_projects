from flask import Flask, jsonify, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    gpa = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return self.id

# students = { # 1, 2, 3 max()
#     '1': {
#         'name': 'Gregor',
#         'group': 17,
#         'gpa': 3.4
#     },
#     '2': {
#         'name': 'John',
#         'group': 15,
#         'gpa': 3.2
#     },
#     '3': {
#         'name': 'George',
#         'group': 16,
#         'gpa': 3.5
#     }
# }

# Home route
@app.route('/')
def home_page():
    students = Students.query.all()
    return render_template('index.html', data = students)

# get all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Students.query.all()
    output = {}
    for student in students:
        output[student.id] = {
            'name': student.name,
            'group': student.group,
            'gpa': student.gpa
        }
    return jsonify(output)

# get student by id
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    try:
        data = Students.query.get(id) # Object Class -> data
        ans = {
            "name": data.name,
            "group": data.group,
            "gpa": data.gpa
        }
        if ans:
            return jsonify(ans)
        else:
            return jsonify({'message': 'Student not found'})
    except Exception as e:
        return jsonify({'error': str(e)})
        

# add new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    add_data = Students(
        name=data['name'],
        group=data['group'],
        gpa=data['gpa']
    )
    db.session.add(add_data)
    db.session.commit()
    return 'New student added successfully!'

# delete student from database
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    try:
        Students.query.filter_by(id=id).delete()
        return f'Student with id: {id} deleted successfully!'
    except Exception as e:
        return f'Error: {e}'
    
# update student data
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    try:
        data = request.get_json()
        student = Students.query.get(id)
        student.name = data['name']
        student.group = data['group']
        student.gpa = data['gpa']
        db.session.commit()
        return 'Successfully Updated!'
    except Exception as e:
        return f'Error: {e}'

# add new student via Web Form
@app.route('/students_add', methods=['POST'])
def add_student_form():
    add_data = Students(
        name=request.form.get('name'),
        group=int(request.form.get('group')),
        gpa=float(request.form.get('gpa'))
    )
    db.session.add(add_data)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
