from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Question, Answer

# Create your views here.
 
def index(request : HttpRequest):
   ''' Display the homepage with all answers and the user can search for a specific question '''

   questions = Question.objects.all()

   if 'search' in request.GET:
      questions = Question.objects.filter(title__contains=request.GET["search"])
   
      
   return  render(request, "main/index.html",{"questions": questions})

def ask_question_page(request : HttpRequest):
   ''' Provide a from for user to Ask his question '''

   if request.method == "POST":
      #to add a new entry
      new_question = Question(user = request.user, title= request.POST["title"], details = request.POST["details"])
      new_question.save()
      return redirect("main:index_page")

   return render(request, "main/ask_question.html")

def answers_details_page(request : HttpRequest, question_id):
   ''' Display question details and all it's answers '''

   question = Question.objects.get(id=question_id)

   if request.method == "POST":
      #to add a new entry
      new_answer = Answer(user = request.user, question=question, answer = request.POST["answer"])
      new_answer.save()
      return redirect("main:answers_details_page", question_id = question_id)
   
   answers = Answer.objects.filter(question = question)
   answers_number = Answer.objects.filter(question = question).count()

   return render(request, "main/answers_details.html", {"question" : question, "answers" : answers, "answers_number" : answers_number})

def profile(request : HttpRequest):
   question_number = Question.objects.filter(user = request.user).count()
   answers_number = Answer.objects.filter(user = request.user).count()

   return render(request, "main/profile.html",{"question_number" : question_number,"answers_number" : answers_number})

def questions(request : HttpRequest):
   questions = Question.objects.filter(user = request.user)
   questions_number = Question.objects.filter(user = request.user).count()
   if 'search' in request.GET:
      questions = Question.objects.filter(title__contains=request.GET["search"])
   

   return render(request, "main/questions.html",{"questions" : questions, "questions_number" : questions_number})

def answers(request : HttpRequest):
   answers = Answer.objects.filter(user = request.user)
   answers_number = Answer.objects.filter(user = request.user).count()
   
   return render(request, "main/answers.html",{"answers" : answers, "answers_number" : answers_number})


# def delete_question(request : HttpRequest, question_id):
#    #  if not request.user.is_staff:
#    #      return redirect("main:index_page")

#     question = Question.objects.get(id=question_id)
#     question.delete()
#     return redirect("main:add_clinics_page")
