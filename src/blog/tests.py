from datetime import datetime

from django.test import TestCase
from django.utils import timezone

from blog.models import Blog


class BlogTestCase(TestCase):
    """
    Тестирование функций блога.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Blog.objects.create(
            title="Blog №1 title",
            content="Blog №1 content. " * 100,
            image="Blog №1 image path",
            publication_date=datetime(2022, 12, 20, tzinfo=timezone.utc),
        )

    def test_blog_messages_creation(self) -> None:
        """
        Тестирование моделей сообщений для блога.

        :return:
        """

        blog = Blog.objects.get(title="Blog №1 title")

        content = "Blog №1 content. " * 100
        self.assertEqual(blog.summary(), content[:100] + "...")
        self.assertEqual(blog.publication_date_format(), "Dec 20 2022")
        self.assertEqual(str(blog), f'Объект "Сообщение блога" (id={blog.pk})')
