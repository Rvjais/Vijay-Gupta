import os
import re

files_to_update = [
    "about-doctor.html",
    "blogs.html",
    "testimonials.html",
    "frequently-asked-questions.html",
    "events.html",
    "videos.html"
]

root_dir = "/home/veer/Ranveer/Suraj"

def remove_costs_nav(content):
    # Desktop nav
    content = re.sub(r'<div class="nav-dropdown">\s*<a href="index\.html#costs"[\s\S]*?</div>\s*</div>', '', content)
    # Mobile nav
    content = re.sub(r'<div class="mobile-submenu">\s*<div class="mobile-submenu-header">\s*<span>Costs</span>[\s\S]*?</div>\s*</div>', '', content)
    return content

for filename in files_to_update:
    filepath = os.path.join(root_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = remove_costs_nav(content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Removed Costs navigation from all other pages.")
