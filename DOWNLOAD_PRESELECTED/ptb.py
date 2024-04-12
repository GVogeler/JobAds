from download_library import *
import math

######## SETTINGS #########
USERNAME = "uni-graz-job-ads"   # credentials to the OeNB IIIF - not to share with anybody not involved in the JobAds Project
PASSWORD = "Q4ZsP7CowOGKN9PgyeeD"
STARTING_YEAR = 1877    # first year of the newspaper we want to download
ENDING_YEAR = 1938      # last year of the newspaper we want to download
NEWSPAPER_TAG = "ptb"   # ANNO tag of the newspaper we want to download
output_path = f'C:/Users/venglaro/Desktop/preselected_pages/{NEWSPAPER_TAG}'  # path where the images should be stored
similar_days = ["Di", "Mi", "Do", "Fr"]

# applies functions and hand-crafted rules to exclude pages which probably don't contain job offers; 
# for an overview of the function, see download_library.py; for the pre-selection rules the read-me
for year in range(STARTING_YEAR, ENDING_YEAR+1):
    print(f"*********************working on: {year}*********************")
    if year != 1935:
        path = f"{output_path}/{year}"

        create_dir(path)
        newspaper_url = f"https://anno.onb.ac.at/cgi-content/anno?aid={NEWSPAPER_TAG}&datum={year}&zoom=33"
        soup = get_html_page(newspaper_url)
        days_urls = get_days_url(soup)
        for url in tqdm.tqdm(days_urls):
            soup = get_html_page(url)
            DAY, MONTH = get_date(soup, url)
            pages_urls = get_pages_urls(soup)

            if MONTH == 12:
                target_pages = pages_urls[1:]

            elif DAY == "Mo":
                if year == 1877:
                    target_pages = pages_urls[-1:]
                elif (1878 <= year < 1900) or (year == 1900 and MONTH < 10):
                    target_pages = pages_urls[-(math.ceil(len(pages_urls)/2)):]
                elif year == 1900 and MONTH >= 10:
                    target_pages = pages_urls[math.floor((len(pages_urls)-4)/2):-4]
                elif 1901 <= year < 1914:
                    target_pages = pages_urls[4:]
                elif year == 1914 and MONTH <= 2:
                    target_pages = pages_urls[-2:]
                elif 1914 <= year < 1916:
                    target_pages = pages_urls[2:]
                elif 1916 <= year < 1918:
                    target_pages = pages_urls[3:]
                elif 1918 <= year < 1919:
                    target_pages = pages_urls[-1:]
                elif 1919 <= year <= 1938:
                    target_pages = pages_urls[11:]
            elif DAY in similar_days:
                if year < 1881:
                    target_pages = pages_urls[-(math.ceil(len(pages_urls)/3)):]
                elif 1881 <= year < 1900:
                    target_pages = pages_urls[-(math.ceil(len(pages_urls)/2)):]
                elif year == 1900 and MONTH < 10:
                    target_pages = pages_urls[12:28]
                elif year == 1900 and MONTH >= 10:
                    target_pages = pages_urls[math.floor((len(pages_urls))*(2/5))-1:]
                elif 1901 <= year < 1910:
                    if DAY == "Fr":
                        target_pages = pages_urls[8:]
                    else:
                        target_pages = pages_urls[12:]
                elif 1910 <= year < 1936:
                    target_pages = pages_urls[6:]
                elif 1936 <= year <= 1938:
                    target_pages = pages_urls[-4:]
            elif DAY == "Sa":
                if year < 1900:
                    target_pages = pages_urls[-(math.ceil(len(pages_urls)/2)):]
                elif year == 1900 and MONTH < 10:
                    target_pages = pages_urls[12:28]
                elif year == 1900 and MONTH >= 10:
                    target_pages = pages_urls[math.floor((len(pages_urls))*(2/5))-1:]
                elif 1901 <= year < 1910:
                    target_pages = pages_urls[11:]       
                elif year >= 1910:
                    target_pages = pages_urls[6:]
            elif DAY == "So":
                if year < 1881:
                    target_pages = pages_urls[-(math.ceil(len(pages_urls)/2)):]    
                elif 1881 <= year < 1900:
                    target_pages = pages_urls[math.floor((len(pages_urls))/3)-1:]
                elif 1900 <= year < 1936:
                    target_pages = pages_urls[11:]        
                elif 1936 <= year <= 1938:
                    target_pages = pages_urls[4:]   

            else:
                print(f"***** no rule applicable to {url} ********")
                
            for page in target_pages:
                iiif_link, name = generate_iiif_link(page)
                output_path_day = f"{output_path}/{year}/{name[:-4]}"
                create_dir(output_path_day)
                save_img_from_web(iiif_link, USERNAME, PASSWORD, output_path_day, name)