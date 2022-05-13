"""
plugins_flags.py
------------

Plugin Managing Utility.
"""

from __future__ import annotations

import pkg_resources

from manim import console

__all__ = ["list_plugins"]


"""
It returns a dictionary of all the plugins that are installed
:return: A dictionary of plugins.
"""


def get_plugins():
    plugins = {
        entry_point.name: entry_point.load()
        for entry_point in pkg_resources.iter_entry_points("manim.plugins")
    }
    return plugins


'''
This code is printing a list of all the plugins that are currently loaded
'''


def list_plugins():
    console.print("[green bold]Plugins:[/green bold]", justify="left")

    plugins = get_plugins()
    for plugin in plugins:
        console.print(f" • {plugin}")
