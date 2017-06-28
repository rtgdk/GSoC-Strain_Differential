#!/bin/bash

python /home/ubuntu/GSoC-Strain_Diffrential/Testing/test_scripts/write.py
bgzip -c original_modified.vcf > original_modified.vcf.gz
pytest /home/ubuntu/GSoC-Strain_Diffrential/Testing/test_scripts/write_test.py
