import unittest
from unittest.mock import patch
import todoist_cli

class TestTodoistCLI(unittest.TestCase):

    @patch("todoist_cli.requests.get")
    def test_get_tasks_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"id": 1, "content": "Task 1"},
            {"id": 2, "content": "Task 2"}
        ]

        tasks = todoist_cli.get_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]['content'], "Task 1")
        self.assertEqual(tasks[1]['content'], "Task 2")

    @patch("todoist_cli.requests.get")
    def test_get_tasks_failure(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 400
        mock_response.text = "Bad Request"

        with self.assertRaises(Exception) as context:
            todoist_cli.get_tasks()

        self.assertIn("Failed to fetch tasks", str(context.exception))

if __name__ == "__main__":
    unittest.main()