# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Claire Duvallet.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import dbotu
from Bio import SeqIO

import pandas as pd

# QIIME types, etc
from q2_types.feature_data import DNAFASTAFormat

# This function is mostly copied from the dbotu3 code,
# with a few additions to play nicely with qiime2 types
def call_otus(table: pd.DataFrame,
              sequences: DNAFASTAFormat,
              gen_crit: float=0.1,
              abund_crit: float=10.0,
              pval_crit: float=0.0005
              ) -> (pd.DataFrame, DNAFASTAFormat):
    '''
    Read in input files, call OTUs, and return output feature table.

    seq_table_fh: filehandle
      sequence count table, tab-separated
    fasta_fn: str
      sequences fasta filename
    output_fh: filehandle
      place to write main output OTU table
    gen_crit, abund_crit, pval_crit: float
      threshold values for genetic criterion, abundance criterion, and distribution criterion (pvalue)
    log, membership, debug: filehandles
      places to write supplementary output
    '''

    # ensure valid argument values
    assert gen_crit >= 0
    assert abund_crit >= 0.0
    assert pval_crit >= 0.0 and pval_crit <= 1.0

    ## read in the sequences table
    #seq_table = read_sequence_table(seq_table_fh)

    ## set up the input fasta records
    # Note: calling str(DNAFastaFormat) returns the file path of the fasta
    records = SeqIO.index(str(sequences), 'fasta')

    # generate the caller object
    caller = dbotu.DBCaller(table, records,
        gen_crit, abund_crit, pval_crit, log=None, debug=None)

    # Call OTUs
    caller.run()

    # Get OTU table and sequences
    dbotu_table = caller.otu_table()

    # Write the representative sequences
    # First, initiate new object with type DNAFASTAFormat
    clustered_sequences = DNAFASTAFormat()
    # Pass it in to write_fasta as a file handle
    caller.write_fasta(open(str(clustered_sequences), 'w'))

    return dbotu_table, clustered_sequences

    # # write the setup values to the log file (if present)
    # caller._print_progress_log('---')
    # caller._print_progress_log('time_started', datetime.datetime.now())
    # caller._print_progress_log('genetic_criterion_threshold', gen_crit)
    # caller._print_progress_log('abundance_criterion_threshold', abund_crit)
    # caller._print_progress_log('distribution_criterion_threshold', pval_crit)
    # caller._print_progress_log('sequence_table_filename', os.path.realpath(seq_table_fh.name))
    # caller._print_progress_log('fasta_filename', os.path.realpath(fasta_fn))
    # caller._print_progress_log('otu_table_output_filename', os.path.realpath(output_fh.name))
    # caller._print_progress_log('progress_log_output_filename', os.path.realpath(log.name))
    #
    # if membership is not None:
    #     caller._print_progress_log('membership_output_filename', os.path.realpath(membership.name))
    #
    # if debug is not None:
    #     caller._print_progress_log('debug_log_output_filename', os.path.realpath(debug.name))
    #
    # caller._print_progress_log('---')
    #
    # # run it!
    # caller.run()
    # caller.write_otu_table(output_fh)
    #
    # if membership is not None:
    #     caller.write_membership(membership)
