import hexchat
import sys
import time
import os

__module_name__ = "news"
__module_version__ = "0.1"
__module_description__ = "news"

def news( userdata ):

    try:
        if os.path.exists("/home/user/prog/newsAlert/ndtv_delhi-news.txt"):
            alert = open( "/home/user/prog/newsAlert/ndtv_delhi-news.txt" , "r" )
            message = alert.read()
            alert.close()

            channel = hexchat.find_context( channel = "##mynameisonpc" )
            channel.set()

            for ele in str.splitlines(message):
                channel.command( "say " + ele )

            os.remove( "/home/user/prog/newsAlert/ndtv_delhi-news.txt" )
            os.remove( "/home/user/prog/newsAlert/temp.txt")


    except:
        pass

    return True

hexchat.hook_timer( 10 , news ) #updated every 10 milliseconds
