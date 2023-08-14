import os
import logging

# For Slack Bolt
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from datetime import datetime

logging.basicConfig(level=logging.INFO)

from dotenv import load_dotenv
load_dotenv()



SLACK_BOT_TOKEN = os.environ.get("ACA_App_Bot_User_OAuth_Token")
SLACK_APP_TOKEN = os.environ.get("ACA_App_Socket_Mode_Token")

app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")
def mention_handler(body, context, payload, options, say, event):
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y | %H:%M:%S")
    say(f"Hi! The current time is {current_time}")

@app.event("message")
def handle_message(payload, context):
    channel_id = payload.get('channel')
    text = payload.get('text')
    subtype = payload.get('subtype')

    print(f"Full payload: {payload}")
    print(f"Channel ID: {channel_id}, Text: {text}, Subtype: {subtype}")

    client = context.client

    if channel_id and text and subtype is None:  # Only respond to messages without a subtype
        client.chat_postMessage(channel=channel_id, text=text)
    else:
        print("Not sending message, missing required fields or handling a subtype.")




#test w/ friend
@app.event("member_joined_channel")
def welcome_msg(event,say):
    welcome_txt = f"Welcome <@{event['user']}> to the channel!"
    say(text=welcome_txt, channel=event['channel'])


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()