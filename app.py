from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/<username>')
def repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        return render_template('repositories.html', username=username, repos=repos)
    else:
        return f"Failed to get repositories for {username}. Status code: {response.status_code}"


if __name__ == '__main__':
    app.run(debug=True)
