<p align="center">
  <a href="https://github.com/xsudoxx/HackSentry" rel="noopener" target="_blank"><img width="150" height="133" src="https://github.com/xsudoxx/HackSentry/assets/127046919/46b2cc1d-2ff0-4e44-ae5b-5e15f8f75f71" alt="HackSentry Logo"></a>
</p>

<h1 align="center">HackSentry</h1>

HackSentry is a Python script designed to analyze and test the security of URLs and domains. It performs various checks and manipulations on the provided URLs, allowing users to monitor their accessibility and status codes. The script is particularly useful for security analysts and penetration testers.

<p align="center">
  <span style="font-size: 24px;"><strong>Visitor Count:</strong></span>
  <img src="https://profile-counter.glitch.me/xsudoxx/count.svg" alt="Visitor Count" />
</p>

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
```
Replace the placeholders with your desired values:

<url>: The single URL to be analyzed.
<domains>: The file containing a list of domains to iterate through.
<port>: The port number for querying each URL.
<wordlist>: The file containing endpoints to test against the URLs.
<output>: The output file for recording the results.

## Examples
To check a single URL without any modifications:
````
python3 Sentry.py -u https://www.example.com
````
To check a list of domains from a file and output the results to a file:
````
python3 Sentry.py -d domains.txt -o output.txt
````
To check a single URL with a specified port and wordlist:
````
python3 Sentry.py -u https://www.example.com -p 8080 -w endpoints.txt
````
To check a list of domains with a specified port and wordlist and output the results to a file:
````
python3 Sentry.py -d domains.txt -p 443 -w endpoints.txt -o results.txt
````
Feel free to adjust the parameters based on your specific testing needs.
## Contributing
Contributions are always welcome! If you have any improvements or feature suggestions, please feel free to create a pull request

## License
This project is licensed under the MIT License - see the LICENSE file for details.
