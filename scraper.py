import os
import re
import urllib.request
import urllib.error
from bs4 import BeautifulSoup

def main():
    # 1. Read index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_html = f.read()
    
    # 2. Extract links from nav section
    nav_match = re.search(r'<nav.*?</nav>', index_html, re.DOTALL)
    if not nav_match:
        print("Could not find <nav> in index.html")
        return
    
    nav_html = nav_match.group(0)
    links = set(re.findall(r'href="(https://drvikasneuro\.com/[^"]+)"', nav_html))
    
    blogs_match = re.search(r'href="(/blogs[^"]*)"', nav_html)
    if blogs_match:
        links.add("https://drvikasneuro.com" + blogs_match.group(1))
        
    print(f"Found {len(links)} links to scrape.")
    
    # 3. Create mapping of URL to local filename
    url_to_local = {}
    for url in links:
        if url.endswith('/'):
            part = url.rstrip('/').split('/')[-1]
        else:
            part = url.split('/')[-1]
        if not part.endswith('.html'):
            local_name = part + '.html'
        else:
            local_name = part
        url_to_local[url] = local_name
        
    # Also add the mappings for any local pages we already know about
    url_to_local['https://drvikasneuro.com/'] = 'index.html'
    url_to_local['https://drvikasneuro.com'] = 'index.html'
    
    # Split index.html into header and footer templates
    nav_end = nav_match.end()
    footer_start = index_html.find('<footer class="site-footer">')
    
    header_template = index_html[:nav_end]
    footer_template = index_html[footer_start:]
    
    # Add tailwind script to header_template just before </head> if not present
    if "cdn.tailwindcss.com" not in header_template:
        header_template = header_template.replace('</head>', '    <script src="https://cdn.tailwindcss.com"></script>\n</head>')
        
    # 4. Fetch and create pages
    for url, local_name in url_to_local.items():
        if local_name == 'index.html':
            continue # Don't overwrite index.html with scraped content
            
        print(f"Scraping {url} -> {local_name}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            html_content = urllib.request.urlopen(req).read().decode('utf-8')
            soup = BeautifulSoup(html_content, 'html.parser')
            
            main_tag = soup.find('main')
            if main_tag:
                # Get the title
                title_tag = soup.find('title')
                page_title = title_tag.string if title_tag else local_name.replace('.html', '').replace('-', ' ').title()
                
                # Replace the title in the header template
                custom_header = re.sub(r'<title>.*?</title>', f'<title>{page_title}</title>', header_template)
                
                main_str = str(main_tag)
                
                # Update URLs in the main_str
                for original_url, new_local in url_to_local.items():
                    main_str = main_str.replace(original_url, new_local)
                
                # Update URLs in custom_header
                for original_url, new_local in url_to_local.items():
                    custom_header = custom_header.replace(original_url, new_local)
                
                # Create final HTML
                final_html = custom_header + '\n' + main_str + '\n' + footer_template
                
                with open(local_name, 'w', encoding='utf-8') as f:
                    f.write(final_html)
                print(f"  Saved {local_name}")
            else:
                print(f"  No <main> tag found in {url}")
        except Exception as e:
            print(f"  Error fetching {url}: {e}")
            
    # 5. Update index.html to point to local files
    print("Updating index.html with local links...")
    for original_url, new_local in url_to_local.items():
        if original_url not in ['https://drvikasneuro.com/', 'https://drvikasneuro.com']:
            index_html = index_html.replace(original_url, new_local)
            
    # Replace the local /blogs with blogs.html
    index_html = index_html.replace('href="/blogs"', 'href="blogs.html"')
            
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
        
    print("All done!")

if __name__ == "__main__":
    main()
