import vcf


data_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/original.vcf.gz"
print "Enter the data file path"
temp_path = raw_input("type d for default path else type a path and file name:")
if temp_path != "d":
    data_file_path = temp_path

vcf_reader = vcf.Reader(open(data_file_path))

read_no_bases = raw_input("enter the no of bases to read:")

count = 0
print "Reference Strain \t Strain 1"
for record in vcf_reader:
    count = count + 1
    print "record.samples\t", record.samples
    for sample in record.samples:
        print "sample['GT']", sample['GT']
        for i in sample['GT']:
            #print type(i)
            if i == "0|0" or i == "0/0":
                print "0|0\t", record.REF, '\t', record.REF
            elif i == "1|1" or i == "1/1":
                #handling
                print "1|1\t", record.REF, '\t', record.ALT
            else:
                #handling heterozygous
                print "hetro\t", record.REF, 'H'
    count = count + 1
    if count > read_no_bases:
        break


