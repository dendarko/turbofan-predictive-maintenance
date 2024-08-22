import matplotlib.pyplot as plt
import numpy as np
import os

def plot_feature_importance(model, features, dataset_name):
    """Generate a bar plot for feature importance."""
    importance = model.coef_
    indices = np.argsort(importance)

    plt.figure(figsize=(10, 6))
    plt.title(f"Feature Importance for {dataset_name}")
    plt.barh(range(len(indices)), importance[indices], align='center')
    plt.yticks(range(len(indices)), [features[i] for i in indices])
    plt.xlabel('Relative Importance')
    plt.savefig(f'static/images/feature_importance_{dataset_name}.png')
    plt.close()

def plot_predictions_vs_true(y_true, y_pred, dataset_name):
    """Generate a scatter plot comparing true vs. predicted values."""
    plt.figure(figsize=(10, 6))
    plt.scatter(y_true, y_pred, edgecolors=(0, 0, 0))
    plt.plot([min(y_true), max(y_true)], [min(y_true), max(y_true)], 'k--', lw=3)
    plt.title(f"Predictions vs. True Values for {dataset_name}")
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.savefig(f'static/images/predictions_vs_true_{dataset_name}.png')
    plt.close()
