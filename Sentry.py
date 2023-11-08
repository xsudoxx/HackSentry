import argparse
import re
import requests
import sys
import concurrent.futures

def print_sentry_gun():
    print("   __,_____")
    print("  / __.==--'")
    print(" /#(-'")
    print("/#_#_#_#_#_#")
    print("#_#_#_#_#_#_#")
    print("'-'-'-'-'-'-'")

def check_url(url, port=None, wordlist=None, output=None):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.match(regex, url):
        if wordlist and port and output:
            with open(wordlist, 'r') as f:
                endpoints = f.read().split()
            for endpoint in endpoints:
                parsed_url = re.match(r'^(?P<protocol>https?://)(?P<domain>[^/:]+)(?P<wordlist>.*)$', url)
                if parsed_url:
                    modified_url = f"{parsed_url.group('protocol')}{parsed_url.group('domain')}:{port}/{endpoint.lstrip('/')}"
                    print(f"The provided URL: {url} is valid!")
                    print(f"The modified URL: {modified_url}")
                    check_status_and_write_to_file(modified_url,output)

        elif wordlist and port:
            with open(wordlist, 'r') as f:
                endpoints = f.read().split()
            for endpoint in endpoints:
                parsed_url = re.match(r'^(?P<protocol>https?://)(?P<domain>[^/:]+)(?P<wordlist>.*)$', url)
                if parsed_url:
                    modified_url = f"{parsed_url.group('protocol')}{parsed_url.group('domain')}:{port}/{endpoint.lstrip('/')}"
                    print(f"The provided URL: {url} is valid!")
                    print(f"The modified URL: {modified_url}")
                    check_status_and_write_to_file(modified_url,output)
        elif wordlist:
            with open(wordlist, 'r') as f:
                endpoints = f.read().split()
            for endpoint in endpoints:
                parsed_url = re.match(r'^(?P<protocol>https?://)(?P<domain>[^/:]+)(?P<path>/.*)$', url)
                if parsed_url:
                    protocol = parsed_url.group('protocol')
                    domain = parsed_url.group('domain')
                    path = endpoint.lstrip('/')
                    modified_url = f"{protocol}{domain}/{path}"
                    if port:
                        modified_url = f"{protocol}{domain}:{port}/{path}"
                    print(f"The provided URL: {url} is valid!")
                    print(f"The modified URL: {modified_url}")
                    check_status_and_write_to_file(modified_url, output)

        elif port:
            parsed_url = re.match(r'^(?P<protocol>https?://)(?P<domain>[^/:]+)(?::\d+)?(?P<wordlist>.*)$', url)
            if parsed_url:
                domain = parsed_url.group('domain')
                modified_url = f"{parsed_url.group('protocol')}{domain}:{port}{parsed_url.group('wordlist')}"
                print(f"The provided URL: {url} is valid!")
                print(f"The modified URL: {modified_url}")
                check_status_and_write_to_file(modified_url, output)

        else:
            print(f"The provided URL: {url} is valid!")
            check_status_and_write_to_file(url)
    else:
        print(f"The provided URL: {url} did not pass the initial inspection.")

def check_urls_from_domains(domains, port=None, wordlist=None, output=None):
    with open(domains, 'r') as f:
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:  # Limiting to 20 workers
            urls = [line.strip() for line in f]  # Ensure no leading or trailing whitespaces
            futures = [executor.submit(check_url, url, port, wordlist, output) for url in urls]
            concurrent.futures.wait(futures)


def check_status_and_write_to_file(modified_url, output_file=None):
    try:
        response = requests.get(modified_url)
        if response.status_code == 200:
            if output_file:
                with open(output_file, 'a') as file:
                    file.write(modified_url + '\n')
                print(f"The URL: {modified_url} returned a status code of 200. Written to file.")
            else:
                print(f"The URL: {modified_url} returned a status code of 200.")
        else:
            print(f"The URL: {modified_url} returned a status code of {response.status_code}.")
    except requests.exceptions.SSLError as e:
        print(f"The URL: {modified_url} is not accessible due to an SSL error. Error: {e}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="HackSentry flag options below")
    parser.add_argument('-u', '--url', type=str, help="Single URL")
    parser.add_argument('-d', '--domains', type=str, help='Wordlists of domains to iterate through')
    parser.add_argument('-p', '--port', type=int, help='port number to query on each url', default=None)
    parser.add_argument('-w', '--wordlist', type=str, help='This is every endpoint we want to query against')
    parser.add_argument('-o', '--output', type=str, help='Use this to output results to a file of your choice', default=None)
    return parser.parse_args()

def handle_args(args):
    if args.url and not args.domains:
        check_url(args.url, args.port, args.wordlist, args.output)
    elif args.domains and not args.url:
        check_urls_from_domains(args.domains, args.port, args.wordlist, args.output)

    else:
        print("Please provide either a single URL using -u or a file with domains using -d.")


def main():
    try:
        print_sentry_gun()
        args = parse_arguments()
        handle_args(args)
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Script execution stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()