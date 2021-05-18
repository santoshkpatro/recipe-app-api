from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_use_with_email_successful(self):
        email = 'test@gmail.com'
        password = 'Testpass1122'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # Test creating user with no email raise error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@123')

    def test_create_new_super_user(self):
        # Test creating a new super user
        user = get_user_model().objects.create_superuser(
            'test@london.com',
            'abanc@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
