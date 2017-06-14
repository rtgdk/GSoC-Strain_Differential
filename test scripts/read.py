import vcf

vcf_reader = vcf.Reader(open('C:\\Users\\arpit\\Documents\\GitHub\\GSoC-Strain_Diffrential\\test.vcf', 'r'))
for record in vcf_reader:
	print record.CHROM, record.POS, record.REF, record.ALT