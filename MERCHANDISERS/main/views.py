from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Question, Answer, QuestionScore, AnswerScore
from django.contrib.auth.models import User


# Create your views here.
 
def index(request : HttpRequest):
   ''' Display the homepage with all answers and the user can search for a specific question '''

   questions = Question.objects.all()

   if 'search' in request.GET:
      questions = Question.objects.filter(title__contains=request.GET["search"]) 

   return  render(request, "main/index.html",{"questions": questions})



def ask_question_page(request : HttpRequest):
   ''' Provide a form for user to Ask his question '''

   if request.method == "POST":
      #to add a new entry
      new_question = Question(user = request.user, title= request.POST["title"], details = request.POST["details"])
      new_question.save()
      return redirect("main:index_page")

   return render(request, "main/ask_question.html")



def answers_details_page(request : HttpRequest, question_id):
   ''' Display question details and all it's answers '''

   question = Question.objects.get(id=question_id)
   question_score = QuestionScore.objects.filter(question=question, is_rated_up=True).count() - QuestionScore.objects.filter(question=question, is_rated_up=False).count()
  

   if request.method == "POST":
      #to add a new entry
      new_answer = Answer(user = request.user, question=question, answer = request.POST["answer"])
      new_answer.save()
      return redirect("main:answers_details_page", question_id = question_id)
   
   answers = Answer.objects.filter(question = question)
   answers_number = Answer.objects.filter(question = question).count()

   return render(request, "main/answers_details.html", {"question" : question, "answers" : answers, "answers_number" : answers_number, "question_score" : question_score})



def my_profile(request : HttpRequest):
   ''' Diaplsy the user's profile '''

   questions_number = Question.objects.filter(user = request.user).count()
   answers_number = Answer.objects.filter(user = request.user).count()

   return render(request, "main/my_profile.html",{"questions_number" : questions_number,"answers_number" : answers_number})



def my_questions(request : HttpRequest):
   ''' Display all user's questions '''

   questions = Question.objects.filter(user = request.user)
   questions_number = Question.objects.filter(user = request.user).count()

   if 'search' in request.GET:
      questions = Question.objects.filter(title__contains=request.GET["search"])
   

   return render(request, "main/my_questions.html",{"questions" : questions, "questions_number" : questions_number})



def my_answers(request : HttpRequest):
   ''' Display all user's questions '''

   answers = Answer.objects.filter(user = request.user)
   answers_number = Answer.objects.filter(user = request.user).count()

   return render(request, "main/my_answers.html",{"answers" : answers, "answers_number" : answers_number})



def others_profile(request : HttpRequest, user_id):
   ''' Display other user profile '''

   user = User.objects.get(id=user_id)
   questions_number = Question.objects.filter(user = user).count()
   answers_number = Answer.objects.filter(user = user).count()

   return render(request, "main/others_profile.html",{"user" : user, "questions_number" : questions_number, "answers_number" : answers_number})



def others_questions(request : HttpRequest, user_id):
   ''' Dispaly other users questions '''

   user = User.objects.get(id=user_id)
   questions = Question.objects.filter(user = user)
   questions_number = Question.objects.filter(user = user).count()


   return render(request, "main/others_questions.html",{"questions" : questions, "questions_number" : questions_number, "user" : user})



def others_answers(request : HttpRequest, user_id):
   ''' Display other users answers '''
   user = User.objects.get(id=user_id)
   answers = Answer.objects.filter(user = user)
   answers_number = Answer.objects.filter(user = user).count()

   return render(request, "main/others_answers.html",{"answers" : answers, "answers_number" : answers_number, "user" : user})



def delete_question(request : HttpRequest, question_id):
    ''' User can delete his questions '''

   #  if not request.user.is_staff:
   #      return redirect("main:index_page")

    question = Question.objects.get(id=question_id)
    question.delete()
    return redirect("main:my_questions_page")



def edit_question(request : HttpRequest, question_id):
    ''' User can can edit his questions '''
   #  if not request.user.is_staff:
   #      return redirect("main:index_page")

    question = Question.objects.get(id=question_id)

    if request.method == "POST":
        question.title = request.POST["title"]
        question.details = request.POST["details"]
        question.save()
        return redirect("main:my_questions_page")

    return render(request, "main/edit_question.html", {"question" : question})
   


def delete_answer(request : HttpRequest, answer_id):
    ''' User cane delete his answers '''

   #  if not request.user.is_staff:
   #      return redirect("main:index_page")

    answer = Answer.objects.get(id=answer_id)
    answer.delete()
    return redirect("main:my_answers_page")



def edit_answer(request : HttpRequest, answer_id : int):
    ''' User can can edit his questions '''
   #  if not request.user.is_staff:
   #      return redirect("main:index_page")

    answer = Answer.objects.get(id=answer_id)

    if request.method == "POST":
        answer.answer = request.POST["answer"]
        answer.save()
        return redirect("main:my_answers_page")

    return render(request, "main/edit_answer.html", {"answer" : answer})



def upgrade_question(request : HttpRequest, question_id: int):
   ''' give the question 1 point up '''

   question = Question.objects.get(id=question_id)
   question_score  = QuestionScore.objects.filter(user=request.user, question=question).first()

   if question_score:
      question_score.is_rated_up = True
      question_score.is_rated_down = False
      question_score.save()
   else:
      new_score = QuestionScore(user = request.user, question=question)
      new_score.is_rated_up = True
      new_score.save()

   return redirect("main:answers_details_page", question_id = question_id)



def downgrade_question(request : HttpRequest, question_id: int):
   ''' take from the question 1 point  '''

   question = Question.objects.get(id=question_id)
   question_score  = QuestionScore.objects.filter(user=request.user, question=question).first()

   if question_score:
      question_score.is_rated_up = False
      question_score.is_rated_down = True
      question_score.save()
   else:
      new_score = QuestionScore(user = request.user, question=question)
      new_score.is_rated_down = False
      new_score.save()

   return redirect("main:answers_details_page", question_id = question_id)



def cancel_question_vote(request : HttpRequest, question_id: int):

   question = Question.objects.get(id=question_id)
   my_vote  = QuestionScore.objects.filter(user=request.user, question=question).first()
   if my_vote:
      my_vote.delete()
   # my_vote = QuestionScore.objects.get( id = question_id)

   return redirect("main:answers_details_page", question_id = question_id)



def upgrade_answer(request : HttpRequest, question_id: int, answer_id: int):
   ''' give the question 1 point up '''

   answer = Answer.objects.get(id=answer_id)
   answer_score  = AnswerScore.objects.filter(user=request.user, answer=answer).first()

   if answer_score:
      answer_score.is_rated_up = True
      answer_score.is_rated_down = False
      answer_score.save()
   else:
      new_score = AnswerScore(user = request.user, answer=answer)
      new_score.is_rated_up = True
      new_score.save()

   return redirect("main:answers_details_page2", question_id = question_id, answer_id = answer_id)




def downgrade_answer(request : HttpRequest, question_id: int, answer_id: int):
   ''' give the question 1 point up '''

   answer = Answer.objects.get(id=answer_id)
   answer_score  = AnswerScore.objects.filter(user=request.user, answer=answer).first()

   if answer_score:
      answer_score.is_rated_up = False
      answer_score.is_rated_down = True
      answer_score.save()
   else:
      new_score = AnswerScore(user = request.user, answer=answer)
      new_score.is_rated_down = False
      new_score.save()

   return redirect("main:answers_details_page2", question_id = question_id, answer_id = answer_id)



def cancel_answer_vote(request : HttpRequest, question_id: int, answer_id: int):

   answer = Answer.objects.get(id=answer_id)
   my_vote  = AnswerScore.objects.filter(user=request.user, answer=answer).first()
   if my_vote:
      my_vote.delete()
   # my_vote = QuestionScore.objects.get( id = question_id)

   return redirect("main:answers_details_page2", question_id = question_id, answer_id = answer_id )


def answers_details_page2(request : HttpRequest, question_id, answer_id):
   ''' Display question details and all it's answers '''

   question = Question.objects.get(id=question_id)
   question_score = QuestionScore.objects.filter(question=question, is_rated_up=True).count() - QuestionScore.objects.filter(question=question, is_rated_up=False).count()
  
   answer = Answer.objects.get(id=answer_id)
   answer_score = AnswerScore.objects.filter(answer=answer, is_rated_up=True).count() - AnswerScore.objects.filter(answer=answer, is_rated_up=False).count()
  

   if request.method == "POST":
      #to add a new entry
      new_answer = Answer(user = request.user, question=question, answer = request.POST["answer"])
      new_answer.save()
      return redirect("main:answers_details_page", question_id = question_id)
   
   answers = Answer.objects.filter(question = question)
   answers_number = Answer.objects.filter(question = question).count()

   return render(request, "main/answers_details.html", {"question" : question, "answers" : answers, "answers_number" : answers_number, "question_score" : question_score, "answer_score" : answer_score})



