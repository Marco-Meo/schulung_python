# Jupyter Notebook

[Dokumentation](https://jupyter-notebook.readthedocs.io/en/latest/?badge=latest)

Installation mit pip

`pip install jupyter`

Starte Jupyter notebook server

`jupyter notebook`


## Tipps und Tricks
Anzeigen von lokalen Dateien
```
In [1]: !ls
example.jpeg list tmp
In [2]: !pwd
/home/Parul/Desktop/Hello World Folder'
In [3]: !echo "Hello World"
Hello World
```
Diese können auch in Variablen gespeichert werden:
```
In [4]: files= !ls
In [5]: print(files)
['example.jpeg', 'list', 'tmp']
In [6]: directory = !pwd
In [7]: print(directory)
['/Users/Parul/Desktop/Hello World Folder']
In [8]: type(directory)
IPython.utils.text.SList
```

## Installation von Erweiterungen
`pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install`

### Empfohlene Erweiterungen
- Hinterland
- Snippets
- Table of Contents