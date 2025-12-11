import json

# Load the notebook
with open('BigData_Project_Complete.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Extract actual outputs
cells = notebook['cells']

print("=== EXTRACTING ACTUAL OUTPUTS ===\n")

for i, cell in enumerate(cells):
    if cell['cell_type'] == 'code':
        outputs = cell.get('outputs', [])
        if outputs:
            source_preview = ''.join(cell.get('source', []))[:60]
            print(f"\nCell {i}: {source_preview}...")
            
            for out in outputs:
                if out.get('output_type') == 'stream':
                    text = ''.join(out.get('text', []))
                    print(f"  OUTPUT: {text[:200]}")
                elif out.get('output_type') == 'display_data':
                    if 'text/plain' in out.get('data', {}):
                        plain_text = ''.join(out['data']['text/plain'])
                        print(f"  DISPLAY: {plain_text[:200]}")
