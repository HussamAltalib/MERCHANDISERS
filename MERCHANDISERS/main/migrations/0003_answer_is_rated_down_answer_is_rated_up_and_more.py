# Generated by Django 4.1.7 on 2023-02-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_answer_answer_score_question_question_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_rated_down',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='answer',
            name='is_rated_up',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='is_rated_down',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='is_rated_up',
            field=models.BooleanField(default=False),
        ),
    ]