import os
import time

print('As dependências estão sendo instaladas...')

time.sleep(1)

deps = ['pip install bcrypt']

for dep in deps:
    os.system(dep)