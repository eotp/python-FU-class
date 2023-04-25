def text_extraction(link):
    # access the website
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    # extract the html blocks
    commentary_div = soup.find_all('div', {"id": re.compile(r'vv_textfield_[0-9]*_commentary')})
    if len(commentary_div ) > 0:
        opened_info = commentary_div[0].find_all('div', {'class': 'opened_info'})[0]
        # extract the text data
        txt = opened_info.text
        return txt
    else:
        return ''