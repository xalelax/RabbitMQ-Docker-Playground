import unittest
from producer.producer import app


class TestProducer(unittest.TestCase):

    def test_index(self):
        response = app.test_client().get('/')
        self.assertEqual(response.status_code, 200)

        body = response.json['body']
        self.assertEqual(body, "Thanks for visiting!")


if __name__ == '__main__':
    unittest.main()
