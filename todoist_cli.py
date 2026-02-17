import requests
import os

def get_tasks():
    """Fetch tasks from Todoist"""
    api_key = os.getenv("TODOIST_API_KEY")
    if not api_key:
        raise EnvironmentError("API key not found in environment")

    url = "https://api.todoist.com/api/v1/tasks"
    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        raise Exception(f"Failed to fetch tasks: {response.status_code}, {response.text}")

if __name__ == "__main__":
    try:
        tasks = get_tasks()
        print("Fetched tasks:")
        for task in tasks:
            print(f"- {task['content']}")
    except Exception as e:
        print(e)