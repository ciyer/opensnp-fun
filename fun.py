#!/usr/bin/env python
# encoding: utf-8

"""Scratch pad for 23 and me data
"""

import parse23andme
import glob
import os
import data_utilities


def twenty3_and_me_files():
    """Return the opensnp files that are 23 and me format"""
    all_twenty3_and_me_files= glob.glob('../opensnp_datadump.current/*.23andme.txt')
    fifteen_mb = 15 * 1000 * 1000
    non_junk_files = [path for path in all_twenty3_and_me_files if os.path.getsize(path) > fifteen_mb]
    return non_junk_files


def subsample():
    """Subsample the full data set"""
    subset = twenty3_and_me_files()[0:10]
    parsed = parse23andme.ParseToDict(subset)
    return parsed

def delink_chromosomes():
    # Get some data for working with
    data_set = subsample()
    # Group all the snps by chromosome and sort by location
    chromosomes = data_utilities.sorted_snps_by_chromosome(data_set)
    # Delink the snps on the chromosome so we can feed it into PCA
    delinked_chromosomes = dict((k, data_utilities.discard_correlated_snps(v)) for k, v in chromosomes.items())


