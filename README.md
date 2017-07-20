# pydashbutton #

## Overview ##
Run Python when pressing a Dash button! Works for all types of Dash buttons, not just the
(AWS IoT Button)[https://aws.amazon.com/iotbutton/].

I included an example where button press dates and times are logged to a Google Sheet, but feel free to run any Python
method you want.

## Requirements ##
Requires Python 2.7 (for now at least) and a machine with access to root.

Tested on Ubuntu 16.04 and macOS 10.12.5. It should work on something like a RaspberryPi running Raspbian as well.

The computer this is running on must be on the same Wi-Fi network as your Dash button for this to work.

If you're having errors or not seeing button presses, make sure you're running `pydashbutton.py` as root and your
computer is connected to the same network as your Dash button.
