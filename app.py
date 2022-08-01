from os import environ

from flask import Flask

env_list = [
    "HOSTNAME",
    "KUBERNETES_SERVICE_HOST",
    "KUBERNETES_SERVICE_PORT",
    "NAMESPACE_NAME",
    "POD_UID",
    "POD_NAME",
    "POD_IP_ADDRESS",
    "SERVICE_ACCOUNT_NAME",
    "NODE_NAME",
    "NODE_IP_ADDRESS",
]

POD_INFO = {}

for env in env_list:
    POD_INFO[env] = environ.get(env, "none")

app = Flask(__name__)


@app.route("/")
def index():
    return {"result": POD_INFO}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")
