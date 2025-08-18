# app.py
# Run with: marimo run app.py

import marimo

__generated_with = "0.6.0"
app = marimo.App()


# Cell 1: Imports and contact
@app.cell
def __():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    # Author: Avra (Data Scientist)
    # Contact: 24f1002255@ds.study.iitm.ac.in
    return mo, np, plt


# Cell 2: Synthetic dataset
@app.cell
def __():
    # Generate a simple dataset: x vs quadratic relation with noise
    rng = np.random.default_rng(42)
    x = np.linspace(0, 10, 200)
    noise = rng.normal(0, 2, size=x.shape)
    y = 2 * x**2 + 3 * x + 5 + noise

    # Data flows forward: (x, y) used in plots & analysis
    return x, y


# Cell 3: Interactive slider
@app.cell
def __(mo):
    # Slider for polynomial degree (variable dependency on y,x later)
    degree_slider = mo.ui.slider(1, 5, value=2, label="Polynomial Degree")

    # Output the widget so it’s visible in the UI
    return degree_slider


# Cell 4: Polynomial fitting (depends on x, y, degree_slider)
@app.cell
def __(degree_slider, np, x, y):
    # Fit polynomial of selected degree
    degree = degree_slider.value
    coeffs = np.polyfit(x, y, degree)
    poly = np.poly1d(coeffs)

    # Predicted values
    y_pred = poly(x)

    # Data flows to plotting and metrics
    return degree, coeffs, y_pred, poly


# Cell 5: Plot actual vs predicted (depends on y_pred, x, y)
@app.cell
def __(plt, x, y, y_pred, degree):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(x, y, s=15, alpha=0.6, label="Observed")
    ax.plot(x, y_pred, color="red", label=f"Polynomial deg={degree}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Polynomial Regression Fit")
    ax.legend()
    fig.tight_layout()
    fig
    return fig,


# Cell 6: Dynamic Markdown output (depends on degree, coeffs)
@app.cell
def __(mo, degree, coeffs):
    mo.md(f"""
    ### Fit Summary

    - **Selected Polynomial Degree**: {degree}
    - **Coefficients**: {coeffs}

    Increasing the degree may improve the fit (lower error) but risks **overfitting**.
    """)
    return
