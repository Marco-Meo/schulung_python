# Installation


Download und Installation Python
https://www.python.org

Wir nutzen die Version 3.8.x

####Terminal: 

`python –version`

####Virtual environment:

[Dokumentation](https://virtualenv.pypa.io/en/stable/index.html)

`python -m pip install --user virtualenv`

`virtualenv venv`

`venv\scripts\activate`

####Download und Installation git (Versionsverwaltung)

`https://git-scm.com/downloads`

#####Terminal:

`mkdir schulung_python`

`cd schulung_python`

`git clone https://github.com/Marco-Meo/schulung_python.git`

#### Installation weiterer librarys mit pip
`pip install pandas`

##### Liste der installierten librarys
`pip list`

##### Erstellen einer requirements.txt Liste
`pip freeze -> requirements.txt`

##### Laden einer requirements.txt Datei
`pip install -r requirements.txt`