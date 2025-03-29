from django.test import TestCase
from accounts.models import User

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='test123',
            first_name='Test',
            last_name='User'
        )
        self.superuser = User.objects.create_superuser(
            email='superuser@example.com',
            password='superuser123',
            first_name='Super',
            last_name='User'
        )

    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('test123'))
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_superuser_creation(self):

        self.assertTrue(isinstance(self.superuser, User))
        self.assertEqual(self.superuser.email, 'superuser@example.com')
        self.assertTrue(self.superuser.check_password('superuser123'))
        self.assertEqual(self.superuser.first_name, 'Super')
        self.assertEqual(self.superuser.last_name, 'User')
        self.assertTrue(self.superuser.is_active)
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)
