import vcf 

vcf_reader = vcf.Reader(open("/home/ubuntu/GSoC-Strain_Diffrential/plant_test.vcf.gz"))

count = 0
for record in vcf_reader:
	print record
	count = count +1 
	if count > 9:
		break 
