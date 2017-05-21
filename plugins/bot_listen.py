from slackbot.bot import listen_to
import re

pastmsg = ''
pastmsg2 = ''

@listen_to(r'.+')
def savemsg(message):
    global pastmsg2
    global pastmsg
    pastmsg2 = pastmsg
    pastmsg = message.body['text']

@listen_to(r'^s/+\S+/+\S+/$')
def replace(message):
    before = re.findall(r'^s/(.*)/+\S+/', pastmsg)
    after = re.findall(r'^s/+\S+/(.*)/', pastmsg)
    if before[0] in pastmsg2:
        message.send('「' + pastmsg2.replace(before[0], after[0]) + '」って言いたかったんだね')
    else:
        message.send('前の文章に「' + before[0] + '」は入って無いよ？')
