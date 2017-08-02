import vcf


def writer():

    # file path to the reference file
    data_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/data/original.vcf.gz"
    # raw_input("Enter path to reference VCF file")
    vcf_reader = vcf.Reader(open(data_file_path))

    write_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/data/Toy\ Examples/test_toy3.vcf"
    #print "Enter writing path"
    # reading from user input.
    #temp_path = raw_input("type d for default path else type a path:")
    #temp_path = temp_path + raw_input("Enter toy example name:") + ".vcf"
    #if temp_path != "d":
        #write_file_path = temp_path
    temp_path = write_file_path 

    vcf_writer = vcf.Writer(open(write_file_path, 'w'), vcf_reader)
    count  = 1
    for record in vcf_reader:
        print "\nEnter the values for input" + str(count) + ":\n"
        print (record)
        print (record.ALT)
        print( record.is_snp )
        print(record.is_indel )
        print(record.is_deletion)
        record.POS = raw_input("Enter POS:")
        record.REF = raw_input("Enter REF for POS " + record.POS + " :")
        record.ALT = raw_input("Enter ALT for POS " + record.POS + " :")
        #record.is_indel = raw_input("Enter is_indel (true or false) for POS " + record.POS + " :")
        #record.is_deletion = raw_input("Enter is_deletion (true or false) for POS " + record.POS + " :")
        #record.is_snp = raw_input("Enter is_snp (true or false) for POS " + record.POS + " :")
        vcf_writer.write_record(record)
        if raw_input("Press enter if you want to continue else press any other key:") != "":
            break

        count = count + 1

    # writing the value to permanent storage.
    # vcf_writer.write_record(record)
    vcf_writer.flush()


    vcf_reader = vcf.Reader(open(temp_path))

    for record in vcf_reader:
        print (record)


# calling the writer function.
writer()
