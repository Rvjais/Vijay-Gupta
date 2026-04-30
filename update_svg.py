import re

log_path = "/home/veer/.gemini/antigravity/brain/9dbec449-f955-4fee-a602-72b4b397669a/.system_generated/logs/overview.txt"
with open(log_path, 'r') as f:
    content = f.read()

# Find the background-image provided by the user
match = re.search(r'(background-image:\s*url\([\'"]?data:image/svg\+xml[^\)]+\)[\'"]?;?)', content)

if match:
    css_rules = "background-color: #DFDBE5;\n  " + match.group(1)
    
    with open('/home/veer/Ranveer/Suraj/style.css', 'a') as f:
        f.write('\n\n/* Added SVG background */\n.hero-svg-bg {\n  position: absolute;\n  inset: 0;\n  z-index: 1;\n  ' + css_rules + '\n  opacity: 0.15; /* Default opacity so it blends nicely, adjust as needed */\n}\n')
    print("Successfully added CSS rule to style.css")
else:
    print("Could not find the SVG string in logs")

