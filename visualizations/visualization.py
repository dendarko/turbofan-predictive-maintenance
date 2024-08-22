import matplotlib.pyplot as plt
import numpy as np
import os

def plot_feature_importance(model, features, dataset_name):
    """Generate a bar plot for feature importance."""
    importance = model.coef_

    # Sort features by importance
    indices = np.argsort(importance)[::-1]
    sorted_features = [features[i] for i in indices]
    sorted_importance = importance[indices]

    plt.figure(figsize=(12, 8))
    plt.title(f"Feature Importance for {dataset_name}", fontsize=16)
    plt.barh(range(len(indices)), sorted_importance, align='center', color='skyblue')
    plt.yticks(range(len(indices)), sorted_features, fontsize=12)
    plt.xlabel('Relative Importance', fontsize=14)
    plt.gca().invert_yaxis()  # Most important feature at the top
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    plt.savefig(f'static/images/feature_importance_{dataset_name}.png', bbox_inches='tight')
    plt.close()

def plot_predictions_vs_true(y_true, y_pred, dataset_name):
    """Generate a scatter plot comparing true vs. predicted values."""
    plt.figure(figsize=(12, 8))
    plt.scatter(y_true, y_pred, edgecolors='k', color='dodgerblue', s=100, alpha=0.6, label='Predictions')
    plt.plot([min(y_true), max(y_true)], [min(y_true), max(y_true)], 'r--', lw=2, label='Perfect Prediction Line')

    plt.title(f"Predictions vs. True Values for {dataset_name}", fontsize=16)
    plt.xlabel('True Values', fontsize=14)
    plt.ylabel('Predictions', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)

    plt.savefig(f'static/images/predictions_vs_true_{dataset_name}.png', bbox_inches='tight')
    plt.close()
