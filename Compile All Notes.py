#!/usr/bin/env python3

from pathlib import Path


def compile_obsidian_vault():
    # Use current working directory (pwd)
    vault = Path.cwd()
    output = vault / "compiled_vault.md"

    print(f"Searching for markdown files in: {vault}")

    # Recursively find all .md files
    md_files = sorted(vault.rglob("*.md"))

    # Exclude the output file itself
    md_files = [f for f in md_files if f != output]

    print(f"Found {len(md_files)} markdown files.")

    with output.open("w", encoding="utf-8") as outfile:
        outfile.write("# Compiled Obsidian Vault\n\n")
        outfile.write(f"Source: {vault}\n\n")
        outfile.write("---\n\n")

        for i, md_file in enumerate(md_files, 1):
            relative_path = md_file.relative_to(vault)

            print(f"[{i}/{len(md_files)}] {relative_path}")

            outfile.write("\n")
            outfile.write("=" * 80 + "\n")
            outfile.write(f"# FILE: {relative_path}\n")
            outfile.write("=" * 80 + "\n\n")

            try:
                content = md_file.read_text(
                    encoding="utf-8",
                    errors="replace"
                )
                outfile.write(content)
                outfile.write("\n\n")
            except Exception as e:
                outfile.write(
                    f"\n[ERROR READING FILE: {relative_path}]\n{e}\n\n"
                )

    print("\nCompilation complete.")
    print(f"Output file: {output}")


if __name__ == "__main__":
    compile_obsidian_vault()