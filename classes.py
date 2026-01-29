from typing import TYPE_CHECKING, NewType, cast

from django.db import models
from django.db.models.manager import Manager

from editor.models import Project


class IntegerChoice(models.IntegerChoices):
    OPTION_A = 1, "Option A"
    OPTION_B = 2, "Option B"


class TextChoice(models.TextChoices):
    OPTION_X = "X", "Option X"
    OPTION_Y = "Y", "Option Y"


DefaultName = NewType("DefaultName", str)


class Default(models.Model):
    char_field = models.CharField(max_length=255, default="default_value")
    float_field = models.FloatField(default=0.0)
    int_field = models.IntegerField(default=0)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    nullable_project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, related_name="nullable_projects"
    )

    projects = models.ManyToManyField(Project)

    integer_choice = models.IntegerField(choices=IntegerChoice.choices)
    text_choice = models.CharField(max_length=1, choices=TextChoice.choices)

    new_type = cast(
        "DefaultName", models.CharField(max_length=255, default="default_name")
    )


class WithId(models.Model):
    id = models.UUIDField(primary_key=True)


class ReporterTyped(models.Model):
    full_name = models.CharField(max_length=70)
    articles: Manager["ArticleTyped"]


class ArticleTyped(models.Model):
    reporter = models.ForeignKey(ReporterTyped, on_delete=models.CASCADE)


class ReporterUntyped(models.Model):
    full_name = models.CharField(max_length=70)


class ArticleUntyped(models.Model):
    reporter = models.ForeignKey(ReporterUntyped, on_delete=models.CASCADE)
