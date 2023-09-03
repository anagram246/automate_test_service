# Function to read prompt txt file
def read_txt(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    return content


# Function to dynamically create the prompt for question generation based on standard and topic
def create_question_prompt(filepath, standard, topic):
    text = read_txt(filepath)
    text_out = text.replace("<VAR_STANDARD_NAME>", standard)\
                 .replace("<VAR_STUDENT_TOPIC>", topic)
    return text_out


# Function to dynamically create the prompt for marking an answer based on question, answer and marking criteria
def mark_answer_prompt(filepath, definition, context, question, answer, rubric):
    text = read_txt(filepath)
    text_out = text.replace("<VAR_STANDARD_DEFINITION>", definition)\
                   .replace("<VAR_QUESTION_CONTEXT>", context)\
                   .replace("<VAR_QUESTION_QUESTION>", question)\
                   .replace("<VAR_STUDENT_ANSWER>", answer)\
                   .replace("<VAR_RUBRIC_RESPONSE>", rubric)
    return text_out

# Function to dynamically create the prompt for simulating a student and answering the given question
def simulate_answer_prompt(filepath, exam_question):
    text = read_txt(filepath)
    text_out = text.replace("<VAR_EXAM_Q_RESPONSE_NO_EXAMPLE>", str(exam_question))
    return text_out