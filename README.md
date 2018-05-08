# Quantum Computing News Scraper
This tool scrapes webpages on the internet for news and tweets related to quantum information

After running scrape.py. An output file will be generated in the /output
directory

# Dependencies
This project runs on 
- Scrapy

# To Run Version 1
Install requirements to run
    
    $ pip install -r requirements.txt 

Navigate to the quantumnews folder

    $ cd quantumnews

List the spider 

    $ scrapy list

Running the spiders and save output to a json file

    $ scrapy crawl <spider name> -o	filename-datetime.json

Running the spiders and save output to a csv file

    $ scrapy crawl <spider name> -o filename-datetime.csv -t csv


# To Run Method 2
Altenatively you can run the scrape.sh file which will automatically run the crawl scripts. This outputs csv files by default

    $ ./scrape.sh
