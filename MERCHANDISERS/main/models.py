from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    details = models.TextField()
    asked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} "
    

    
class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField()
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user} : {self.question.title}"
    

    

class QuestionScore(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    is_rated_up = models.BooleanField(default=False)
    is_rated_down = models.BooleanField(default=False)



class AnswerScore(models.Model):

    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    is_rated_up = models.BooleanField(default=False)
    is_rated_down = models.BooleanField(default=False)
    question_score = models.IntegerField(default=0)



    


