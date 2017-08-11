import vcf

data = "/home/ubuntu/GSoC-Strain_Diffrential/data/original.vcf.gz"

vcf_reader = vcf.Reader(open(data))

temp = 0

for record in vcf_reader:
    temp = temp + 1
print temp
