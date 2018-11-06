# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACc1fcc3e666679a327a74770e44cd96e9'
auth_token = 'd476720013ca25497bc0aa997e728367'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        record=True,
                        url='https://handler.twilio.com/twiml/EH34a155df270e7370815211cd326435d9',
                        to='+5521969490755',
                        from_='+552145601743'
                    )

print(call)