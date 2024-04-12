from download_library import *

######## SETTINGS #########
USERNAME = "uni-graz-job-ads"   # credentials to the OeNB IIIF - not to share with anybody not involved in the JobAds Project
PASSWORD = "Q4ZsP7CowOGKN9PgyeeD"
STARTING_YEAR = 1850    # first year of the newspaper we want to download
ENDING_YEAR = 1950      # last year of the newspaper we want to download
NEWSPAPER_TAG = "wrz"   # ANNO tag of the newspaper we want to download
output_path = f'C:/Users/venglaro/Desktop/preselected_pages/{NEWSPAPER_TAG}'   # path where the images should be stored

# applies functions and hand-crafted rules to exclude pages which probably don't contain job offers; 
# for an overview of the function, see download_library.py; for the pre-selection rules see the read-me
for year in range(STARTING_YEAR, ENDING_YEAR+1):
    print(f"*********************working on: {year}*********************")
    if year < 1941 or year > 1944: 
        path = f"{output_path}/{year}"
        create_dir(path)
        newspaper_url = f"https://anno.onb.ac.at/cgi-content/anno?aid={NEWSPAPER_TAG}&datum={year}&zoom=33"
        soup = get_html_page(newspaper_url)
        days_urls = get_days_url(soup)
        days_urls = [item for item in days_urls if "bl" not in item]
        for url in tqdm.tqdm(days_urls):
            soup = get_html_page(url)
            DAY, MONTH = get_date(soup, url)
            pages_urls = get_pages_urls(soup)

            if 1850 <= year < 1860:
                if DAY == "Mo":
                    target_pages = []
                else:
                    target_pages = pages_urls[14:]
            elif (1860 <= year < 1865) or (year == 1865 and MONTH <= 10):
                if DAY == "Mo":
                    target_pages = []
                target_pages = pages_urls[9:]
            elif (year == 1865 and MONTH >= 11) or (1865 < year < 1890):
                target_pages = pages_urls[6:]
            elif 1890 <= year <= 1910:
                if DAY == "Mo":
                    target_pages = []
                elif DAY == "So":
                    target_pages = pages_urls[12:]
                    target_pages.extend(pages_urls[-5:])
                    target_pages = list(set(target_pages))  
                else: 
                    target_pages = pages_urls[14:]
                    target_pages.extend(pages_urls[-5:])
                    target_pages = list(set(target_pages))  
            elif 1911 <= year <= 1932:
                if DAY == "Mo":
                    target_pages = []
                else:
                    target_pages = pages_urls[8:]
            elif 1933 <= year <= 1940:
                if DAY == "Mo":
                    target_pages = pages_urls[5:]
                else:
                    target_pages = pages_urls[8:]
            # ****** 1941-end 1945 no issues *******
            elif 1945 <= year <= 1946:
                target_pages = pages_urls[2:]
            elif 1947 <= year <= 1950:
                target_pages = pages_urls[-3:]
            else:
                print(f"***** no rule applicable to {url} ********")

            if len(target_pages) > 0:    
                for page in target_pages:
                    iiif_link, name = generate_iiif_link(page)
                    output_path_day = f"{output_path}/{year}/{name[:-4]}"
                    create_dir(output_path_day)
                    save_img_from_web(iiif_link, USERNAME, PASSWORD, output_path_day, name)