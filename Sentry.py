import argparse
import re
import requests

def print_sentry_gun():
    print("   __,_____")
    print("  / __.==--'")
    print(" /#(-'")
    print("/#_#_#_#_#_#")
    print("#_#_#_#_#_#_#")
    print("'-'-'-'-'-'-'")

def check_url(url, port=None, wordlist=None):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.match(regex, url):
        if wordlist and port:
            with open(wordlist, 'r') as f:
                endpoints = f.read().split()
            for endpoint in endpoints:
                domain, path = re.match(r'^(?P<protocol>https?://)(?P<domain>[^/:]+)(?P<path>.*)$', url).group('domain', 'path')
                modified_url = f"{domain}:{port}/{endpoint.lstrip('/')}"
                print(f"The provided URL: {url} is valid!")
                print(f"The modified URL: {modified_url}")
                check_status_and_write_to_file(modified_url)
        elif wordlist:
            with open(wordlist, 'r') as f:
                endpoints = f.read().split()
            for endpoint in endpoints:
                domain, _ = re.match(r'^(?P<protocol>https?://)(?P<domain>[^/:]+)(?P<path>.*)$', url).group('domain', 'path')
                modified_url = f"{domain}/{endpoint.lstrip('/')}"
                print(f"The provided URL: {url} is valid!")
                print(f"The modified URL: {modified_url}")
                check_status_and_write_to_file(modified_url)
        elif port:
            parsed_url = re.match(r'^(?P<protocol>https?://)(?P<domain>[^/:]+)(?P<path>.*)$', url)
            if parsed_url:
                modified_url = f"{parsed_url.group('protocol')}{parsed_url.group('domain')}:{port}{parsed_url.group('path')}"
                print(f"The provided URL: {url} is valid!")
                print(f"The modified URL: {modified_url}")
                check_status_and_write_to_file(modified_url)
        else:
            print(f"The provided URL: {url} is valid!")
            check_status_and_write_to_file(url)
    else:
        print(f"The provided URL: {url} did not pass the initial inspection.")

def check_status_and_write_to_file(modified_url):
    response = requests.get(modified_url)
    if response.status_code == 200:
        with open('output.txt', 'a') as file:
            file.write(modified_url + '\n')

check_url('http://example.com', 8080, 'wordlist.txt')


def check_urls_from_domains(domains, port=None,wordlist=None):
    with open(domains, 'r') as f:
        for line in f:
            url = line.strip()
            check_url(url, port,wordlist)

def check_status_and_write_to_file(modified_url):
    response = requests.get(modified_url)
    if response.status_code == 200:
        with open('output.txt', 'a') as file:
            file.write(modified_url + '\n')

def main():
    print_sentry_gun()
    
    parser = argparse.ArgumentParser(description="HackSentry flag options below")
    parser.add_argument('-u','--url',type=str,help="Single URL")
    parser.add_argument('-d','--domains',type=str,help='Wordlists of domains to iterate through')
    parser.add_argument('-p','--port',type=int,help='port number to query on each url',default=None)
    parser.add_argument('-w','--wordlist',type=str,help='This is every endpoint we want to query against')
    args = parser.parse_args()

    if args.url and args.port and args.wordlist:
        check_url(args.url,args.port,args.wordlist)
    elif args.url and args.port:
        check_url(args.url, args.port)
    elif args.url:
        check_url(args.url)
    elif args.domains and args.port and args.wordlist:
        check_urls_from_domains(args.domains, args.port, args.wordlist)
    elif args.domains and args.port:
        check_urls_from_domains(args.domains, args.port)
    elif args.domains:
        check_urls_from_domains(args.domains)

if __name__ == "__main__":
    main()

