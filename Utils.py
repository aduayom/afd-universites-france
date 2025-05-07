import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution_by_quantile(data, col, quantiles, bins=20, figsize=(12, 6)):
    """
    Plot the distribution of a continuous variable by quantiles.

    Parameters:
    - data: pandas DataFrame containing the data.
    - col: str, the name of the continuous variable to plot.
    - quantiles: list of str, the quantile categories to consider (e.g., ['C1', 'C2', ..., 'C10']).
    - bins: int, the number of bins for the histogram (default: 20).
    - figsize: tuple, the size of the figure (default: (12, 6)).
    """
    plt.figure(figsize=figsize)
    
    # Create a subplot for each quantile
    for i, q in enumerate(quantiles, 1):
        plt.subplot(2, 5, i)
        subset = data[data[f'{col}_categorie'] == q]
        sns.histplot(subset[col], kde=True, bins=bins)
        plt.title(f'Quantile {q}')
        plt.xlabel(col)
        plt.ylabel('Fréquence')
    
    plt.suptitle(f'Distribution de {col} par quantile', y=1.02)
    plt.tight_layout()
    plt.show()

# Example usage
#plot_distribution_by_quantile(data, 'taux_de_chomage_regional', ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10'])


# Fonction pour calculer les statistiques par quantile
def analyse_cluster(data, variable):
    stats = data.groupby(f'{variable}_categorie')[variable].agg(
        ['count', 'mean', 'median', 'min', 'max']
    ).rename(columns={
        'count': 'Nombre d\'observations',
        'mean': 'Moyenne',
        'median': 'Médiane',
        'min': 'Minimum',
        'max': 'Maximum'
    }).sort_values("Moyenne")  # 🔁 tri ici
    return stats

# Afficher les statistiques pour chaque variable
'''for col in variables_continues:
    print(f"\n🔍 Statistiques pour {col} par quantile:")
    display(analyse_cluster(data, col))'''