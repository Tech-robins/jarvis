import os
from GoogleImageScrapper.GoogleImageScrapper import GoogleImageScraper

def GoogleImage():
    oo = open('P:\\AI Asisstant\\Data.txt','rt')
    query = str(oo.read())
    oo.close() 
    pppp = open('P:\\AI Asisstant\\Data.txt','r+')
    pppp.truncate(0)
    pppp.close()

    webdriver = "P:\\AI Asisstant\\Database\\webdriver\\chromedriver.exe"
    photos = "P:\\AI Asisstant\\Database\\googlephotos\\"

    search_keys = query
    number = 10
    head = False
    max = (1000, 1000)
    min = (0,0)

    for search_key  in search_keys:
        image_search = GoogleImageScraper(webdriver,photos,search_keys,number,head,min,max)
        image_url = image_search.find_image_urls()
        image_search.save_images(image_url)
    os.startfile(photos)        
  
GoogleImage()