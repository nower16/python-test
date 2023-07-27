from Question import Question


question_prompt = [
    'what color are Apples? \n(a) Red/Green \n(b) Purple \n(c) Orange\n',
    'what color are Bananas? \n(a) Teal \n(b) Magenta \n(c) Yellow\n',
    'what color are strawberries? \n(a) Yellow \n(b) Red \n(c) Blue\n'  
    
    ] 


questions = [
    Question(question_prompt[0], 'a'),
    Question(question_prompt[1], 'c'),
    Question(question_prompt[2], 'b'),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
           score +=1
           
    print('You got ' + str(score) + '/' + str(len(questions)) + 'Correct')
    
run_test(questions)