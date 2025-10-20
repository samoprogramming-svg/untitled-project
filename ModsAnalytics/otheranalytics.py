'''

import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from pandastable import Table
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

df = pd.read_csv("finalfile.csv")

# Ensure downloads are numeric
df["downloads"] = pd.to_numeric(df["downloads"], errors="coerce")

# Group by author and sum downloads, take top 5
top5 = df.groupby("author_name")["downloads"].sum().sort_values(ascending=False).head(5)

# Plot
ax = top5.plot(kind="bar")
plt.xlabel("Author")
plt.ylabel("Total Downloads")
plt.title("Top 5 Authors by Total Downloads")
plt.xticks(rotation=0)

# Add total downloads on top/left of each bar
for i, v in enumerate(top5):
    ax.text(i, v, str(int(v)), ha='right', va='center')

plt.tight_layout()
#plt.show()
'''

'''
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("finalfile.csv")

# Ensure downloads are numeric
df["downloads"] = pd.to_numeric(df["downloads"], errors="coerce")

# Take top 5 mods by downloads
top5_mods = df.sort_values("downloads", ascending=False).head(5)

# Plot
plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(top5_mods)), top5_mods["downloads"], color="purple")

# Set X-axis ticks to be the mod names, centered under each bar
plt.xticks(range(len(top5_mods)), top5_mods["mod_name"], rotation=0, ha='center')

plt.xlabel("Mod Name")
plt.ylabel("Downloads")
plt.title("Top 5 Mods by Downloads")

# Add download numbers on top of each bar
for i, v in enumerate(top5_mods["downloads"]):
    plt.text(i, v, str(int(v)), ha='center', va='bottom')

plt.tight_layout()
plt.show()

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Optional: to show plots inline if you're using Jupyter Notebook
# %matplotlib inline

# Example DataFrame structure:
# df = pd.read_csv('your_mod_data.csv')
# For now, we assume your DataFrame `df` has these columns:
# ['Mod Name', 'Author', 'Downloads', 'Year', 'Description', 'Mod URL', 'Author URL', 'Version']

df = pd.read_csv("DataFrames/finalfile.csv")

top_authors = df.groupby('author_name')['downloads'].sum().sort_values(ascending=False).head(5)
others = df[~df['author_name'].isin(top_authors.index)]['downloads'].sum()

pie_data = top_authors.copy()
pie_data['Others'] = others

# Format labels to show both % and raw values
def format_label(pct, allvals):
    absolute = int(pct / 100. * sum(allvals))
    return f'{pct:.1f}%\n({absolute:,})'

plt.figure(figsize=(8, 8))
plt.pie(pie_data, labels=pie_data.index,
        autopct=lambda pct: format_label(pct, pie_data),
        startangle=140)
plt.title('Share of Downloads: Top 5 Authors vs Others')
plt.tight_layout()
plt.show()


