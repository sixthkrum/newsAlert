import os
import shutil
import sys
import time
import requests
from bs4 import BeautifulSoup

reported = []

def news():
    links_list = []
    matches = []

    try:
        page = requests.get( "http://ndtv.com/delhi-news" )
        soup_page = BeautifulSoup( page.content , 'html.parser' )

        for item in soup_page.find_all( 'a' , href = True ):
            links_list.append( item[ 'href' ] )

        matches = [ item for item in links_list if "delhi-news" in item and not "delhi-news/page-" in item ]
        matches = list( dict.fromkeys( matches ) )
        matches = list( set( matches ) - set( reported ) )

        reported.extend( matches )

        if len( matches ) > 0:
            print("updated")
            content = open( "temp.txt" , "a" )
            content.write( "\nNews alert\n" )

            for item in matches:
                page = requests.get( item )
                soup_page = BeautifulSoup( page.content , 'html.parser' )

                lines = soup_page.find_all('p')
                del lines[-4:]

                article = ""
                for item1 in lines:
                    article += item1.get_text() + '\n'

                content.write("\nreport:\n" + article)

            if os.path.exists( "/home/user/prog/newsAlert/ndtv_delhi-news.txt" ):
                os.remove( "/home/user/prog/newsAlert/ndtv_delhi-news.txt" )

            content.close()
            shutil.copy( "/home/user/prog/newsAlert/temp.txt" , "/home/user/prog/newsAlert/ndtv_delhi-news.txt" )

    except:
        pass

    return True

while True:
    news()
    #instant updates
