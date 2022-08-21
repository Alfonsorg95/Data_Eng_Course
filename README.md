# Data Engineer Course with Python

The course intention is to replicate a full process to create an ETL using python. 

This project consist in create a web scrapper to extract some news from different newspapers, clean the data obtained and load the clean data to a database. All of this process is automated in a single run of the program.

## Extract

To extract the news the program take all the articles links in the newspaper's main page and them with every link the program extract the body and the title from the article.

To easily add different newspapers all the project was made using abstractions of the process. The file config.yaml on the extract folder can be modified to add, delete or change the newspapers you want to scrape.

## Transform

All data must be cleaned, in this process the program search for duplicates, strips some columns, creates unique ids for articles, add useful columns as words count for titles and bodies. At the end of this phase we have a clean data ready to load.

## Load

As the name suggest all clean data now es loaded to a database, in this case sqlite. The file newspaper.db created contains all the clean data.

## Pipeline

The file pipeline.py just executes the whole process automatically.