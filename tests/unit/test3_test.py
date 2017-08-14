import sys
sys.path.insert(0, '../../src/')

import pytest
from subprocess import call
from test import reader
from  hash import hash
import time
import os 
from cleaner import clean 

def test3_test():

    #timing for performance test
    t0 = time.time()

    data_path = "../data/test/test3"
    write_path = " ../data/result/test3"
    strain_num = 6268

    print reader(data_path, write_path, strain_num)

    call(["bgzip","test3_result.vcf"])

    crossval_hash = hash("../data/cross_validation/test3_crossval.vcf.gz")
    result_hash = hash("../data/result/test3_result.vcf.gz")

    assert crossval_hash == result_hash
    
    t1 = time.time()
    print "Time for test 3:" + (t1-t0)


def test3.1_test():

    # timing for performance test
    t0 = time.time()

    data_path = "../data/test/test3_result"
    write_path = " ../data/result/test3_cons"
    strain_num = 6269

    print reader(data_path, write_path, strain_num)

    call(["bgzip","test3_cons_result.vcf"])

    crossval_hash = hash("../data/cross_validation/test3_cons_crossval.vcf.gz")
    result_hash = hash("../data/result/test3_result.vcf.gz")

    assert crossval_hash == result_hash
    
    t1 = time.time()
    print "time for test 3.1 :" + (t1-t0)

    # Cleaning files created
    os.remove("../data/result/test3_result.vcf.gz")
    os.remove("../data/result/test3_cons_result.vcf.gz")
    #cleaning other files 
    clean()

        



