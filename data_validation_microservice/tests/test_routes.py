import unittest
from flask import Flask
from app import create_app, db
from app.models import ExampleModel

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_data(self):
        response = self.client.post('/add-data', json={'data': 'Test data'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['message'], 'Data added successfully!')

if __name__ == '__main__':
    unittest.main()
