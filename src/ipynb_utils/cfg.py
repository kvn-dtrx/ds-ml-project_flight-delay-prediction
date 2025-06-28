# ---
# description: Configuration settings for notebooks.
# ---

# Required imports.
import os
import subprocess
import matplotlib.pyplot as plt
from typing import Any, Dict

# ---

# General configurations

# Configuration dictionary to hold various settings.
CFG: Dict[str, Any] = {}

# Random seed for reproducibility.
CFG["RSEED"] = 42

# Matplotlib style
# CFG["PLT_STYLE"] = "fast"
# CFG["PLT_STYLE"] = "dark_background"
CFG["PLT_STYLE"] = "seaborn-v0_8-darkgrid"

# "Resolution" for stored plots.
CFG["DPI"] = 600

# Root directory of the project.
CFG["ROOT_DIR"] = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"],
    capture_output=True,
    text=True,
).stdout.strip()

# Directory for storing data, plots, and source code.
ROOT_DIR = CFG["ROOT_DIR"]
CFG["DATA_DIR"] = os.path.join(ROOT_DIR, "data")
CFG["SRC_DIR"] = os.path.join(ROOT_DIR, "src")
CFG["NOTEBOOKS_DIR"] = os.path.join(ROOT_DIR, "notebooks")

DATA_DIR = CFG["DATA_DIR"]
CFG["TRAIN_DATA_PATH"] = os.path.join(DATA_DIR, "train.csv")
CFG["AIRPORTS_DATA_PATH"] = os.path.join(DATA_DIR, "airports.csv")
CFG["PROCESSED_DATA_PATH"] = os.path.join(DATA_DIR, "df.pkl")

NOTEBOOKS_DIR = CFG["NOTEBOOKS_DIR"]
CFG["PLOTS_DIR"] = os.path.join(NOTEBOOKS_DIR, "plots")
CFG["LOGS_DIR"] = os.path.join(NOTEBOOKS_DIR, "logs")

# ---

# Matplotlib style

# Basic matplotlib style settings
PLT_STYLE = CFG["PLT_STYLE"]
try:
    plt.style.use(PLT_STYLE)
except:
    print("Could not load the specified matplotlib style:")
    print(PLT_STYLE)
    print("Default style will be used")

plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.titlesize"] = 18
plt.rcParams["axes.labelsize"] = 12
plt.rcParams["axes.labelweight"] = "bold"
# plt.rcParams["axes.labelcolor"] = "white"

plt.rcParams["figure.dpi"] = 600
plt.rcParams["figure.figsize"] = (10, 5)
plt.rcParams["savefig.format"] = "svg"
plt.rcParams["savefig.dpi"] = 600

plt.rcParams["grid.color"] = "gray"
plt.rcParams["grid.linestyle"] = "--"

plt.rcParams["xtick.labelsize"] = 10
plt.rcParams["ytick.labelsize"] = 10
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"

plt.rcParams["legend.loc"] = "upper right"
plt.rcParams["legend.frameon"] = False

plt.rcParams["lines.linewidth"] = 2
plt.rcParams["lines.markersize"] = 8
