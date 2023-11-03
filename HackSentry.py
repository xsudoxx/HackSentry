import argparse

def print_sentry_gun():
    print("   __,_____")
    print("  / __.==--'")
    print(" /#(-'")
    print("/#_#_#_#_#_#")
    print("#_#_#_#_#_#_#")
    print("'-'-'-'-'-'-'")

def main():
    print_sentry_gun()
    
    parser = argparse.ArgumentParser(description="HackSentry flag options below")
    parser.add_argument('-u','--url',action='store_true',help="Single URL")
    parser.add_argument('-w','--wordlist',action='store_true',help='Wordlists to iterate through')
    parser.parse_args()



if __name__ == "__main__":
    main()

