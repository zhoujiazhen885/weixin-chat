from wxpy import *

api_key = "8ee4adc708234b60a7816e5b4c42f2d6"
bot = Bot()
tuling = Tuling(api_key=api_key)

my_group = ensure_one(bot.groups().search("肥肠团"))
my_friend = ensure_one(bot.friends().search("Tang J."))

@bot.register(my_group)
def auto_replay_group(msg):
    tuling.do_reply(msg)

@bot.register(my_friend)
def auto_replay_person(msg):
    tuling.do_reply(msg)

bot.join()





