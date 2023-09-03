# import packages
from flask import Flask, render_template, request, jsonify
import json

# import other python modules
import inputs
import ai_calls as ai
import prompt_functions as pf

# Create app object
app = Flask(__name__)

# List of Common Standards (you can expand this)
STANDARDS = ['CCSS.ELA-LITERACY.W.4.9']

# Index.html as home page. Pass it list of Standards
@app.route('/')
def index():
    return render_template('index.html', standards=STANDARDS)

# function to create question based on user inputs
@app.route('/get_question', methods=['POST'])
def get_question():

    # topic and Standard from from end
    topic = request.form.get('topic')
    standard = request.form.get('standard')

    # dynamically construct prompt
    question_prompt = pf.create_question_prompt('dynamic_prompts/3_createQuestionPrompt.txt', standard, topic)
        
    ## generate question and load to JSON
    exam_question = ai.call_ai(question_prompt)
    exam_question_json = json.loads(exam_question)
    
    # Option to print question in terminal
    # print(exam_question)

    # take the example answer generated to mark it
    example_answer = exam_question_json['Exam Question']['Example']
    
    # dynamically construct prompt
    mark_example_prompt = pf.mark_answer_prompt('dynamic_prompts/4_markAnswerPrompt.txt',
                                str(inputs.STANDARD_DEFINITION_JSON["Definition"]),
                                str(exam_question_json['Exam Question']['Context']),   
                                str(exam_question_json['Exam Question']['Question']),
                                example_answer,
                                str(inputs.MARKING_RUBRIC_JSON["Marking"])
                                )

    # generate marking and store in JSON
    marking = ai.call_ai(mark_example_prompt)
    marking_json = json.loads(marking)

    # attach the explanation of the marked example to question JSON
    exam_question_json['Exam Question']['Example Explanation'] = marking_json['Explanation']

    # return question to front end
    return jsonify(exam_question=exam_question_json['Exam Question'])


# function to mark user's answer
@app.route('/check_answer', methods=['POST'])
def validate_answer():

    # get the user's answer along with required elements of the question 
    student_answer = request.form.get('answer')
    context = request.form.get('context')
    question = request.form.get('question')
    
    # dynamically construct prompt
    mark_student_prompt = pf.mark_answer_prompt('dynamic_prompts/4_markAnswerPrompt.txt',
                                str(inputs.STANDARD_DEFINITION_JSON["Definition"]),
                                context,   
                                question,
                                student_answer,
                                str(inputs.MARKING_RUBRIC_JSON["Marking"])
                                )

    # generate marking and explanation and store as JSON
    marking = ai.call_ai(mark_student_prompt)
    marking_json = json.loads(marking)

    # return marking to front end
    return jsonify(marking=marking_json)

# run app
if __name__ == '__main__':
    app.run(debug=True)
