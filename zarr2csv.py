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

## Open the input file
z1 = zarr.open(args.inputzarr)

## get entire thing as nusmpy array
np0 = z1[...]
#np0 = np.array(x)

if (np0.ndim != 2):
    sys.exit(1);
    
#np1 = np.array(np0)
## Save in native numpy
## This can't be loaded in R due to segfault
#np.save("output.npy",np0)

## Save the output as a csv file
np.savetxt(args.output,np0,delimiter=",")
