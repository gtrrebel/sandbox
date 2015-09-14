import urllib2, re, os, math, time
from lxml import html
import requests

url1 = 'http://wiki.helsinki.fi/display/mathstatKurssit/Fourier+analysis%2C+fall+2015'
url2 = 'https://wiki.helsinki.fi/display/mathstatKurssit/Kompleksianalyysi+I%2C+syksy+2015'
url3 = 'https://wiki.helsinki.fi/display/mathstatKurssit/Real+analysis+II%2C+fall+2015'

tag_parse = {}
teaching = ['Teaching:', 'Teaching:', 'Opetus:', 'Teaching: ']
teacher = ['Teacher:', 'Opettaja:', 'Vastuuopettaja:']
scope = ['Scope:', 'Laajuus:']
coursetype = ['Type:', 'Tyyppi:']

for name in teaching:
	tag_parse[name] = 'Teaching'
for name in teacher:
	tag_parse[name] = 'Teacher'
for name in scope:
	tag_parse[name] = 'Scope'
for name in coursetype:
	tag_parse[name] = 'Type'

def find_course(name):
	pass

def parse_info(part):
	p = part[0]
	name = tag_parse[p.text]
	if name == 'Teaching':
		if len(part) > 1 and part[1].tag == 'br':
			return name, part[1].tail
		else:
			return name, p.tail
	elif name == 'Teacher':
		return name, part[1].text
	elif name == 'Scope':
		return name, p.tail
	elif name == 'Type':
		return name, p.tail

def parse_dict(url):
	cont = {}
	page = requests.get(url)
	tree = html.fromstring(page.text)
	div = tree.xpath('//div[@class="panelContent"]')[0]
	for part in div:
		if len(part) > 0:
			for p in part:
				if p.tag == 'strong':
					if p.text in tag_parse:
						info1, info2 = parse_info(part)
						cont[info1] = info2
	for k in cont:
		print k, cont[k]

def get_data(url):
	cont = get_content(url)
	print get_teaching(cont)

def get_content(url):
	page = requests.get(url)
	tree = html.fromstring(page.text)
	return tree.xpath('//div[@id="main-content"]')[0]

def get_panel(content):
	for c in content:
		if c.get('class') == 'panel':
			return c

def get_teaching(content):
	for i in xrange(len(content)):
		c = content[i]
		if c.tag in ['h1', 'h2', 'h3']:
			if c.text in ['Opetusajat', 'Teaching', 'Schedule', 'Teaching schedule']:
				t = content[i+1].text
				if t != '':
					return t

