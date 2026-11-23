"""Entry for One Word, First Thought: writes the entry text to /output/entry.txt."""
import os
ENTRY = 'Petrichor'
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
print("wrote /output/entry.txt", len(ENTRY), "chars")
