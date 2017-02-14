#proj2.py


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here

import requests
from bs4 import BeautifulSoup
import urllib

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,'html.parser')

for story_heading in soup.find_all(class_="story-heading")[:10]:
    if story_heading.a:

        print(story_heading.a.text.replace("\n", " ").strip())
    else:

        print(story_heading.contents[0].strip())
#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
url = 'https://www.michigandaily.com/'
g = requests.get(url)
soup1 = BeautifulSoup(g.text, 'html.parser')

#print (soup1)
new = soup1.find_all(class_ = 'view view-most-read view-id-most_read view-display-id-panel_pane_1 view-dom-id-99658157999dd0ac5aa62c2b284dd266')
for item in new:
    print (item.get_text())


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
kitty_url = 'http://newmantaylor.com/gallery.html'
kitty = requests.get(kitty_url)
kitty_soup = BeautifulSoup(kitty.text, 'html.parser')

for image in kitty_soup.findAll("img"):
    try:
        print (image['alt'])
    except:
        print ('No alternate text provided')



#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
count = 0
umsi_url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
u = requests.get(umsi_url)
umsi = BeautifulSoup (u.text, 'html.parser')
items = umsi.find_all(class_ = 'ds-1col node node-person node-teaser view-mode-teaser clearfix')
#print (items)
tags = umsi.find_all('a')
#print (tags)
for item in tags:
    print (item.get('href'))
