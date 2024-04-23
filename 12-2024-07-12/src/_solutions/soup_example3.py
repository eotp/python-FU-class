tags = soup.find_all('div',{'class': 'card'})
for tag in tags:
    print(tag.h5.text)
    print(tag.a.text)