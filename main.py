import os
import logging

# For Slack Bolt
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

#For Functions
from datetime import datetime

logging.basicConfig(level=logging.INFO)

from dotenv import load_dotenv
load_dotenv()

SLACK_BOT_TOKEN = os.environ.get("ACA_App_Bot_User_OAuth_Token")
SLACK_APP_TOKEN = os.environ.get("ACA_App_Socket_Mode_Token")

app = App(token=SLACK_BOT_TOKEN)


@app.event("member_joined_channel")
def welcome_msg(event,say):
    welcome_txt = f"Welcome <@{event['user']}> to the channel! Start with typing '*!guide*' "
    say(text=welcome_txt, channel=event['channel'])

@app.message("!guide")
def guide(message,say):
     user_id = message['user']
     say(f"<@{user_id}> Hi there! I am a BOT that facilitates this fine channel."
         "\n\n Here are some a helpful commands to use:"
         "\n\n1) *!time* - Tell the current day and time."
         "\n2) *!parrot* - Will echo what you say once. ")

@app.event("app_mention")
def mention_handler(body, context, payload, options, say, event):
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y | %H:%M:%S")
    say(f"Hi! The current time is {current_time}")


@app.message("!time")
def time_response(message, say):
    user_id = message['user']
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y | %H:%M:%S")
    say(f"<@{user_id}> The current time is {current_time}")



# Set to store user IDs who have initiated the recipricate mode
recipricate_to_user = set()

@app.message("!parrot")
def initiate_recipricate(message, say):
    user_id = message['user']
    recipricate_to_user.add(user_id)
    say(f"<@{user_id}>, you have initiated Parrot Mode. I'll echo back your message only once.")

@app.message() # This decorator will match all messages
def echo_message(message, say):
    user_id = message['user']
    text = message['text']

    if user_id in recipricate_to_user:  # Check if user has initiated recipricate mode
        say(text=text)  # Echo back the text
        recipricate_to_user.remove(user_id)  # Remove user from the set, so the echo only happens once


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()