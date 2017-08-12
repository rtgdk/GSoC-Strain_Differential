import sys
sys.path.insert(0, '../../src/')

import pytest
from subprocess import call
from test import reader
from  hash import hash
def test1_test():
    
    data_path = "/home/ubuntu/GSoC-Strain_Diffrential/tests/data/test/test1"
    write_path = "/home/ubuntu/GSoC-Strain_Diffrential/tests/data/result/test1"
    strain_num = 6268
    
    print reader(data_path, write_path, strain_num)
    
    call(["bgzip","test1_result.vcf"])
    
    crossval_hash = hash("../data/cross_validation/test1_crossval.vcf.gz")
    result_hash = hash("../data/result/test1_result.vcf.gz")
    
    assert crossval_hash == result_hash

def multiChange_test():

    data_path = "/home/ubuntu/GSoC-Strain_Diffrential/tests/data/result/test1_result"
    write_path = "/home/ubuntu/GSoC-Strain_Diffrential/tests/data/result/test1_result"
    strain_num = 6268
    
    print reader (data_path, write_path, strain_num)
    
    call(["bgzip", "../data/result/test1_result_result.vcf"])
    
    test_hash = hash("../data/result/test1_result.vcf.gz")
    result_hash = hash("../data/result/test1_result_result.vcf.gz")
    
    assert test_hash == result_hash
