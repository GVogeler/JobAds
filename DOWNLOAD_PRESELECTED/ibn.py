from download_library import *

######## SETTINGS #########
USERNAME = "uni-graz-job-ads"   # credentials to the OeNB IIIF - not to share with anybody not involved in the JobAds Project
PASSWORD = "Q4ZsP7CowOGKN9PgyeeD"
STARTING_YEAR = 1854    # first year of the newspaper we want to download
ENDING_YEAR = 1945      # last year of the newspaper we want to download
NEWSPAPER_TAG = "ibn"   # ANNO tag of the newspaper we want to download
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

        if year < 1864:
            wanted_days = ["Di", "Do", "Sa"]
            if DAY in wanted_days:
                target_pages = pages_urls[3:]
            else:
                target_pages = []
        elif 1864 <= year < 1874:
            target_pages = pages_urls[3:]
        elif 1874 <= year < 1884:
            target_pages = pages_urls[4:]
        elif 1884 <= year < 1897:
            target_pages = pages_urls[5:]
        elif 1897 <= year < 1904:
            target_pages = pages_urls[4:]
        elif 1904 <= year < 1914:
            target_pages = pages_urls[5:]
        elif 1914 <= year < 1917:
            if DAY == "So":
                target_pages = []
            else:
                target_pages = pages_urls[7:]
        elif 1917 <= year < 1924:
            if DAY == "So":
                target_pages = pages_urls[2:]
            else:
                target_pages = pages_urls[4:]          
        elif 1924 <= year < 1934:
            target_pages = pages_urls[6:]
        elif 1934 <= year < 1940:
            if DAY == "Sa":
                target_pages = pages_urls[-3:]
            else:
                target_pages = pages_urls[-2:]
        elif 1940 <= year < 1944:
            target_pages = pages_urls[3:]
        elif year >= 1944:
            if DAY == "Sa":
                target_pages = pages_urls[5:]
            else:
                target_pages = pages_urls[3:]

        else:
            print(f"***** no rule applicable to {url} ********")

        if len(target_pages) > 0:    
            for page in target_pages:
                iiif_link, name = generate_iiif_link(page)
                output_path_day = f"{output_path}/{year}/{name[:-4]}"
                create_dir(output_path_day)
                save_img_from_web(iiif_link, USERNAME, PASSWORD, output_path_day, name)