import sys
from hash import hash
#from cleaner import clean
sys.path.insert(0, '../../src/')

import pytest
import time
from subprocess import call
from test import reader
import os



'''test to assert reference change of snp's and multiple change on one base'''
def test1_test():
    
    # timing the function for performance testing
    t0 = time.time()   

    #sending data to main function
    data_path = "../data/test/test1"
    write_path = "../data/result/test1"
    strain_num = 6268
    
    #calling main function 
    reader(data_path, write_path, strain_num)
    
    #compressing the file
    call(["bgzip","../data/result/test1_result.vcf"])
    
    #asserting the results
    crossval_hash = hash("../data/cross_validation/test1_crossval.vcf.gz")
    result_hash = hash("../data/result/test1_result.vcf.gz")
    
    assert crossval_hash == result_hash

    #printing tie results
    t1 = time.time()
    print "Time for snp change :" + str(t1-t0)


'''test to check completeness, and cordinate system'''
def test_multiChange():
    
    # timing the function for performance 
    t0 = time.time()

    #sending data to main function
    data_path = "../data/result/test1_result"
    write_path = "../data/result/test1_result"
    strain_num = 6268
    
    #calling main function 
    reader (data_path, write_path, strain_num)
    
    # compressing the results to .vcf.gz
    call(["bgzip", "../data/result/test1_result_result.vcf"])
    
    # generating checksum for validation
    test_hash = hash("../data/test/test1.vcf.gz")
    result_hash = hash("../data/result/test1_result_result.vcf.gz")
    
    # asserting test validation
    assert test_hash == result_hash

    #printing time results
    t1 = time.time()
    print "SNP Multichange time:" + str(t1-t0)

    # cleaning data created in this test
    
#    os.remove("../data/result/test1_result.vcf.gz")
#    os.remove("../data/result/test1_result_result.vcf.gz")
   
     # cleaning other redundant files
#    clean() 
