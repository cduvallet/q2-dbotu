# q2-dbotu

QIIME 2 plugin for distribution-based clustering.

To learn more about distribution-based clustering, check out the [original publication](http://dx.doi.org/10.1128/AEM.00342-13) or the [python implementation, dbOTU3](https://github.com/swo/dbotu3) (and its [associated publication](https://doi.org/10.1371/journal.pone.0176335)). This plugin is essentially a QIIME 2 wrapper around this new implementation.

## Installation instructions

To install this plugin, clone this repo, activate your qiime environment, and run:

```
pip install .
```

To test that it works, run `qiime` and make sure that `dbotu` is one of the commands listed.

Once you install this plugin, it becomes part of the qiime distribution in the environment you're in (so you don't need to re-install it every time you re-activate the environment).
If you install a new version of qiime, however, you'll need to re-install the plugin in that new environment.
Note that you need a 2019 QIIME 2 release (version `2019.1`) or later for this plugin to work.

## Usage

Currently, the dbOTU plugin has only one function, the distribution-based OTU caller in `call-otus`.
From within a QIIME 2 environment, run:

```
qiime dbotu call-otus \
	--i-table test_data/counts.qza \
	--i-sequences test_data/seq.qza \
	--o-representative-sequences dbotu_seqs.qza \
	--o-dbotu-table dbotu_table.qza
```

### Genetic, abundance, and p-value criteria parameters

There are optional parameters that you can change to improve the performance of clustering.
You can see these parameters by typing `qiime dbotu call-otus --help`, and you can learn more about how to choose them by reading the [original  publication](http://dx.doi.org/10.1128/AEM.00342-13) and the [dbotu3 update](https://doi.org/10.1371/journal.pone.0176335).

Note that this plugin wraps the dbotu3 version of distribution-based clustering, which recommends using slightly different parameters than the original version.

### Membership file

Currently, the membership information can be printed using the `--verbose` flag.
The first column of the membership file has the representative sequence for each OTU, and all subsequent columns have the sequences which are grouped into that OTU.
If you want to see the membership file (which shows which sequences are grouped into which "OTU"), use the `--verbose` flag (and optionally pipe the output to a separate file):

```
qiime dbotu call-otus \
    ...
    --verbose > membership_file.txt
```

### Data

To run distribution-based clustering, you need (1) some dereplicated sequences and (2) a table of counts indicating how many times each of those sequences is in each of your samples.
Dereplicated sequences can be:

- exact sequence variants output by DADA2 or deblur's denoise commands,      
- dereplicated sequences, which you can get by clustering at 100% identity with vsearch,      
- some other set of representative sequences, perhaps output from clustering with vsearch at a different identity threshold (e.g. 97% OTUs).

The important thing is that the input sequence file contains only non-duplicated sequences (i.e. it is *not* just all the raw reads present in your dataset).
The sequence IDs in the counts table should match the IDs in the input sequences file, and every sequence ID in your dereplicated sequences file must be present in the table.

### Using non-QIIME 2 artifact data

If you want to use this plugin but you're not using QIIME 2 for any of your other steps, you'll need to first import your data (a feature table of counts and a fasta file of dereplicated sequences) into qiime.
From within the qiime environment, you can do:

```
qiime tools import \
  --input-path your_sequence_file.fasta \
  --output-path your_sequence_file.qza \
  --type 'FeatureData[Sequence]'

  qiime tools import \
    --input-path your_table.biom \
    --output-path your_table.qza \
    --type 'FeatureTable[Frequency]'
```

## Versions

* 2019.2 - update package to use QIIME 2 plugin template
* 2019.1 - re-build package with Python 3.6 for newer versions of QIIME 2
* 2018.4.2 - output membership info with the `--verbose` flag      
* 2018.4.1 - fixed bug: transpose table before and after calling dbotu3, so that dbotu3 gets data in expected format (sequences in rows) despite input qiime2 format (sequences in columns)     
* 2018.4.0 - original "working" plugin, uploaded to conda     
