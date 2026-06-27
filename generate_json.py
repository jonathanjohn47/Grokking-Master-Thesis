import os
import json
import re

workspace_dir = "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis"

# 1. First, scan all .md files in the workspace to build a dictionary mapping file stem to node_id and absolute path
md_map = {}

def normalize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9_]', '_', text)
    text = re.sub(r'_+', '_', text)
    return text.strip('_')

for root, dirs, files in os.walk(workspace_dir):
    if "graphify-out" in root:
        continue
    for f in files:
        if f.endswith(".md"):
            stem = f[:-3]
            parent = os.path.basename(root)
            node_id = f"{normalize(parent)}_{normalize(stem)}"
            md_map[stem] = {
                "id": node_id,
                "path": os.path.abspath(os.path.join(root, f)),
                "parent": parent
            }

# Let's read parsed_files.json
with open("parsed_files.json", "r") as f:
    parsed_files = json.load(f)

nodes = []
edges = []

# List of files in chunk 4 (using absolute paths)
chunk_files = [
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
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Power - Grokking: Generalisation Beyond Overfitting on Small Algorithmic Datasets.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Rocks - Memorizing Without Overfitting.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Sokolić - Robust Large Margin Deep Neural Networks.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Spigler - A Jamming Transition Affects Generalization.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Varma - Explaining Grokking Through Circuit Efficiency.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Xu - Dynamics in Deep Classifiers with the Square Loss.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Zhang - Understanding Deep Learning Still Requires Rethinking Generalization.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/04 - Synthesis/Competing Theories of Grokking.md",
    "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/04 - Synthesis/Empirical Evidence Across Studies.md"
]

# Standardize names to verify keys in parsed_files
parsed_keys_map = {os.path.abspath(k): k for k in parsed_files.keys()}

# 2. Extract Nodes
for f in chunk_files:
    abs_f = os.path.abspath(f)
    if abs_f not in parsed_keys_map:
        print(f"Warning: {f} not found in parsed files!")
        continue
    
    orig_key = parsed_keys_map[abs_f]
    info = parsed_files[orig_key]
    
    # Get stem details
    filename = os.path.basename(abs_f)
    stem_name = filename[:-3]
    parent_dir = os.path.basename(os.path.dirname(abs_f))
    
    node_id = f"{normalize(parent_dir)}_{normalize(stem_name)}"
    
    # Determine file_type
    if "03 - Literature" in abs_f:
        file_type = "paper"
    elif "04 - Synthesis" in abs_f:
        file_type = "document"
    else:
        file_type = "concept"
        
    label = stem_name
    # Clean label (e.g. remove "Biroli - " prefix or replace " — " with " - ")
    if " — " in label:
        label = label.replace(" — ", " - ")
    
    # Parse source_url, captured_at, author, contributor from frontmatter if available
    fm = info.get("frontmatter", {})
    
    nodes.append({
        "id": node_id,
        "label": label,
        "file_type": file_type,
        "source_file": f, # Verbatim absolute path from chunk_files
        "source_location": None,
        "source_url": fm.get("source_url"),
        "captured_at": fm.get("captured_at"),
        "author": fm.get("author"),
        "contributor": fm.get("contributor")
    })

# 3. Extract Edges
for f in chunk_files:
    abs_f = os.path.abspath(f)
    if abs_f not in parsed_keys_map:
        continue
    orig_key = parsed_keys_map[abs_f]
    info = parsed_files[orig_key]
    
    filename = os.path.basename(abs_f)
    stem_name = filename[:-3]
    parent_dir = os.path.basename(os.path.dirname(abs_f))
    source_id = f"{normalize(parent_dir)}_{normalize(stem_name)}"
    
    # Process wiki links
    for link in info.get("links", []):
        # Resolve target and optional alias
        target = link.split("|")[0].strip()
        
        # Check if the target is in the workspace md_map
        if target in md_map:
            target_id = md_map[target]["id"]
            
            # Determine relationship type
            # literature to literature -> cites
            # literature to concept -> references
            # synthesis to literature -> cites or references
            # synthesis to concept -> references
            relation = "references"
            if "03 - Literature" in md_map[target]["path"]:
                relation = "cites"
            elif "04 - Synthesis" in md_map[target]["path"]:
                relation = "conceptually_related_to"
                
            # Avoid self loops
            if source_id == target_id:
                continue
                
            edges.append({
                "source": source_id,
                "target": target_id,
                "relation": relation,
                "confidence": "EXTRACTED",
                "confidence_score": 1.0,
                "source_file": f, # Verbatim path
                "source_location": None,
                "weight": 1.0
            })
        else:
            print(f"Link target '{target}' in file '{filename}' not found in md_map.")

# Add the inferred semantic similarity edge between Sokolić and Xu
edges.append({
    "source": "03_literature_sokoli_robust_large_margin_deep_neural_networks",
    "target": "03_literature_xu_dynamics_in_deep_classifiers_with_the_square_loss",
    "relation": "semantically_similar_to",
    "confidence": "INFERRED",
    "confidence_score": 0.85,
    "source_file": "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/03 - Literature/Sokolić - Robust Large Margin Deep Neural Networks.md",
    "source_location": None,
    "weight": 1.0
})

# 4. Hyperedges
hyperedges = [
    {
        "id": "algorithmic_grokking_mechanisms",
        "label": "Algorithmic Grokking Mechanisms and Predictors",
        "nodes": [
            "03_literature_nanda_progress_measures_for_grokking_via_mechanistic_interpretability",
            "03_literature_pomarico_transfer_entropy_and_o_information_to_detect_grokking",
            "03_literature_varma_explaining_grokking_through_circuit_efficiency"
        ],
        "relation": "form",
        "confidence": "INFERRED",
        "confidence_score": 0.95,
        "source_file": "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/04 - Synthesis/Competing Theories of Grokking.md"
    },
    {
        "id": "neural_collapse_theory",
        "label": "Neural Collapse Mathematical Theory",
        "nodes": [
            "03_literature_papyan_prevalence_of_neural_collapse",
            "03_literature_mixon_neural_collapse_with_unconstrained_features",
            "03_literature_fang_layer_peeled_model_and_minority_collapse",
            "03_literature_xu_dynamics_in_deep_classifiers_with_the_square_loss"
        ],
        "relation": "participate_in",
        "confidence": "INFERRED",
        "confidence_score": 0.95,
        "source_file": "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/04 - Synthesis/Empirical Evidence Across Studies.md"
    },
    {
        "id": "double_descent_theory",
        "label": "Double Descent and Interpolation Theory",
        "nodes": [
            "03_literature_mei_generalization_error_of_random_features_regression",
            "03_literature_rocks_memorizing_without_overfitting",
            "03_literature_spigler_a_jamming_transition_affects_generalization"
        ],
        "relation": "form",
        "confidence": "INFERRED",
        "confidence_score": 0.95,
        "source_file": "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/04 - Synthesis/Empirical Evidence Across Studies.md"
    }
]

# Deduplicate edges (same source, target, relation, source_file)
seen_edges = set()
deduped_edges = []
for edge in edges:
    key = (edge["source"], edge["target"], edge["relation"], edge["source_file"])
    if key not in seen_edges:
        seen_edges.add(key)
        deduped_edges.append(edge)

# Construct final JSON
output_data = {
    "nodes": nodes,
    "edges": deduped_edges,
    "hyperedges": hyperedges,
    "input_tokens": 0,
    "output_tokens": 0
}

# Verify output path and save
output_path = "/Users/jonathanjohn/Library/Mobile Documents/iCloud~md~obsidian/Documents/Grokking Master Thesis/graphify-out/.graphify_chunk_04.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as out:
    json.dump(output_data, out, indent=2, ensure_ascii=False)

print(f"Successfully generated knowledge graph chunk 4! Nodes: {len(nodes)}, Edges: {len(deduped_edges)}, Hyperedges: {len(hyperedges)}")
