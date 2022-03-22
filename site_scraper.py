from bs4 import BeautifulSoup as sp
import requests
url ="https://www.vulnerability-lab.com/list-of-bug-bounty-programs.php" # Replace this URL with your target URL
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
webpage = requests.get(url=url, headers=header)
soup = sp(webpage.content, 'html.parser')
tables = soup.find_all('table')
print(len(tables))
a_tags = tables[4].find_all('a')
sites_list = open('bug-bounty-sites.txt', 'w')
print('[-]. Program started ........')
for a in a_tags:
	sites_list.write(a.get('href') + '\n')


print('[-]. Getting the subdomains')

sites_list = open('bug-bounty-sites.txt', 'r')
sites = sites_list.readlines()
domain_list = open('bug-bounty-domains.txt', 'w')
for site in sites:
	split_site = site.split('/')
	if len(split_site) > 1:
		domain_list.write(split_site[2] + '\n')
print('[-]. Subdomains gotten')