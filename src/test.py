import vcf


def reader(path_temp, write_file_path, strain_change_num):
    
 #   path = raw_input("Enter the path to the file and the strain to change with a space in between:")
  #  flag = 0
   # strain_change_num = 0
   # path_temp = ""
  #  for char in path:
   #     if char != ' ' and flag == 0: 
    #        path_temp = path_tenp + char
    #    else:
     #       flag = 1
     #       strain_change_num = strain_change_num * 10 + int(char)
 #   path_temp = "/home/ubuntu/GSoC-Strain_Diffrential/data/brachypodium_distachyon"

    data_file_path = path_temp + ".vcf.gz"
    
    write_file_path = write_file_path + "_result.vcf"

    vcf_reader = vcf.Reader(open(data_file_path))

    vcf_writer = vcf.Writer(open(write_file_path, 'w'), vcf_reader)

#    strain_change_num = raw_input("Enter the strain to change the reference strain to:")

    record = next(vcf_reader)
    print "started"
    strain_pos = 0

    for samples in record.samples:
        strain_pos = strain_pos + 1
        if samples.sample == strain_change_num:
            break

    for record in vcf_reader:

#        print "Unchanged Record: " + str(record)

        # Store the no of alternate base pairs available.
        #alt_len = record.ALT.__len__()
        #if alt_len == 1:
            #break

        ref_num = int(record.samples[0]['GT'][:1])

        if record.ALT[int(ref_num)] == record.REF:
            break
        else:
#            print type(record.REF)
#            print type(record.ALT[int(ref_num)])
#            print type(record.ALT)
            
            temp = record.ALT[int(ref_num)]
            record.ALT[int(ref_num)] = record.REF
            record.REF = temp
#            temp = record.REF
#            record.REF = record.ALT[int(ref_num)]
#            record.ALT[int(ref_num)] = temp

        # print record
        # print record.samples

        # Iterate over all strains in the data.
        for sample in record.samples:

            if sample.sample != strain_change_num:

                if sample['GT'] == str(ref_num) + "|" + str(ref_num): # or

                    sample['GT'] = "0|0"

                elif sample['GT'] == str(ref_num) + "/" + str(ref_num):

                    sample['GT'] = "0/0"

                if sample['GT'] == "0|0":

                    sample['GT'] = sample['GT'] = str(ref_num) + "|" + str(ref_num)

                elif sample['GT'] == "0/0":

                    sample['GT'] = sample['GT'] = str(ref_num) + "/" + str(ref_num)

            # print sample
            # print sample['GT']
        vcf_writer.write_record(record)
 #       print "Changed Record: " + str(record)

    vcf_writer.flush()
    return "reference change done"



