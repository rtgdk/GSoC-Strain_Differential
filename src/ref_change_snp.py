import vcf
import sys

tran_ref = dict()
tran_alt = dict()


def reader():
    # Add file path to the reference
    path_template = "/home/ubuntu/GSoC-Strain_Diffrential/original"

    data_file_path = path_template + ".vcf.gz"

    write_file_path = path_template + "_result" + ".vcf.gz"

    vcf_reader = vcf.Reader(open(data_file_path))

    vcf_writer = vcf.Writer(open(write_file_path, 'w'), vcf_reader)

    for record in vcf_reader:
        strain_num = record.ALT.__len__()
        for sample in record.samples:
            # print "sample['GT']", sample['GT']
            # check for homogeneity, alternate base.
            for x in range(0, strain_num):
                if sample['GT'] == "\"" + str(x) + "|" + str(x) + "\"" or sample['GT'] == "\"" + str(x) + "/" + str(
                        x) + "\"":
                    ref_record = record.REF

                    # if the reference record contains more than one base, the matrix will be translated...
                    # else it would simply be treated as bitset matrix
                    if ref_record.__len__() == 1:
                        temp = record.ALT[x]
                        record.ALT[x] = record.REF
                        record.REF = temp

                    else:
                        # Handle in INDEL code
                        print("INDEL SPOTTED!")

                    sys.stdout.write("\t")
                    alt_record = record.ALT[x]
                    sys.stdout.write(str(alt_record))
                    sys.stdout.flush()

                    """Sample code for translating alt records."""
                    # if alt_record.__len__() > 1:
                    #     trans(alt_record, record)
                    #     tran_ref[record.POS] = alt_record.__len__()
                    # else:
                    #     sys.stdout.write("\t")
                    #     sys.stdout.write(str(alt_record))

                    sys.stdout.flush()
                    break
                # check for homogeneity, same base.
                elif sample['GT'] == "0|0" or sample['GT'] == "0/0":
                    print "0|0\t", record.REF, "\t", record.REF, ": No change"
                    break
                # check for heterogeneity.
                else:
                    print "Hetro\t", record.REF, "\t", "H"
                    break

                # Need fix here, data annotation needs to be changed in case of INDELS.
                # check for SNP
                if record.is_snp:
                    sys.stdout.write("\tSNP\n")
                # check for INDEL
                elif record.is_indel:
                    sys.stdout.write("\tINDEL\n")

                vcf_writer.write_record(record)

                # read_no_bases = read_no_bases - 1
                # if read_no_bases < 1:
                #     break

    # Flush data from memory
    vcf_writer.flush()
    sys.stdout.flush()
    
    # test code for checking file formatting and changing annotation.
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

