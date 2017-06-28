import vcf
import sys
import pytest


def read_func():
    data_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/original.vcf.gz"
    print "Enter the data file path"
    temp_path = raw_input("type d for default path else type a path and file name:")
    if temp_path != "d":
        data_file_path = temp_path

    vcf_reader = vcf.Reader(open(data_file_path))

    read_no_bases = int(raw_input("enter the no of bases to read:"))
    # read_no_bases = 10

    print "Sample\tReference Strain\tStrain 1\tSNP/INDEL"

    for record in vcf_reader:
        # print "record.samples\t", record.samples
        for sample in record.samples:
            # print "sample['GT']", sample['GT']
            if sample['GT'] == "1|1":
                sys.stdout.write(sample['GT'])
                sys.stdout.write("\t")
                sys.stdout.write(record.REF)
                sys.stdout.write("\t")
                alt_record = record.ALT[0]
                sys.stdout.write(str(alt_record))
                sys.stdout.flush()
            elif sample['GT'] == "0|0" or sample['GT'] == "0/0":
                print "0|0\t", record.REF, "\t", record.REF
            else:
                print "Hetro\t", record.REF, "\t", "H"
            if record.is_snp:
                sys.stdout.write("\tSNP\n")
            elif record.is_indel:
                sys.stdout.write("\tINDEL\n")
            sys.stdout.flush()
        read_no_bases = read_no_bases - 1
        if read_no_bases < 1:
            break


# def test(capsys):
    