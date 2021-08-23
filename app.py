from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "import random
print(random.randrange(1, 59), random.randrange(1, 59), random.randrange(1, 59), random.randrange(1, 59), random.randrange(1, 59), random.randrange(1, 59))

import random
print(random.randrange(1, 50), random.randrange(1, 50), random.randrange(1, 50), random.randrange(1, 50), random.randrange(1, 50))
print(random.randrange(1, 12), random.randrange(1, 12))
"
