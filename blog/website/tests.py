from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase, Client
from website.models import Project

# Create your tests here.

class TestViews(TestCase):

    def setUp(self):
        """Creating a client object and 3 projects into DB"""
        user = User.objects.create(username='tester')
        user.set_password('motdepasse')
        user.save()
        self.client = Client()
        self.client.login(username='tester', password='motdepasse')

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
    
    def test_add_comment(self):
        """Testing to add a comment"""
        response = self.client.post('/project/1', {'content':'Hello there'})
        self.assetEqual=(200, response.status_code)
