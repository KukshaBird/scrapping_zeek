from bs4 import BeautifulSoup
import csv
import requests
#Get zheky diraction
page = requests.get("https://kiev.vgorode.ua/reference/zheky/")
soup = BeautifulSoup(page.text, 'html.parser')
pages = soup.find(class_='list')
#Extract list of links
lis = pages.find_all('li')
#Create .csv file
f = csv.writer(open('ЖЭК инфо.csv', 'w'), delimiter=';')
f.writerow(['Город', 'Район', 'Адрес', 'Телефон'])

for item in range(len(lis)):
	#Draw single url
    url = lis[item].a['href'].split(',')[-2][1:-1]
    info = requests.get(url)
    local_soup = BeautifulSoup(info.text, 'html.parser')
    block = local_soup.find(class_='cast')
    data = block.find_all(class_='col-sm-8')
    try:
        f.writerow([data[0].get_text(), data[2].get_text(), data[1].get_text()[1:-1], data[3].get_text()])
    except:
        f.writerow([data[0].get_text(), data[1].get_text()[1:-1]])
        print(item+1, "is not OK")
        continue
    print(item+1, 'ROW DONE!')    