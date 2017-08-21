import vcf
# import json


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
    record = next(vcf_reader)
    vcf_reader = vcf.Reader(open(data_file_path))

    vcf_writer = vcf.Writer(open(write_file_path, 'w'), vcf_reader)

    #    strain_change_num = raw_input("Enter the strain to change the reference strain to:")


#    print "started"
    strain_pos = 0


    for samples in record.samples:
        strain_pos = strain_pos + 1
	print samples.sample, strain_change_num
        if str(samples.sample) == str(strain_change_num):
            break

    for record in vcf_reader:
 #       print record
        #        print "Unchanged Record: " + str(record)

        # Store the no of alternate base pairs available.
        # alt_len = record.ALT.__len__()
        # if alt_len == 1:
        # break

        ref_num = int(record.samples[strain_pos - 1]['GT'][:1] )
	print str(strain_pos) + " strin pos, ref num : " +  str(ref_num) + " this is record: " + str(record)       
        if record.ALT[int(ref_num-1)] == record.REF:
            print record.REF
#	    vcf_writer.write_record(record)
            continue
	elif ref_num == 0:
	    print "num == 0"
#	    vcf_writer.write_record(record)
            continue
        else:
            #            print type(record.REF)
            #            print type(record.ALT[int(ref_num)])
            #            print type(record.ALT)
	    print "swap"
            temp = record.ALT[int(ref_num -1)]
            record.ALT[int(ref_num -1 )] = record.REF
            record.REF = temp
        # temp = record.REF
        #            record.REF = record.ALT[int(ref_num)]
        #            record.ALT[int(ref_num)] = temp

        # print record
        # print record.samples

        # Iterate over all strains in the data.
        for i,data in enumerate(record.samples):
 #           print data.sample
            if data.sample != strain_change_num:
   #             print "this is GT: ",  data['GT']
  #              print ref_num
                if data['GT'] == str(ref_num ) + "|" + str(ref_num ):  
#		    print "reached for change: "
                    data.data = data.data._replace(GT='0|0')

                elif data['GT'] == str(ref_num) + "/" + str(ref_num):
           
                    data.data = data.data._replace(GT='0/0')

                if data['GT'] == "0|0":
 #                   print "enter 0|0" 
                    att = str(ref_num) + "|" + str(ref_num)
		    data.data = data.data._replace(GT=att)

                elif data['GT'] == "0/0":
                    att = str(ref_num) + "/" + str(ref_num )
                    #setattr(data, 'GT', st)
                    data.data = data.data._replace(GT=att)

  #              print data
	            # print sample['GT']
 #       vcf_writer.write_record(record)
        #       print "Changed Record: " + str(record)

    vcf_writer.flush()
    return "reference change done"

'''
data = raw_input("Enter data path:")
write = raw_input("Enter write path:")
strain = raw_input("enter strain number")
reader(data,write,strain)
'''

