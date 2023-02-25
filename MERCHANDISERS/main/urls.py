from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
       path("", views.index, name="index_page"),
       path("ask/question/", views.ask_question_page, name="ask_question_page"),
       path("answers/details/<question_id>/", views.answers_details_page, name="answers_details_page"),

       path("my/profile/", views.my_profile, name="my_profile_page"),
       path("my/questions/", views.my_questions, name="my_questions_page"),
       path("my/answers/", views.my_answers, name="my_answers_page"),

       path("profile/<user_id>/", views.profile, name="profile_page"),
       path("questions/<user_id>/", views.questions, name="questions_page"),
       path("answers/<user_id>/", views.answers, name="answers_page"),







]