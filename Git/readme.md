## Kurze Einführung in Git und Github
### Hilfreiche Links: 
[Git](https://git-scm.com/downloads) |
[Github](https://github.com) |
[Youtube Tutorial](https://www.youtube.com/playlist?list=PL4cUxeGkcC9goXbgTDQ0n_4TBzOO0ocPR)

### Befehle
Initialisiere ein Git Repository:

`git init`

Füge Dateien zum Repository hinzu:

`git add .`

Prüfe Status des Git Repository:

`git status`

Schreibe einen Stand in das Repository:

`git commit -m "initial commit"`

Prüfe commits:

`git log --oneline`

Lade einen alten Stand:

`git checkout <commit number>`

Füge ein externes Git Repository z.B. Github hinzu:

`git remote add origin https://github.com/Marco-Meo/test.git`

`git branch -M main`

`git push -u origin main`