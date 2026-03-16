import requests

def get_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    events = response.json()
    
    print(f"Recent activity for {username}:\n")
    
    for event in events[:10]:
        event_type = event['type']
        repo_name = event['repo']['name']
        date = event['created_at'][:10]  # Just the date part
        print(f"- [{date}] {event_type} on {repo_name}")

get_github_activity("ganeshbk11")