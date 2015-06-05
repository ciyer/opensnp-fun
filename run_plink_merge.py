#!/usr/bin/env python
# encoding: utf-8

import glob
import os
import subprocess

'''
Merge PLINK files into single one for filter/PCA
'''

def plink_beds():
	"""Return all PLINK BED files"""
	all_bed_files = glob.glob("../plink_binaries/*.bed")
	return all_bed_files

def plink(all_bed_files):
	tmp_file_list = open("plink_merge_list.txt","w")
	for l in all_bed_files:
		#ol = l + " " + l.replace(".bed",".bim") + " " + l.replace(".bed",".fam")+"\n"
		ol = l.replace(".bed","") + "\n"
		tmp_file_list.write(ol) 
	tmp_file_list.close()

beds = plink_beds()
plink(beds)

#run merge via plink
call = "../plink_v190/plink -bfile ../plink_binaries/2 --merge-list plink_merge_list.txt --make-bed --out merged_23andme_opensnp"
subprocess.call(call,shell=True)
