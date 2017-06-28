import vcf

def writer():
    data_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/original.vcf.gz"
    print "Enter the data file path"
    temp_path = raw_input("type d for default path else type a path and file name:")
    if temp_path != "d":
        data_file_path = temp_path

    vcf_reader = vcf.Reader(open(data_file_path))

    write_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/original_modified.vcf"
    print "Enter writing path"
    temp_path = raw_input("type d for default path else type a path:")
    temp_path = temp_path + "original_modified.vcf"
    if temp_path != "d":
        write_file_path = temp_path

    vcf_writer = vcf.Writer(open(write_file_path, 'w'), vcf_reader)

    change_no_bases = int(raw_input("enter the no of bases to change:"))
    # Storing the chrom no. of the data - as only 100 bases are read, the chrom no. will not change only one is saved.
    count = 1
    record = next(vcf_reader)
    ref_list = [record.CHROM]
    for record in vcf_reader:
        record.REF = 'C'
        print record.REF
        ref_list.extend([record.POS])
        vcf_writer.write_record(record)
        vcf_writer.flush()
        count = count + 1
        if count > change_no_bases:
            break


writer()