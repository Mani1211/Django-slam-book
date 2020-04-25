from django import forms
from .models import Questions

class QuestionsForm():
    number = forms.IntegerField(help_text='Enter only numbers')
    class Meta:
        model = Questions
        fields = '__all__'
