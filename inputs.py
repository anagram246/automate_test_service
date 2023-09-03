import json

# List of Common Standards for website drop down
STANDARDS = ['CCSS.ELA-LITERACY.W.4.9']

# This definition would be stored in a database of all standard and their definitions
# The prompt in '1_standardDefinitionPrompt.txt' could be used to check it is up to date
STANDARD_DEFINITION_JSON = {
    "Reference" : "CCSS.ELA-Literacy.W.4.9",
    "Definition" : "Draw evidence from literary or informational texts to support analysis, reflection, and research."
}

# For consistency the marking rubric should also be stored in a database. It could be human or AI created.
# The prompt in '2_markingRubricPrompt.txt' is an example of how this one was created using AI
MARKING_RUBRIC_JSON = {
    "Reference" : "CCSS.ELA-LITERACY.W.4.9",
    "Marking" : {
        "3" : "Answer comprehensively integrates information from the provided text, demonstrates a clear understanding of the text, and directly addresses the open-ended question with well-supported details.",
        "2" : "Answer integrates some information from the provided text, demonstrates a general understanding of the text, but may lack some details or not fully address the open-ended question.",
        "1" : "Answer minimally references the provided text, demonstrates limited understanding of the text, and inadequately addresses the open-ended question.",
        "0" : "Answer does not reference the provided text, demonstrates no understanding of the text, or does not address the open-ended question at all."
    }
}