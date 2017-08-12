import vcf
import sys


def reader():
    """reads data from vcf file and prints as bitset matrix.

    :String data_file_path: default data file path.
    :String temp_path: user entered path stored temporarily.
    :Integer read_no_bases: the no of bases to read from the vcf file.

    :Object vcf_reader: vcf reader object for reading data from vcf file.

    :return: void
    """

    data_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/original.vcf.gz"
    print "Enter the data file path"
    # take user input
    temp_path = raw_input("type d for default path else type a file path:")
    temp_path = temp_path + "original_modified.vcf.gz"
    if temp_path != "d":
        data_file_path = temp_path

    vcf_reader = vcf.Reader(open(data_file_path))

    read_no_bases = int(raw_input("enter the no of bases to read:"))
    # read_no_bases = 10

    # printing formatting.
    print "Sample\tReference Strain\tStrain 1\tSNP/INDEL"

    for record in vcf_reader:
        # print "record.samples\t", record.samples
        for sample in record.samples:
            # print "sample['GT']", sample['GT']
            # check for homogeneity, alternate base.
            if sample['GT'] == "1|1":
                #  printing data as bitset matrix
                sys.stdout.write(sample['GT'])
                sys.stdout.write("\t")
                sys.stdout.write(record.REF)
                sys.stdout.write("\t")
                alt_record = record.ALT[0]
                sys.stdout.write(str(alt_record))
                sys.stdout.flush()
            # check for homogeneity, same base.
            elif sample['GT'] == "0|0" or sample['GT'] == "0/0":
                print "0|0\t", record.REF, "\t", record.REF
            #check for heterogeneity.
            else:
                print "Hetro\t", record.REF, "\t", "H"
            # check for SNP
            if record.is_snp:
                sys.stdout.write("\tSNP\n")
            #  check for INDEL
            elif record.is_indel:
                sys.stdout.write("\tINDEL\n")
            sys.stdout.flush()
        read_no_bases = read_no_bases - 1
        if read_no_bases < 1:
            break

    # test code for checking file formatting.
    '''
    for i in sample['GT']:
        #print type(i)
        if i == ref_val or i == ref_val_alt:
            print "0|0\t", record.REF, '\t', record.REF
        elif i == alt_val or i == alt_val_alt:
            #handling
            print "1|1\t", record.REF, '\t', record.ALT
        else:
            #handling heterozygous
            print "hetro\t", record.REF, 'H'
    '''

# calling reader() function.
reader()