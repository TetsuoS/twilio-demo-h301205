from twilio.rest import Client
account_sid = "xxxxxxxx" # Your Account SID from www.twilio.com/console
auth_token  = "yyyyyyy"  # Your Auth Token from www.twilio.com/console

client = Client(account_sid, auth_token)

call = client.calls.create(
    from_="+81xxxxxxxx",
    to="+81zzzzzzz",
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)
