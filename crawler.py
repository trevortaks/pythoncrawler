import urllib2
from bs4 import BeautifulSoup
import sqlite3
#import os

home = ['http://localhost/myweb/Programming-TutorialsPoint/www.tutorialspoint.com/',]
other = []


class spider():
	def __init__(url):
		data = urllib2.urlopen(url)
		soup = BeautifulSoup(data)


	def getImage(url):
		#Trevor put some code here
		pass

	def getVideo(url):
		#Trevor put some code here
		pass

	def getUrl(url):
		print 'hakuna  mtata'
		print url
		outfile = open('new.txt','a+')
		try:
			
			for link in soup.find_all('a'):
				href = link.get('href')
				if href == None:
					continue
				else:
					if href.find('http')==False:
						continue
					else:
						href = url + href
					if any(href == s for s in other):
						continue
					else:
						other.append(href)
						outfile.write(href + '\n')
						#print href
		except urllib2.URLError, e:
			print'Could not open url(',url,'):',e

		outfile.close()

	def dbConnect():
		db = sqlite3.connect()
		db.execute('DROP table IF exists urls')
		db.execute('CREATE table urls (title text,url string')

	def sliceUrl(url):
		st = url
		while(st[-1]!='/'):
			st = st[:-1]
		return st


def main():
	pass	


if __name__ =='__main__':
	main()