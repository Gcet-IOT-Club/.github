import re

file_path = 'profile/README.md'
with open(file_path, 'r') as f:
    content = f.read()
    
# Regex to find the capsule-render img tag at the top
pattern = r'<img width="100%" src="https://capsule-render\.vercel\.app/api\?type=waving.*?/>'
replacement = '<img width="100%" src="https://raw.githubusercontent.com/Gcet-IOT-Club/.github/main/assets/header-pixel-lab.jpg" alt="GCET IoT Club Pixel Lab Header" />'

new_content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)

with open(file_path, 'w') as f:
    f.write(new_content)
    
with open('README.md', 'w') as f:
    f.write(new_content)
