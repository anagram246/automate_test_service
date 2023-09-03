import json

import prompt_functions as pf
import ai_calls as ai
import inputs

print()
print('Running Simulation')
print()
print()

standard = inputs.STANDARDS[0]

# specify topic of interest (7)
topicPrompt = pf.read_txt('dynamic_prompts/7_simulateRandomTopic.txt')
topic = ai.call_ai(topicPrompt)

print('Student: ' + standard + ' on topic of ' + topic)
print()
print()

# generate question and mark answer (3)
question_prompt = pf.create_question_prompt('dynamic_prompts/3_createQuestionPrompt.txt', standard, topic)
exam_question = ai.call_ai(question_prompt)
exam_question_json = json.loads(exam_question)

print('Website: ' + exam_question_json['Exam Question']['Introduction'])
print()
print(exam_question_json['Exam Question']['Context'])
print()
print(exam_question_json['Exam Question']['Question'])
print()
print()


# mark example (4)
example_answer = exam_question_json['Exam Question']['Example']
mark_example_prompt = pf.mark_answer_prompt('dynamic_prompts/4_markAnswerPrompt.txt',
                                str(inputs.STANDARD_DEFINITION_JSON["Definition"]),
                                str(exam_question_json['Exam Question']['Context']),   
                                str(exam_question_json['Exam Question']['Question']),
                                example_answer,
                                str(inputs.MARKING_RUBRIC_JSON["Marking"])
                                )
markingExample = ai.call_ai(mark_example_prompt)
markingExample_json = json.loads(markingExample)

# simulate student answer (5)
exam_q_list = ['Introduction', 'Context', 'Question']
exam_q_no_example = {key: exam_question_json['Exam Question'][key] for key in exam_q_list}

simulateAnswerPrompt = pf.simulate_answer_prompt('dynamic_prompts/5_simulateStudentPrompt.txt', exam_q_no_example)
simulateAnswer = ai.call_ai(simulateAnswerPrompt)
simulateAnswer_json = json.loads(simulateAnswer)

print('Student Persona: ' + simulateAnswer_json['Persona'])
print()
print('Student Answer: ' + simulateAnswer_json['Answer'])
print()
print()

# Mark student answer (4)
mark_student_prompt = pf.mark_answer_prompt('dynamic_prompts/4_markAnswerPrompt.txt',
                                str(inputs.STANDARD_DEFINITION_JSON["Definition"]),
                                exam_question_json['Exam Question']['Context'],   
                                exam_question_json['Exam Question']['Question'],
                                simulateAnswer_json['Answer'],
                                str(inputs.MARKING_RUBRIC_JSON["Marking"])
                                )

# generate marking and explanation and store as JSON
markingStudent = ai.call_ai(mark_student_prompt)
markingStudent_json = json.loads(markingStudent)

print('Score given: ' + str(markingStudent_json['Score']))
print()
print('Website: ' + markingStudent_json['Explanation'])
print()
print()
print('Student: Request example of good answer')
print()
print()
print('Website: ' + example_answer)
print()
print('Score given: ' + str(markingExample_json['Score']))
print()
print('Website: ' + markingExample_json['Explanation'])
print()
print('End')