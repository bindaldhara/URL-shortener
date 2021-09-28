import pyshorteners #library in python for shortening URL
def shorten_url(url):
    return pyshorteners.Shortener().tinyurl.short(url)

url = input("Enter URL: ") #takes input(URL) from the user
print("Shortened URL : ", shorten_url(url)) 