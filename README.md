# 🔮 Revelio

**Revelio** è un laboratorio interattivo per la scoperta e la valutazione di regole interpretabili su dataset tabellari.  
Il progetto unisce un motore di rule evaluation in Python con un frontend web reattivo basato su **Shiny for Python**, offrendo un ambiente visuale per testare e validare pattern esplicativi nei dati.

---

## 🧭 Obiettivo

Revelio nasce per supportare analisti e ricercatori nel campo del **machine learning interpretabile (IML)**, consentendo di:
- Caricare dataset in formato CSV o Excel.
- Definire regole esplicite (es. `close > open and volume > 1000`).
- Valutarne la coerenza rispetto a una colonna target.
- Calcolare metriche di classificazione per validarne l’efficacia.

L’approccio è pensato per essere **modulare e trasparente**, in modo da integrarsi facilmente in pipeline di analisi o sistemi di rule learning.

---

## 🧩 Architettura

```
revelio/
├── core/
│   ├── __init__.py
│   ├── rule_engine.py      # parsing e valutazione delle regole
│   ├── metrics.py          # metriche di accuratezza, precisione, recall, ecc.
│
├── frontend/
│   ├── app_shiny.py        # interfaccia utente basata su Shiny for Python
│
├── data/                   # (facoltativo) dataset di esempio
└── README.md
```

---

## 🚀 Installazione

### 1️⃣ Clona il repository

```bash
git clone https://github.com/<tuo-username>/revelio.git
cd revelio
```

### 2️⃣ Crea un ambiente virtuale

```bash
conda create -n revelio python=3.11
conda activate revelio
```

### 3️⃣ Installa le dipendenze

```bash
pip install -r requirements.txt
```

Un file `requirements.txt` tipico può contenere:

```
shiny
pandas
openpyxl
scikit-learn
```

---

## 🧠 Utilizzo

### Avvia l’applicazione web

```bash
shiny run --reload revelio/frontend/app_shiny.py
```

Poi apri il link fornito in console (tipicamente `http://127.0.0.1:8000`) nel browser.

---

### Flusso di lavoro

1. **Carica un dataset**  
   - Supporta CSV e Excel.  
   - In caso di CSV, scegli separatore e decimale.  
   - In caso di Excel, seleziona il foglio da caricare.

2. **Seleziona la colonna target**  
   Viene popolata automaticamente in base al dataset caricato.

3. **Definisci una regola**  
   Scrivi una condizione Python-like, ad esempio:
   ```
   (close > open) & (volume > 1000)
   ```

4. **Valuta la regola**  
   Revelio calcola le metriche di classificazione rispetto al target scelto:
   - Accuracy
   - Precision
   - Recall
   - F1-score

---

## 🧱 Moduli principali

### `rule_engine.py`
Valuta espressioni logiche scritte in linguaggio naturale o Python-like, restituendo un vettore booleano corrispondente alle righe che soddisfano la regola.

### `metrics.py`
Calcola metriche standard di classificazione a partire da `y_true` e `y_pred`.

### `app_shiny.py`
Fornisce il frontend interattivo, con:
- Sidebar di configurazione
- Popup dinamici per il caricamento dati
- Anteprima del dataset
- Editor per le regole e pannello risultati

---

## 🧪 Esempio rapido

```python
from revelio.core.rule_engine import evaluate_rule
from revelio.core.metrics import compute_metrics
import pandas as pd

# Dataset di esempio
df = pd.DataFrame({
    "open": [10, 12, 9, 15],
    "close": [11, 10, 13, 14],
    "volume": [1000, 1500, 800, 2000],
    "target": [1, 0, 1, 1]
})

# Definisci una regola
mask = evaluate_rule(df, "(close > open) & (volume > 1000)")

# Calcola metriche
metrics = compute_metrics(df["target"], mask.astype(int))
print(metrics)
```

---

## 🧭 Roadmap

- [ ] Supporto per rule sets multipli e confronto visuale  
- [ ] Esportazione delle regole in formato YAML/JSON  
- [ ] Integrazione con algoritmi di rule learning (es. RuleFit, CN2)  
- [ ] Modulo di explainability per confronto tra regole e modelli ML  

---

## 🤝 Contributi

Pull request e suggerimenti sono benvenuti!  
L’obiettivo del progetto è mantenere **trasparenza e semplicità**, offrendo un ambiente aperto alla ricerca e alla collaborazione.

---

## 📜 Licenza

Distribuito sotto licenza **MIT** — vedi il file [LICENSE](LICENSE) per i dettagli.

---

> “The truth lies hidden in plain sight — you just need the right spell to reveal it.” ✨  
> — *Revelio*