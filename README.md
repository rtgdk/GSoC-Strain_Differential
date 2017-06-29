[![N|Solid](https://blog.tameesh.in/sites/default/files/inline-images/Screenshot%20from%202017-05-05%2001-06-34_0.png)](https://summerofcode.withgoogle.com/projects/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BmtMbABy2QHWwVfPokBUNnw%3D%3D#5216557551583232)

# Strain Differential

The objective of the project is to get a scrollable web view for gene variations after changing the reference strain of genome data in real time.

The three major parts of the project are:
  - Data Pipeline
  - Reference Change Algorithm Implementation
  - Visualization

## Requirments

##### [Python 2.7.13](https://docs.python.org/2/using/index.html)

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

##### [pip](https://pip.pypa.io/en/stable/)

```sh
$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 
$ sudo pip install --upgrade virtualenv 
```
##### [PyVCF](http://pyvcf.readthedocs.io/)

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

##### [PyTest](https://docs.pytest.org/en/latest/getting-started.html)

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

## Usage


_*Coming Soon*_


### Useful Links

- [VCF file format](https://en.wikipedia.org/wiki/Variant_Call_Format) details.
- Download genome data from [here](http://ensemblgenomes.org/info/access/ftp).

