import json
import os
from pathlib import Path

# Load Setting JSON.
current = os.path.dirname(__file__)
file = os.path.join(current, 'setting.json')
json_open = open(file, 'r')
load = json.load(json_open)

p = Path(__file__)
root = p.parents[2]

# Make SQL string from modulars.
sql = ''
for module in load['modulars']:
  init_file = os.path.join(root, 'modulars', module, 'sql', 'init.sql')
  
  if not os.path.exists(init_file):
    continue

  with open(init_file, 'r', encoding="utf-8") as f:
    sql += f.read()
    sql += '\n'


# Make inittialize sql file.
init_sql = os.path.join(root, 'infrastructure', 'database', 'init', 'init.sql')
print(init_sql)
if os.path.exists(init_sql):
  os.remove(init_sql)

with open(init_sql, 'w', encoding="utf-8") as f:
  f.write(sql)