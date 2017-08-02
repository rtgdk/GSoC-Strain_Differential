import vcf

def length_test_snp:
    """ Checks for the length integrity in case of snp.

    :return: void
    """
    test_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/data/length_test_data/test_toy1.vcf"
    vcf_reader_test = vcf.Reader(open(test_file_path))

    test_count = 0
    for record in vcf_reader_test:
        if record.is_snp:
            test_count = test_count + 1

    result_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/data/length_test_data/test_toy1_result.vcf"
    vcf_reader_result = vcf.Reader(open(result_file_path))

    result_count = 0
    for record in vcf_reader_result:
        if record.is_snp:
            result_count = result_count + 1

    if test_count == result_count:
        print ("Length Test PASS")
    else:
        print ("Length Test FAIL")


def length_test_indel:
    """ Checks for the length integrity in case of indels.

        :return: void
        """
    test_file_path = "INDEL TOY EXAMPLE"
    vcf_reader_test = vcf.Reader(open(test_file_path))

    result_file_path = "INDEL TOY RESULT"
    vcf_reader_result = vcf.Reader(open(result_file_path))


    test_count = 0
    for record in vcf_reader_test:
        if record.is_indel:
            test_count = test_count + 1
            
    base_length_test = 0
    base_length_result = 0
    result_count = 0
    for record in vcf_reader_result:
        if record.is_indel:
            test_record = vcf_reader_test.fetch(record.CHROM, record.POS, record.POS)
            base_length_test = len(test_record.REF) + len(test_record.ALT)
            base_length_result = len (record.REF) + len(record.ALT)
            
            result_count = result_count + 1

    if test_count == result_count && base_length_result == base_length_test:
        print ("Length Test PASS")
    else:
        print ("Length Test FAIL")

      
length_test_snp()
#length_test_indel()

