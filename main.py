# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import os
from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


'''
import smtplib
import datetime as dt
import pandas as pd
from random import randint

# AFTER (secrets stored securely in GitHub)
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

##################### Normal Starting Project ######################


# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)


now = dt.datetime.now()
today_tuple = (now.month, now.day)

# HINT 2: Use pandas to read the birthdays.csv

with open("birthdays.csv", "r") as bdfile:
    df = pd.read_csv(bdfile) #return dataframe
    # print(df)
    # bddict = df.to_dict(orient="records")

# print(bddict)
#
# for (x,y) in df.iterrows():
#     # print(x)
#     # print(y)
#     print(y.month, int(y.day))


# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# bdict = {
#     (bmonth, bday): data_row
# }

#Dictionary comprehension template for pandas DataFrame looks like this:
#JMK - iterate through the df, creating a tuple for each data_row

#bdict = { (dataElement1, dataElement2): data_row [what we want back] for each index, data_row in the df }
bdict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

# print(bdict)

#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

if today_tuple in bdict:
    rnd = randint(1,3) #pick random letter
    filename = f"letter_templates/letter_{rnd}.txt"
    person = bdict[today_tuple] #get the person record
    with open(filename, "r") as f:
        bodytext = f.read()
        new_body = bodytext.replace("[NAME]", person["name"])

#now create and send email using SMTP stuff
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()  # transport layer security; makes connection secure
        connection.login(user=myEmail, password=app_password)

        # Subject is part of msg parameter
        connection.sendmail(from_addr=myEmail,
                            to_addrs=person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{new_body}") #"JMKinNH@comcast.net"
'''
