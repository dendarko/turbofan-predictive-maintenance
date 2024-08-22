import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

sns.set(style="whitegrid")  # Set the seaborn style

def plot_feature_importance(model, features, dataset_name):
    """Generate a bar plot for feature importance."""
    importance = model.coef_

    # Sort features by importance
    indices = np.argsort(importance)[::-1]
    sorted_features = [features[i] for i in indices]
    sorted_importance = importance[indices]

    plt.figure(figsize=(12, 8))
    sns.barplot(x=sorted_importance, y=sorted_features, palette="coolwarm")
    plt.title(f"Feature Importance for {dataset_name}", fontsize=16)
    plt.xlabel('Relative Importance', fontsize=14)
    plt.ylabel('Features', fontsize=14)

    plt.savefig(f'static/images/feature_importance_{dataset_name}.png', bbox_inches='tight')
    plt.close()

def plot_predictions_vs_true(y_true, y_pred, dataset_name):
    """Generate a scatter plot comparing true vs. predicted values."""
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x=y_true, y=y_pred, color='dodgerblue', s=100, edgecolor='k', alpha=0.6)
    sns.lineplot(x=y_true, y=y_true, color='red', linestyle='--', lw=2)  # Perfect prediction line

    plt.title(f"Predictions vs. True Values for {dataset_name}", fontsize=16)
    plt.xlabel('True Values', fontsize=14)
    plt.ylabel('Predictions', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.savefig(f'static/images/predictions_vs_true_{dataset_name}.png', bbox_inches='tight')
    plt.close()
