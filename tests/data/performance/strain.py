def cutter(rname, fname,strain_count):
	strain_count += 9
	r = open(rname,'r')
	f = open(fname,'w+')
	strain = ''
	row = 0
	for file in r:
		if row < 8:
			f.write(file)
			row += 1
			continue
		if row == 8:
			f.write(file[:45])
			row +=1
			continue
        	# print file
       		count = 0
        	strain = ''
        	for let in file:
                	let = str(let)
        		if let == "\t" and count >= strain_count:
        			#print strain
        			f.write(strain + "\n")
	        		break
			else:
        			strain = strain + let
        			if let == "\t":
        				count = count + 1

print " 1kb 10 strain Strated"
rname = "1kb_allstrains.vcf"
fname = "1kb_10strains.vcf"
strain_count = 10
cutter(rname, fname, strain_count)
print "1k10s done"
rname = "1kb_allstrains.vcf"
fname = "1kb_100strains.vcf"
strain_count = 100
cutter(rname, fname, strain_count)
print "1k100s done"
rname = "10kb_allstrains.vcf"
fname = "10kb_10strains.vcf"
strain_count = 10
cutter(rname, fname, strain_count)
print "10k10s done"
rname = "10kb_allstrains.vcf"
fname = "10kb_100strains.vcf"
strain_count = 100
cutter(rname, fname, strain_count)
print"10k100s done"
rname = "100kb_allstrains.vcf"
fname = "100kb_10strains.vcf"
strain_count = 10
cutter(rname, fname, strain_count)
print "100k10s done"
rname = "100kb_allstrains.vcf"
fname = "100kb_100strains.vcf"
strain_count = 100
cutter(rname, fname, strain_count)
print "100k100s done"

