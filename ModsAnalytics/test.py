import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from pandastable import Table
import pandas as pd
import matplotlib.pyplot as plt

def check_last_updated_type(file_path):
    df = pd.read_csv(file_path)

    invalid_indexes = []
    for i, val in enumerate(df["last_updated"]):
        try:
            float(val)
        except (ValueError, TypeError):
            invalid_indexes.append(i)

    if not invalid_indexes:
        print("All values can be and were converted to float data-type")
    else:
        print("Non-float-compatible values found at indexes:", invalid_indexes)

    return invalid_indexes

check_last_updated_type("finalfile.csv")

