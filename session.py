from datetime import datetime
import math
import hashlib
import re
import requests

class generateCredentials(object):
    def __init__(self, devId, sessionId, action):
        self.devId = devId
        self.sessionId = sessionId
        self.action = action

    def generate_timestamp(self):
        utcTime = datetime.utcnow()
        utcTime = re.findall(r"\w{2,4}", str(utcTime))
        timestamp = "".join(utcTime[0:6])
        return str(timestamp)

    def generate_signature(self):
        timestamp = self.generate_timestamp()
        expression = self.devId + self.action + self.sessionId + timestamp
        signature = hashlib.md5(expression.encode()).hexdigest()
        return str(signature), timestamp
    
    def generate_session(self):
        signature, timestamp = self.generate_signature()
        response = requests.get(f"http://api.paladins.com/paladinsapi.svc/createsessionjson/\
                                {self.devId}/{signature}/{timestamp}")

        return response.json()['session_id']
