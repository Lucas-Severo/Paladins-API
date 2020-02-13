from session import generateCredentials
from flask import Flask, jsonify
import requests

app = Flask(__name__)

devId = ""
sessionId = ""

@app.route("/getplayer/<player>")
def getPlayer(player):
    session = generateCredentials(devId, sessionId, "createsession").generate_session()
    signature, timestamp = generateCredentials(devId, sessionId, "getplayer").generate_signature()
    response = requests.get(f"http://api.paladins.com/paladinsapi.svc/getplayerjson/\
                            {devId}/{signature}/{session}/{timestamp}/{player}")
    return jsonify(response.json())

@app.route("/getchampions/<player>")
def getChampion(player):
    session = generateCredentials(devId, sessionId, "createsession").generate_session()
    signature, timestamp = generateCredentials(devId, sessionId, "getchampionranks").generate_signature()
    response = requests.get(f"http://api.paladins.com/paladinsapi.svc/getchampionranksjson/\
                            {devId}/{signature}/{session}/{timestamp}/{player}")
    return jsonify(response.json())

if __name__ == "__main__":
    app.run()