# -*- coding: utf-8 -*-
from pathlib import Path
text = Path("utils.py").read_bytes().decode("utf-8", errors="ignore")
print("found?", "、EThoughts】" in text)
