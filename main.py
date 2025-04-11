def best_first_search(graph, depart, but):
    """
    Implémentation de l'algorithme Best-First Search pour un graphe pondéré.

    Args:
        graph: Le graphe représenté comme un dictionnaire d'adjacence
        depart: Le nœud de départ
        but: Le nœud objectif

    Returns:
        Un tuple (chemin, coût_total) si une solution est trouvée, (None, 0) sinon
    """
    # Initialiser la liste ouverte avec le nœud de départ
    # Format: (coût_actuel, noeud, chemin)
    liste_ouverte = [(0, depart, [depart])]
    visites = set()

    print(f"Initialisation:")
    print(f"Liste ouverte: {[item for item in liste_ouverte]}")
    print(f"Nœuds visités: {visites}\n")

    while liste_ouverte:
        # Trier la liste selon le coût actuel (premier élément du tuple)
        liste_ouverte.sort(key=lambda x: x[0])

        # Extraire le nœud avec le coût le plus bas
        cout_actuel, noeud, chemin = liste_ouverte.pop(0)

        # Si ce nœud est l'objectif, retourner la solution
        if noeud == but:
            visites.add(noeud)
            print(f"Liste ouverte: {[item for item in liste_ouverte]}")
            print(f"Nœuds visités: {visites}")
            print(f"Solution trouvée: {' -> '.join(chemin)}, Coût total: {cout_actuel}")
            return chemin, cout_actuel

        # Ignorer si déjà visité
        if noeud in visites:
            continue

        # Marquer comme visité
        visites.add(noeud)

        # Générer les successeurs
        for voisin, poids in graph.get(noeud, []):
            if voisin not in visites:
                nouveau_chemin = chemin + [voisin]
                nouveau_cout = cout_actuel + poids
                liste_ouverte.append((nouveau_cout, voisin, nouveau_chemin))

        print(f"\nNœud traité: {noeud}")
        print(f"Liste ouverte: {[item for item in liste_ouverte]}")
        print(f"Nœuds visités: {visites}")

    # Si la liste est vide et qu'aucune solution n'a été trouvée
    print("\nÉchec: aucun chemin trouvé.")
    return None, 0


# Définition du graphe
graph = {
    'S': [('A', 5), ('B', 2), ('C', 4)],
    'A': [('D', 9), ('E', 4)],
    'B': [('G', 6)],
    'C': [('F', 2)],
    'D': [('H', 7)],
    'E': [('G', 6)],
    'F': [('G', 1)],
    'G': [],
    'H': []
}

# Exécution de l'algorithme
print("=== Best-First Search ===")
start_node = 'S'
goal_node = 'G'
solution_path, total_cost = best_first_search(graph, start_node, goal_node)

if solution_path:
    print("\n=== Résultat final ===")
    print(f"Chemin optimal: {' -> '.join(solution_path)}")
    print(f"Coût total: {total_cost}")
else:
    print("\nAucun chemin trouvé entre le nœud de départ et l'objectif.")