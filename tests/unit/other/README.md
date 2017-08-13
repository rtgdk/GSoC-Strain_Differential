#### Test1

This test is made to verify whether the program is able to read and write data from a VCF file to a new VCF file.

Run the script:

```sh
$./write.sh
```
`write.py` will be excuted. 

Enter the path and filename of your vcf file and the path where you want the modified file (`original_modified.vcf`) to be saved.

All the references will be changed to `C` in the modified file.

The script will then bgzip this file to `original_modified.vcf.gz`

write_test.py will be executed.

This will run the pytest which will assert that `original_modified.vcf.gz` has all the references as `C` and all other factors (`POS`, `ALT` et cetra) are same as the original file or not.

#### Test2

This test made to verify the ability to handle the VCF data as bitset matrix.

Run the script:  
```sh
$./read.sh
```
This will execute `read.py`. 

It will read the data in the form of bitset matrix and print it to console and also store that data. 

Then `read_test.py` will be executed. 

This will test `read.py` for known `POS` of data for known output (handwritten).
