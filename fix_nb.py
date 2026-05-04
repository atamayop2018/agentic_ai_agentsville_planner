import json

with open('project_starter.ipynb', 'r') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if 'VacationInfo' in ''.join(cell['source']):
        print(f'Cell type: {cell["cell_type"]}, has **********: {"**********" in "".join(cell["source"])}')
        print(f'Source: {cell["source"][-10:]}')  # last 10 lines