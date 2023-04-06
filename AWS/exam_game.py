import random
import sys
import os
import json

f = open("questionnaires.json")

questionnaire = json.load(f)["qcm"]
print(len(questionnaire))


def generate_question(questionnaire):
    question = random.choice(questionnaire)
    options = question["options"]
    random.shuffle(options)
    formatted_options = [f"{i+1}. {option['text']}" for i, option in enumerate(options)]
    formatted_question = f"{question['question']}\n{chr(10).join(formatted_options)}\n\n"
    answer = input(formatted_question)
    is_correct = False
    try:
        answer = int(answer)
        print(options)
        if answer > 0 and answer <= len(options) and options[answer-1]["is_correct"]=='True':
            is_correct =True
    except ValueError:
        pass
    if is_correct:
        print("\nCorrect!")
        return 1
    else:
        print("\nIncorrect! et la bonne réponse est: ")
        n=1
        for d in options:
            if d['is_correct']=='True':
                print("\t--> "+str(n)+". " +str(d["text"]))
                n+=1
        return 0




score = 0
num_questions = len(questionnaire)

for i in range(num_questions):
    print("\n------------------------------------")
    question = generate_question(questionnaire)
    score += question
    print(f"Score actuel : {score}/{i+1}")

print(f"Score final : {score}/{num_questions}")