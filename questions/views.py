from django.shortcuts import render
from .models import Questions

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        return render(request,'questions.html',{'name':name})
    else:

        return render(request,'home.html')

def questions(request):
    if request.method == 'POST':
        print(request.method)
        questions = Questions()

        questions.name  = request.POST['name']
        questions.number  = request.POST['number']
        questions.advice  = request.POST['advice']
        questions.positive = request.POST['positive']
        questions.weakness  = request.POST['weakness']
        questions.like  = request.POST['like']
        questions.words  = request.POST['words']
        questions.memory  = request.POST['memory']
        questions.talents = request.POST['talents']
        questions.change = request.POST['change']
        questions.save()
        return render(request,'thank.html')
    else:
        return render(request,'questions.html')