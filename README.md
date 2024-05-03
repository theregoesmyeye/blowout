# blowout
DOESN"T WORK YET - Blowout is a brand new SSH cracking tool for Termux. It randomly generates IP addresses, scans to see if it's a host with an open SSH port, and then begins cracking using a predefined wordlist.

## How to use:
1. Get a copy of this repo using ``` git clone https://github.com/theregoesmyeye/blowout ```
2. ``` cd blowout ```
3. ``` chmod +x install_required_stuff.sh && bash install_required_stuff.sh ```
~~4. Obtain your own  copy of rockyou.txt for a list containing around 14 million passwords. Find it here:  https://github.com/zacheller/rockyou~~ install_required_stuff.sh will now download rockyou.txt and put it in the correct place.
5. ``` python3 blowout.py ```
