import vcf


def readfile():
    data_path = "/home/ubuntu/GSoC-Strain_Diffrential/original_modified.vcf.gz"
    temp_path = raw_input("enter file path, d for default path:")
    if temp_path != "d":
        data_path = temp_path
    vcf_reader = vcf.Reader(open(data_path, 'r'))
    # for record in vcf_reader:
    #     print record.CHROM, record.POS, record.REF, record.ALT
    return vcf_reader


def testfunc():
    vcf_reader = readfile()
    for record in vcf_reader:
        assert record.REF == "C"
