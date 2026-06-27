import json

with open("parsed_files.json", "r") as f:
    data = json.load(f)

with open("all_contents.txt", "w", encoding="utf-8") as out:
    for path, info in data.items():
        out.write("=" * 80 + "\n")
        out.write(f"PATH: {path}\n")
        out.write(f"TAGS: {info.get('frontmatter', {}).get('tags', [])}\n")
        out.write(f"LINKS: {info.get('links', [])}\n")
        out.write("-" * 40 + "\n")
        out.write(info.get("body", ""))
        out.write("\n\n")

print("Wrote all contents to all_contents.txt")
