from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
       path("", views.index, name="index_page"),
       path("ask/question/", views.ask_question_page, name="ask_question_page"),
       path("answers/details/<question_id>/", views.answers_details_page, name="answers_details_page"),
       path("answers/details/<question_id>/<answer_id>/", views.answers_details_page2, name="answers_details_page2"),

       path("my/profile/", views.my_profile, name="my_profile_page"),
       path("my/questions/", views.my_questions, name="my_questions_page"),
       path("my/answers/", views.my_answers, name="my_answers_page"),

       path("others/profile/<user_id>/", views.others_profile, name="others_profile_page"),
       path("others/questions/<user_id>/", views.others_questions, name="others_questions_page"),
       path("others/answers/<user_id>/", views.others_answers, name="others_answers_page"),

       path("delete/question/<question_id>/", views.delete_question, name="delete_question"),
       path("edit/question/<question_id>/", views.edit_question, name="edit_question_page"),

       path("delete/answer/<answer_id>/", views.delete_answer, name="delete_answer"),
       path("edit/answer/<answer_id>/", views.edit_answer, name="edit_answer_page"),

       path("upgrade/question/<question_id>/", views.upgrade_question, name="upgrade_question"),
       path("downgrade/question/<question_id>/", views.downgrade_question, name="downgrade_question"),
       path("cancel/question/vote/<question_id>/", views.cancel_question_vote, name="cancel_question_vote"),

       path("upgrade/answer/<question_id>/<answer_id>/", views.upgrade_answer, name="upgrade_answer"),
       path("downgrade/answer/<question_id>/<answer_id>/", views.downgrade_answer, name="downgrade_answer"),
       path("cancel/answer/vote/<question_id>/<answer_id>/", views.cancel_answer_vote, name="cancel_answer_vote"),


]