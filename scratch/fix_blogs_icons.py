
import os

filepath = "/home/veer/Ranveer/Suraj/blogs.html"
with open(filepath, 'r') as f:
    content = f.read()

# Add icons to blog card meta
old_meta = """<div class="blog-card-meta">
                <span>Nov 23, 2025</span>
                <span>Neuro-Oncology</span>
            </div>"""

new_meta = """<div class="blog-card-meta">
                <div class="flex items-center gap-1.5">
                    <span class="material-symbols-outlined text-sm">calendar_today</span>
                    <span>Nov 23, 2025</span>
                </div>
                <div class="flex items-center gap-1.5">
                    <span class="material-symbols-outlined text-sm">folder</span>
                    <span>Neuro-Oncology</span>
                </div>
            </div>"""

content = content.replace(old_meta, new_meta)

# Replace other occurrences roughly
import re
content = re.sub(r'<span>(Nov \d+, \d+)</span>\s*<span>([^<]+)</span>', 
                r'<div class="flex items-center gap-1.5"><span class="material-symbols-outlined text-sm">calendar_today</span><span>\1</span></div><div class="flex items-center gap-1.5"><span class="material-symbols-outlined text-sm">folder</span><span>\2</span></div>', 
                content)

with open(filepath, 'w') as f:
    f.write(content)

print("Updated blog card icons in blogs.html")
