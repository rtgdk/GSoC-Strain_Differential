import vcf

def reader():

    data_file_path = "/home/ubuntu/GSoC-Strain_Diffrential/tests/data/test/test2.vcf.gz"
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
        for i,sample in enumerate(record.samples):
            print sample.sample
            print type(sample.data.GT)
            print sample['GT']
	    print getattr(sample.data,'GT')
#	    setattr(sample.data,'GT','YOLO')
#	    record.samples[i]=record.samples[i]._replace('GT'='0|0')
	    sample.data= sample.data._replace(GT='YOL')
	    print "modiof : "+str(sample.data)
	    print sample['GT']
	print record.samples
reader()
