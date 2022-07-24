# dhbw-machine-learning
Ich generiere Elon Musk Tweets mit Transfer learning. Das Modell wurde anhand einer Umfrage in einem Unikurs evaluiert.
In `musk.ipynb` befindet sich das dokumentierte Notebook, mit dem die Daten vorverarbeitet wurden und das Modell erstellt wurde.
Um es auszuführen müssen die Abhängigkeiten aus `requirements.txt` installiert werden.
Im Ordner Server befindet sich der Server mit dem die Website für die Umfrage betrieben wird.
Es gibt eine Datei `server_live.py`, mit der der Server die Tweets live generiert und einen server `server_database.py`, mit dem die Tweets aus der Datenbank abgerufen werden.
Im Ordner `data` befindet sich ein Dump der Datenbank mit den Umfrageergebnissen.