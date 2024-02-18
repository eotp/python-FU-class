tags = soup.find_all('h5')
for tag in tags:
    print(tag.text)