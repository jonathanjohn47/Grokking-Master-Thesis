import json

with open("parsed_files.json", "r") as f:
    data = json.load(f)

for path, info in data.items():
    print("=" * 60)
    print("PATH:", path)
    print("FM:", info.get("frontmatter"))
    print("LINKS:", info.get("links"))
    print("CONTENT (first 300 chars):")
    print(info.get("body")[:300])
    print("...")
