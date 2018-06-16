import requests, time, threading
from win10toast import ToastNotifier
import bs4


def liveCricket():

    res = requests.get("http://www.cricbuzz.com/live-cricket-scores/")
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    linkElems = soup.select(' .cb-lv-scrs-col')
    match = str(linkElems[0].getText('span'))
    x = match.replace('span','')
    toaster = ToastNotifier()
    toaster.show_toast(x, duration = 5)
    time.sleep(5)
    threading.Timer(5.0, liveCricket).start()


liveCricket()