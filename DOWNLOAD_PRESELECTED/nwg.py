from download_library import *

######## SETTINGS #########
USERNAME = "uni-graz-job-ads"   # credentials to the OeNB IIIF - not to share with anybody not involved in the JobAds Project
PASSWORD = "Q4ZsP7CowOGKN9PgyeeD"
STARTING_YEAR = 1867    # first year of the newspaper we want to download
ENDING_YEAR = 1945      # last year of the newspaper we want to download
NEWSPAPER_TAG = "nwg"   # ANNO tag of the newspaper we want to download
output_path = f'C:/Users/venglaro/Desktop/preselected_pages/{NEWSPAPER_TAG}'   # path where the images should be stored
no_issue_year = list(range(1879,1883))

# applies functions and hand-crafted rules to exclude pages which probably don't contain job offers; 
# for an overview of the function, see download_library.py; for the pre-selection rules see the read-me
for year in range(STARTING_YEAR, ENDING_YEAR+1):
    if year not in no_issue_year:
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

            if year == 1867:
                target_pages = pages_urls[-2:]
                if DAY == "So":
                     target_pages.extend(pages_urls[6:8])
            elif 1868 <= year <= 1870:
                 target_pages = pages_urls[5:8]
                 target_pages.extend(pages_urls[-1:])
                 if len(pages_urls) > 17:
                      target_pages.extend(pages_urls[-3:-2])
            elif year >= 1871:
                if len(pages_urls) <= 6:
                    target_pages = pages_urls[-1:]
                else:
                    target_pages = pages_urls[5:]
            else:
                print(f"***** no rule applicable to {url} ********")

            if len(target_pages) > 0:    
                for page in target_pages:
                    iiif_link, name = generate_iiif_link(page)
                    output_path_day = f"{output_path}/{year}/{name[:-4]}"
                    create_dir(output_path_day)
                    save_img_from_web(iiif_link, USERNAME, PASSWORD, output_path_day, name)