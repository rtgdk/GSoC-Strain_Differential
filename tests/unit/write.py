import vcf


def writer():
    """reads vcf file, edits REF to 'C' and writes it to new .vcf file

    :String data_file_path: default data file path.
    :String write_file_path: default modified data file path.
    :String temp_path: user entered path stored temporarily.
    :Integer change_no_bases: user input, no of bases to edit.
    :Integer count: loop counter.

    :Object vcf_reader: vcf reader object for reading data from vcf file.
    :Object vcf_writer: vcf writed object for writing modified vcf file.
    :Object record: loop variable, iterates over all records in vcf file.

    :return: void.
    """
    data_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/original.vcf.gz"
    print "Enter the data file path"
    # reading from user input
    temp_path = raw_input("type d for default path else type a path and file name:")
    if temp_path != "d":
        data_file_path = temp_path

    vcf_reader = vcf.Reader(open(data_file_path))

    write_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/original_modified.vcf"
    print "Enter writing path"
    # reading from user input.
    temp_path = raw_input("type d for default path else type a path:")
    temp_path = temp_path + "original_modified.vcf"
    if temp_path != "d":
        write_file_path = temp_path

    vcf_writer = vcf.Writer(open(write_file_path, 'w'), vcf_reader)

    change_no_bases = int(raw_input("enter the no of bases to change:"))

    # POS of every REF changes is stored in a list for testing,ll the POS edited are tested in the test function...
    # Only one chrom no. is stored - as only 100 bases are read...
    # very less probability of chrom changing.
    # the chrom no. is stored at 0th index ref_list and the POS values are appended.
    # Uncomment line 44, 45 and 58 for using ref_list.

    # record = next(vcf_reader)
    # ref_list = [record.CHROM]

    count = 1

    # iterating over all values in the vcf_reader object and changing to 'C'
    for record in vcf_reader:
        # editing value of all REF.
        record.REF = 'C'
        print record.REF
        # Appends pos value for each record to a list.
        # ref_list.extend([record.POS])

        # writing the value to permanent storage.
        vcf_writer.write_record(record)
        vcf_writer.flush()
        count = count + 1
        if count > change_no_bases:
            break

# calling the writer function.
writer()
