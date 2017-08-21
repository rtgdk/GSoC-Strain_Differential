import vcf 
import sys

vcf_reader = vcf.Reader(open("1001genomes_snp-short-indel_only_ACGTN.vcf.gz"))
write_path =  raw_input("enter write path: ")
vcf_writer = vcf.Writer(open(write_path, 'w'), vcf_reader)
strains = raw_input("enter the no. of strains to cut down to")

count = 0
for record in vcf_reader:
    count = count + 1 
#    print count
    vcf_writer.write_record(record)
    if count == int(strains):
        break
vcf_writer.flush()


'''
count = 0
record = next(vcf_reader)
for samples in record.samples:
    count = count + 1
print count
'''

'''
flag = 0
for record in vcf_reader:
    flag = flag + 1
    if flag <2 :
         continue
    count = 0
    strain = 0
    for sample in record.samples:
        count = count +1
        if str(sample['GT'][:1]) != ".":
            if  str(sample['GT'][:1]) != "0" and str(sample['GT'][:1]) != "1":
                strain = 1
                sys.stdout.write (str(sample['GT'][:1]))
                sys.stdout.write (", ")
    if strain == 1:
        sys.stdout.write("\n")
    if flag == 10000:
        sys.stdout.write ("\n")
        break
'''
