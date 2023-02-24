from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
       path("", views.index, name="index_page"),
       path("question/", views.question_page, name="question_page"),
       path("answers/details/<question_id>/", views.answers_details_page, name="answers_details_page"),

]