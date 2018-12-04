#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

#import sys, codecs
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

app = Flask(__name__)

@app.route('/say', methods=['GET', 'POST'])
def say():
    # TwiMLを作成
    resp = VoiceResponse()
    resp.say("こんにちは。トゥイリオってとても楽しいですね。", language="ja-JP", voice="alice")
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
