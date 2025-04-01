import os
import sys
import requests
from dotenv import load_dotenv

def create_github_repo():
    """Create a new GitHub repository for TextApp Lite"""
    load_dotenv()
    
    # Get GitHub token from environment
    token = os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')
    if not token:
        print("Error: GITHUB_PERSONAL_ACCESS_TOKEN not found in .env file")
        sys.exit(1)
    
    # Repository settings
    repo_name = "textapp_lite"
    repo_description = "Lightweight version of the Text Application"
    
    # GitHub API endpoint
    url = "https://api.github.com/user/repos"
    
    # Headers for authentication
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Repository data
    data = {
        "name": repo_name,
        "description": repo_description,
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }
    
    try:
        # Create repository
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        print(f"Repository created successfully: {response.json()['html_url']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error creating repository: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    create_github_repo()
