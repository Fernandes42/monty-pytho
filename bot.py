import os
import praw

# Removed credentials for obvious reasons  
reddit = praw.Reddit(client_id='-',
                     client_secret='-',
                     password='-',
                     user_agent='testscript by /u/spanishinquisitionbt',
                     username='spanishinquisitionbt')

subreddit = reddit.subreddit("MontyPythonMemes")
for submission in subreddit.hot(limit=5):
    for top_level_comment in submission.comments:
        if "spanish inquisition" in top_level_comment.body.lower():
            top_level_comment.reply("Behind the coal shed?")
