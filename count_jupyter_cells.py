import json
# def jupyter_cells(file_abs_path: str) -> int:

try:
    with open('/Users/imran-m/MLflow-project/mlflow_experiments_bayesiansearch_hp_tuning.ipynb', 'r') as file:
        notebook_data = json.load(file)
        print(f'Total cells: {len(notebook_data['cells'])}')

except FileNotFoundError as error:
    print(error)
        
