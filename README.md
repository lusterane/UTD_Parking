# UTD_Parking
Finds available parking for UTD students

Contains web crawler as part of implementation for Alexa Skill. Indexes information from UTD Auxilliary Services Real-Time parking information.

## Dependencies

Required dependencies for project to work in Lambda integration

beautifulsoup4==4.7.1

* soupsieve [required: >=1.2, installed: 1.9.1]

certifi==2019.3.9

setuptools==39.1.0

urllib3==1.24.2


[Note: soupseive is still a required dependency. Just need >=1.2 version]

## How To Use/Integrate

**Crawl_Parking_Structures.py** is the required module.
1. Install the required dependencies noted above in Lambda
2. Import functional class from Crawl_Parking_Structures.py, 'CrawlRoot'
* `from Crawl_Parking_Structures import CrawlRoot`
3. Declare CrawlRoot object to use methods
* `cr = CrawlRoot()`
4. **[IMPORTANT]**  Run the web indexing with find_parking() method to fill dictionary
* `cr.find_parking()`
5. A dictionary will be populated called `intent_dict`. 
* Grab this from the module with `cr.intent_dict` to integrate into Lambda


