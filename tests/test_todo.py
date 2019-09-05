from unittest import TestCase
from run import create_app
import json

class TodoResourceTestCase(TestCase):
    ''' Class to test all /to-do endpoints '''
    # This would be called everytime a test runs
    def setUp(self):
        # Create a test environment
        # Create test client for application
        self.app = create_app()
        self.app.test_request_context().push()
        self.client = self.app.test_client()
        self.headers = {'Content-Type': 'application/json'}


    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        response = self.client.get('/')
        # assert the status code of the response
        self.assertEqual(response.status_code, 200) 

    def test_to_retrieve_all_todos(self):
        ''' Retrieve all todos '''
        response = self.client.get('/api/v1/to-do')
        assert response.status_code == 200

    def test_to_retrieve_a_single_todo_that_does_not_exist(self):
        ''' Retrieve a specific todos '''
        response = self.client.get('/api/v1/to-do/60000')
        expected_response = 'todo not found'
        assert response.status_code == 404
        self.assertEqual(response.json.get('error'), expected_response)

    def test_to_create_a_todo(self):
        ''' Create a specific todos' title '''
        todo_object = {
            "title": "hand dryer",
            "body": "b jknhkjnkj ",
            "completed": True
        }
        response = self.client.post('/api/v1/to-do', data = json.dumps(todo_object), headers=self.headers)
        expected_response = {
            "title": "hand dryer",
            "body": "b jknhkjnkj ",
            "completed": True,
            
        }
        assert response.status_code == 201
        self.assertEqual(response.json.get('todo').get('title'), expected_response['title'])
        self.assertEqual(response.json.get('todo').get('completed'), expected_response['completed'])
        self.assertEqual(response.json.get('todo').get('body'), expected_response['body'])

    def test_to_retrieve_a_single_todo(self):
        ''' Retrieve a specific todos '''
        response = self.client.get('/api/v1/to-do/4')

        assert response.status_code == 200

    def test_to_update_a_single_todo(self):
        ''' Update a specific todos' title '''
        todo_object = {
            'title': 'I am getting updated'
        }
        response = self.client.patch('/api/v1/to-do/4', data = json.dumps(todo_object), headers=self.headers)
        expected_response = 'I am getting updated'
        assert response.status_code == 200
        self.assertEqual(response.json.get('todo').get('title'), expected_response)

    def test_to_update_an_invalid_todo(self):
        ''' Update a specific todos that is doesn't exist '''
        response = self.client.patch('/api/v1/to-do/600000')
        expected_response = 'todo not found'
        assert response.status_code == 404
        self.assertEqual(response.json.get('error'), expected_response)

    def test_to_update_todo_without_any_object(self):
        ''' Update todo without passing the fields to update '''
        todo_object = {}
        response = self.client.patch('/api/v1/to-do/4', data = json.dumps(todo_object), headers=self.headers)
        expected_response = 'Enter either a title, body or completed'
        assert response.status_code == 400
        self.assertEqual(response.json.get('error'), expected_response)
    
    # def test_to_delete_a_todo(self):
    #     ''' Delete a specific todos '''
    #     response = self.client.delete('/api/v1/to-do/2')
    #     assert response.status_code == 200
