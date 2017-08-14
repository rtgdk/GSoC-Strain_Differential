import sys
sys.path.insert(0, '../../src/')

import pytest
import time
from subprocess import call
from test import reader
from  hash import hash
from cleaner import clean
import os


def test1_test():
    
    # timing the function for performance testing
    t0 = time.time()   

    data_path = "/home/ubuntu/GSoC-Strain_Diffrential/tests/data/test/test1"
    write_path = "/home/ubuntu/GSoC-Strain_Diffrential/tests/data/result/test1"
    strain_num = 6268
    
    print reader(data_path, write_path, strain_num)
    
    call(["bgzip","test1_result.vcf"])
    
    crossval_hash = hash("../data/cross_validation/test1_crossval.vcf.gz")
    result_hash = hash("../data/result/test1_result.vcf.gz")
    
    assert crossval_hash == result_hash
    t1 = time.time()
    print "Time for snp change :" + (t1-t0)

def multiChange_test():
    
    # timing the function for performance 
    t0 = time.time()

    data_path = "/home/ubuntu/GSoC-Strain_Diffrential/tests/data/result/test1_result"
    write_path = "/home/ubuntu/GSoC-Strain_Diffrential/tests/data/result/test1_result"
    strain_num = 6268
    
    print reader (data_path, write_path, strain_num)
    
    call(["bgzip", "../data/result/test1_result_result.vcf"])
    
    test_hash = hash("../data/result/test1_result.vcf.gz")
    result_hash = hash("../data/result/test1_result_result.vcf.gz")
    
    assert test_hash == result_hash

    t1 = time.time()
    print "SNP Multichange time:" + t1-t0

    # cleaning data created in this test
    
    os.remove("../data/result/test1_result.vcf.gz")
    os.remove("../data/result/test1_result_result.vcf.gz")
   
     # cleaning other redundant files
    clean() 
