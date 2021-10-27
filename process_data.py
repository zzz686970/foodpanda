import yaml 
import sys
import subprocess

"""execute sql query

open yaml file and execute sql queries
"""

with open('question.yaml', 'r') as f:
    try:
        data = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        print(exc)
        sys.exit()
    

for key, value in data.items():
    # print(value['query'])
    query = value['query']
    cmd = f"""bq query --use_legacy_sql=false '{query}'"""
    subprocess.run(cmd, shell=True)