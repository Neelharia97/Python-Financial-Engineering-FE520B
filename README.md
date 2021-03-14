# Python-Financial-Engineering-FE520B
## Contents
I have included all the assignments and class notes in this repository. Please, check out the final project as well.

## Project Introduction
Built a tool for scraping data from SEC for any firm. To use the tool you need to know the CID of the company you want to scrape data from. 
Currently, the tool is limited to fetching data from 10-K forms, either textual or numerical data. 

## Data Pipeline
> The data is extracted from SEC and is copied to a text file. The purpose to copy the data into a text file is to reduce calls/requests to the server. We do not want to exceed the limited amount of request calls permitted.

> After adding the data into the text file, I manually analyzed the data and understood the structure of the data. Following that, I performed EDA which helped me realize what the important columns and fields were. 

> After analyzing the data, I realized that the data I received wasn't ideal. By that, I mean that the data I received wasn't clean enough to store it as is. 

> The next step, Data Cleaning. 
>>* The data cleaning process included removing *NULL* values and blank spaces. 
>>* I also realized that the *Numerical* values were in the string data type and the units($) for it were not consistent.
>>* I also replaced the blank spaces with NaN values.
>>* Columns with more than 50% blank values were eliminated entirely.
>>* Numerical columns with blank spaces and were filled with the mean of the columns in the case where calculations with the specific column were required.

> Following data cleaning, the data was stored in a MySQL database, with the help of Python.
> I prepared SQL queries which were used as scripts to extract data from the database.
> To make it usable by everyone, I prepared an API with Flask and Postman.
![Pipeline](https://user-images.githubusercontent.com/54964516/111053356-23928180-8431-11eb-9749-348b8877e4b6.jpeg)
