import os
import re

def update_file(filepath, is_procedure=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Costs Navigation
    content = re.sub(r'<div class="nav-dropdown">\s*<a href="\.\./index\.html#costs"[\s\S]*?</div>\s*</div>', '', content)
    content = re.sub(r'<div class="mobile-submenu">\s*<span class="mobile-submenu-title">Costs</span>[\s\S]*?</div>', '', content)

    # 2. Remove Cost Section in Article
    # Look for h2 with "Cost" in it and remove until next h2 or section end
    content = re.sub(r'<h2[^>]* id="heading-[^"]*cost[^"]*"[\s\S]*?(?=<h2|</div>\s*</div>\s*<!-- FAQ Section -->)', '', content, flags=re.IGNORECASE)
    
    # 3. Add Image after Hero Section
    image_src = "../assets/condition-brain.jpg"
    if "spine" in filepath.lower() or "cervical" in filepath.lower() or "lumbar" in filepath.lower() or "disc" in filepath.lower() or "fixation" in filepath.lower() or "fusion" in filepath.lower():
        image_src = "../assets/condition-spine.jpg"
    elif is_procedure:
        image_src = "../assets/procedure-surgery.jpg"
    elif "neuralgia" in filepath.lower() or "nerve" in filepath.lower() or "carpal" in filepath.lower():
        image_src = "../assets/condition-nerve.jpg"

    image_html = f'\n<!-- Condition Image -->\n<div class="mb-12 rounded-2xl overflow-hidden shadow-2xl">\n    <img src="{image_src}" alt="Medical Illustration" class="w-full h-[400px] object-cover">\n</div>\n'
    
    # Insert after the hero section (around line 171) or before the first paragraph in article
    if '<div class="space-y-4 scroll-mt-24 article" id="about">' in content:
        content = content.replace('<div class="space-y-4 scroll-mt-24 article" id="about">', '<div class="space-y-4 scroll-mt-24 article" id="about">\n' + image_html)
    elif '<div class="text-base text-subtle-light dark:text-subtle-dark leading-relaxed prose prose-lg max-w-none dark:prose-invert article">' in content:
        content = content.replace('<div class="text-base text-subtle-light dark:text-subtle-dark leading-relaxed prose prose-lg max-w-none dark:prose-invert article">', '<div class="text-base text-subtle-light dark:text-subtle-dark leading-relaxed prose prose-lg max-w-none dark:prose-invert article">\n' + image_html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Update conditions
cond_dir = "/home/veer/Ranveer/Suraj/conditions"
for filename in os.listdir(cond_dir):
    if filename.endswith(".html"):
        update_file(os.path.join(cond_dir, filename), is_procedure=False)

# Update procedures
proc_dir = "/home/veer/Ranveer/Suraj/procedures"
for filename in os.listdir(proc_dir):
    if filename.endswith(".html"):
        update_file(os.path.join(proc_dir, filename), is_procedure=True)

print("Updated all condition and procedure pages.")
