# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#   return "Hello World!"

# if __name__ == "__main__":
#   app.run()



# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import re

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    msg = request.form['Body']
    joke = re.search(r'(.*)joke(.*)', msg, re.I)
    greet = re.search(r'(.*)[hi|hey|hello](.*)', msg, re.I)
    quote = re.search(r'(.*)quote(.*)', msg, re.I)
    # joke = re.search(r'(.*)joke(.*)', msg, re.I)

    if joke: resp.message("I wanted to look for my watch but I couldn't find the time!")
    elif quote: resp.message("A great player is the one who makes the game look easy!")
    elif greet: resp.message("Greetings! I am your assistant!")

    # Add a message
    else: resp.message("Ahoy! You said, '" + msg + "'")
    print(request.form)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
