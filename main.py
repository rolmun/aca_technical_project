import os
import logging

# For Slack Bolt
from pyexpat.errors import messages

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.INFO)
load_dotenv()

SLACK_BOT_TOKEN = os.environ.get("ACA_App_Bot_User_OAuth_Token")
SLACK_APP_TOKEN = os.environ.get("ACA_App_Socket_Mode_Token")

app = App(token=SLACK_BOT_TOKEN)
@app.event("app_mention")

def mention_handler(body, context, payload, options, say, event):
    say("Hello World!")

#test w/ friend
@app.event("member_joined_channel")
def welcome_msg(event,say):
    welcome_txt = f"Welcome <@{event['user']}> to the channel!"
    say(text=welcome_txt, channel=event['channel'])

@app.event("message")
def mention_handler(body, context, payload, options, say, event):
    pass

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()