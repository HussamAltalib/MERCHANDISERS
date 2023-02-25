from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
       path("", views.index, name="index_page"),
       path("question/", views.ask_question_page, name="ask_question_page"),
       path("answers/details/<question_id>/", views.answers_details_page, name="answers_details_page"),
       path("profile/", views.profile, name="profile_page"),
       path("questions/", views.questions, name="questions_page"),
       path("answers/", views.answers, name="answers_page"),




]