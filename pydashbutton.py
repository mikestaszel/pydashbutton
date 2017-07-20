import datetime
import gspread
from scapy.layers.dhcp import DHCP
from scapy.layers.l2 import Ether
from scapy.sendrecv import sniff
from oauth2client.service_account import ServiceAccountCredentials


# Tested on Mac OS X 10.12.5 and Ubuntu 16.04 using Python 2.7. Must run as root/sudo.


MAC_ADDRESS_BUTTON1 = "fc:a6:xx:xx:xx:xx"
MAC_ADDRESS_BUTTON2 = "fc:a6:xx:xx:xx:xx"
GOOGLE_DRIVE_CREDENTIALS_FILE_LOCATION = "service_key.json"
GOOGLE_SHEET_NAME = "BottonPressLog"


def log_button_press():
    now = datetime.datetime.now()
    now_date_str = now.strftime("%m/%d/%Y")
    now_time_str = now.strftime("%I:%M %p")
    print("logging button press: {} {}".format(now_date_str, now_time_str))

    scope = ["https://spreadsheets.google.com/feeds"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_DRIVE_CREDENTIALS_FILE_LOCATION, scope)
    gc = gspread.authorize(credentials)
    wks = gc.open(GOOGLE_SHEET_NAME).sheet1
    wks.append_row([now_date_str, now_time_str])
    print("success!")


def detect_button(pkt):
    if pkt.haslayer(DHCP):
        if pkt[Ether].src == MAC_ADDRESS_BUTTON1:
            print("This button doesn't do anything yet.")
        elif pkt[Ether].src == MAC_ADDRESS_BUTTON2:
            log_button_press()


sniff(prn=detect_button, filter="(udp and (port 67 or 68))", store=0)
