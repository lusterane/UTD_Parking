'''
Author: Toby Chow
Description: Crawls UTD Auxiliary Service's Parking information page for Amazon Alexa Skill
'''

import urllib3
import certifi
from bs4 import BeautifulSoup


class CrawlRoot:

    def __init__(self):
        self.ps1 = {}
        self.ps3 = {}
        self.ps4 = {}

    # finds parking options and available Spaces of PS1
    # returns dictionary of available space and level+color
    def find_parking_ps1(self, soup):
        for element in soup.findAll('table', {'id': 'ps1'}):
            body = element.find('tbody')
            # finds each row for parking
            for row in body.findAll('tr'):
                cells = row.findAll("td")
                level = cells[0].text
                option = cells[1].text
                avail_space = cells[2].text
                # note: levels may not be needed for this project
                self.ps1[option] = avail_space
                # print('Level: ' + level + ' | Option: ' + option + ' | Available Spaces: ' + avail_space + " : ENTERED INTO DICTIONARY")

    # finds parking options and available Spaces of PS3
    # returns dictionary of available space and level+color
    def find_parking_ps3(self, soup):
        for element in soup.findAll('table', {'id': 'ps3'}):
            body = element.find('tbody')
            # finds each row for parking
            for row in body.findAll('tr'):
                cells = row.findAll("td")
                level = cells[0].text
                option = cells[1].text
                avail_space = cells[2].text
                # note: levels may not be needed for this project
                self.ps3[option] = avail_space
                # print('Level: ' + level + ' | Option: ' + option + ' | Available Spaces: ' + avail_space + " : ENTERED INTO DICTIONARY")

    # finds parking options and available Spaces of PS4
    # returns dictionary of available space and level+color
    def find_parking_ps4(self, soup):
        for element in soup.findAll('table', {'id': 'ps4'}):
            body = element.find('tbody')
            # finds each row for parking
            for row in body.findAll('tr'):
                cells = row.findAll("td")
                level = cells[0].text
                option = cells[1].text
                avail_space = cells[2].text
                # note: levels may not be needed for this project
                self.ps4[option] = avail_space
                # print('Level: ' + level + ' | Option: ' + option + ' | Available Spaces: ' + avail_space + " : ENTERED INTO DICTIONARY")
        '''
        # last checked info
        last_checked = soup.find('table', {'id': 'ps4'}).find('p', {'class': 'centertight'}).text
        print(last_checked)
        '''

    def find_parking(self):
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        url_php = "https://www.utdallas.edu/services/transit/garages/_code.php"
        response = http.request('GET', url_php)
        soup = BeautifulSoup(response.data, features="html.parser")
        self.find_parking_ps1(soup)
        self.find_parking_ps3(soup)
        self.find_parking_ps4(soup)
'''
    # finds the corresponding color for level of parking structure
    # "PS1" is Parking Structure 1, "PS3" is Parking Structure 3, "PS4" is Parking Structure 4
    # paramaters: parking_struc is corresponding parking structure and level is level of parking structure
    def find_color(self, parking_struc, level):
        # finding color for parking structure 1
        if parking_struc == "PS1":
            switcher = {
                1: "Pay-By-Space",
                2: "Purple&Orange",
                3: "Orange&Gold",
                4: "Gold",
                5: "Green"
            }
            return switcher.get(level, "Invalid Level")
'''

