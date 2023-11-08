# HackSentry <img src ="https://github.com/xsudoxx/HackSentry/assets/127046919/98448f5d-915e-4805-b445-ad12e736b926" width = "75" height = "120"/>

HackSentry is a Python script designed to analyze and test the security of URLs and domains. It performs various checks and manipulations on the provided URLs, allowing users to monitor their accessibility and status codes. The script is particularly useful for security analysts and penetration testers.

## Features

- Validate the provided URLs for proper formatting and structure.
- Check the status code of the URLs and domains to determine their accessibility.
- Modify URLs by adding or replacing ports and paths for testing purposes.
- Output the results to a specified file for record-keeping and analysis.

## Installation

1. Clone the repository to your local machine.
2. Ensure you have Python 3 installed.
3. Install the required dependencies: `pip install -r requirements.txt`.

## Usage

```bash
python3 Sentry.py -u <url> -d <domains> -p <port> -w <wordlist> -o <output>

Replace the placeholders with your desired values:

<url>: The single URL to be analyzed.
<domains>: The file containing a list of domains to iterate through.
<port>: The port number for querying each URL.
<wordlist>: The file containing endpoints to test against the URLs.
<output>: The output file for recording the results.
```
## Examples
```
python3 Sentry.py -u https://www.example.com -p 443 -w wordlist.txt -o results.txt
```
This command checks the provided URL https://www.example.com with port 443, using the wordlist.txt file, and outputs the results to results.txt.

## Contributing
Contributions are always welcome! If you have any improvements or feature suggestions, please feel free to create a pull request

## License
This project is licensed under the MIT License - see the LICENSE file for details.
