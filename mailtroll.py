#!/usr/bin/env python3
# Author: Francis Sy

# NOTE: When initially prompted with 'bad credential error', just follow this
# link to allow 3rd party access to gmail account: https://support.google.com/accounts/answer/6010255

import smtplib
import sys
from getpass import getpass

if __name__ == '__main__':
    # DEBUGGING
    # for i, j in enumerate(sys.argv):
        # print("sys.argv[%d]" % i, j)

    # check to see that there are argument flags
    if len(sys.argv) != 4:
        print("Error: no or missing flags\nexit(-1)")
        exit(-1)

    
    # create a SMTP session and start tls for security
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    # login authentication
    num_tries = 3
    while True:
        if num_tries == 0:
            print("Wrong Password. Exiting now\nexit(-1)")
            exit(-1)

        # obtain password: hide keylog
        password = str(getpass("Please enter account password: "))

        try:
            s.login(str(sys.argv[1]), password)
        except smtplib.SMTPAuthenticationError:
            print("Wrong password. Please try again.")
            num_tries -= 1
        else:
            break

    # create list for single or multiple recipient accounts
    recipient_list = sys.argv[2].split(" ")

    # message to send
    msg_head = str(input("Message Header: "))
    msg_text = str(input("Input message: "))
    message = 'Subject: {}\n\n{}'.format(msg_head, msg_text)

    # loop send the mail to all recipients
    send_message = message # initial
    for i in range(len(recipient_list)):
        for j in range(int(sys.argv[3])):
            send_message += str(j+1)
            s.sendmail(sys.argv[1], recipient_list[i], send_message)
            send_message = message # reset

    s.quit() # quit
