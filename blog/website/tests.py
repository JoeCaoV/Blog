from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase, Client
from website.models import Project, Comment

# Create your tests here.

class TestViews(TestCase):

    def setUp(self):
        """Creating a client object and 3 projects into DB"""
        user = User.objects.create(username='tester')
        user.set_password('motdepasse')
        user.save()
        self.client = Client()

        for number in range(3):
            project = Project.objects.create(number=number,
                                             content='content ' + str(number),
                                             title='title ' + str(number))
        self.projects = Project.objects.all()
    
    def test_get_project_page(self):
        """Testing if the views for the 3 projects are OK"""
        for project in self.projects:
            response = self.client.get('/project/' + str(project.number)).status_code
            self.assertEqual(200, response)
    
    def test_get_wrong_page(self):
        """Testing if the views for a non existing project return a 404"""
        response = self.client.get('/project/5').status_code
        self.assertEqual(404, response)

    def test_inscription(self):
        """testing a registration"""
        data = {'username':'testeur', 'password1':'adefze', 'password2':'adefze'}
        response = self.client.post('/registration', data)
        self.assertEqual(200, response.status_code)
        form = UserCreationForm(data)
        self.assertTrue(form.is_valid)
    
    def test_comment(self):
        """Testing to add a comment"""
        self.client.login(username='tester', password='motdepasse')
        response = self.client.post('/project/1', {'content':'Hello there'})
        self.assertEqual(200, response.status_code)
        comment = Comment.objects.get(pk=1)
        self.assertEqual('Hello there', comment.content)

        """Testing now to delete the comment just born, yeah I'm cruel"""
        self.client.post('/delete-comment', {'comment_id' : 1})
        self.assertRaises(Comment.DoesNotExist, Comment.objects.get, id=1)