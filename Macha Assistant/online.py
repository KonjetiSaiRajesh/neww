import requests
import wikipedia
import pywhatkit as kit

def find_my_ip():
    ip_address = requests.get('https://api.ipify.org?format=json').json()
    return ip_address['ip']

def search_on_wikipedia(queri):
    results = wikipedia.summary(queri, sentences=2 )
    return results

def search_on_google(queri):
    kit.search(queri)

def youtube(video):
    kit.playonyt(video)