import argparse
import re

def print_sentry_gun():
    print("   __,_____")
    print("  / __.==--'")
    print(" /#(-'")
    print("/#_#_#_#_#_#")
    print("#_#_#_#_#_#_#")
    print("'-'-'-'-'-'-'")

def check_url(url):
    #Regex to check if the url is proper, if it isnt will not make the request
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return re.match(regex,url) is not None

def main():
    print_sentry_gun()
    
    parser = argparse.ArgumentParser(description="HackSentry flag options below")
    parser.add_argument('-u','--url',type=str,help="Single URL")
    parser.add_argument('-w','--wordlist',type=str,help='Wordlists to iterate through')
    args = parser.parse_args()

    if args.url:
        if check_url(args.url):
            print(f"The provide url: {args.url} is valid!")
        else:
            print(f"The provided url: {args.url} sucks! Try again:)")


if __name__ == "__main__":
    main()

