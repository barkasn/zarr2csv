#!/usr/bin/env python3

# Imports
import argparse

# Parse the command line
parser = argparse.ArgumentParser(description = 'Zarr to CSV converter')
parser.add_argument('-v','--verbose', help='set verbosity', action='store_true')
parser.add_argument('--inputzarr', help='input zarr file')
parser.add_argument('--output', help='output csv file')

args = parser.parse_args()

## Load other libs
import zarr
from numcodecs import blosc
import numpy as np

zarrprefix = args.inputzarr
tmpoutput = 'tmp/'

## Cell id
z_cell_id = zarr.open(zarrprefix + '/cell_id')
cell_id = z_cell_id[...]
cell_id_pd = pd.DataFrame(cell_id);
cell_id_pd.to_csv(tmpoutput+'cell_id.csv')

## Cell meta numeric
z_cell_metadata_numeric = zarr.open(zarrprefix + '/cell_metadata_numeric')
cell_metadata_numeric = z_cell_metadata_numeric[...]
np.savetxt(tmpoutput+'cell_metadata_numeric.csv',cell_metadata_numeric,delimiter=",")

## cell meta num name
z_cell_metadata_numeric_name = zarr.open(zarrprefix + '/cell_metadata_numeric_name')
cell_metadata_numeric_name = z_cell_metadata_numeric_name[...]
cell_metadata_numeric_name_pd = pd.DataFrame(cell_metadata_numeric_name)
cell_metadata_numeric_name_pd.to_csv(tmpoutput + 'cell_metadata_numeric_name.csv')

## cell meta string
z_cell_metadata_string = zarr.open(zarrprefix + '/cell_metadata_string')
cell_metadata_string = z_cell_metadata_string[...]
cell_metadata_string_pd = pd.DataFrame(cell_metadata_string)
cell_metadata_string_pd.to_csv(tmpoutput + 'cell_metadata_string.csv')

## cell meta string name
z_cell_metadata_string_name = zarr.open(zarrprefix + '/cell_metadata_string_name')
cell_metadata_string_name = z_cell_metadata_string_name[...]
cell_metadata_string_name_pd = pd.DataFrame(cell_metadata_string_name)
cell_metadata_string_name_pd.to_csv(tmpoutput + 'cell_metadata_string_name.csv')

## expression
z_expression = zarr.open(zarrprefix + '/expression')
expression = z_expression[...]
np.savetxt(tmpoutput + 'expression.csv',expression,delimiter=",")

## gene_id
z_gene_id = zarr.open(zarrprefix + '/gene_id')
gene_id = z_gene_id[...]
gene_id_pd = pd.DataFrame(gene_id)
gene_id_pd.to_csv(tmpoutput + 'gene_id.csv')
