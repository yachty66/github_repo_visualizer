import os
import subprocess
from urllib.parse import urlparse

def clone_repo(repo_url):
    # Parse the URL to extract the repo name
    parsed_url = urlparse(repo_url)
    repo_name = os.path.splitext(os.path.basename(parsed_url.path))[0]

    try:
        # Clone the repository
        subprocess.run(["git", "clone", repo_url], check=True)
        print(f"Repository cloned successfully: {repo_name}")
        return repo_name
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")
        return None

# This allows the function to be imported and used in other Python files
if __name__ == "__main__":
    # If run as a script, you can test it here
    test_url = "https://github.com/yachty66/github_repo_visualizer"
    result = clone_repo(test_url)
    if result:
        print(f"Cloned repo folder name: {result}")