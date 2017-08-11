import vcf

def reader():

    data_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/data/indel_toy.vcf.gz"
    vcf_reader = vcf.Reader(open(data_file_path))
    for record in vcf_reader:
 #       print record
#	print record.ALT.__len__()
        print type(record.samples[0].data)
  #      print record.samples
        temp = record.samples[0].data
        print temp
        print record.samples[0]['GT'][:1]
        record.samples[0].sample = 2
	print record.samples[0].sample
        for sample in record.samples:
            print sample.sample
            print "YOLO"
      #      print sample['GT']

reader()
