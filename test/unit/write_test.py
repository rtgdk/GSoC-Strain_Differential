import vcf


def readfile():
    """ function to read data from modified vcf file.

    :String data_path: default file path to original_modified.vcf.gz

    :Object vcf_reader: vcf Reader object variable.

    :return: vcf_reader object.
    """
    data_path = "/home/ubuntu/GSoC-Strain_Diffrential/original_modified.vcf.gz"
    # taking user input for file path, commented for ease of use.
    #temp_path = raw_input("enter file path, d for default path:")
    #if temp_path != "d":
    #    data_path = temp_path
    vcf_reader = vcf.Reader(open(data_path, 'r'))
    # for record in vcf_reader:
    #     print record.CHROM, record.POS, record.REF, record.ALT
    return vcf_reader


def testfunc():
    """pytest function, asserts validity of modified vcf file.

    :Object record: loop variable, iterates over all values of vcf_reader.
    :Object vcf_reader, stores return readfile().
    
    :return: void
    """
    vcf_reader = readfile() 
    for record in vcf_reader:
        assert record.REF == "C"
