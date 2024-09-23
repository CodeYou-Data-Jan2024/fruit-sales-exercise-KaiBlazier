# kaibl@KaisPC MINGW64 ~/onedrive/CodeProjects/Projects2
$ git clone https://github.com/CodeYou-Data-Jan2024/fruit-sales-exercise-KaiBlazier.git
Cloning into 'fruit-sales-exercise-KaiBlazier'...
remote: Enumerating objects: 36, done.
remote: Counting objects: 100% (19/19), done.
remote: Compressing objects: 100% (12/12), done.
remote: Total 36 (delta 11), reused 7 (delta 7), pack-reused 17 (from 1)
Receiving objects: 100% (36/36), 10.22 KiB | 10.22 MiB/s, done.
Resolving deltas: 100% (11/11), done.

$ cd fruit-sales-exercise-KaiBlazier

kaibl@KaisPC MINGW64 ~/onedrive/CodeProjects/Projects2/fruit-sales-exercise-KaiBlazier (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

kaibl@KaisPC MINGW64 ~/onedrive/CodeProjects/Projects2/fruit-sales-exercise-KaiBlazier (main)
$ nano fruitsales.csv

kaibl@KaisPC MINGW64 ~/onedrive/CodeProjects/Projects2/fruit-sales-exercise-KaiBlazier (main)
$ ls
README.md  fruitsales.csv  fruitsales.py  requirements.txt  tests.py

kaibl@KaisPC MINGW64 ~/onedrive/CodeProjects/Projects2/fruit-sales-exercise-KaiBlazier (main)
$ cat fruitsales.csv
Year,Sales1,Sales2
2017,35,21
2018,41,34


kaibl@KaisPC MINGW64 ~/onedrive/CodeProjects/Projects2/fruit-sales-exercise-KaiBlazier (main)
$ python3 -m venv venv

kaibl@KaisPC MINGW64 ~/onedrive/CodeProjects/Projects2/fruit-sales-exercise-KaiBlazier (main)
$ source venv/bin/activate
bash: venv/bin/activate: No such file or directory

kaibl@KaisPC MINGW64 ~/onedrive/CodeProjects/Projects2/fruit-sales-exercise-KaiBlazier (main)
$ python -m venv venv

kaibl@KaisPC MINGW64 ~/onedrive/CodeProjects/Projects2/fruit-sales-exercise-KaiBlazier (main)
$ pip install -r reequirments.txt
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'reequirments.txt'

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: C:\Users\kaibl\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip

kaibl@KaisPC MINGW64 ~/onedrive/CodeProjects/Projects2/fruit-sales-exercise-KaiBlazier (main)
$ ls
README.md  fruitsales.csv  fruitsales.py  requirements.txt  tests.py  venv/

kaibl@KaisPC MINGW64 ~/onedrive/CodeProjects/Projects2/fruit-sales-exercise-KaiBlazier (main)
$ source venv/bin/activate
bash: venv/bin/activate: No such file or directory

add your code here
