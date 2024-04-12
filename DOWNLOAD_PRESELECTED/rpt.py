from download_library import *

######## SETTINGS #########
USERNAME = "uni-graz-job-ads"   # credentials to the OeNB IIIF - not to share with anybody not involved in the JobAds Project
PASSWORD = "Q4ZsP7CowOGKN9PgyeeD"
STARTING_YEAR = 1910    # first year of the newspaper we want to download
ENDING_YEAR = 1915      # last year of the newspaper we want to download
NEWSPAPER_TAG = "rpt"   # ANNO tag of the newspaper we want to download
output_path = f'C:/Users/klara/Desktop/preselected_pages/{NEWSPAPER_TAG}'   # path where the images should be stored

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

        if len(pages_urls) >= 50:
            target_pages = pages_urls[20:]
        elif len(pages_urls) <= 4:
            target_pages = pages_urls[-2:]
        elif MONTH == 12 or DAY == "So":
            target_pages = pages_urls[6:]
        elif year < 1907:
            if len(pages_urls) >= 8:
                target_pages = [pages_urls[6], pages_urls[7], pages_urls[-1]]
                target_pages = list(set(target_pages))
            else: 
                target_pages = pages_urls[-1:]
        elif year == 1907:
            target_pages = []
            target_pages.append(pages_urls[7])
            target_pages.extend(pages_urls[-4:])
            target_pages = list(set(target_pages))
        elif 1908 <= year <= 1910:
            target_pages = pages_urls[-4:]
        elif 1911 <= year <= 1918:
            if DAY == "Mo":
                target_pages = pages_urls[-4:]
            else:
                target_pages = pages_urls[len(pages_urls)-10:len(pages_urls)-4]
        elif year == 1919 and MONTH <= 4:
            target_pages = pages_urls[len(pages_urls)-6:len(pages_urls)-4]
        elif year >= 1919:
            target_pages = pages_urls[-2:]
        else:
            print(f"***** no rule applicable to {url} ********")
            
        for page in target_pages:
            iiif_link, name = generate_iiif_link(page)
            output_path_day = f"{output_path}/{year}/{name[:-4]}"
            create_dir(output_path_day)
            save_img_from_web(iiif_link, USERNAME, PASSWORD, output_path_day, name)
