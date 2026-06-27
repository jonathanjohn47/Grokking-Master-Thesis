import os
import re

workspace_dir = "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis"

md_map = {}

def normalize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9_]', '_', text)
    text = re.sub(r'_+', '_', text)
    return text.strip('_')

for root, dirs, files in os.walk(workspace_dir):
    # Skip graphify-out
    if "graphify-out" in root:
        continue
    for f in files:
        if f.endswith(".md"):
            stem = f[:-3]
            # immediate parent directory
            parent = os.path.basename(root)
            node_id = f"{normalize(parent)}_{normalize(stem)}"
            md_map[stem] = {
                "id": node_id,
                "path": os.path.join(root, f),
                "parent": parent
            }

print(f"Total md files found: {len(md_map)}")
# Print a few examples
for k, v in list(md_map.items())[:10]:
    print(f"  {k} -> {v['id']}")
