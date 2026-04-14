# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



import requests

USERNAME = "Aomine2k"

def fetch_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def format_table(data):
    table = f"""
+------------------+----------------------+
| Field            | Value                |
+------------------+----------------------+
| Login            | {data.get('login')} 
| Name             | {data.get('name')} 
| Public Repos     | {data.get('public_repos')} 
| Followers        | {data.get('followers')} 
| Following        | {data.get('following')} 
| Created At       | {data.get('created_at')} 
+------------------+----------------------+
"""
    return table

if __name__ == "__main__":
    user_data = fetch_user(USERNAME)
    print(format_table(user_data))