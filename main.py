'''
Author: Toby Chow
Description: Main method for testing Crawler
'''
from Crawl_Parking_Structures import CrawlRoot


def main():
    cr = CrawlRoot()
    cr.find_parking()
    print('Parking Structure 1')
    print(cr.ps1)
    print('Parking Structure 3')
    print(cr.ps3)
    print('Parking Structure 4')
    print(cr.ps4)

if __name__ == "__main__":
    main()
