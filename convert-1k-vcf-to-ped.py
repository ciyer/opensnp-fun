import glob
import subprocess

# apparently there's no easy way to do all files for all populations at the same time. this is a crude hack to get at least some interesting populations out for all 22 chromosomes. requires you to have the vcfs in the same folder, along with the sample panel

vcfs = glob.glob("*.vcf")

pops = "-population FIN -population GBR -population CHS -population CDX -population PUR -population IBS -population ACB -population GWD -population ESN -population MSL -population -CEU -population YRI"

for i in vcfs:
	print i
	call = "perl vcf_to_ped_convert.pl -vcf " + i 
	call += " -sample integrated_call_samples_v3.20130502.ALL.panel -region "
	ia = i.split(".")[1].replace("chr","")
	call += ia + ":1-249240543 " + pops
	subprocess.call(call,shell=True)
	
