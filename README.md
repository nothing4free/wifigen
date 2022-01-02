![wifigen_ascii_logo](https://raw.githubusercontent.com/nothing4free/wifigen/main/wifigen.png)

A simple Python-based wifi (or anything, really!) password dictionary generator. <br>
Given a dictionary type and password length, this script will generate a file containing all possible character combinations, for later use with brute-forcing tools.
## Usage
`python3 wifigen.py -t <type> -l <length> -o <filename>`

Supported dictionary types:
+ Numeric
+ Alphabetic
+ Alphanumeric

Please note that wifigen does not overwrite already existing files, so a new filename is needed in order to generate a dictionary successfully.

## Credits

2021 Jorge Martinez | nothing4free <br>
You can reuse this code as long as you credit me somewhere :) <br>
Happy hacking!
