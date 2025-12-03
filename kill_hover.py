#!/usr/bin/env python3
"""
Remove ALL hover tooltips completely - make them truly invisible.
"""

from pathlib import Path
import re

def fix_file(filepath):
    """Fix a single HTML file to completely disable hover tooltips."""
    print(f"Processing: {filepath.name}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the Plotly.relayout section to completely disable hover
    old_pattern = r"Plotly\.relayout\(div,\s*\{[^}]*'hovermode'[^}]*\}\);"
    
    new_code = """Plotly.relayout(div, {
                    'hovermode': false
                });"""
    
    if re.search(old_pattern, content):
        content = re.sub(old_pattern, new_code, content, flags=re.DOTALL)
        print(f"  ✓ Disabled hover tooltips in {filepath.name}")
    else:
        print(f"  ⚠ Pattern not found in {filepath.name}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    script_dir = Path(__file__).parent
    html_files = list(script_dir.glob('interactive_*.html'))
    
    print(f"Found {len(html_files)} files\n")
    
    for filepath in html_files:
        try:
            fix_file(filepath)
        except Exception as e:
            print(f"  ✗ Error: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\n✓ Done!")

if __name__ == '__main__':
    main()
