import os
import logging

# For Slack Bolt
from pyexpat.errors import messages

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.INFO)
load_dotenv()

SLACK_BOT_TOKEN = os.environ.get("ACA_App_Socket_Mode_Token")
SLACK_APP_TOKEN = os.environ.get("ACA_App_Bot_User_OAuth_Token")

app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")
def mention_handler(body, context, payload, options, say, event):
    say("Hello World!")

@app.event("message")
def mention_handler(body, context, payload, options, say, event):
    pass

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))