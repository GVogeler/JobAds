from download_library import *
import math

######## SETTINGS #########
USERNAME = "uni-graz-job-ads"   # credentials to the OeNB IIIF - not to share with anybody not involved in the JobAds Project
PASSWORD = "Q4ZsP7CowOGKN9PgyeeD"
STARTING_YEAR = 1867    # first year of the newspaper we want to download
ENDING_YEAR = 1918      # last year of the newspaper we want to download
NEWSPAPER_TAG = "pab"   # ANNO tag of the newspaper we want to download
output_path = f'C:/Users/klara/Desktop/preselected_pages/{NEWSPAPER_TAG}'   # path where the images should be stored
WORKING_DAYS = ["Mo", "Di", "Mi", "Do", "Fr"]

# applies functions and hand-crafted rules to exclude pages which probably don't contain job offers; 
# for an overview of the function, see download_library.py; for the pre-selection rules see according file
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

        if DAY == "Sa":
            target_pages = pages_urls[math.floor(len(pages_urls)/3):]
        elif DAY in WORKING_DAYS and year < 1888:
            target_pages = pages_urls[2:]
        elif DAY in WORKING_DAYS and year >= 1888:
            target_pages = pages_urls[math.floor(len(pages_urls)/2):]
        else:
            print(f"***** no rule applicable to {url} ********")
            
        for page in target_pages:
            iiif_link, name = generate_iiif_link(page)
            output_path_day = f"{output_path}/{year}/{name[:-4]}"
            create_dir(output_path_day)
            save_img_from_web(iiif_link, USERNAME, PASSWORD, output_path_day, name)