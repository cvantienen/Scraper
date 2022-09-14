# Cody Vantienen

# importing modules 

from tracemalloc import start
from turtle import done, end_fill
import requests
import bs4
import lxml
from xlsxwriter import Workbook
import re



# ny times

nyTimes = "https://www.nytimes.com/" 
result = requests.get(nyTimes)
soup = bs4.BeautifulSoup(result.text,'html.parser')
soup.prettify()

article = soup.find_all("section" ,class_="story-wrapper")
storys = []
    
for story in article:
    cleantext = story.text.strip()
    storys.append(cleantext)
    done
 
 
    
# Guardian


theGuardian = "https://www.theguardian.com/us" 
gresult = requests.get(theGuardian)
gsoup = bs4.BeautifulSoup(gresult.text,'html.parser')
gsoup.prettify()

guardianArticle = gsoup.find_all('a', class_="u-faux-block-link__overlay js-headline-text")
guardianStorys = []
    
for guardianStory in guardianArticle:
    cleantext = guardianStory.text.strip()
    guardianStorys.append(cleantext)
    done
    
   
   
    
# ap news
# 
apnews = "https://www.apnews.com/" 
aresult = requests.get(apnews)
wsoup = bs4.BeautifulSoup(aresult.text,'html.parser')
wsoup.prettify()

aarticle = wsoup.find_all("h2")
aaarticle = wsoup.find_all("h4")
astorys = []
    
for astory in aarticle:
    cleantext = astory.text.strip()
    astorys.append(cleantext)
    done

for aastory in aaarticle:
    wcleantext = aastory.text.strip()
    astorys.append(wcleantext)
    done
    
    
# the washington post 
reuters = "https://www.washingtonpost.com/" 
rresult = requests.get(reuters)
rsoup = bs4.BeautifulSoup(rresult.text,'html.parser')
rsoup.prettify()

rArticle = rsoup.find_all('span')
rStorys = []
    
for rStory in rArticle:
    cleantext = rStory.text.strip()
    rStorys.append(cleantext)
    done


# foxnews 
fox = "https://www.foxnews.com/" 
fresult = requests.get(fox)
fsoup = bs4.BeautifulSoup(fresult.text,'html.parser')
fsoup.prettify()

fArticle = fsoup.find_all('a')
fStorys = []
    
for fStory in fArticle:
    cleantext = fStory.text.strip()
    fStorys.append(cleantext)
    done
    

# nbc
# <a href="https://www.nbcnews.com/news/world/ukraine-volodymyr-zelenskyy-izyum-rcna47634" class="related-content__headline-link">Russia launches cruise missiles at Ukraine after Zelenskyy visits recently retaken city</a>
nbc = "https://www.nbcnews.com/" 
nresult = requests.get(nbc)
nsoup = bs4.BeautifulSoup(nresult.text,'html.parser')
nsoup.prettify()

nArticle = nsoup.find_all('a')
nStorys = []
    
for nStory in nArticle:
    cleantext = nStory.text.strip()
    nStorys.append(cleantext)
    done


# abc
# <a href="https://www.nbcnews.com/news/world/ukraine-volodymyr-zelenskyy-izyum-rcna47634" class="related-content__headline-link">Russia launches cruise missiles at Ukraine after Zelenskyy visits recently retaken city</a>
abc = "https://abcnews.go.com/" 
abcresult = requests.get(abc)
abcsoup = bs4.BeautifulSoup(abcresult.text,'html.parser')
abcsoup.prettify()

abcArticle = abcsoup.find_all('span')
abcStorys = []
    
for abcStory in abcArticle:
    cleantext = abcStory.text.strip()
    abcStorys.append(cleantext)
    done
    
    
# npr
# <a href="https://www.npr.org/2022/09/14/1122958027/amazon-union-election-vote-albany" data-metrics="{&quot;action&quot;:&quot;Click Story Title&quot;,&quot;category&quot;:&quot;Story List&quot;}">Amazon warehouse workers in Albany will vote on unionization in October</a>
npr = "https://www.npr.org/" 
nprresult = requests.get(npr)
nprsoup = bs4.BeautifulSoup(nprresult.text,'html.parser')
nprsoup.prettify()

nprArticle = nprsoup.find_all('a')
nprStorys = []
    
for nprStory in nprArticle:
    cleantext = nprStory.text.strip()
    nprStorys.append(cleantext)
    done
    
    
    
#cbs
#<span <p class="item__dek">

usnews = "https://www.cbsnews.com/" 
usresult = requests.get(usnews)
ussoup = bs4.BeautifulSoup(usresult.text,'html.parser')
ussoup.prettify()

usArticle = ussoup.find_all('p', class_='item__dek')
cbsStorys = []
    
for usStory in usArticle:
    cleantext = usStory.text.strip()
    cbsStorys.append(cleantext)
    done
    
    
    
#pbs
#<span>

pbsnews = "https://www.pbs.org/newshour/" 
pbsresult = requests.get(pbsnews)
pbssoup = bs4.BeautifulSoup(pbsresult.text,'html.parser')
pbssoup.prettify()

pbsArticle = pbssoup.find_all('span')
pbsStorys = []
    
for pbsStory in pbsArticle:
    cleantext = pbsStory.text.strip()
    pbsStorys.append(cleantext)
    done

    

#print(storys)
#print()
#print(guardianStorys)
#print()
#print(astorys)
#print()
#print(rStorys)
#print(fStorys)
#print(nStorys)
#print(abcStorys)
#print(nprStorys)
#print(cbsStorys)
print(pbsStorys)




#workbook = Workbook('my_file.xlsx')
#Report_Sheet = workbook.add_worksheet()
#
## Write the column headers if required.
#Report_Sheet.write(0, 0, 'Move Name')
#Report_Sheet.write(0, 1, 'Startup Frames')
#Report_Sheet.write(0, 2, 'Landing Lag')
#
## Write the column data.
#Report_Sheet.write_column(1, 0, moveName)
#Report_Sheet.write_column(1, 1, moveStartUp)
#Report_Sheet.write_column(1, 2, landingLag)
#workbook.close()

#all_move_data = zip(moveName, #moveStartUp, totalFrames, landingLag)
#
#
#with open('my_file.csv', 'w') as #my_file:
#    for (moveName, moveStartUp, #totalFrames, landingLag) in #all_move_data:
#        my_file.write("{0},{1}\n".format#(moveName, moveStartUp, #totalFrames, landingLag))
#print('File created')
#
