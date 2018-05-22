# q2-dbotu

QIIME 2 plugin for distribution-based clustering.

To learn more about distribution-based clustering, check out the [original publication](http://dx.doi.org/10.1128/AEM.00342-13) or the [python implementation, dbOTU3](https://github.com/swo/dbotu3). This plugin is essentially a QIIME 2 wrapper around this new implementation.

# Installation

Distribution-based clustering is available on conda:

```
conda install -c cduvallet dbotu_q2
```

Note that you need the April 2018 QIIME 2 release (version `2018.4`) or later for this plugin to work.

If that doesn't work, you can clone or download this repo to your computer, activate your qiime environment, and then run:

```
python setup.py install
```

# Usage

Currently, the dbOTU plugin has only one function, the distribution-based OTU caller in `call-otus`.
From within a QIIME 2 [environment](https://docs.qiime2.org/2018.4/install/native/#activate-the-conda-environment) (i.e. after doing `source activate qiime2-2018.4`), run:

```
qiime dbotu-q2 call-otus \
	--i-table test_data/counts.transpose.qza \
	--i-sequences test_data/seq.qza \
	--o-representative-sequences dbotu_seqs.qza \
	--o-dbotu-table dbotu_table.qza
```

## Data

To run distribution-based clustering, you need (1) some dereplicated sequences and (2) a table of counts indicating how many times each of those sequences is in each of your samples.
Dereplicated sequences can be:

- exact sequence variants output by DADA2 or deblur's denoise commands,      
- dereplicated sequences, which you can get by clustering at 100% identity with vsearch,      
- some other set of representative sequences, perhaps output from clustering with vsearch at a different identity threshold (e.g. 97% OTUs).

The important thing is that the input sequence file contains only non-duplicated sequences (i.e. it is *not* just all the raw reads present in your dataset).
The sequence IDs in the feature table should match the IDs in the input sequences file.

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

# To do

- output membership info          
    - first attempt will be just to print membership to stdout     
    - in the future, will want to define a new file format and write membership to that      
    - in the more distant future, perhaps there could even be a way to visualize that membership       

_Small semantic note: the repo is called q2-dbotu to keep in line with other qiime 2 plugin repo names, but the function is called dbotu_q2 so that it (1) does not conflict with the existing pip package called `dbotu` and (2) shows up alphabetically under `dbotu` which is where I assume most mortal humans will be looking for it in the qiime plugin listings. Sorry for any confusion (and I assure you it has confused me more than you!)_
