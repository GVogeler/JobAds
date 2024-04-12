Code and documentation of preselected pages from the ANNO corpus via the IIIF access.
The pages were pre-selected by manually searching for some general patterns in every newspaper separetely. The full table is available on the JobAds Project Google Drive: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=0. The downloaded data is available on the Uni-Graz Cloud: https://cloud.uni-graz.at/s/PFfxma38yKf2KM6.

Note: The code contains credentials to the OeNB API which should not be shared with anybody not involved in the project.

# Documentation of which pages were preselected
Note: The rules apply in the presented order with according priority. If one rule applies, no other rule is applied anymore, unless specified otherwise.
Note 2: If one page should selected more times (e.g., we select pages 7-8 and the last page, and the page 8 is also the last page), it is ensured that the page is selected only once.
Note 3: In case the result of division is not an integer (e.g., when selecting the second half of the issue), the number is always rounded up or down to include also the page in question.

## APR (Die Presse)
1) Before December 1852: Select the last page.
2) Dec 1852-1862 (including): Select all pages from the page 8 on.
3) 1863-1879 (including): Select all pages from the page 5 on.
4) 1880-Jan 1896 (including): Select pages 8, 12, 16, and the last page.
5) In 1896: Select pages 8, 10, and the last page.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=223393421

## AWI (Arbeiterwille)
1) Before 1898: Select pages 4, 6, 7, and 8.
2) 1989-1900 (including): Select all pages from the page 8 on.
3) From 1901: For Sundays, select all pages from the page 3 on. For all other days, select all pages from the page 2 on.

Note: No issues in 1895 and 1931-1945.
According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=2024003262

## AZE (Arbeiter-Zeitung)
1) In 1893: Select pages 7-8.
2) In 1894: Select last two pages.
3) 1895-1899 (included): Select the third page from the end, and also the last one.
4) From 1900 on: For Saturdays and Sundays, select the last two pages. For other days, select the last page.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=722243557

## BTB (Bregenzer Tagblatt/Vorarlberger Tagblatt)
1) If the issue has 2 pages: Select the second one.
2) If the issue has 4 pages: Select the last two pages.
If none of above mentioned applies:
3) Before 1900: For Saturdays, select last 3 pages. For all other days, select last 2 pages.
4) From 1900: For Saturdays, selest the second half of the issue. For all otherdays, select last 3 pages.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=1968717603

## DVB (Deutsches Volksblatt)
1) Ignore all Monday issues.
2) For Sundays: Until 1890, select all pages from the page 5 on. Between 1891-1914 (including), select the second half of the newspaper and also all pages from the page 16 on, if it was not included by the first rule. From 1915 on, select the last page.
3) If the issue is equal to or longer than 30 pages: Select all pages from the page 20 on.
4) In all other cases: Select the 9th page from the end, the 7th page from the end, the 5th page from the end and the last page.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=104705909

## FDB (Fremden-Blatt)
1) Before 1852: Select all pages from the page 3 on.
2) 1852-1876: Select all pages from the page 4 on.
3) In 1902: For Mondays, select all pages from 11 till the penultimate page. For other days, select all pages from 19 till the 4th page from the end (excluding).
4) 1913-1919: For Mondays, select all pages from the page 12 till the end, for other days select all pages from the page 20 till the end.

Note: No issues between 1877-1902 und 1903-1913.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=1685759620

## FST (Freie Stimmen)
1) In 1881: Select all pages from the page 4 on.
2) 1892-1898 (including): Select all pages from the page 5 on.
3) 1899-March 1908 (including): Select all pages from the page 6 on.
4) April 1908-1911 (including): For Saturdays, select all pages from the page 10 on. For other days, select pages from the page 6 on.
5) 1912-1914 (including): For Sundays, select all pages from the page 11 on. For Mondays which have only 4 pages, select the last page. For Mondays with different number of pages and any other day, select all pages from the page 6 on.
6) 1915-1917 (including): For Saturdays and Sundays, select all pages from the page 8 on. For other days, select all pages from the page 5 on.
7) 1918-September 1920 (including): For Sundays, select all pages from the page 5 on. For other days, select all pages from the page 3 on.
8) Oct 1920-Apr 1921 (including): For Saturdays, select all pages from the page 5 on. For other days, select all pages from the page 3 on.
9) May 1921-1925 (including): For Saturdays, select pages from the page 5 until the 5th page from the end (the last 4 pages is a Beilage without ads). For other days, select all pages form the page 3 on.
10) 1926-1930 (including): For Sundays, select the pages from the page 7 until the 5th page from the end. For other days: If the issues has 4 pages, select the last one. If the number of pages is different, select all  pages from the page 5 on.
11) From 1931 on: Select all pages from the page 7 on.

According notes from the process of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=1417552135

## GRE (Grazer Volksblatt)
1) Before 1880: Select all pages from the page 3 on.
2) 1880-1915 (included): Select all pages from the page 6 on.
3) 1916-1923 (included): For Sondays: select pages from the page 4 on. For other days: if the issue has 12 or 14 pages: select pages from the page 3 until the 4th page from the end (as the 4 last pages are an appendix without job ads). Otherwise: select all pages from the page 4 on.
4) From 1924 on: Select all pages from the page 4 on.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=1229189483

## GTB (Grazer Tagblatt)
a) If the day is MONDAY:
  1) Before 1900: If the month is December, select last 4 pages. For any other month, select last 3 pages.
  2) In 1900: Select last 3 pages and then last 3 pages before Abend-Ausgabe which is 6 pages long.
  3) 1901-1916 (including): select last 3 pages.
  4) From 1917 on: select the last page.
  
b) If the day is TUESDAY:
  1) Until 1903 (including): select last two pages; then consider the issue without Abend-Ausgabe which is 4 pages long, and select second half of it plus one page before.
  2) 1904 and 1905: Select pages 10-16 and all pages from page 19 on.
  3) 1906 and 1907: Select pages 7-22.
  4) 1908-1914 (including): Select pages 4-20 and the last page.
  5) In 1915: Select pages 8-11.
  6) 1916-1921 (including): Select pages 3-9.
  7) 1922 and 1923: Select pages 7-8 and 11-12.
  8) In 1924: If the issue has exactly 10 pages, select pages 7-8. If the issue has exactly 16 pages, select pages 11-12. If it has another lenght, select all pages from 7 on.
  9) 1925 and 1926: Select pages 8-12.
  10) 1927-1929 (including): Select pages 7-14.
  11) In 1930: Select pages 9-10 and 17-18.
  12) 1931-1934 (including): Select pages 7-10.

c) If the day is WEDNESDAY:
  1) In 1891: Select the 5th page from the end (= a page before Abend-Ausgabe).
  2) In 1892: Select all pages from the second half of the newspaper.
  3) 1893 and 1894: Select all pages from page 7 on.
  4) In 1895: Select the 5th page from the end and the last page.
  5) 1896-1903 (including): Select pages 8-18 and the last page.
  6) 1904-1909 (includong): Select pages 8-20 and the last page.
  7) 1910-1914 (including): Select pages 4-17 and the last page.
  8) 1915-1917 (including): Select pages 4-11 and the last page.
  9) In 1918: Select pages 4-15 and the last page.
  10) 1919-1922 (including): Select pages 3-11 and the last page.
  11) 1923 and 1924: Select pages 7-12.
  12) 1925-1930 (including): Select pages 8-16.
  13) 1931-1934 (including): Select pages 7-10.
  
 d) If the day is THURSDAY:
  1) In 1891: Select the 5th page from the end and the last page.
  2) 1892-1896 (including): Select pages 8-19 and the last page.
  3) 1897-1900 (including): Select pages 7-26 and the last page.
  4) 1901-1903 (including): Select pages 8-16.
  5) 1904-1909 (including): Select all pages from the page 7 on.
  6) 1910-1915 (including): Select pages 4-22 and the last page.
  7) 1916-1920 (including): Select pages 3-11 and the last page.
  8) For 1921, 1924 and 1929: Select pages 7-13.
  9) 1922-1923 (including): Select pages 5-10 and the last page.
  10) 1925-1928 (including): Select pages 9-16 and 21-22-
  11) 1930-1934 (including): Select pages 8-11.
 
 e) If the day is FRIDAY:
  1) 1891-1894 (including): Select pages 7-16 and the last page.
  2) In 1895: Select pages 4-14 and the last page.
  3) 1896-1909 (including): Select pages 8-18 and the last page.
  4) 1910-1914 (including): Select pages 5-17 and the last page.
  5) 1915-1919 (including): Select pages 4-11 and the last page.
  6) 1920-1924 (including): Select pages 7-11 and the last page.
  7) 1925-1930 (including): Select pages 9-15.
  8) 1931-1934 (including): Select pages 7-10 and the last page.
Additional rule applied to all Friday issues: If the issue has more than 30 pages, select also all pages from 20 on, in addition to other applied rules.
 
 f) If the day is SATURDAY:
  1) Until 1892 (including): Select the 5th page from the end and the last one.
  2) 1893-1896 (including): Select pages 7-16 and the last page.
  3) 1897-1900 (including): Select pages 6-24 and the last page.
  4) 1901-1907 (including): Select pages 5-19.
  5) 1908-1910 (including): Select all pages from page 7 on.
  6) 1911-1913 (including): Select pages 4-19 and the last three pages.
  7) 1914-1918 (including): Select pages 3-13 and the last page.
  8) In 1919: Select pages 2-8.
  9) 1920-1924 (including): Select pages 7-11 and the last page.
  10) 1925-1929 (including): Select pages 6-16 and the last page.
  11) 1930-1934 (including): Select pages 7-11 and the last three pages.
 
 g) If the day is SUNDAY: 
  1) For all Sundays: Select everything from page 4 on (as Sunday issues are extremely irregular).

According notes from the process of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=1353717428

## IBN (Innsbrucker Nachrichten)
1) Before 1864: For Tuesday, Thursday and Saturday, select pages from the page 4 on. Other days no job ads.
2) 1864-1873 (including): Select pages from the page 4 on (for all days of the week from now on).
3) 1874-1883 (including): Select pages from the page 5 on.
4) 1884-1896 (including): Select pages from the page 6 on.
5) 1897-1903 (including): Select pages from the page 5 on.
6) 1904-1913 (including): Select pages from the page 6 on.
7) 1914-1916 (including): For Sundays, do not select any pages (no job ads). For other days, select all pages from the page 8 on.
8) 1917-1923 (including): For Sundays, select pages from the page 3 on. For other days, select pages from the page 5 on.
9) 1924-1933 (including): Select pages from the page 7 on.
10) 1934-1939 (including): For Saturdays, select last three pages. For other days, select last two pages.
11) 1940-1943 (including): Select pages from the page 4 on.
12) From 1944: For Saturdays, select pages from the page 6 on. For other days, select pages from the page 4 on.
               
According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=2039328125

## KRZ (Illustrierte Kronen Zeitung)
1) Before 1919: Exclude the first page, keep everything else (job ads are in columns on the side on any page).
2) From 1919 on: Select the last third of the issue (new layout).

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=43024366

## LVB (Linzer Volksblatt)
1) Before 1872: Select the last page.
2) 1872-1933 (including): For Sundays, select all pages from the page 3 on. For all other days, select the last two pages.
3) 1934-1944 (including): Select all pages from the page 6 on.
4) From 1945 on: Select the last two pages.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=1842284931
Note: No issues in 1876, 1880, and 1939-1945.

## MOP (Morgen-Post)
1) Until the end of 1868: The issues usually have 4 pages. If there are 4 pages or less, select only the last page. If there are more pages, select everything from the 4th page on.
2) 1869-1883 (including): Select pages 7 and 8 (Kleiner Anzeiger on the page 8; exceptionally some ads on 7).
3) 1884: Select pages 7, 8, and the last two pages.
4) From 1885: Select last two pages.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=709714272

## NFP (Neue Freie Presse)
1) Before 1869: For Mondays, select pages from the page 4 on. For other days, select pages from the page 6 on.
2) 1869-1873 (including): For Mondays, select pages from the page 4 on. For other days, select pages 14-16.
3) 1874-1879 (including): For Mondays, select pages from the page 4 on. For other days, select pages 10-16.
4) 1880-1889 (including): For Mondays: If the issue has 12 pages, than take pages 5-8; otherwise select the last two pages. For Sundays, select everything from the page 12 on. For all other days: if the issue has 12 pages or less, select all pages from the page 7 on; otherwise select all pages from the page 12 until the 4th page from the end (the last four pages is Abendblatt).
5) 1890-1899 (including): For Mondays, select last two pages. For Sundays, select all pages from the page 16 on. For other days, select all pages from the page 14 until the 4th page from the end, plus include also the very last page.
6) 1900-1939 (including): For Mondays, select the last page. For other days: If the issue has less than 20 pages, then select the last four pages. Otherwise, if the day is Sonday, select all pages from the page 18 on. For other days, select all pages from the page 16 on, but without the last two pages.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=439480777

## NWB (Neuigkeits-Welt-Blatt)
1) If the issue has more than 19 pages: Select all pages from the page 5 on. Otherwise:
2) Before September 1902: Select all pages from the page 5 on.
3) From September 1902 on: Select the last page of the issue.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=1013766658

## NWG (Neues Wiener Tagblatt (Tagesausgabe))
1) 1867: Select 2 last pages. For Sunddays, add also pages 7 and 8.
2) 1868-1870 (included): Select pages 6-8 and the last page. If the issue is longer than 17 pages, than include also the 3rd page from the end.
3) From 1871: If the issue has less than 7 pages, take the last page. Otherwise, select all pages from the page 6 on.

Note: No issues between 1879-1882.
According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=859862047

## NWJ (Neues Wiener Journal: unparteiisches Tagblatt)
1) Before 1895: For Sondays, select the last two pages. For any other day, select the last page only.
2) 1895-October 1897 (including): For Mondays, select all pages from the page 4 on. For any other day, select the last three pages.
3) November 1897-1899 (including): For Mondays, select all pages from the page 4 on. For Sunday issues with more than 23 pages: Select the second half of te issue. For any other day and all Sunday issues shorter than 24 pages: Select pages 7-16.
4) 1900-August 1914 (including): For Sundays, select the second half of the issue. For other days: If the issue has at least 20 pages, select the last three pages. If they are shorter, select the last two pages.
5) September 1914-October 1921 (including): For Sundays, select the last 6 pages. For Mondays, select the last page. For other days, select pages from 6th from the end till the 4th from the end (i.e., exclude last 4 pages and select the two last before them).
6) November-December 1921: For Sundays, select the last 6 pages. For Mondays, select the last page. For other days, select last 6 pages.
7) From 1922 on: For Sundays, select the last 5 pages. For Mondays, select the last page. For other days, select the last 2 pages.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=2047364621

## PAB (Prager Abendblatt)
1) If the day of the week is Saturday: Exclude first third of the newspaper.
2) If it is a working day before 1888: Exclude first 2 pages.
3) If it is a working day from 1888 on: Select the second half of the newspaper.
4) If no rule applicable (e.g., occasional issues on Sundays): the program will notify you; check manually the specific page, if it contains job offers, select it manually as well.

Note: There are no issues on Sundays.
According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=388080852

## PEL (Pester Lloyd)
1) Before 1912: Select all pages from the page 4 on.
2) From 1912 on: Select all pages from the page 5 on.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=440051696
Note: No issues in 

## PIT (Pilsner Tagblatt)
1) Before 1923: second half of the newspaper.
2) From 1923 on: always the last page.

Note: 1919-1922: no issues at all. From half 1931: no issues on Mondays.
According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=1705783887

## PTB (Prager Tagblatt)
a) all DEZEMBERS: all pages except the first one.
b) MONDAYS:
  1) In 1877: Select the last page.
  2) 1878-September 1900 (including): Select the second half of the issue
  3) October and November 1900: Exclude the last four pages, select the second half of the resting pages.
  4) 1901-1913 (including): Exclude first four pages.
  5) January and February 1914: Select last two pages.
  6) March 1914-1915 (including): Exclude first two pages.
  7) 1916-1917 (including): Exclude first three pages.
  8) In 1918: Select the last page.
  9) From 1919 on: Select all pages from the page 12 on.

c) TUESDAYS, WEDNESDAYS, THURSDAYS, FRIDAYS:
  1) Before 1881: Select the last third of the issue.
  2) 1881-1899 (including): Select the second half of the newspaper.
  3) January-September 1900: Select pages 13-28.
  4) October and November 1900: Exclude first two fifths of the issue.
  5) 1901-1909 (including): For Fridays, select all pages from the page 9 on. For Tuesdays, Wednesdays and Thursdays, select all pages from the page 13 on.
  6) 1910-1935 (including): Select all pages from the page 7 on.
  7) From 1936 on: Select the last four pages.

d) SATURDAYS:
  1) Before 1900: Selecthe second half of the issue.
  2) January-September 1900: Select pages 13-28.
  3) October-November 1900: Exclude the first two fifths of the issue.
  4) 1901-1909 (including): Select all pages form the page 12 on.
  5) From 1910 on: Select all pages from the page 7 on.

e) SUNDAYS:
  1) Before 1881: Select the second half of the issue.
  2) 1881-1899: Exclude the first third of the issue.
  3) 1900-1935: Select all pages from the page 12 on.
  4) From 1936 on: Exclude first four pages.  

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=1130640601

## RPT (Reichspost)
1) Long editions are irregular. If the issue contains more than 50 pages, then select everything from the page 21 onwards.
2) If the issue consists only of 4 pages, then select the last two pages.
3) Issues in Decembers and on Sondays have irregular layout. Select everything from the page 7 onwards.
4) Before 1907: Select pages 7, 8, and the last page.
5) In 1907: Select page 8 and four last pages.
6) 1908-1910 (including): Select last 4 pages.
7) 1911-1918 (including): If the day of the week is Monday, then select last 4 pages (as there is no Nachmittagsausgabe).
                          Any other day: exclude the last 4 pages (Nachmittagsausgabe), from the rest select the last 6 pages.
8) In 1919 until the end of April: Exclude the last 4 pages (Mittagsblatt), from the rest select the last 2 pages.
9) From May 1919 until the end: Select the last two pages.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=1558287901

## SCH (Salzburger Chronik für Stadt und Land)
1) Before 1867: Select pages 6, 7, and 8.
2) 1867-1868: For Fridays, select all pages from the page 4 on. Ignore other days.
3) 1869-1872 (including): Select all pages from the page 3 on (for all days already).
4) 1873-1881 (including): Select all pages from the page 2 on.
5) 1882-1891 (including): For Thursdays and Sundays, select all pages. Ignore other days.
6) In 1891: For Thursdays and Saturdays, select all pages from the page 2. For other days, select the last page.
7) 1892-1900 (including): Select all pages from the page 4 on.
8) 1901-1906 (including): Select all pages from the page 3 on.
9) 1907-1909 (including): For Saturdays, select all pages from the page 6 on. For Thursdays, select the last pages and also pages 5-7 (if not included by the first rule). For other days, select tha last 5 pages.
10) 1910-1911 (including): For Saturdays, select all pages from the page 6 on. For all other days, select the last 5 pages.
11) 1912-Feb 1913 (including): For Saturdays, select all pages from the page 8 on. For all other days, select the last 4 pages.
12) Mar 1913-1918 (including): For Sundays, select all pages from the page 8 on. For all other days, select the last 4 pages.
13) 1919-Jun 1929: For Sundays, if the issue has 10 pages or less, select last 2 pages; if it is longer, exclude the last 2 pages (Beilage) and select the last 2 pages before the excluded ones. For all other days, select the last 2 pages.
14) From 1929: For Saturdays, select the last 5 pages. For all other days, select the last 2 pages.

Note: No issues in 1890.
According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=306586680

## SVB (Salzburger Volksblatt: die unabhängige Tageszeitung für Stadt und Land Salzburg)
1) 1871-1881 (including): Select all pages from the page 3 on.
2) 1882-November 1921 (including): Select all pages from the page 4 on.
3) December 1921-May 1933 (including): For Saturday, select all pages from the page 8 on. For working days, select last 2 pages.
4) June 1933-August 1939 (including): For Saturdays, select all pages from the page 18 on. For working days, select last 2 pages.
5) September 1939-1940 (including): For Saturdays, select all pages from the page 10 on. For working days, select all pages from the page 6 on.
6) From 1941 onwards: For Saturdays, select all pages from the page 6 on. For working days, select all pages from the page 4 on.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=1550166835

## TPT ((Linzer) Tages-Post)
1) 1865-June 1868 (including): Exclude all weekdays. From weekend days, select the lst page.
2) July 1868-1869 (including): Select all pages from the page 4 on.
3) 1870-1888 (including): For week days, select last two pages. For weekend days, select the second half of the issue.
4) 1889-1904 (including): Select all pages from the page 6 on.
5) 1905-August 1925 (including): Select all pages from the page 8 on.
6) September 1925-1926 (including): For Sundays, select all pages from the page 8 on. For all other days, select all pages from the page 8 until the second page from the end (excluding; the last 2 pages are appendix without ads).
7) 1927-1929 (including): For Sundays, select all pages from the page 8 on. For all other days, select all pages from the page 8 until the third page from the end (excluding).
8) 1930-June 1933 (including): For Saturdays, select all pages from the page 8 until the fourth page from the end (excluding). For all other days, select all pages from the page 6 until the fourth page from the end (excluding).
9) July 1933-1935 (including): For Saturdays, select all pages from the page 8 until the end. For all other days, select all pages from the page 6 until the fourth page from the end (excluding).
10) 1936-August 1939 (including): For Saturdays, select all pages from the page 8 until the end. For all other days, select all pages from the page 5 until the fourth page from the end (excluding).
11) September-December 1939 (including): Select the last third of the issue.
12) 1940-October 1941 (including): Select all pages from the page 6 on.
13) November 1941-1942 (including): Select all pages from the page 3 on.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=1235652705

## VLZ (Vorarlberger Landes-Zeitung)
1) If the issue has less than 4 pages, then select the last one.
2) If the issue has exactly 4 pages, then select the last two.
3) If the issue has more than 4 pages, then select all pages from the page 4 on.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=83295301

## VTL (Das Vaterland)
1) Before December 1866: Select all pages from the page 4 on.
2) December 1866-1879 (including): Ignore Mondays. For other days, select pages from the page 3 on.
3) 1880-1892 (including): For Mondays, select pages 3-4. For other days, select all pages from the page 6 on.
4) 1893-1907: For Mondays, select the last page. For Sondays, select all pages from the page 8 on. For other days, select pages from the page 6 till the 5th page from the end including (the last 4 pages is an appendix).
5) From 1908 on: For Mondays, select the last page. For Sondays, select all pages from the page 9 on. For other days, select pages from the page 8 till the 5th page from the end including (the last 4 pages is still the appendix).

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=200862772

## VVB (Vorarlberger Volks-Blatt)
1) 1866-1868 (including): Select pages from the page 3 onwards.
2) In 1869: Select pages from the page 4 onwards.
3) 1870-1886 (including): If the issue has 4 pages, then select pages 3 and 4. Otherwise, select last 3 pages.
4) 1887-1899 (including): If the issue has 4 pages, then select pages 3 and 4. Otherwise, select all pages from the page 5 on.
5) 1900-1918 (including): If the issue has 4 pages, then select pages 3 and 4. Otherwise, select all pages from the page 4 on.
6) 1918-1936: Select all pages from the page 3 on.
7) 1937-1938: Select all pages from the page 5 on.
8) 1946-1950 (including): Select all pages from the page 3 on.

Note: No issues between 1939-1945.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=303367050

## WRZ (Wiener Zeitung)
1) 1850-1859 (including): If the day is Monday, don't select any page (no job ads on Mondays); for all other days, select all pages from the page 15 on.
2) 1860-October 1865 (including): Select no pages for Mondays; for all other days select all pages from page 10 on.
3) November 1865-1889 (including): For all days, select all pages from the page 7 on.
4) 1890-1910 (including): Select no pages for Mondays; for Sundays select all pages from the page 13 on and the last 5 pages; for other days select all pages from the page 15 on and the last five pages.
5) 1911-1932 (including): Select no pages for Mondays; for all other days, select all pages from the page 9 on.
6) 1933-1940 (including): For Mondays, select all pages from the page 6 on; for other days, select all pages from the page 8 on.
7) 1945-1946 (including): For all days, select all pages from the page 3 on.
8) 1947-1950 (including): For all days, select last three pages.

Note: no issues in 1941-end 1945.

According notes from the proccess of the rules creation: https://docs.google.com/spreadsheets/d/1aNxN2O0FH36IX8WGCR2WMviyki6A-fcp2Ma4JynFX60/edit#gid=117236976
