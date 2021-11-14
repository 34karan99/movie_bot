import pandas as pd
import numpy as np
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import MessageEntity
import logging

movies=pd.read_csv("All_Streaming_Shows.csv")
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

a=-1
high_R_movie=list()
for i in movies["IMDB Rating"]:
    a=a+1
    if i>=float(9.2):
        high_R_movie.append(movies["Series Title"][a])


b=-1
drama_show=list()
Action_show=list()
Comedy_show=list()
Adventure_show=list()
History_show=list()
Romance_show=list()
Fantasy_show=list()
Crime_show=list()
Science_show=list()
Horror_show=list()

for i in movies["Genre"]:
    b=b+1
    if "Drama" in i and movies['IMDB Rating'][b]> float(8.5):
        drama_show.append(movies["Series Title"][b])
    if "Comedy" in i and movies['IMDB Rating'][b]> float(8.5):
        Comedy_show.append(movies["Series Title"][b])
    if "Action" in i and movies['IMDB Rating'][b]> float(8.5):
        Action_show.append(movies["Series Title"][b])
    if "Adventure" in i and movies['IMDB Rating'][b]> float(8.5):
        Adventure_show.append(movies["Series Title"][b])
    if "History" in i and movies['IMDB Rating'][b]> float(8.5):
        History_show.append(movies["Series Title"][b])
    if "Romance" in i and movies['IMDB Rating'][b]> float(8.5):
        Romance_show.append(movies["Series Title"][b])
    if "Fantasy" in i and movies['IMDB Rating'][b]> float(8.5):
        Fantasy_show.append(movies["Series Title"][b])
    if "Crime" in i and movies['IMDB Rating'][b]> float(8.5):
        Crime_show.append(movies["Series Title"][b])
    if "Science" in i and movies['IMDB Rating'][b]> float(8):
        Science_show.append(movies["Series Title"][b])
    if "Horror" in i and movies['IMDB Rating'][b]> float(7):
        Horror_show.append(movies["Series Title"][b])



f=-1
ninteen_show=list()
seventeen_show=list()
fifteen_show=list()
ten_show=list()
old_show=list()
for i in movies['Year Released']:
    f=f+1
    if (i==2019 or 2018) and movies['IMDB Rating'][f]> float(8.5):
        ninteen_show.append(movies['Series Title'][f])
    if (i==2017 or 2016) and movies['IMDB Rating'][f]> float(8.5):
        seventeen_show.append(movies['Series Title'][f])
    if (i==2015 or 2014) and movies['IMDB Rating'][f]> float(8.5):
        fifteen_show.append(movies['Series Title'][f])
    if (2010<i<2014) and movies['IMDB Rating'][f]> float(8.5):
        ten_show.append(movies['Series Title'][f])
    if (i<2010) and movies['IMDB Rating'][f]> float(8.5):
        old_show.append(movies['Series Title'][f])

def start(update, context):
	context.bot.sendMessage(chat_id=update.effective_chat.id, text="hello, {name} ,i am a Movie Recommendation Bot.\n I only recommend movies which are rated 8 or higher on IMDB \n type '/1' for continue".format(name=update.effective_user.full_name))
	print(update)

def zero(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Choose a category \n 1'/Genre_based' \n 2'/based_on_ReleasedYear' \n 3'/Highest_rated_shows_onIMDB'")

def genre(update, context):
	context.bot.sendMessage(chat_id=update.effective_chat.id, text="What do you wanna watch ? \n 1 '/Highest_rated_shows_onIMDB' \n 2 '/Comedy'\n3 '/Drama'\n4 '/Action' \n5 '/Adventure' \n6 '/History' \n7 '/Romance' \n8 '/Fantasy' \n9 '/Crime' \n10 '/Science' \n11 '/Horror'")

def year(update, context):
	context.bot.sendMessage(chat_id=update.effective_chat.id, text=" \n 1 '/2018and2019' \n 2 '/2016and2017'\n3 '/2014and2015' \n4 '/2010to2014' \n'/Old_Movies'")

	

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="  ? i didn't get it sorry")
    print(update)


def high_r(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= high_R_movie)

def drama(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= drama_show)

def Comedy(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= Comedy_show)

def Action(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= Action_show)

def Adventure(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= Adventure_show)

def History(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= History_show)

def Romance(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= Romance_show)

def Fantasy(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= Fantasy_show)

def Crime(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= Crime_show)

def Science(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= Science_show)

def Horror(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= Horror_show)

def ninteen(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= ninteen_show[0:20])

def seventeen(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= seventeen_show[0:20])

def fifteen(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= fifteen_show[0:20])

def ten(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= ten_show[0:20])

def old(update, context):
 	context.bot.sendMessage(chat_id=update.effective_chat.id, text= old_show)

updater = Updater(token='2134576991:AAER763Ru7WWPYHWVxoFZd50O2uOHczfV0I', use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start",start))
dispatcher.add_handler(CommandHandler("1",zero))
dispatcher.add_handler(CommandHandler("based_on_ReleasedYear",year))
dispatcher.add_handler(CommandHandler("Highest_rated_shows_onIMDB",high_r))
dispatcher.add_handler(CommandHandler("Genre_based",genre))
dispatcher.add_handler(CommandHandler("Comedy",Comedy))
dispatcher.add_handler(CommandHandler("drama",drama))
dispatcher.add_handler(CommandHandler("Action",Action))
dispatcher.add_handler(CommandHandler("Adventure",Adventure))
dispatcher.add_handler(CommandHandler("History",History))
dispatcher.add_handler(CommandHandler("Romance",Romance))
dispatcher.add_handler(CommandHandler("Fantasy",Fantasy))
dispatcher.add_handler(CommandHandler("Crime",Crime))
dispatcher.add_handler(CommandHandler("Science",Science))
dispatcher.add_handler(CommandHandler("Horror",Horror))
dispatcher.add_handler(CommandHandler("Old_Movies",old))
dispatcher.add_handler(CommandHandler("2018and2019",ninteen))
dispatcher.add_handler(CommandHandler("2016and2017",seventeen))
dispatcher.add_handler(CommandHandler("2014and2015",fifteen))
dispatcher.add_handler(CommandHandler("2010to2014",ten))


dispatcher.add_handler(MessageHandler(Filters.text |Filters.video | Filters.photo & (~Filters.command), echo))



updater.start_polling()
updater.idle()
