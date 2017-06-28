import vcf


data_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/original.vcf.gz"
print "Enter the data file path"
temp_path = raw_input("type d for default path else type a path and file name:")
if temp_path != "d":
    data_file_path = temp_path

vcf_reader = vcf.Reader(open(data_file_path))

count = 0
for record in vcf_reader:
    print record.FORMAT, record.samples
    count = count + 1
    if count > 10:
        break
