newsAlert uses IRC to report news updates from ndtv.com/delhi-news to a channel on freenode

news.py is the hexchat script that sends the messages to the channel

tearer.py scrapes ndtv.com/delhi-news constantly and whenever it finds an article that it hasn't reported yet it adds it to a file that news.py reads and sends to the irc channel

tearer.py parses the article and removes ndtv's headers and footers on the article

Add news.py to the addons in hexchat and run tearer.py from the terminal

Update file paths in the scripts (use absolute paths) to run it on your machine
