#!/bin/bash

#run write.py, will read, modify, and make a new file original_modified.vcf at the default location.
python /home/ubuntu/GSoC-Strain_Diffrential/Testing/test_scripts/write.py

#compress original_modified.vcf to original_modified.vcf.gz (PyVCF requirement).
bgzip -c original_modified.vcf > original_modified.vcf.gz

#run pytest to assert validity fo the new file.
pytest /home/ubuntu/GSoC-Strain_Diffrential/Testing/test_scripts/write_test.py
