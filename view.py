"""
created 9/25/20

@author: akreitz
"""

import tkinter as tk
from tkinter import ttk

class View(tk.Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

    def main(self):
        print("in View's main")