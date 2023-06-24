# Progetto Metodi del Calcolo Scientifico ~ Compressione di immagini

## Descrizione rapida dei file

- `README.md`
  - Descrizione tecnica del progetto
- `utils.py`
  - Definizione di funzioni utili all'aplicazione
- `interface.py`
  - File eseguibile dove viene costriutata l'interfaccia dell'applicazione che richiama i dovuti metodi per la compressione delle immagini
- `DCT.py`
  - File di implentazione della libreria custom sulla DCT
- `testTimeDCT.py`
  - Verifica che i tempi dovrebbero essere proporzionali a $N^3$ per la DCT2 fatta in casa e a $N^2$ per la versione fast ottenuta realizzata da una libreria già fatta (`scipy`)
- `verifyDCT.py`
  - Test fittizi per verificare la correttezza sia per la DCT monodimensionale, sia per quella bidimensionale

## ToDo

Aggiornato a 05/06/2023

- [ ] Realizzazione della libreria che permetterà la compressione delle immagini
- [ ] Realizzazione dell'interfaccia della applicazione
  - [ ] possibilità di salvare l'immagine compressa
