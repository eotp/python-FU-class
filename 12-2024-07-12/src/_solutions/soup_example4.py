all_divs = soup.find_all('div',{'class': 'card-body'})
for divs in all_divs:
    print(divs.find('a').get('href'))