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
  - Verifica che i tempi dovrebbero essere proporzionali a $O(N^3)$ per la DCT2 fatta in casa e a $O(N^2\log (N))$ per la versione fast ottenuta realizzata da una libreria già fatta(`cv2`)
  - I test sono stati fatti su matrici contenti numeri casuali da 0 a 255 delle seguente dimensioni  $\left[\begin{matrix}320\times320&640\times640&1280\times1280&2560\times2560&5120\times5120\\\end{matrix}\right]$
- `verifyDCT.py`
  - Test fittizi per verificare la correttezza sia per la DCT monodimensionale, sia per quella bidimensionale, effettuati controlli anche su quella inversa
