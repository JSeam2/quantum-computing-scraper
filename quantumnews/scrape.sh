#!/bin/bash

dt=`date '+%d-%m-%Y_%H:%M:%S'`
  
scrapy crawl rss -o rss_$dt.csv -t csv


