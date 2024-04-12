from download_library import *
import math

######## SETTINGS #########
USERNAME = "uni-graz-job-ads"   # credentials to the OeNB IIIF - not to share with anybody not involved in the JobAds Project
PASSWORD = "Q4ZsP7CowOGKN9PgyeeD"
STARTING_YEAR = 1893    # first year of the newspaper we want to download
ENDING_YEAR = 1939      # last year of the newspaper we want to download
NEWSPAPER_TAG = "nwj"   # ANNO tag of the newspaper we want to download
output_path = f'C:/Users/venglaro/Desktop/preselected_pages/{NEWSPAPER_TAG}'   # path where the images should be stored

# applies functions and hand-crafted rules to exclude pages which probably don't contain job offers; 
# for an overview of the function, see download_library.py; for the pre-selection rules see the read-me
for year in range(STARTING_YEAR, ENDING_YEAR+1):
    print(f"*********************working on: {year}*********************")
    path = f"{output_path}/{year}"
    create_dir(path)
    newspaper_url = f"https://anno.onb.ac.at/cgi-content/anno?aid={NEWSPAPER_TAG}&datum={year}&zoom=33"
    soup = get_html_page(newspaper_url)
    days_urls = get_days_url(soup)
    for url in tqdm.tqdm(days_urls):
        soup = get_html_page(url)
        DAY, MONTH = get_date(soup, url)
        pages_urls = get_pages_urls(soup)

        if year < 1895:
            if DAY == "So":
                target_pages = pages_urls[-2:]
            else: 
                target_pages = pages_urls[-1:]
        elif (1895 <= year < 1897) or (year == 1897 and MONTH < 11):
            if DAY == "Mo":
                target_pages = pages_urls[3:]
            else: 
                target_pages = pages_urls[-3:]
        elif (year == 1897 and MONTH >= 11) or 1898 <= year < 1900:
            if DAY == "So" and len(pages_urls) >= 24:
                target_pages = pages_urls[-(math.ceil(len(pages_urls)/2)):]
            elif DAY == "Mo":
                target_pages = pages_urls[3:]
            else:
                target_pages = pages_urls[6:16]
        elif (1900 <= year <= 1913) or (year == 1914 and MONTH < 9):
            if DAY == "So":
                target_pages = pages_urls[-(math.ceil(len(pages_urls)/2)):]
            elif len(pages_urls) >= 20:
                target_pages = pages_urls[-3:]
            else: 
                target_pages = pages_urls[-2:]
        elif (1914 <= year < 1921) or (year == 1921 and MONTH < 11):
            if DAY == "So":
                target_pages = pages_urls[-6:]
            elif DAY == "Mo":
                target_pages = pages_urls[-1:]
            else:
                target_pages = pages_urls[-6:-4]
        elif year == 1921 and MONTH >= 10:
            if DAY == "So":
                target_pages = pages_urls[-6:]
            elif DAY == "Mo":
                target_pages = pages_urls[-1:]
            else:
                target_pages = pages_urls[-6:]
        elif year >= 1922:
            if DAY == "So":
                target_pages = pages_urls[-5:]
            elif DAY == "Mo":
                target_pages = pages_urls[-1:]
            else:
                target_pages = pages_urls[-2:]            
        else:
            print(f"***** no rule applicable to {url} ********")

        if len(target_pages) > 0:    
            for page in target_pages:
                iiif_link, name = generate_iiif_link(page)
                output_path_day = f"{output_path}/{year}/{name[:-4]}"
                create_dir(output_path_day)
                save_img_from_web(iiif_link, USERNAME, PASSWORD, output_path_day, name)
