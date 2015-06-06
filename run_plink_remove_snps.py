#!/usr/bin/env python
# encoding: utf-8

import glob
import os
import subprocess

'''
Remove bad 23andMe SNPs 
PLINK format
'''

def twenty3_and_me_files():
	all_twenty3_and_me_files= glob.glob('../plink_binaries/*.bed')
	return all_twenty3_and_me_files


def run_plink_format(usable_files):
	'''Get data out!'''
	for f in usable_files:
		gid = f.split("/")[-1].replace(".bed","")
		print "convert gid " + gid
		call = "../plink_v190/plink --bfile " + f.replace(".bed","") + " --exclude ../plink_v190/merged-23andme-opensnp-merge.missnp --make-bed --out ../plink_binaries_filtered/" + gid + "-filtered"
		subprocess.call(call,shell=True)

usable_files = twenty3_and_me_files()
run_plink_format(usable_files)
