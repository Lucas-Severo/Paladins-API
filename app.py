from session import generateCredentials
from flask import Flask, jsonify
import requests

app = Flask(__name__)

devId = "devId"
sessionId = "sessionId"

@app.route("/getPlayer/<player>")
def getPlayer(player):
    session = generateCredentials(devId, sessionId, "createsession").generate_session()
    signature, timestamp = generateCredentials(devId, sessionId, "getplayer").generate_signature()
    response = requests.get(f"http://api.paladins.com/paladinsapi.svc/getplayerjson/\
    {devId}/{signature}/{session}/{timestamp}/{player}")
    return jsonify(response.json())

if __name__ == "__main__":
    app.run()