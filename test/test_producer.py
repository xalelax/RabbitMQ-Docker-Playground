import unittest
from unittest.mock import Mock
import producer.producer


class TestProducer(unittest.TestCase):

    def setUp(self):
        self.app = producer.producer.app
        producer.producer.channel = Mock()

    def test_index(self):
        response = self.app.test_client().get('/')
        self.assertEqual(response.status_code, 200)

        body = response.json['body']
        self.assertEqual(body, "Thanks for visiting!")


if __name__ == '__main__':
    unittest.main()
