import smtplib as spt

#You need to set this in your google account, to get an app password
my_email = "your_email@gmail.com"
password = "your_app_password"

with spt.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="your_destin_email@gmail.com", 
        msg="Subject:Greetings!\n\nHello friend!"
    )
