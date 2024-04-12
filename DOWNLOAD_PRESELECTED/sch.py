from download_library import *

######## SETTINGS #########
USERNAME = "uni-graz-job-ads"   # credentials to the OeNB IIIF - not to share with anybody not involved in the JobAds Project
PASSWORD = "Q4ZsP7CowOGKN9PgyeeD"
STARTING_YEAR = 1865    # first year of the newspaper we want to download
ENDING_YEAR = 1938      # last year of the newspaper we want to download
NEWSPAPER_TAG = "sch"   # ANNO tag of the newspaper we want to download
output_path = f'C:/Users/venglaro/Desktop/preselected_pages/{NEWSPAPER_TAG}'   # path where the images should be stored
no_issue_years = [1890]

# applies functions and hand-crafted rules to exclude pages which probably don't contain job offers; 
# for an overview of the function, see download_library.py; for the pre-selection rules see the read-me
for year in range(STARTING_YEAR, ENDING_YEAR+1):
    if year not in no_issue_years:
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

            if year < 1867:
                target_pages = pages_urls[5:8]
            elif year == 1867 or year == 1868:
                if DAY == "Fr":
                    target_pages = pages_urls[3:]
                else:
                    target_pages = []
            elif 1869 <= year < 1873:
                target_pages = pages_urls[2:]
            elif 1873 <= year < 1882:
                target_pages = pages_urls[1:]
            elif 1882 <= year < 1891:
                if DAY == "Do" or DAY == "So":
                    target_pages = pages_urls
                else:
                    target_pages = []
            elif year == 1891:
                if DAY == "Do" or DAY == "Sa":
                    target_pages = pages_urls[1:]
                else: 
                    target_pages = pages_urls[-1:]
            elif 1892 <= year < 1901:
                target_pages = pages_urls[3:]
            elif 1901 <= year < 1907:
                target_pages = pages_urls[2:]
            elif 1907 <= year < 1910:
                if DAY == "Sa":
                    target_pages = pages_urls[5:]
                elif DAY == "Do":
                    target_pages = pages_urls[-5:]
                    target_pages.extend(pages_urls[4:7])
                    target_pages = list(set(target_pages))
                else:
                    target_pages = pages_urls[-5:]
            elif 1910 <= year < 1912:
                if DAY == "Sa":
                    target_pages = pages_urls[5:]
                else:
                    target_pages = pages_urls[-5:]      
            elif (year == 1912) or (year == 1913 and MONTH < 3):
                if DAY == "Sa":
                    target_pages = pages_urls[7:]
                else:
                    target_pages = pages_urls[-4:]      
            elif 1913 <= year < 1919:
                if DAY == "So":
                    target_pages = pages_urls[7:]
                else:
                    target_pages = pages_urls[-4:]
            elif (1919 <= year < 1929) or (year == 1929 and MONTH < 6):
                if DAY == "So":
                    if len(pages_urls) <= 10:
                        target_pages = pages_urls[-2:]
                    elif len(pages_urls) > 10:
                        target_pages = pages_urls[-4:-2]
                else: 
                    target_pages = pages_urls[-2:]
            elif 1929 <= year < 1939:
                if DAY == "Sa":
                    target_pages = pages_urls[-5:]
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
    else:
        print(f"---------------- no issues in {year} ------------------------")
