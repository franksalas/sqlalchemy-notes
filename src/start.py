
# required
import pandas as pd
import numpy as np

# Pandas options
pd.set_option('max_columns', 1000)
pd.set_option('max_rows', 100)
pd.set_option('display.max_colwidth', 100)


# database
import sqlalchemy

# python
import sys,os
import re
import glob
import pickle
# Visualization

# seaborn
# import seaborn as sns
# sns.set(rc={'figure.figsize':(10,5)})
# import matplotlib.pyplot as plt
# import matplotlib
# increase size of standar plots
#plt.rcParams["figure.figsize"] = [10, 5]
#plt.style.use('ggplot')

# # plotly
# import plotly
# import plotly.graph_objs as go
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# init_notebook_mode(connected=True)

# plot save paths

print(f'''
python\t{sys.version}
---------------------
Versions:
----------------------
pandas      {pd.__version__}
numpy       {np.__version__}
sqlalchemy  {sqlalchemy.__version__}
----------------------
''')

print('''
Loaded Libraries
-------------------
import pandas as pd
import numpy as np
import sys,os
import re
import glob
----------------


GLOBAL VARIABLES
--------------------------

SRC_DIR: list files in `src\` directory
------------------------------


source file: src/start.py

''')

# GLOBAL VARIABLES
# --------------------------
# HERE_DIR: list current directory path
# RAW_DIR: list files in `data\\raw` directory
# INTER_DIR: list files in `data\\interim` directory
# FINAL_DIR: list files in `data\\processed` directory
# SRC_DIR: list files in `src\` directory
# ------------------------------
# source file: src/start.py


