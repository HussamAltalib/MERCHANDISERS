from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Question, Answer

# Create your views here.
 
def index(request : HttpRequest):
   
   questions = Question.objects.all()
   return  render(request, "main/index.html",{"questions": questions})

def question_page(request : HttpRequest):

   if request.method == "POST":
      #to add a new entry
      new_question = Question(user = request.user, title= request.POST["title"], details = request.POST["details"])
      new_question.save()
      return redirect("main:index_page")

   return render(request, "main/question.html")
