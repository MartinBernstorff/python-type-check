from typing import reveal_type

import pydantic
from django.db import models
from django_stubs_ext.db.models import TypedModelMeta

from classes import (
    Default,
    ReporterTyped,
    ReporterUntyped,
    WithId,
)


def inferred_django_fields() -> None:
    # Primitives
    generic_char_fields = Default().char_field
    reveal_type(generic_char_fields)

    float = Default().float_field
    reveal_type(float)

    integer = Default().int_field
    reveal_type(integer)

    # Newtypes
    new_type = Default().new_type
    reveal_type(new_type)

    # Choices
    integer_choice = Default().integer_choice
    reveal_type(integer_choice)

    text_choice = Default().text_choice
    reveal_type(text_choice)

    ## Extra instance methods
    choice_label = Default().get_integer_choice_display()
    reveal_type(choice_label)

    # Relations
    ## Primary keys
    auto_generated_id = Default().id
    reveal_type(auto_generated_id)

    auto_generated_pk = Default().pk
    reveal_type(auto_generated_pk)

    specified_id = WithId().id
    reveal_type(specified_id)

    specified_pk = WithId().pk
    reveal_type(specified_pk)

    ## Foreign keys
    foreign_key = Default().project
    reveal_type(foreign_key)

    foreign_key_id = Default().project_id
    reveal_type(foreign_key_id)

    chained = Default().project.company
    reveal_type(chained)

    nullable = Default().nullable_project
    reveal_type(nullable)

    ## M2M relations
    m2m = Default().projects
    reveal_type(m2m)

    m2m_all = m2m.all()
    reveal_type(m2m_all)

    for item in m2m_all:
        reveal_type(item)

    m2m_filter = m2m.filter(name="Example")
    reveal_type(m2m_filter)

    ## Reverse relationships
    reverse = Project().company_set
    reveal_type(reverse)

    reverse_untyped = ReporterUntyped().articles
    reveal_type(reverse_untyped)

    reverse_typed = ReporterTyped().articles
    reveal_type(reverse_typed)

    # Plain queries
    query_set = Default.objects.filter(int_field__gt=10)
    reveal_type(query_set)

    materialised = list(query_set.all())
    reveal_type(materialised)

    ## Joins
    # Not supported by the Python type system

    ## Aggregations
    total_sum = Default.objects.aggregate(models.Sum("int_field"))
    reveal_type(total_sum)

    payroll_total = PayrollTotal(
        Default.objects.aggregate(total=models.Sum("int_field")).get("total"),  # type: ignore
    )
    reveal_type(payroll_total)


class PayrollTotal(pydantic.RootModel[int]):
    root: int


class ExternalDataSource(models.Model):
    class Meta(TypedModelMeta):
        indexes = [
            models.Index(fields=["company", "sync_enabled"]),
            models.Index(fields=["next_sync_at"]),
            2,
        ]
