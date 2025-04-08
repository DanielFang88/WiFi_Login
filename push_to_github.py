import os
import subprocess

def push_to_github(commit_message="Update WiFi login script"):
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Pushed to GitHub successfully!")
    except subprocess.CalledProcessError as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    push_to_github()
