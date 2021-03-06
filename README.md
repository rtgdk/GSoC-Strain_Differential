[![N|Solid](https://developers.google.com/open-source/gsoc/resources/downloads/GSoC-logo-horizontal.svg)](https://summerofcode.withgoogle.com/projects/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BmtMbABy2QHWwVfPokBUNnw%3D%3D#5216557551583232)

# Strain Differential

The objective of the project is to get a scrollable web view for gene variations after changing the reference strain of genome data in real time.

The three major parts of the project are:
  - Data Pipeline
  - Reference Change Algorithm Implementation
  - Visualization

## Requirments

#### [Python 2.7.13](https://docs.python.org/2/using/index.html)

First, install some dependencies:

```sh
$sudo apt-get install build-essential checkinstall
$sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
```
Then download using the following command:
```sh
$version=2.7.13
$cd ~/Downloads/
$wget https://www.python.org/ftp/python/$version/Python-$version.tgz
```
Extract and go to the directory:

```sh
$tar -xvf Python-$version.tgz
$cd Python-$version
```
Now, install using `checkinstall`:
```sh
$./configure
$make
$sudo checkinstall
```

#### [pip](https://pip.pypa.io/en/stable/)

```sh
$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 
$ sudo pip install --upgrade virtualenv 
```
#### [PyVCF](http://pyvcf.readthedocs.io/)

First, install the dependencies of PyVCF:
```sh
$pip install Cython
```
```sh
$sudo apt-get install setuptools
```
```sh
$pip install pysam
```
Install PyVCF:
```sh
$pip install pyvcf
```
_Note: if there is some error in running the fetch function, switch to `pysam!=0.8.0`_

#### [PyTest](https://docs.pytest.org/en/latest/getting-started.html)

```sh
$pip install -U pytest
```

_Note: This will not work on Windows because [Pysam](https://github.com/pysam-developers/pysam) is dependency of PyVCF to use `fetch()` function. Pysam is only made for linux as is written in this [issue](https://github.com/pysam-developers/pysam) on GitHub._


## File Structure

- `data`: vcf and tabix files.
    - `toy_examples`: hand written examples for tests.
- `docs`: documents and documentation.
- `logs`: runtime logs and data logs.
- `src`: source code.
- `test`: performance and integrity tests.
    - `checksums`: file checksums.
    - `other`: other files for running test.
    - `unit`: unit test.
    - `integration`: end-to-end integration tests.

## Weekly TODO:
1.	July 1st Week  (1st - 7th):
    -   Implement translation, test against large dataset.
2.   July 2nd Week (8th - 14th): 
    -	Implement Reference change for bitset matrix
      -	Implement the algorithm (Both for SNP and INDEL)
3.	July 3rd Week (15th - 21st):
    -	Finish Implementing Reference Change .
    -	Start working on the test suite.
      -	Discuss parameters for testing.
      -	Write the code for testing (Working on a proper testing suite).
      -	Make  the toy examples.
      -	Test for full dataset and toy examples.
4.	July 4th Week (22nd - 28th):
    -	Testing continues
    -	Work on implementing heterogeneity.
      -	If any solution has been thought of implement it.
      -	Else work on a solution 
      -	Implement the solution     
5.	Work on Visualization begins.

## Testing

### How to use tests

 #### All tests
  - switch to `tests/unit/` directory
  - run `pytest -v` 
 #### Single Tests
  - switch to `tests/unit` directory
  - run `pytest -v 'test_name.py'` to run a specific test
 #### File Structure
 All test data is stored in `/tests/data` in the following structure:
 - `test` - contains all required test.vcf.gz file for running the unit test.
 - `results` - all the results generated from the tests are stored here before they are deleted by the test code cleanup module.
 - `cross_validation` - all cross validation data is stored here.
 - `performance_test` - all performance test data of varrying sizes are stored here.
 
### Logic Tests
 - Is length of sequence as expected? (check after insertion and deletion)
 - Is SNP changed correctly and in the correct position?
 - Is the insertion changed correctly and in the correct position?
 - Is the deletion etc. etc.
 - If you change the reference and then change back, do you get the original sequence? (better with an indel)
 - Does the coordinate system remain intact when you make one change? i.e. test for the effect of 2 successive changes in different positions - make sure 2nd change occurs in the right place.
 - Check predictions from VCF (read by your code) against FASTA files for each genome
 
### Performance tests
 - Using actual data - how long does it take to initialise, then flip, for 1 kb, 10 kb, 100 kb, and entire chromosome.
 - Similarly with 10, 100, 1000 strains.

## Documentation

The repository uses [Python Docstyle](https://www.python.org/dev/peps/pep-0257/) documentaion.

## Usage

_*Coming Soon*_


### Useful Links

- [VCF file format](https://en.wikipedia.org/wiki/Variant_Call_Format) details.
- Download genome data from [here](http://ensemblgenomes.org/info/access/ftp).

