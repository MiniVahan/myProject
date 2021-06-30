from django.shortcuts import render
from .forms import PlayForm, AddQuestionForm
from .models import Question
import random


def game(request):
    return render(request, 'game.html')


questions = []
all_questions = Question.objects.all()
for question in all_questions:
    questions.append(question)
number = 0
question = random.choice(questions)


def play(request):
    global number
    global question
    form = PlayForm()
    info = ''
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer == question.right_answer:
            info = 'Right'
            number += 1
        else:
            info = 'Wrong'
        try:
            questions.remove(question)
        except ValueError:
            question.right_answer = None
        if len(questions) != 0:
            question = random.choice(questions)
        else:
            info = f'"Game over!Your score is {number}/10!"'
    return render(request, 'millionaire.html', {'form': form, 'question': question, 'info': info, 'number': number})


def add_question(request):
    form = AddQuestionForm()
    info = ''
    if request.method == 'POST':
        Question.objects.create(question=request.POST.get('question'),
                                answer1=request.POST.get('answer1'),
                                answer2=request.POST.get('answer2'),
                                answer3=request.POST.get('answer3'),
                                answer4=request.POST.get('answer4'),
                                right_answer=request.POST.get('right_answer')
                                )
        info = 'Your question successfully added into database '
    return render(request, 'questions.html', {'form': form, 'info':info})
