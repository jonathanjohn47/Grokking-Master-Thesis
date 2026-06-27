import json

with open("parsed_files.json", "r") as f:
    data = json.load(f)

for path, info in data.items():
    fm = info.get("frontmatter", {})
    if any(k in fm for k in ["source_url", "captured_at", "author", "contributor"]):
        print(f"File {path} has frontmatter: {fm}")
