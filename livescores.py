import requests, bs4
import notify2
import time
import threading

notify2.init("hello")

n = notify2.Notification(None)

n.set_timeout(1000)

def wc():

    res = requests.get("http://www.cricbuzz.com/live-cricket-scores/")
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    linkElems = soup.select('.cb-lv-scrs-col')
    match= str(linkElems[0].getText('span'))
    x=match.replace('span','')
    n.update(x)
    n.show()
    time.sleep(5)
    threading.Timer(5.0, wc).start()


wc()
