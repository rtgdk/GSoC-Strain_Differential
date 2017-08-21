import sys
from hash import hash 
#from cleaner import clean
sys.path.insert(0, '../../src/')

import pytest
from subprocess import call
from test import reader
import time
import os 

'''
test to assert reference change of indels, multiple strain change and base change at same position"
'''
def test2_test():

    # timing for performance test
    t0 = time.time()

    #sending data to main function
    data_path = "../data/test/test2"
    write_path = "../data/result/test2"
    strain_num = 6268

    # calling main fucntion
    reader(data_path, write_path, strain_num)

    # compressing file to .vcf.gz
    call(["bgzip","../data/result/test2_result.vcf"])

    # generating checksums
    crossval_hash = hash("../data/cross_validation/test2_crossval.vcf.gz")
    result_hash = hash("../data/result/test2_result.vcf.gz")

    # validating checksums 
    assert crossval_hash == result_hash
    
    #printing time results
    t1 = time.time()
    print "Indel test time: " + str(t1-t0) 



''' test to assert validation of cordinate system by changing back to the original reference strain'''
def test_multichange():

    # timing for performance test 
    t0 = time.time()

    # sending data to main function
    data_path = "../data/result/test2_result"
    write_path = " ../data/result/test2_result"
    strain_num = 6268
     
    # calling the main function 
    reader(data_path, write_path, strain_num)

 #   call(["bgzip","../data/result/test2_result_result.vcf"])

    # generatig checksums
    crossval_hash = hash("../data/test/test2.vcf.gz")
    result_hash = hash("../data/result/test2_result_result.vcf.gz")

    #validating checksums
    assert crossval_hash == result_hash

    # printing time outputs
    t1 = time.time()
    print " Extra test 1:" + str(t1-t0)


'''

def test_multiChange():
    
    # timing for performance test 
    t0 = time.time()

    data_path = "../data/result/test2_result"
    write_path = "../data/result/test2_result"
    strain_num = 6268

    print reader (data_path, write_path, strain_num)

    call(["bgzip", "../data/result/test2_result_result.vcf"])

    test_hash = hash("../data/result/test2_result.vcf.gz")
    result_hash = hash("../data/result/test2_result_result.vcf.gz")

    assert test_hash == result_hash

    t1 = time.time()
    print "Multichange in indel time:" + str(t1-t0)

    # cleaning up other created files
#    os.remove("../data/result/test2_result.vcf.gz")
#    os.remove("../data/result/test2_result_result.vcf.gz")
#    os.remove("../data/result/test2_cons_result.vcf.gz")
    #removing other files
   # clean()
'''
