# TamperX - Verb Tampering Vulnerability Checker

This tool checks whether a target URL is vulnerable to verb tampering.

## Requirements

- Python 3.x
- The packages listed in `requirements.txt`

## Installation

1. Clone this repository to your local machine.
2. Navigate to the directory where you cloned the repository.
3. Install the required packages by running `pip install -r requirements.txt`.

## Usage

To use the TamperX, run the following command:

python tamperx.py <url>


Replace `<url>` with the URL of the target server. The tool will send a series of HTTP requests with different verb combinations and report whether any of the requests result in unexpected behavior, which may indicate a vulnerability to verb tampering.

```
  __     __     ______     ______   __     ______     __   __
 /\ \  _ \ \   /\  __ \   /\__  _\ /\ \   /\  __ \   /\ "-.\ \
 \ \ \/ ".\ \  \ \  __ \  \/_/\ \/ \ \ \  \ \ \/\ \  \ \ \-.  \
  \ \__/".~\_\  \ \_\ \_\    \ \_\  \ \_\  \ \_____\  \ \_\"\_ \
   \/_/   \/_/   \/_/\/_/     \/_/   \/_/   \/_____/   \/_/ \/_/
        TamperX V1.0: Verb Tampering Vulnerability Checker

[+] Target Url: https://example.com/admin/restricted

Method     Status     Content
--------------------------------
GET        404        4416
HEAD       404        0
POST       404        4416
PUT        404        4416
DELETE     404        4416
CONNECT    405        150
TRACE      405        150
PATCH      404        4416
```

## Disclaimer
For educational purposes only. Do not use for illegal activities. Use at your own risk. By using this tool, you agree to comply with all applicable laws and regulations. Unauthorized use is strictly prohibited. Always obtain permission before using this tool. No warranties.

## License

`WebSecurityVision` is made with ♥  by [Wation](https://github.com/TheWation) and it's released under the MIT license.