from download_library import *
import math

######## SETTINGS #########
USERNAME = "uni-graz-job-ads"   # credentials to the OeNB IIIF - not to share with anybody not involved in the JobAds Project
PASSWORD = "Q4ZsP7CowOGKN9PgyeeD"
STARTING_YEAR = 1864    # first year of the newspaper we want to download
ENDING_YEAR = 1939      # last year of the newspaper we want to download
NEWSPAPER_TAG = "nfp"   # ANNO tag of the newspaper we want to download
output_path = f'C:/Users/venglaro/Desktop/preselected_pages/{NEWSPAPER_TAG}'   # path where the images should be stored
WEEKEND = ["Sa", "So"]

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

        if year <= 1868:
            if DAY == "Mo":
                target_pages = pages_urls[3:]
            else:
                target_pages = pages_urls[5:]
        elif 1869 <= year <= 1873:
            if DAY == "Mo":
                target_pages = pages_urls[3:]
            else:
                target_pages = pages_urls[13:16]
        elif 1874 <= year < 1880:
            if DAY == "Mo":
                target_pages = pages_urls[3:]
            else:
                target_pages = pages_urls[9:16]
        elif 1880 <= year < 1890:
            if DAY == "Mo":
                if len(pages_urls) == 12:
                    target_pages = pages_urls[4:8]
                else:
                    target_pages = pages_urls[-2:]
            elif DAY == "So":
                target_pages = pages_urls[11:]
            else:
                if len(pages_urls) <= 12:
                    target_pages = pages_urls[6:]
                else:
                    target_pages = pages_urls[11:-4]
        elif 1890 <= year < 1900:
            if DAY == "Mo":
                target_pages = pages_urls[-2:]
            elif DAY == "So":
                target_pages = pages_urls[15:]
            else:
                target_pages = pages_urls[13:-4]
                target_pages.extend(pages_urls[-1:])
        elif 1900 <= year <= 1939:
            if DAY == "Mo":
                target_pages = pages_urls[-1:]
            elif len(pages_urls) <= 20:
                target_pages = pages_urls[-4:]
            elif DAY == "So":
                target_pages = pages_urls[17:]
            else:
                target_pages = pages_urls[15:-2]
        else:
            print(f"***** no rule applicable to {url} ********")

        if len(target_pages) > 0:    
            for page in target_pages:
                iiif_link, name = generate_iiif_link(page)
                output_path_day = f"{output_path}/{year}/{name[:-4]}"
                create_dir(output_path_day)
                save_img_from_web(iiif_link, USERNAME, PASSWORD, output_path_day, name)