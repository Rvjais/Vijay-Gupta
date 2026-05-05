
import os

filepath = "/home/veer/Ranveer/Suraj/blogs.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Remove Hero Section and replace with Breadcrumbs + Title
hero_pattern = content[content.find('<!-- Hero Section -->'):content.find('<div class="container mx-auto px-4 py-8 md:py-12">')]

new_header = """<!-- Page Header -->
<div class="pt-32 pb-8 bg-accent/5">
    <div class="container mx-auto px-4">
        <nav class="flex text-sm text-black/60 mb-6" aria-label="Breadcrumb">
            <ol class="flex items-center space-x-2">
                <li><a href="index.html" class="hover:text-primary">Home</a></li>
                <li><span class="mx-2">/</span></li>
                <li class="text-primary font-medium">Blogs</li>
            </ol>
        </nav>
        <h1 class="text-4xl md:text-5xl font-black text-primary tracking-tight">Health Insights & <span class="text-accent">Expert Articles</span></h1>
    </div>
</div>
"""

content = content.replace(hero_pattern, new_header)

# 2. Fix all Blog Card Links to point to blog-post.html for demo consistency
import re
content = re.sub(r'href="https://drvikasneuro.com/blog/[^"]+"', 'href="blog-post.html"', content)

# 3. Fix Pagination styling (remove slate)
content = content.replace('hover:bg-slate-100', 'hover:bg-accent/10 text-primary')
content = content.replace('dark:hover:bg-slate-800', '')
content = content.replace('size-10', 'size-12') # Slightly larger for premium feel

# 4. Standardize Sidebar fully
old_sidebar_start = content.find('<aside class="w-full lg:w-1/3 xl:w-3/12 space-y-10 sticky top-24 self-start">')
old_sidebar_end = content.find('</aside>', old_sidebar_start) + 8

new_sidebar = """<aside class="w-full lg:w-1/3 xl:w-3/12 space-y-10 sticky top-24 self-start">
    <!-- Categories -->
    <div class="bg-white rounded-3xl p-8 shadow-sm border border-black/5">
        <h3 class="text-xl font-bold text-primary mb-6">Categories</h3>
        <ul class="space-y-4">
            <li class="flex justify-between items-center text-black/60 hover:text-primary transition-colors cursor-pointer group">
                <span class="font-medium group-hover:translate-x-1 transition-transform">Artificial Intelligence</span>
                <span class="text-primary font-bold">(1)</span>
            </li>
            <li class="flex justify-between items-center text-black/60 hover:text-primary transition-colors cursor-pointer group">
                <span class="font-medium group-hover:translate-x-1 transition-transform">Brain Tumours</span>
                <span class="text-primary font-bold">(9)</span>
            </li>
            <li class="flex justify-between items-center text-black/60 hover:text-primary transition-colors cursor-pointer group">
                <span class="font-medium group-hover:translate-x-1 transition-transform">Stroke Care</span>
                <span class="text-primary font-bold">(17)</span>
            </li>
            <li class="flex justify-between items-center text-black/60 hover:text-primary transition-colors cursor-pointer group">
                <span class="font-medium group-hover:translate-x-1 transition-transform">Neuro-Oncology</span>
                <span class="text-primary font-bold">(5)</span>
            </li>
            <li class="flex justify-between items-center text-black/60 hover:text-primary transition-colors cursor-pointer group border-b border-black/5 pb-4">
                <span class="font-medium group-hover:translate-x-1 transition-transform">Vascular Care</span>
                <span class="text-primary font-bold">(2)</span>
            </li>
        </ul>
    </div>

    <!-- Popular Posts -->
    <div class="bg-white rounded-3xl p-8 shadow-sm border border-black/5">
        <h3 class="text-xl font-bold text-primary mb-6">Popular Posts</h3>
        <ul class="space-y-6">
            <li>
                <a href="blog-post.html" class="text-black/70 hover:text-accent font-medium leading-snug block transition-colors">How AI Is Revolutionizing Stroke Diagnosis and Treatment</a>
            </li>
            <li>
                <a href="blog-post.html" class="text-black/70 hover:text-accent font-medium leading-snug block transition-colors">Best Neurosurgeons Near Noida: A Patient & Caregiver Guide</a>
            </li>
            <li>
                <a href="blog-post.html" class="text-black/70 hover:text-accent font-medium leading-snug block transition-colors">How Stress and Anxiety Affect Your Nervous System</a>
            </li>
        </ul>
    </div>
</aside>"""

if old_sidebar_start != -1:
    content = content[:old_sidebar_start] + new_sidebar + content[old_sidebar_end:]

with open(filepath, 'w') as f:
    f.write(content)

print("Updated blogs.html")
