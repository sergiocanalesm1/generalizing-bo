from django.db import models

from generalizing_core.models.lesson import Lesson
from generalizing_core.models.mixins.identity_mixin import IdentityMixin


class LessonFile(IdentityMixin):

    lesson = models.ForeignKey(
        Lesson,
        db_column='lesson',
        verbose_name='Lesson'
    )

    file = models.FileField(
        upload_to='lesson/',
        db_column='file',
        verbose_name='File'
    )