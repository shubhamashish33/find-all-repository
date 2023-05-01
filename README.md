# Find-all-repository

This repository let's you list down all the repository inside a GitHub Profile

## Requirements

- Flask

- requests

## How to use

1. First, install the required libraries: **Flask and requests**. You can use pip to install them:

``` python
pip install Flask requests
```

2. Create a new Python file named `app.py` and add the following code:

``` python
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

```


- Run the app.py file

- Open the browser and go to  `http://localhost:5000/<username>` where `<username>` is the GitHub username you want to retrieve the repositories for.

- Enter the GitHub username

- Click on submit

- You will get the list of all the repository inside that GitHub profile

