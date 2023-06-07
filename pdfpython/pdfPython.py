#%%
# vanaf die volgende bron:
# https://realpython.com/creating-modifying-pdf/

# Om te gebruik installeer pypdf:
# $ python -m pip install pypdf

#%%
from pypdf import PdfReader
from pathlib import Path
import os as os

#%%
pdf_path = (
    Path().absolute()
    / "Pride_and_Prejudice.pdf"
)

# %%
pdf_reader = PdfReader(pdf_path)
# %%
print(len(pdf_reader.pages))


# %%
