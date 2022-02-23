from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from ..models import Post


from ..models import Group, Post, User


User = get_user_model()


class PaginatorViewsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test-slug',
            description='Тестовое описание',
        )
        cls.post = Post.objects.bulk_create([
            Post(
                author=cls.user,
                text='Тестовая пост',
                group=cls.group
            )
        ])

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_index_show_correct_context(self):
        """Шаблон index сформирован с правильным контекстом."""
        response = self.authorized_client.get(reverse('posts:index'))

        first_object = response.context['page_obj'][0]
        print(response.context['page_obj'][0].text)
        task_text_0 = first_object.text
        task_author_0 = first_object.author.username
        task_group_0 = first_object.group.title

        self.assertEqual(task_text_0, 'Тестовая пост')
        self.assertEqual(task_author_0, 'auth')
        self.assertEqual(task_group_0, 'Тестовая группа')

    def test_group_list_show_correct_context(self):
        """Шаблон group_list сформирован с правильным контекстом."""
        response = self.authorized_client.get(
            reverse('posts:group_list', kwargs={'slug': self.group.slug}))

        first_object = response.context['page_obj'][0]
        print(response.context['page_obj'][0].text)
        task_text_0 = first_object.text
        task_author_0 = first_object.author.username
        task_group_0 = first_object.group.title

        self.assertEqual(task_text_0, 'Тестовая пост')
        self.assertEqual(task_author_0, 'auth')
        self.assertEqual(task_group_0, 'Тестовая группа')

    def test_profile_show_correct_context(self):
        """Шаблон profile сформирован с правильным контекстом."""
        response = self.authorized_client.get(
            reverse('posts:profile', kwargs={'username': self.user.username}))

        first_object = response.context['page_obj'][0]
        print(response.context['page_obj'][0].text)
        task_text_0 = first_object.text
        task_author_0 = first_object.author.username
        task_group_0 = first_object.group.title

        self.assertEqual(task_text_0, 'Тестовая пост')
        self.assertEqual(task_author_0, 'auth')
        self.assertEqual(task_group_0, 'Тестовая группа')
