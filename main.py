import pandas,smtplib
import datetime as dt

#-----------------Parameters-------------------#

my_email=""
password=""

#--------------Read Data From CSV---------------- #

data=pandas.read_csv("birthdays.csv")
data_dict=data.to_dict(orient="records")
now=dt.datetime.now()

#-------------Process Data And Send Mails----------#

for data_record in data_dict:
    if now.day==data_record['day'] and now.month==data_record['month']:
        #Read Template File and replace with record name 
        with open("./letter_templates/letter_2.txt") as file:
            my_data=file.readlines()
            my_data[0]=my_data[0].replace('[NAME]',data_record['name'])
            final_file=''.join(my_data)
        ##Send msg using SMTP protocol
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"subject:Happy Birth Day\n\n{final_file}")    



