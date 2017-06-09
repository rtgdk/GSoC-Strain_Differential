import vcf

vcf_reader = vcf.Reader(open('/home/ubuntu/GSoC-Strain_Diffrential/test.vcf.gz'))
# vcf_reader = vcf.Reader(open('C:\\Users\\arpit\\Documents\\GitHub\\GSoC-Strain_Diffrential\\test.vcf'))


snp_count = 0
indel_count = 0
for record in vcf_reader:
    # if record.is_snp:
    # 	snp_count = snp_count + 1
    # 	print "\nSNP Found :"
    # 	print "Record Position: ", record.POS, "\nRecord REF: ", record.REF, "\nRecord ALT:", record.ALT
    if record.is_indel:
        indel_count = indel_count + 1
        print "\nINDEL Found:"
        print "Record Position: ", record.POS, "\nRecord REF: ", record.REF, "\nRecord ALT:", record.ALT, "\nDeletion: ", record.is_deletion
    if indel_count > 5:
        break
print "\nIndel Count: ", indel_count, "\nSnp count: ", snp_count
vcf_writer = vcf.Writer(open('/dev/null', 'w'), vcf_reader)
# vcf_writer = vcf.Writer(open('NUL', 'w'), vcf_reader)

count = 0
record = next(vcf_reader)
REF_list = [record.CHROM]
for record in vcf_reader:
    print record.REF, record.POS
    # if record.REF != 'C':
    #     record.REF = 'C'
    # else:
    #     record.REF = 'A'
    record.REF = 'C'
    print record.REF
    REF_list.extend([record.POS])
    vcf_writer.write_record(record)
    count = count + 1
    if count > 100:
        break


print("REF_list", REF_list)
count = 0
# print "\n\n Checking\n"
# for i in range(0, len(REF_list)):
#     for record in vcf_reader.fetch(REF_list[0], i-1, i):
#         print record.REF, record.POS
#         count = count + 1
#         if count > 100:
#             break

for record in vcf_reader.fetch(REF_list[0],REF_list[1] - 1, REF_list[1]):
	print record.REF

