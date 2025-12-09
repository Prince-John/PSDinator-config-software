"""
plot_loader.py — dynamic loader for visualization plot modules.

Searches visualizer_app.plots for any .py file containing a class
that inherits from BasePlot, ignoring BasePlot itself.
"""

import importlib
import pkgutil
from visualizer_app.core.base_plot import BasePlot


def load_plot_classes(package: str = "visualizer_app.plots"):
    """
    Discover all plot classes inside the given package.

    Returns
    -------
    List[type]
        A list of classes (not instances) that inherit from BasePlot.
    """
    plot_classes = []

    # Import the package that contains the plot modules
    pkg = importlib.import_module(package)

    # Iterate over all modules under visualizer_app.plots
    for finder, module_name, ispkg in pkgutil.iter_modules(pkg.__path__):
        full_module = f"{package}.{module_name}"

        module = importlib.import_module(full_module)

        # Scan module for classes that inherit BasePlot
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if (
                    isinstance(attr, type)
                    and issubclass(attr, BasePlot)
                    and attr is not BasePlot
            ):
                plot_classes.append(attr)

    return plot_classes
