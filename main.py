import pandas as pd
import datetime as dt
import random
import smtplib

df = pd.read_csv("birthdays.csv")
birthday_data = df.iloc[0].to_dict()   #to get the data in perfect dict format and no list involved

now=dt.datetime.now()
letter = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]
if now.month == birthday_data["month"] and now.day == birthday_data["day"]:
    letter_choose=random.choice(letter)
    # print(letter_choose)
    with open(letter_choose,"r") as file:
        inletter=file.read()
    change_name=inletter.replace("[NAME]",birthday_data["name"])

    my_email = "testmailpython1290@gmail.com"
    password = "vwhkggwpmkkfkywb"
    to_email = birthday_data["email"]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:HAPPY BIRTHDAY\n\n{change_name}")
        connection.close()

    #smtp
    #step 1:get your email,password,to_email
    #step 2:open connection using with
    #step 3:starttls() then login() then sendmail() then close()
