import os
import json
import random
from flask import Flask, jsonify, request

app = Flask(__name__)

math_directory = "MATH"

# Endpoint to get a random math problem
@app.route('/random-problem', methods=['GET'])
def return_random_problem():
    topic = request.args.get('topic')
    level = request.args.get('level')
    if topic not in ('algebra', 'counting_and_probability', 'geometry', 'intermediate_algebra', 'number_theory', 'prealgebra', 'precalculus')\
                or level not in('1', '2', '3', '4', '5'):
        return jsonify({'message': 'No math problems found for the given topic and difficulty.'}), 404
    
    folder_path = os.path.join(math_directory, topic.lower() + '\Level ' + level)

    files = [file for file in os.listdir(folder_path) if file.endswith('.json')]                    

    file_path = folder_path + '/' + random.choice(files)

    with open(file_path, 'r') as file:
        math_problem = json.load(file)
        return jsonify(math_problem)

if __name__ == '__main__':
    app.run(debug=True)
