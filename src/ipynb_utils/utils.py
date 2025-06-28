# ---
# description: Utility functions for notebooks.
# ---

import os
import matplotlib.pyplot as plt
from ipynb_utils.cfg import CFG


def plt_savefig(
    core: str,
    extension: str = ".png",
    dir: str = CFG["PLOTS_DIR"],
    dpi: int = CFG["DPI"],
    bbox_inches: str = "tight",
) -> None:
    name = core + extension
    path = os.path.join(dir, name)
    plt.savefig(path, dpi=dpi, bbox_inches=bbox_inches)
