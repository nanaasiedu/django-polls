# Generated by Django 3.1.1 on 2020-10-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
