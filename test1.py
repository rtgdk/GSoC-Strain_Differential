import vcf

vcf = vcf.Reader(open('C:\\Users\\arpit\\Desktop\\GSoC\\test\\testdata.vcf'))

snp_count = 0
indel_count = 0
for record in vcf:
	# if record.is_snp:
	# 	snp_count = snp_count + 1
	# 	print "\nSNP Found :"
	# 	print "Record Position: ", record.POS, "\nRecord REF: ", record.REF, "\nRecord ALT:", record.ALT
	if record.is_indel:
		indel_count = indel_count + 1
		print "\nINDEL Found:"
		print "Record Position: ", record.POS, "\nRecord REF: ", record.REF, "\nRecord ALT:", record.ALT, "\nDeletion: ", record.is_deletion
	if indel_count > 100:
		break
print "\nIndel Count: ", indel_count, "\nSnp count: ", snp_count