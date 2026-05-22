import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse

def fetch_page(url):
    if not url.startswith("http"):
        url = "https://" + url
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect. Check the URL.")
        exit()
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        exit()

def extract_links(url,html):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for tag in soup.find_all("a"):
        href = tag.get("href")
        if href:
            full_url = urljoin(url, href)
            links.append(full_url)
    return links
    
def extract_emails(html):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, html)
    return list(set(emails))

def extract_subdomains(html, base_domain):
    pattern = r'(?:https?://)([\w.-]+\.' + re.escape(base_domain) + ')'
    subdomains = re.findall(pattern, html)
    return list(set(subdomains))

def extract_metadata(response):
    metadata = {}
    metadata["url"] = response.url
    metadata["status_code"] = response.status_code
    metadata["server"] = response.headers.get("Server", "Not found")
    metadata["content_type"] = response.headers.get("Content-Type", "Not found")
    metadata["x_powered_by"] = response.headers.get("X-Powered-By", "Not found")
    return metadata

def save_results(url, links, emails, subdomains, metadata):
    domain = urlparse(url).netloc.replace(".", "_")
    filename = f"{domain}_results.txt"
    
    with open(filename, "w") as f:
        f.write("="*50 + "\n")
        f.write("METADATA\n")
        f.write("="*50 + "\n")
        for key, value in metadata.items():
            f.write(f"{key}: {value}\n")
        
        f.write("\n" + "="*50 + "\n")
        f.write("EMAILS\n")
        f.write("="*50 + "\n")
        for email in emails:
            f.write(email + "\n")
        
        f.write("\n" + "="*50 + "\n")
        f.write("SUBDOMAINS\n")
        f.write("="*50 + "\n")
        for sub in subdomains:
            f.write(sub + "\n")
        
        f.write("\n" + "="*50 + "\n")
        f.write(f"LINKS ({len(links)} total)\n")
        f.write("="*50 + "\n")
        for link in links:
            f.write(link + "\n")
    
    print(f"\n[SAVED] Results saved to {filename}")

url = input("Enter: ")
response = fetch_page(url)
print(response.status_code)
print(response.text[:500])

links = extract_links(url, response.text)
for link in links:
    print(link)

emails = extract_emails(response.text)
print("\n[Emails found]")
for email in emails:
    print(email)

base_domain = urlparse(url).netloc
base_domain = '.'.join(base_domain.split('.')[-2:]) 

subdomains = extract_subdomains(response.text, base_domain)
print("\n[SUBDOMAINS FOUND]")
for sub in subdomains:
    print(sub)

metadata = extract_metadata(response)
print("\n[METADATA]")
for key, value in metadata.items():
    print(f"{key}: {value}")

save_results(url, links, emails, subdomains, metadata)
