# We are looking for the classes named 'course_link' and 'course_name'
course_links_obj = soup.find_all('span', {"class": 'course_link'})
course_names_obj = soup.find_all('span', {"class": 'course_name'})

# get the internet links
course_links = [url+item.find('a').get('href') for item in course_links_obj]
# get the name of the course 
course_names = [item.text for item in course_names_obj]

# build the data frame
df = pd.DataFrame(zip(course_names, course_links), columns=['course_names', 'course_links'])

print(f'There are {df.shape[0]} courses available.')
