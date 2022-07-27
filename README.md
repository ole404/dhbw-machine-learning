# dhbw-machine-learning
Ich generiere Elon Musk Tweets mit Transfer learning. Das Modell wurde anhand einer Umfrage in einem Unikurs evaluiert.
In `musk.ipynb` befindet sich das dokumentierte Notebook, mit dem die Daten vorverarbeitet wurden und das Modell erstellt wurde.
Um es auszuführen müssen die Abhängigkeiten aus `requirements.txt` installiert werden.
Im Ordner Server befindet sich der Server mit dem die Website für die Umfrage betrieben wird.
Es gibt eine Datei `server_live.py`, mit der der Server die Tweets live generiert und einen server `server_database.py`, mit dem die Tweets aus der Datenbank abgerufen werden. Aus Konventionsgründen sollten diese vor dem Ausführen in `main.py` umbenannt werden.
Im Ordner `data` befindet sich ein Dump der Datenbank mit den Umfrageergebnissen.

##Anleitung ausführen
Mac: 
`pip install -r requirements_mac.txt`
Windows, Linux
`pip install -r requirements.txt`
Beide dateien unterscheiden sich darin, dass Fall von Mac-OS Tensorflow-Mac benutzt wird, weil dies in einigen Fällen die Hardware Beschleunigung unterstützt.
Diese ist allerdings nur bedingt für dieses Training zu empfehlen, weil Tensorflow den verbrauchten V-RAM nicht begrenzt und MacOS shared Memory hat. Dadurch werden die Dateien in den SWAP abgelegt und es kann zum Systemabsturz kommen.


## Anleitung Training
Es müssen dafür lediglich alle Zellen des Notebooks bis zum Kapitel "Modelle laden und Inferencing" ausgeführt werden.
Es ist jedoch nicht empfohlen dieses ohne eine dedizierte GPU durchzuführen, weil es sehr Ressourcen intensiv ist. Zudem müssen beide Hyperparameter Optimierungen getrennt durchgeführt werden (Der Jupyter Server muss neugestartet werden), weil es sonst zu einen `RessouceExhaustion`-Runtime-Error kommt.

## Anleitung Out of Sample
Out of Sample bedeutet in diesem Fall einfach Text generieren.
Dafür müssen die fertigen Modelle [hier](https://owncloud.dhbw-stuttgart.de/index.php/s/csd6kSQYypcWPgE) heruntergeladen werden und in den Ordner `musk` entpackt werden.
Dafür muss die erste Zelle mit den Imports im Notebook ausgeführt werden und dann die Zelen ab "Modelle laden und Inferencing"
Da gibt es dann einige Beispiele für Text-Generierung.

Falls der Download link nicht funktioniert, bitte per Mail an mich wenden.