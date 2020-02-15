from session import generateCredentials
from flask import Flask, jsonify
import requests

app = Flask(__name__)

devId = ""
sessionId = ""

def getSession():
    return generateCredentials(devId, sessionId, "createsession").generate_session()

# return the signature and timestamp
def getSignature(method):
    return generateCredentials(devId, sessionId, method).generate_signature()

@app.route("/getplayer/<player>")
def getPlayer(player):
    session = getSession()
    signature, timestamp = getSignature("getplayer")
    response = requests.get(f"http://api.paladins.com/paladinsapi.svc/getplayerjson/\
                            {devId}/{signature}/{session}/{timestamp}/{player}")
    return jsonify(response.json())

@app.route("/getchampions/<player>")
def getChampion(player):
    session = getSession()
    signature, timestamp = getSignature("getchampionranks")
    response = requests.get(f"http://api.paladins.com/paladinsapi.svc/getchampionranksjson/\
                            {devId}/{signature}/{session}/{timestamp}/{player}")
    return jsonify(response.json())

@app.route("/getstatus/<player>")
def getStatus(player):
    session = getSession()
    signature, timestamp = getSignature("getplayerstatus")
    response = requests.get(f"http://api.paladins.com/paladinsapi.svc/getplayerstatusjson/\
                            {devId}/{signature}/{session}/{timestamp}/{player}")
    return jsonify(response.json())

# returns all occurrences of a nickname (case insensitive)
@app.route("/searchplayers/<player>")
def searchPlayer(player):
    session = getSession()
    signature, timestamp = getSignature("searchplayers")
    response = requests.get(f"http://api.paladins.com/paladinsapi.svc/searchplayersjson/\
                            {devId}/{signature}/{session}/{timestamp}/{player}")
    return jsonify(response.json())

@app.route("/getmatches/<player>")
def getMatches(player):
    session = getSession()
    signature, timestamp = getSignature("getmatchhistory")
    response = requests.get(f"http://api.paladins.com/paladinsapi.svc/getmatchhistoryjson/\
                            {devId}/{signature}/{session}/{timestamp}/{player}")
    return jsonify(response.json())

if __name__ == "__main__":
    app.run()
