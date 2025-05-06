# 🎓 Analyse Factorielle Discriminante des Universités Françaises

Ce projet explore les caractéristiques d'insertion professionnelle des diplômés de Master dans les universités françaises à travers une **Analyse Factorielle Discriminante (AFD)**. L'objectif principal est de **comparer les établissements** afin de détecter des **groupes d’universités similaires** et mettre en évidence les **facteurs discriminants**.

---

## 📊 Données utilisées

Les données proviennent de l'enquête nationale sur l'insertion professionnelle des diplômés de Master, coordonnée par le ministère de l'Enseignement supérieur et de la Recherche.

### 🔎 Contenu des données
Les variables décrivent la situation professionnelle des diplômés 30 mois après l'obtention de leur diplôme, pour les sessions 2010 et 2011.

**Extraits des variables incluses :**
- `taux_dinsertion` : taux d’insertion global
- `emplois_cadre`, `emplois_stables`, `emplois_a_temps_plein` : qualité de l'emploi
- `salaire_net_median_des_emplois_a_temps_plein`, `salaire_brut_annuel_estime` : niveaux de salaire
- `femmes`, `de_diplomes_boursiers` : données sociodémographiques
- `emplois_exterieurs_a_la_region_de_luniversite` : mobilité géographique
- `taux_de_chomage_regional`, `salaire_net_mensuel_median_regional` : contexte socio-économique local

**Source officielle :** Ministère de l’Enseignement Supérieur (MENESR)

---

## 🎯 Objectifs du projet

- Réaliser une **analyse comparative** des universités françaises sur la base de l'insertion professionnelle de leurs diplômés.
- Identifier les **universités similaires** en termes de performances à l’insertion.
- Déterminer les **facteurs discriminants** entre les groupes d’universités.
- Proposer une **cartographie visuelle** de ces proximités ou différences.

---

## 🧠 Intérêt de l’étude

### Pour les étudiants :
- Aide à l’orientation : choisir une université en fonction des débouchés réels.
- Meilleure connaissance des dynamiques régionales d’emploi post-Master.

### Pour les établissements :
- Se comparer à d'autres universités.
- Identifier des axes d’amélioration pour l’insertion des diplômés.

### Pour les décideurs :
- Éclairer des politiques publiques sur l’enseignement supérieur.

---

## 🧮 Méthodologie : Analyse Factorielle Discriminante (AFD)

L'AFD est une méthode multivariée permettant :
- de **projeter des observations (universités)** dans un espace de faible dimension (2D) tout en **maximisant la séparation entre groupes**,
- d’**interpréter visuellement** les proximités/différences entre groupes selon les variables discriminantes.

---

## 🧪 Extrait de code (Python)

Voici un exemple d’analyse en Python avec `pandas`, `scikit-learn` et `matplotlib` :

```python
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Charger les données
df = pd.read_csv("donnees_insertion_universites.csv")

# Supposons que 'groupe_region' est la variable de regroupement des universités
X = df.drop(columns=["nom_universite", "groupe_region"])
y = df["groupe_region"]

# Normalisation
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# AFD (LDA en anglais)
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)

# Visualisation
plt.figure(figsize=(10, 6))
for label in y.unique():
    plt.scatter(X_lda[y == label, 0], X_lda[y == label, 1], label=label)
plt.title("Analyse Factorielle Discriminante des Universités")
plt.xlabel("LD1")
plt.ylabel("LD2")
plt.legend()
plt.grid()
plt.show()
