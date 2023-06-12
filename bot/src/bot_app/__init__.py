import logging

"""Imports in __init__.py are performed to prepare the module for use and to provide ease of managing imports in the project.

from .app import dp: means you are importing the dp object from the app module, which is in the same package as __init__.py. Relative import from . points to the current package or module.

from . import commands: means that you are importing the commands module from the current package, which is in the same package as __init__.py. This allows you to use functions, classes, or other objects that are defined in the commands module inside the current package.

Using such imports in __init__.py allows you to conveniently organize your package's modules and provides convenient navigation and use of objects from other modules within the package."""

from .app import dp
from . import commands, random_ten, one_by_one

# Enable logging at the INFO level
logging.basicConfig(level=logging.INFO)