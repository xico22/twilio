import requests

r = requests.get("https://api.twilio.com/2010-04-01/Accounts/ACc1fcc3e666679a327a74770e44cd96e9/Transcriptions/CAd27558a4ff6aec3362163cf7952a0a70.json")

print(r.json)