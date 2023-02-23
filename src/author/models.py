from django.db import models

from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель для хранения данных об авторе
    """

    github_url = models.URLField(verbose_name="Ссылка github")
    resume_url = models.URLField(verbose_name="Ссылка на резюме")
    email = models.EmailField(verbose_name="email автора")

    class Meta:
        verbose_name = "Информация об авторе"
        verbose_name_plural = "Информация об авторе"

    def __str__(self) -> str:
        return f'Объект "автор" (id={self.pk})'
