# 🔍 Best First Search (Recherche Meilleur d'Abord)

Ce projet implémente l'algorithme de recherche "Best First Search" en Python à l'aide d'une structure de graphe pondéré. Il permet de trouver un chemin vers un objectif en choisissant toujours le nœud ayant le plus petit coût heuristique estimé.

## 📁 Structure du projet

Best-First-Search/ ├── main.py # Script principal contenant le graphe et l’algorithme ├── README.md # Ce fichier

python
Copy
Edit

## 🚀 Fonctionnalités

- Définition d’un graphe orienté pondéré
- Tri des successeurs selon le coût
- Fonction `nextSommet()` pour obtenir le prochain nœud à visiter
- Fonction `isObjectif()` pour vérifier si un nœud est un objectif
- Affichage clair du graphe après tri

## 🧠 Extrait de code

```python
graph = {
    'S': [('A', 5), ('B', 2), ('C', 4)],
    'A': [('D', 9), ('E', 4)],
    ...
}

def nextSommet(a):
    return a[0][0]

def isObjectif(a):
    return not graph[a]
📌 Prérequis
Python 3.x

▶️ Exécution
Pour exécuter le programme :

bash
Copy
Edit
python main.py
📚 Références
Wikipedia - Best First Search

AI Algorithms

🧑‍💻 Auteur
Youssef Khalifa
