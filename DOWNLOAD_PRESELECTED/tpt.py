from download_library import *
import math

######## SETTINGS #########
USERNAME = "uni-graz-job-ads"   # credentials to the OeNB IIIF - not to share with anybody not involved in the JobAds Project
PASSWORD = "Q4ZsP7CowOGKN9PgyeeD"
STARTING_YEAR = 1865    # first year of the newspaper we want to download
ENDING_YEAR = 1944      # last year of the newspaper we want to download
NEWSPAPER_TAG = "tpt"   # ANNO tag of the newspaper we want to download
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

        if (1865 <= year <= 1867) or (year == 1868 and MONTH < 7):
            if DAY in WEEKEND:
                target_pages = pages_urls[-1:]
            else: target_pages = []
        elif (year == 1868 and MONTH >= 7) or (year == 1869):
            target_pages = pages_urls[3:]
        elif 1870 <= year < 1889:
            if DAY not in WEEKEND:
                target_pages = pages_urls[-2:]
            else:
                target_pages = pages_urls[math.floor(len(pages_urls)/2):]
        elif 1889 <= year < 1905:
            target_pages = pages_urls[5:]
        elif (1905 <= year <= 1924) or (year == 1925 and MONTH <= 8):
            target_pages = pages_urls[7:]
        elif (year == 1925 and MONTH >= 9) or (year == 1926):
            if DAY != "So":
                target_pages = pages_urls[7:-2]
            else:
                target_pages = pages_urls[7:]
        elif 1927 <= year < 1930:
            if DAY != "So":
                target_pages = pages_urls[7:-3]
            else:
                target_pages = pages_urls[7:]
        elif (1930 <= year < 1933) or (year == 1933 and MONTH < 7):
            if DAY not in WEEKEND:
                target_pages = pages_urls[6:-4]
            elif DAY == "Sa":
                target_pages = pages_urls[8:-4]
        elif (year == 1933 and MONTH >= 7) or (1934 <= year < 1936):
            if DAY not in WEEKEND:
                target_pages = pages_urls[6:-4]
            elif DAY == "Sa":
                target_pages = pages_urls[8:]       
        elif (1936 <= year < 1939) or (year == 1939 and MONTH < 9):
            if DAY not in WEEKEND:
                target_pages = pages_urls[4:-4]
            elif DAY == "Sa":
                target_pages = pages_urls[8:]
        elif (year == 1939 and MONTH >= 9):
            target_pages = pages_urls[-math.ceil(len(pages_urls)/3):]
        elif (year == 1940) or (year == 1941 and MONTH < 11):
            target_pages = pages_urls[5:]
        elif (year == 1941 and MONTH >= 11) or (year >= 1942):
            target_pages = pages_urls[3:]
        else:
            print(f"***** no rule applicable to {url} ********")

        if len(target_pages) > 0:    
            for page in target_pages:
                iiif_link, name = generate_iiif_link(page)
                output_path_day = f"{output_path}/{year}/{name[:-4]}"
                create_dir(output_path_day)
                save_img_from_web(iiif_link, USERNAME, PASSWORD, output_path_day, name)