from flask import Flask, render_template, request, jsonify
import json

import inputs

app = Flask(__name__)

# List of Common Standards (you can expand this)
STANDARDS = ['CCSS.ELA-LITERACY.W.4.9']

# Function to read prompt txt file
def read_txt(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    return content

# Mock function to call Gen Ai
def call_gen_ai(filepath):
    print(inputs.OPEN_AI_API_KEY)
    with open(filepath, 'r') as file:
        content = file.read()
    return content

@app.route('/')
def index():
    return render_template('index.html', standards=STANDARDS)

@app.route('/get_question', methods=['POST'])
def get_question():
    topic = request.form.get('topic')
    standard = request.form.get('standard')
    prompt = read_txt('dynamic_prompts/3_createQuestionPrompt.txt')
    
    ## CALL AI ##
    exam_question = call_gen_ai('responses/3_createQuestionResponse.txt')
    exam_question_json = json.loads(exam_question)
    
    example_answer = exam_question_json['Exam Question']['Example']
    prompt = read_txt('dynamic_prompts/4_markAnswerPrompt.txt')
    
    ## CALL AI ##
    marking = call_gen_ai('responses/4_markAnswerResponse.txt')
    marking_json = json.loads(marking)

    exam_question_json['Exam Question']['Example Explanation'] = marking_json['Explanation']

    return jsonify(exam_question=exam_question_json['Exam Question'])

@app.route('/check_answer', methods=['POST'])
def validate_answer():
    student_answer = request.form.get('answer')
    prompt = read_txt('dynamic_prompts/4_markAnswerPrompt.txt')

    ## CALL AI ##
    marking = call_gen_ai('responses/4_markAnswerResponse.txt')
    marking_json = json.loads(marking)
    print(marking_json)

    return jsonify(marking=marking_json)

if __name__ == '__main__':
    app.run(debug=True)
