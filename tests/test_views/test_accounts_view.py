from django.test import TestCase



class AccountsViewTest(TestCase):
    def setUp(self):
        self.user_data = {
            "email":"kanerumasta@gmail.com",
            "first_name":"John",
            "last_name":"Doe",
            "password":"M4cn1n0@011456",
            "re_password":"M4cn1n0@011456"
        }

    def test_register_user(self):
        response = self.client.post('/api/auth/users/', self.user_data)
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        self.client.post('/api/auth/users/', self.user_data)
        response = self.client.post('/api/auth/jwt/create/',{"email":self.user_data['email'], 'password':self.user_data['password']})
        self.assertIn('access', response.json())

