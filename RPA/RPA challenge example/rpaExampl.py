# import modules
import rpa as r
import pandas as pd

# read the excel file and store in data frame value df
df = pd.read_excel("./challenge.xlsx")

# start the tagUI process
r.init()

# open the website
r.url("https://rpachallenge.com/")
r.wait(10)  # by default the funtion will wait for 5 sec

# click on
r.click('//button[text()="Start"]')  # inspect start button tag

# data entry operations
for index, row in df.iterrows():
    r.type()
    r.type('//input[@ng-reflect-name="labelFirstName"]', row['First Name'])
    r.type('//input[@ng-reflect-name="labelLastName"]',  row['Last Name'])
    r.type('//input[@ng-reflect-name="labelCompanyName"]',
           row['Company Name'])
    r.type('//input[@ng-reflect-name="labelRole"]', row['Role in Company'])
    r.type('//input[@ng-reflect-name="labelAddress"]', row['Address'])
    r.type('//input[@ng-reflect-name="labelEmail"]', row['Email'])
    r.type('//input[@ng-reflect-name="labelPhone"]', str(row['Phone Number']))
    r.click('//input[@value="Submit"]')

# screenshot of webpage
r.snap('/html/body/app-root/div[2]', 'results.png')

# stop the tagUI
r.close()
