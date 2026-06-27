import os
import json
import re

files = [
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Biroli - Dynamical Regimes of Diffusion Models.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Canatar - Spectral Bias and Task-Model Alignment.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Fang - Layer-Peeled Model and Minority Collapse.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Geirhos - Shortcut Learning in Deep Neural Networks.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Jiang - Network Properties Determine Neural Network Performance.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Li - Representations and Generalization in Artificial and Brain Neural Networks.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Martin - Predicting Trends in Neural Network Quality.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Mei - A Mean Field View of Two-Layer Neural Networks.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Mei - Generalization Error of Random Features Regression.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Mixon - Neural Collapse with Unconstrained Features.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Nanda - Progress Measures for Grokking via Mechanistic Interpretability.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Papyan - Prevalence of Neural Collapse.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Pomarico - Transfer Entropy and O-Information to Detect Grokking.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Power - Grokking: Generalisation Beyond Overfitting on Small Algorithactions.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Rocks - Memorizing Without Overfitting.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Sokolić - Robust Large Margin Deep Neural Networks.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Spigler - A Jamming Transition Affects Generalization.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Varma - Explaining Grokking Through Circuit Efficiency.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Xu - Dynamics in Deep Classifiers with the Square Loss.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Zhang - Understanding Deep Learning Still Requires Rethinking Generalization.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/04 - Synthesis/Competing Theories of Grokking.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/04 - Synthesis/Empirical Evidence Across Studies.md"
]

parsed_data = {}

for f in files:
    if not os.path.exists(f):
        # Check alternative filenames
        dir_name = os.path.dirname(f)
        base_name = os.path.basename(f)
        alt_path = None
        if os.path.exists(dir_name):
            prefix = base_name.split(" - ")[0].split(":")[0].split(" ")[0]
            for item in os.listdir(dir_name):
                if item.lower().startswith(prefix.lower()):
                    alt_path = os.path.join(dir_name, item)
                    break
        if alt_path:
            print(f"Mapping {f} to {alt_path}")
            f = alt_path
        else:
            print(f"Could not find alternative for {f}")
            continue

    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Parse YAML frontmatter
    yaml_dict = {}
    frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    body = content
    if frontmatter_match:
        yaml_content = frontmatter_match.group(1)
        body = content[frontmatter_match.end():]
        # parse simple yaml lines
        for line in yaml_content.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                k = k.strip()
                v = v.strip()
                # strip list formatting if any
                if v.startswith("[") and v.endswith("]"):
                    v = [item.strip().strip('"').strip("'") for item in v[1:-1].split(",")]
                yaml_dict[k] = v
    
    # Extract links of form [[Link]] or [[Link|Text]]
    links = []
    # match obsidian style wikilinks [[Link]] or [[Link|Alias]]
    for link in re.findall(r"\[\[(.*?)\]\]", body):
        links.append(link)

    parsed_data[f] = {
        "original_path": f,
        "frontmatter": yaml_dict,
        "links": list(set(links)),
        "content_length": len(body),
        "body": body
    }

# Save parsed data to parsed_files.json
with open("parsed_files.json", "w", encoding="utf-8") as out:
    json.dump(parsed_data, out, indent=2)

print(f"Successfully parsed {len(parsed_data)} files and wrote to parsed_files.json")
