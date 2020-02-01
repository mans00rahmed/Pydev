import urllib.request

def shorten_url(url):

    api_url = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(api_url+url).read()
    return tinyurl.decode("utf-8")

url= input('enter url to be short')
print(shorten_url(url))