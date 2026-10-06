
import requests

# Ask for the domain
domain = input("Enter the domain: ")

# Open the wordlist
sub_list = open("common-crawl-subdomains-10000.txt").read()
subdoms = sub_list.splitlines()

print("\nStarting scan...\n")

# Try every subdomain
for sub in subdoms:

    sub_domain = f"http://{sub}.{domain}"

    print("Checking:", sub_domain)

    try:
        response = requests.get(sub_domain, timeout=5)

        print("  Status:", response.status_code)

    except requests.ConnectionError:
        print("  No connection")

print("\nScan finished.")

