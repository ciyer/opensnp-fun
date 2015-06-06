#!/usr/bin/env python
# encoding: utf-8

import glob
import os
import subprocess

'''
Convert 23andMe files to 
PLINK format
'''

def twenty3_and_me_files():
	"""Return the opensnp files that are 23 and me format"""
	all_twenty3_and_me_files= glob.glob('../opensnp_datadump.current/*.23andme.txt')
	fifteen_mb = 15 * 1000 * 1000
	non_junk_files = [path for path in all_twenty3_and_me_files if os.path.getsize(path) > fifteen_mb]
	return non_junk_files


def run_plink_format(usable_files):
	"""Reformat the 23andMe files into plink binary stuff"""
	for f in usable_files:
		gid = f.split("/")[-1].split("_")[1].replace("file","")
		call = "../plink_v190/plink --23file "+ f + " F" + gid + "ID" + gid + "I 1"
		call += " --out ../plink_binaries/" + gid
		print "convert gid " + gid
		subprocess.call(call,shell=True)

usable_files = twenty3_and_me_files()
run_plink_format(usable_files)
