import datetime

from django.core.validators import URLValidator
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
from django.utils import timezone
from django_enumfield import enum


def validate_positive(value):
    if value < 0:
        raise ValidationError(
            '%(value)s is not a positive integer',
            params={'value': value},
        )

class QuestionType(enum.Enum):
    GAMING = 0
    GENERAL = 1
    MOVIES = 2

    __default__ = GAMING

    __labels__ = {
        GAMING: "Gaming",
        GENERAL: "General",
        MOVIES: "Movies"
    }


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    type = enum.EnumField(QuestionType, default=QuestionType.GAMING)
    rating = models.IntegerField(default=1, validators=[validate_positive])
    site = models.CharField(max_length=200, validators=[URLValidator()], default="")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
