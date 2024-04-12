from download_library import *
import math

######## SETTINGS #########
USERNAME = "uni-graz-job-ads"   # credentials to the OeNB IIIF - not to share with anybody not involved in the JobAds Project
PASSWORD = "Q4ZsP7CowOGKN9PgyeeD"
STARTING_YEAR = 1891    # first year of the newspaper we want to download
ENDING_YEAR = 1934      # last year of the newspaper we want to download
NEWSPAPER_TAG = "gtb"   # ANNO tag of the newspaper we want to download
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

        if DAY == "Mo":
            if year < 1900:
                if MONTH == 12:
                    target_pages = pages_urls[-4:]
                else:
                    target_pages = pages_urls[-3:]
            elif year == 1900:
                target_pages = pages_urls[-3:]
                target_pages.extend(pages_urls[-9:-6])
            elif 1901 <= year <= 1916:
                target_pages = pages_urls[-3:]
            elif year >= 1917:
                target_pages = pages_urls[-1:]
        elif DAY == "Di":
            if year <= 1903:
                target_pages = pages_urls[-2:]
                target_pages.extend(pages_urls[math.floor((len(pages_urls)-4)/2)-2:-4])
            elif year == 1904 or year == 1905:
                target_pages = pages_urls[9:16]
                target_pages.extend(pages_urls[20:])
            elif year == 1906 or year == 1907:
                target_pages = pages_urls[6:22]
            elif 1908 <= year <= 1914:
                target_pages = pages_urls[3:20]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif year == 1915:
                target_pages = pages_urls[7:11]
            elif 1916 <= year <= 1921:
                target_pages = pages_urls[2:9]
            elif year == 1922 or year == 1923:
                target_pages = pages_urls[6:8]
                target_pages.extend(pages_urls[10:12])
            elif year == 1924:
                if len(pages_urls) == 10:
                    target_pages = pages_urls[6:8]
                elif len(pages_urls) == 16:
                    target_pages = pages_urls[10:12]
                else:
                    target_pages = pages_urls[6:]
            elif year == 1925 or year == 1926:
                target_pages = pages_urls[7:12]
            elif 1927 <= year <= 1929:
                target_pages = pages_urls[6:14]
            elif year == 1930:
                target_pages = pages_urls[8:10]
                target_pages.extend(pages_urls[16:18])
            elif 1931 <= year <= 1934:
                target_pages = pages_urls[6:10]
        elif DAY == "Mi":
            if year == 1891:
                target_pages = [pages_urls[-5]]
            elif year == 1892:
                target_pages = pages_urls[math.floor(len(pages_urls)/2)-1:]
            elif year == 1893 or year == 1894:
                target_pages = pages_urls[6:]
            elif year == 1895:
                target_pages = [pages_urls[-5], pages_urls[-1]]
            elif 1896 <= year <= 1903:
                target_pages = pages_urls[7:18]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1904 <= year <= 1909:
                target_pages = pages_urls[7:20]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1910 <= year <= 1914:
                target_pages = pages_urls[3:17]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1915 <= year <= 1917:
                target_pages = pages_urls[3:11]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif year == 1918:
                target_pages = pages_urls[3:15]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1919 <= year <= 1922:
                target_pages = pages_urls[2:11]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1923 <= year <= 1924:
                target_pages = pages_urls[6:12]
            elif 1925 <= year <= 1930:
                target_pages = pages_urls[7:16]
            elif 1931 <= year <= 1934:
                target_pages = pages_urls[6:10]            
        elif DAY == "Do":
            if year == 1891:
                target_pages = pages_urls[-5:-4]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1892 <= year <= 1896:
                target_pages = pages_urls[7:19]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1897 <= year <= 1900:
                target_pages = pages_urls[6:26]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1901 <= year <= 1903:
                target_pages = pages_urls[7:16]
            elif 1904 <= year <= 1909:
                target_pages = pages_urls[7:]
            elif 1910 <= year <= 1915:
                target_pages = pages_urls[3:22]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1916 <= year <= 1920:
                target_pages = pages_urls[2:11]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif year == 1921 or year == 1924 or year == 1929:
                target_pages = pages_urls[6:13]
            elif year == 1922 or year == 1923:
                target_pages = pages_urls[4:10]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1925 <= year <= 1928:
                target_pages = pages_urls[8:16]
                target_pages.extend(pages_urls[20:22])
            elif 1930 <= year <= 1934:
                target_pages = pages_urls[6:11]
        elif DAY == "Fr":
            if 1891 <= year <= 1894:
                target_pages = pages_urls[6:16]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif year == 1895:
                target_pages = pages_urls[3:14]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1896 <= year <= 1909:
                target_pages = pages_urls[7:18]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1910 <= year <= 1914:
                target_pages = pages_urls[4:17]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1915 <= year <= 1919:
                target_pages = pages_urls[3:11]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1920 <= year <= 1924:
                target_pages = pages_urls[6:11]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1925 <= year <= 1930:
                target_pages = pages_urls[8:15]
            elif 1931 <= year <= 1934:
                target_pages = pages_urls[6:10]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            if len(pages_urls) >= 30:
                target_pages.extend(pages_urls[19:])
                target_pages = list(set(target_pages))
        elif DAY == "Sa":
            if year <= 1892:
                target_pages = [pages_urls[-5], pages_urls[-1]]
            elif 1893 <= year <= 1896:
                target_pages = pages_urls[6:16]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1897 <= year <= 1900:
                target_pages = pages_urls[5:24]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))
            elif 1901 <= year <= 1907:
                target_pages = pages_urls[4:19]
            elif 1908 <= year <= 1910:
                target_pages = pages_urls[6:]
            elif 1911 <= year <= 1913:
                target_pages = pages_urls[3:19]
                target_pages.extend(pages_urls[-3:])
                target_pages = list(set(target_pages))
            elif 1914 <= year <= 1918:
                target_pages = pages_urls[2:13]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))    
            elif year == 1919:
                target_pages = pages_urls[1:8]
            elif 1920 <= year <= 1924:
                target_pages = pages_urls[6:11]
                target_pages.extend(pages_urls[-1:])
                target_pages = list(set(target_pages))  
            elif 1925 <= year <= 1929:
                target_pages = pages_urls[5:16]
                target_pages.extend(pages_urls[-2:])
                target_pages = list(set(target_pages)) 
            elif 1930 <= year <= 1934:
                target_pages = pages_urls[6:11]  
                target_pages.extend(pages_urls[-3:])
                target_pages = list(set(target_pages))                
        elif DAY == "So":
            target_pages = pages_urls[3:]
        else:
            print(f"***** no rule applicable to {url} ********")
            
        for page in target_pages:
            iiif_link, name = generate_iiif_link(page)
            output_path_day = f"{output_path}/{year}/{name[:-4]}"
            create_dir(output_path_day)
            save_img_from_web(iiif_link, USERNAME, PASSWORD, output_path_day, name)
