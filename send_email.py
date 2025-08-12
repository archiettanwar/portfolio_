import ssl,smtplib
def send_mail(username,msg):
    host="smtp.gmail.com"
    port=465

    password="ejob drir qfby bpee"
    tomail="archiettanwar71@gmail.com"

    context=ssl.create_default_context()

    msg=f"From {username}{msg}"

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(tomail,password)
        server.sendmail(username,tomail,msg)