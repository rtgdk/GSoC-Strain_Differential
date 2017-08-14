import sys
sys.path.insert(0, '../../src/')

import pytest
from subprocess import call
from test import reader
from  hash import hash
import time
import os 
from cleaner import clean

def test2_test():

    # timing for performance test
    t0 = time.time()

    data_path = "../data/test/test2"
    write_path = " ../data/result/test2"
    strain_num = 6268

    print reader(data_path, write_path, strain_num)

    call(["bgzip","test2_result.vcf"])

    crossval_hash = hash("../data/cross_validation/test2_crossval.vcf.gz")
    result_hash = hash("../data/result/test2_result.vcf.gz")

    assert crossval_hash == result_hash
    
    t1 = time.time()
    print "Indel test time: " + (t1-t0) 

def test2.1_test():

    # timing for performance test 
    t0 = time.time()

    data_path = "../data/test/test2_result"
    write_path = " ../data/result/test2_cons"
    strain_num = 6269

    print reader(data_path, write_path, strain_num)

    call(["bgzip","test2_cons_result.vcf"])

    crossval_hash = hash("../data/cross_validation/test2_cons_crossval.vcf.gz")
    result_hash = hash("../data/result/test2_result.vcf.gz")

    assert crossval_hash == result_hash

    t1 = time.time()
    print " Extra test 1:" + (t1-t0)


def multiChange_test():
    
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
    print "Multichange in indel time:" + (t1-t0)

    # cleaning up other created files
    os.remove("../data/result/test2_result.vcf.gz")
    os.remove("../data/result/test2_result_result.vcf.gz")
    os.remove("../data/result/test2_cons_result.vcf.gz")
    #removing other files
    clean()

