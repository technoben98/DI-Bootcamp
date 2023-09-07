data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def check_answers () :      #init function
    number_correct_answers = 0      # init correct answers variable
    number_incorrect_answers = 0      # init incorrect answers variable
    list_wrong_answers = []      # init wrong answers list

    print("\n ---- The quizz starts ----")      # print starting line
    for quizz in data :      # loop for asking questions from "data"
        user_answer = input(quizz["question"])      # input for user answer
        if user_answer.lower() == quizz["answer"].lower():      # check if user answer right
            number_correct_answers += 1      # than count of correct answer multiply by 1
        else :      # if not right
            number_incorrect_answers += 1      # than count of incorrect answers multiply by 1
            new_quizz = quizz.copy()        # make a copy of the dictionary
            new_quizz["user_answer"] = user_answer      # adding wrong answer to new dict
            list_wrong_answers.append(new_quizz)      #appending list of wrong answers by dict
    
    inform_user(number_correct_answers, number_incorrect_answers, list_wrong_answers)      # using function for inform user about score

def inform_user (correct, incorrect, wrong_answers) :      # init function for informing user
    print("\n ----------------------------")      # print new line
    print(f"You have {correct} correct answers")      # print correct answers
    print(f"You have {incorrect} incorrect answers")      # print incorrect answers
    for global_answer in wrong_answers :      # loop for wrong answers
        print(f'The question was {global_answer["question"]}')      # print question that user answered incorrect
        print(f'Your answer was {global_answer["user_answer"]}')      # print incorrect answer
        print(f'Your got it wrong, the correct answer is {global_answer["answer"]}')      # print correct answer
    
    print("\n --------------------")      # print new line
    if incorrect > 3 :      # check that user has more than 3 incorrect answers
        print(" YOU GOT MORE 3 ANSWERS WRONG Play Again")      # print that user has more than 3 incorrect answers
        check_answers()      # using function for start game from start
    else :      
        print("Good Job - YOU DONT NEED TO REDO THE GAME")      # print that user win

check_answers()      # start programm from using first function