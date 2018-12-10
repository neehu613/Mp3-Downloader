#Python 3

import re, webbrowser, os
from bs4 import BeautifulSoup
from urllib.request import urlopen
os.system("clear")
url = 'http://en.muzmo.ru/search?q='
song = input("Enter the song/artist name: ")
song = re.sub(' ', '+', song)
url += song
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")
allLinks = soup.find_all('a', class_='block')
songList = list()
songs = list()
songQuality = list()
songLinks = list()
num=1
for item in allLinks:
	link = item.get("href")
	checkIfSong = link[0:4]
	if checkIfSong == "/get":
		songList.append("http://en.muzmo.ru" + link)
		song = re.sub('  ', '', item.text)
		songs.append(str(num) + " " + song)
		num+=1
		
for song in songs:
	print (song)

choice = int(input("Enter your choice: "))
if choice > num or choice <= 0:
	print ("Invalid Choice")
else:
	print ("Song selected = " + str(songs[choice-1]))

url = str(songList[choice-1])
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")
allLinks = soup.find_all('a', class_='block')

num=1
for link in allLinks:
	song = link.get("href")
	songQ = song[0:20]
	if songQ == "http://muzmo.ru/get/":
		songQuality.append(str(num) + " " + str(link.text))
		songLinks.append(song)
		num += 1

for quality in songQuality:
	quality = re.sub("  ", "", quality)
	print (quality)

quality = int(input("Select the quality: "))
webbrowser.open_new(songLinks[quality-1])














'''
#For Python 2
import urllib2, re, webbrowser, os
from bs4 import BeautifulSoup

os.system("clear")
url = 'http://en.muzmo.ru/search?q='
song = raw_input("Enter the song/artist name: ")
song = re.sub(' ', '+', song)
url += song
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "lxml")
allLinks = soup.find_all('a', class_='block')
songList = list()
songs = list()
songQuality = list()
songLinks = list()
num=1
for item in allLinks:
	link = item.get("href")
	checkIfSong = link[0:4]
	if checkIfSong == "/get":
		songList.append("http://en.muzmo.ru" + link)
		song = re.sub('  ', '', item.text)
		songs.append(str(num) + " " + song)
		num+=1
		
for song in songs:
	print song

choice = int(input("Enter your choice: "))
if choice > num or choice <= 0:
	print "Invalid Choice"
else:
	print "Song selected = " + str(songs[choice-1])

url = str(songList[choice-1])
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "lxml")
allLinks = soup.find_all('a', class_='block')

num=1
for link in allLinks:
	song = link.get("href")
	songQ = song[0:20]
	if songQ == "http://muzmo.ru/get/":
		songQuality.append(str(num) + " " + str(link.text))
		songLinks.append(song)
		num += 1

for quality in songQuality:
	quality = re.sub("  ", "", quality)
	print quality

quality = int(input("Select the quality: "))
webbrowser.open_new(songLinks[quality-1])
'''
