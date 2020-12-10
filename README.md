# OuijaBot

## Getting set up
**The below guide *should* get your bot working!**

### Getting your credentials
* Create a reddit account
* Register your bot [here](https://old.reddit.com/prefs/apps) to get your reddit API details
* Click "create an app..."
* Name it "OuijaBot"
* Select "script"
* For your description, use "Automatically replies to submissions in the AskOuija subreddit"
* For the "redirect uri", simply link to the bot's account
* Click "create app"

Clone the repo and change into the bot directory:

    git clone https://github.com/titletrack/OuijaBot/ && cd OuijaBot

#### Edit main.py to fit your bot's details
* In line 5, replace "USER_AGENT" with the bot's description
* Replace "CLIENT_ID" in line 6 with the 14 character code given to you when you registered your bot
* Replace "CLIENT_SECRET" in line 7 with the 27 character code given to you when you registered your bot
* Replace "USERNAME" in line 8 and "PASSWORD" in line 9 with your bot's username and password

Run the bot:

    python3 main.py
