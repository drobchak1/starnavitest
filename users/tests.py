from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import User

class AuthTests(APITestCase):
    def test_api_jwt(self):
        """
        Ensure we can register user and create post using JWT-token.
        """
        url = reverse('token_obtain_pair')
        u = User.objects.create_user(username='user', email='user@foo.com', password='pass')
        u.is_active = False
        u.save()

        resp = self.client.post(url, {'email':'user@foo.com', 'password':'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        u.is_active = True
        u.save()

        resp = self.client.post(url, {'username':'user', 'password':'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        print(resp.data)
        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)
        token = resp.data['access']

        verification_url = reverse('api:post-list')
        

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'abc')
        resp = client.post(verification_url, {
            "title": "new post2",
            "description": "kjflkgjdlfkjgklfjdgjd"
        })
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        resp = client.post(verification_url, {
            "title": "new post2",
            "description": "kjflkgjdlfkjgklfjdgjd"
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)