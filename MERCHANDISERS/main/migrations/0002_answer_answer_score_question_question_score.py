# Generated by Django 4.1.7 on 2023-02-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='question_score',
            field=models.IntegerField(default=0),
        ),
    ]
