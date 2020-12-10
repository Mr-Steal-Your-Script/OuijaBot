import praw, time, random, traceback

reddit = praw.Reddit(user_agent='USER_AGENT',
                     client_id='CLIENT_ID',
                     client_secret='CLIENT_SECRET',
                     username='USERNAME',
                     password='PASSWORD')

letters = ['A',
           'B',
           'C',
           'D',
           'E',
           'F',
           'G',
           'H',
           'I',
           'J',
           'K',
           'L',
           'M',
           'N',
           'O',
           'P',
           'Q',
           'R',
           'S',
           'T',
           'U',
           'V',
           'W',
           'X',
           'Y',
           'Z']

while True:
    try:
        for submission in reddit.subreddit('AskOuija').stream.submissions(skip_existing=True):
            a = submission.locked
            if a == False:
                submission.reply(random.choice(letters))
    except Exception as e:
        print(str(traceback.format_exc()))
        time.sleep(60)
