import sys
sys.path.insert(0, '../../src/')

import pytest
from subprocess import call
from test import reader
from  hash import hash
def test3_test():

    data_path = "../data/test/test3"
    write_path = " ../data/result/test3"
    strain_num = 6268

    print reader(data_path, write_path, strain_num)

    call(["bgzip","test3_result.vcf"])

    crossval_hash = hash("../data/cross_validation/test3_crossval.vcf.gz")
    result_hash = hash("../data/result/test3_result.vcf.gz")

    assert crossval_hash == result_hash

def test3.1_test():

    data_path = "../data/test/test3_result"
    write_path = " ../data/result/test3_cons"
    strain_num = 6269

    print reader(data_path, write_path, strain_num)

    call(["bgzip","test3_cons_result.vcf"])

    crossval_hash = hash("../data/cross_validation/test3_cons_crossval.vcf.gz")
    result_hash = hash("../data/result/test3_result.vcf.gz")

    assert crossval_hash == result_hash

        



