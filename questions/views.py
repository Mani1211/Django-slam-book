from django.shortcuts import render,redirect
from .models import Questions
from .forms import QuestionsForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        return render(request,'questions.html', {'name':name})
    else:
        return render(request,'home.html')
    

def questions(request):
    if request.method == 'POST':
        questions = Questions()
        questions.name  = request.POST['name']
        questions.number  = request.POST['number']
        questions.advice  = request.POST['advice']
        questions.positive = request.POST['positive']
        questions.weakness  = request.POST['weakness']
        questions.like  = request.POST['like']
        questions.words  = request.POST['words']
        questions.memory  = request.POST['memory']
        print(request.POST)
        questions.save()
        return redirect('thank')
    else:
        return render(request,'questions.html')

def thank(request):
    return render(request,'thank.html')