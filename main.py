import requests, os
from dotenv import load_dotenv

load_dotenv()

class Youtuber:
    def __init__(self, time, cat, api):
        self.apikey = api
        self.time = time
        self.cat = cat
        self.search()

    def display(self, search):
        for i in search['items']:
            print('---------------------------------------------')
            print("Title:",i['snippet']['title'])
            print("Views:",i['statistics']['viewCount'])
            print("Favorited:",i['statistics']['favoriteCount'])

    def search(self):
        url = f'https://www.googleapis.com/youtube/v3/videos?&key={self.apikey}&part=snippet,contentDetails,statistics&chart=mostPopular&publishedAfter={self.time}T00%3A00%3A00Z{self.cat}'
        search = requests.get(url).json()

        self.display(search)



def ques2(time):
    print('1) Top Rated\n2) Top Favorited\n3) Most Viewed\n4) Most Recent\n')
    choise = input('Please select a feed (or "q" to quit): ')
    feed_arr = ("", "&order=rating", "", "&order=viewCount", "&order=date")

    while True:
        if choise in ['1','2','3','4']:
            cat = feed_arr[int(choise)]
            break
        elif choise == 'q':
            exit()
        else:
            print("Bad choise")
            continue

    youtuber = Youtuber(time, cat, os.getenv('apikey'))    

def ques1():
    print('\n1) today\n2) this week\n3) this month\n4) since youtube started\n')
    choise = input('Please select a time(or "q" to quit): ')
    time_arr = ("", "2019-05-03", "2019-04-26", "2019-04-03", "2000-01-01")

    while True:
        if choise in ['1','2','3','4']:
            ques2(time_arr[int(choise)])
        elif choise == 'q':
            exit()
        else:
            print("Bad choise")
            continue

ques1()


