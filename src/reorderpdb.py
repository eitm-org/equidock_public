import sys
import glob
import os
import pandas as pd
from biopandas.pdb import PandasPdb

def reorder_pdb(ppdb_obj, output_pdb):

    atom_df = ppdb_obj.df['ATOM'].copy()
    atom_df['atom_number'] = pd.to_numeric(atom_df['atom_number'], errors='coerce')
    atom_df = atom_df.sort_values(by='atom_number', na_position='last').reset_index(drop=True)
    
    atom_df['line_idx'] = range(1, len(atom_df) + 1)
    ppdb_obj.df['ATOM'] = atom_df
    os.makedirs(os.path.dirname(output_pdb) or '.', exist_ok=True)
    ppdb_obj.to_pdb(path=output_pdb, records=['ATOM'], gz=False, append_newline=True)