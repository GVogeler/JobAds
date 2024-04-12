# contains common imports and functions for download of ANNO newspapers

import re
from bs4 import BeautifulSoup as bs
import urllib
import requests
import os
import time
import tqdm

# gets soup from url
def get_html_page(url):
    output = urllib.request.urlopen(url).read()
    soup = bs(output, 'html.parser')
    return soup

# gets urls of all days of the actual year from its soup
def get_days_url(soup):
    days_urls = []
    for a in soup.find_all('a', href=True):
        if "datum=" in a["href"]:
            day_url = "https://anno.onb.ac.at" + a["href"]
            if "bl" not in day_url: 
                days_urls.append(day_url)
    return days_urls

# gets day of the week and month for the actual day
def get_date(soup, url):
    date = soup.find("span", {"class": "infotxt"}).getText()
    regex = re.match(".*datum=(\d{4})(\d{2}).*", url)
    day = date[:2]
    month = int(regex.group(2))
    return day, month    

# gets urls of every newspaper page of the actual day from its soup
def get_pages_urls(soup):
    pages_urls = []
    for a in soup.find_all('a', href=True):
        if "seite" in a["href"]:
            page_url = "https://anno.onb.ac.at" + a["href"]
            pages_urls.append(page_url)
    return pages_urls

# uses regex to change the ANNO corpus link to the IIIF link which offers images in better quality    
def generate_iiif_link(url):
    rex = re.match("(https:\/\/anno\.onb\.ac\.at\/cgi-content\/anno\?aid=)(\w{3})(\&datum=)(\d{4})(\d{2})(\d{2})(&seite=)(\d+)(&zoom=33)", url)
    page_number = "0"*(3-len(rex.group(8)))+rex.group(8)
    iiif_link = f"https://iiif-auth.onb.ac.at/images/ANNO/{rex.group(2)}{rex.group(4)}{rex.group(5)}{rex.group(6)}/00000{page_number}/full/full/0/default.jpg"
    name = f"{rex.group(2)}_{rex.group(4)}{rex.group(5)}{rex.group(6)}_{page_number}"
    return iiif_link, name

# in case the page is not accessible through the iiif link, we can use the image in original size from the anno webpage:
def generate_orig_size_link(url):
    rex = re.match("(https:\/\/anno\.onb\.ac\.at\/cgi-content\/anno\?aid=)(\w{3})(\&datum=)(\d{4})(\d{2})(\d{2})(&seite=)(\d+)(&zoom=33)", url)
    page_number = "0"*(3-len(rex.group(8)))+rex.group(8)
    orig_size_link = f"https://anno.onb.ac.at/cgi-content/annoshow?call={rex.group(2)}|{rex.group(4)}{rex.group(5)}{rex.group(6)}|{rex.group(8)}|100.0|0"
    name = f"{rex.group(2)}_{rex.group(4)}{rex.group(5)}{rex.group(6)}_{page_number}"
    return orig_size_link, name

# checks the answer of the server; if 200, thae it saves the image according to the given output path, 
# otherwise it waits 60 seconds and retries
# note: authentifaction is needed in this step
def save_img_from_web(iiif_link, USERNAME, PASSWORD, output_path_day, name, attempt=0):
    attempt+=1
    res = requests.get(iiif_link, auth=(USERNAME, PASSWORD))
    if res.status_code == 200:
        with open(f"{output_path_day}/{name}.jpg", 'wb') as f:
            f.write(res.content)
    else:
        print(f"********* a problem occured with {iiif_link} ***********")
        if attempt <= 5:
            time.sleep(60)
            save_img_from_web(iiif_link, USERNAME, PASSWORD, output_path_day, name, attempt)
        else:
            print(f"********* getting {iiif_link} unsuccesfull***********")
    time.sleep(0.5)

# checks wheter a directory with a given path exists; if not, then a directory is created
def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
