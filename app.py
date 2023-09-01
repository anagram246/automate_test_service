from flask import Flask, render_template, request, jsonify
import json

import inputs
import ai_calls

app = Flask(__name__)

# List of Common Standards (you can expand this)
STANDARDS = ['CCSS.ELA-LITERACY.W.4.9']

# Function to read prompt txt file
def read_txt(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    return content

def create_question_prompt(filepath, standard, topic):
    text = read_txt(filepath)
    text_out = text.replace("<VAR_STANDARD_NAME>", standard)\
                 .replace("<VAR_STUDENT_TOPIC>", topic)
    return text_out

def mark_answer_prompt(filepath, definition, context, question, answer, rubric):
    text = read_txt(filepath)
    text_out = text.replace("<VAR_STANDARD_DEFINITION>", definition)\
                   .replace("<VAR_QUESTION_CONTEXT>", context)\
                   .replace("<VAR_QUESTION_QUESTION>", question)\
                   .replace("<VAR_STUDENT_ANSWER>", answer)\
                   .replace("<VAR_RUBRIC_RESPONSE>", rubric)
    return text_out

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
    question_prompt = create_question_prompt('dynamic_prompts/3_createQuestionPrompt.txt', standard, topic)
        
    ## CALL AI ##
    exam_question = ai_calls.call_ai(question_prompt)

    type(exam_question)
    print(exam_question)

    exam_question_json = json.loads(exam_question)
    
    example_answer = exam_question_json['Exam Question']['Example']
    mark_example_prompt = mark_answer_prompt('dynamic_prompts/4_markAnswerPrompt.txt',
                                str(inputs.STANDARD_DEFINITION_JSON["Definition"]),
                                str(exam_question_json['Exam Question']['Context']),   
                                str(exam_question_json['Exam Question']['Question']),
                                example_answer,
                                str(inputs.MARKING_RUBRIC_JSON["Marking"])
                                )

    ## CALL AI ##
    marking = ai_calls.call_ai(mark_example_prompt)
    marking_json = json.loads(marking)

    exam_question_json['Exam Question']['Example Explanation'] = marking_json['Explanation']

    return jsonify(exam_question=exam_question_json['Exam Question'])

@app.route('/check_answer', methods=['POST'])
def validate_answer():
    student_answer = request.form.get('answer')
    context = request.form.get('context')
    question = request.form.get('question')
    
    mark_student_prompt = mark_answer_prompt('dynamic_prompts/4_markAnswerPrompt.txt',
                                str(inputs.STANDARD_DEFINITION_JSON["Definition"]),
                                context,   
                                question,
                                student_answer,
                                str(inputs.MARKING_RUBRIC_JSON["Marking"])
                                )

    ## CALL AI ##
    marking = ai_calls.call_ai(mark_student_prompt)
    marking_json = json.loads(marking)

    return jsonify(marking=marking_json)

if __name__ == '__main__':
    app.run(debug=True)
