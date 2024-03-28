import requests
from bs4 import BeautifulSoup
import re
import time


response= requests.get(url="https://en.wikipedia.org/wiki/Lists_of_women")
print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find(id="firstHeading")
print(title.string)


#List of ALL LISTS OF WOMEN
timer1 = time.time()
allLinks = soup.find(id="mw-content-text").find_all('a')
#print(allLinks)
masterWomenList = []
#print(allLinks[5])
#Iterate each List of women
for womanList in allLinks:
    if womanList['href'].find("/wiki")==-1:
        continue
    if womanList.get('title') == "Women":
        continue
    #For every link collected, go to that page  
    #print(womanList.get('title'))
    newResponse= requests.get(url= "https://en.wikipedia.org" + womanList['href'])
    soup = BeautifulSoup(newResponse.content,'html.parser')
    
    womenLinks = soup.find_all("a")
    #Adds the title of every link to master list

    for a in womenLinks:
        
        woman = a.get('title')
        if(woman == "None"):
            continue
        if(woman is None):
            continue
        #blacklist=["List","Category","Template","Help","Special","Edit","Discuss","Recent","page","You"]
        blacklist=("(List|Category)|(Template|Help)|(Special|Edit)|(Discuss|Recent)|(page|Music)|(list|Articles)" 
            "|(Guides|Portal)|(in|Women)|(Female|women)|(Visit|How)|(Add|Wikipedia)|(ISBN|Books)|(and|art)|(et|Draft)|(User|Talk)"
            "|(by|wmf)|(Upload|ISSN)")
        if(re.search(blacklist, woman) ):
            continue
        if(woman.isascii()==-1):
            continue
        #print(woman)
        woman = woman.lower()
        masterWomenList.append(woman)
        #success

#CLI game for now
timer2=time.time()
print("Woman database complete")
elapsed = timer2-timer1
print("Time elapsed: ", elapsed)
womanCount = 0
guessed = []
confirm = input("Ready to begin? Press Enter")

clock1 = time.time()
while womanCount <100:
    guess = input(f"Woman Count:\n {womanCount}" )
    guess = guess.lower()

    #If correct and not in guessed list, increment womanCount
    if((guess in masterWomenList) and guess not in guessed):
        guessed.append(guess)
        womanCount += 1

clock2 = time.time()
score = clock2 - clock1
print("Congratulations, you have named 100 women.")
print(f'Time: {score}')

#print(masterWomenList)



