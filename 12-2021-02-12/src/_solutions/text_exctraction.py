def text_extraction(link):
    # access the website
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    # extract the html blocks
    info_obj = soup.find_all('div', {"class": 'opened_info'})
    # extract the text data
    txt = [obj.text for obj in info_obj]
    return txt
