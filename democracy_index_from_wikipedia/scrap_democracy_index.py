# coding: utf-8

#
# Make sure BeautifulSoup is installed, eg:
# pip install beautifulsoup4
#
from bs4 import BeautifulSoup
import csv

input_file = "./democracy_index_2016.html"
myfile = open(input_file, 'r')
current_html = myfile.read()
soup = BeautifulSoup(current_html, 'html.parser')

table = soup.find("table", {"class": "wikitable sortable"})

output_csv = open('democracy_index_2016.csv', 'wb')
csv_writer = csv.writer(output_csv)

csv_writer.writerow(["position", "country_name", "flag_uri", "score",
                     "electoral_process_and_pluralism","functioning_of_government",
                     "political_participation", "political_culture",
                     "civil_liberties", "category"])

# count = 0
for row in table.findAll("tr"):
    cells = row.findAll("td")
#     print(cells)
    if len(cells) > 0:
        country_position = cells[0].string
	country_name = cells[1].find('a').string
#         print(country_name)
        country_flag_uri = cells[1].find('span').find('img')['src']
#         print(country_flag_uri)
        country_score = cells[2].string
#         print(country_score)
        electoral_process_and_pluralism_score = cells[3].string
#         print(electoral_process_and_pluralism_score)
        functioning_of_government_score = cells[4].string
#         print(functioning_of_government_score)
        political_participation_score = cells[5].string
#         print(political_participation_score)
        political_culture_score = cells[6].string
#         print(political_culture_score)
        civil_liberties_score = cells[7].string
#         print(civil_liberties_score)
        country_category = cells[8].string
#         print(country_category)

        csv_writer.writerow([
            country_position,
            country_name,
            country_flag_uri,
            country_score,
            electoral_process_and_pluralism_score,
            functioning_of_government_score,
            political_participation_score,
            political_culture_score,
            civil_liberties_score,
            country_category])
#     count += 1;
#     if count == 2:
#         break

output_csv.close()
