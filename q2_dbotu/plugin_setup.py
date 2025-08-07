# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Claire Duvallet.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import qiime2.plugin
# Import QIIME 2 types
from q2_types.feature_table import FeatureTable, Frequency
from q2_types.feature_data import FeatureData, Sequence

# Import dbOTU functions
import q2_dbotu
from q2_dbotu._call_otus import call_otus

cites = qiime2.plugin.Citations.load('citations.bib',
    package='q2_dbotu')

plugin = qiime2.plugin.Plugin(
    name='q2-dbotu',
    version=q2_dbotu.__version__,
    website='http://www.github.com/cduvallet/q2-dbotu',
    package='q2_dbotu',
    citations=[cites['preheim2013dbotu1'], cites['olesen2017dbotu3']],
    description=('This QIIME 2 plugin calls OTUs using distribution-based '
                 'clustering.'),
    short_description='Plugin for distribution-based clustering.',
    user_support_text=('Raise an issue on the github repo: https://github.com/cduvallet/q2-dbotu')
)


#TODO: add output stats/membership file

# Register function to call dbOTUs
plugin.methods.register_function(
    function=call_otus,
    name=('Distribution-based OTU caller'),
    description=('Calls distribution-based OTUs.'),

    inputs={
        'table': FeatureTable[Frequency],
        'sequences': FeatureData[Sequence]},

    input_descriptions={
        'table': ('The feature table containing counts for the '
                   'dereplicated sequences (e.g. 100% OTUs or ASVs).'),
        'sequences': ('Input sequences. These should be either dereplicated '
                      '(i.e. 100% OTUs) or exact sequence variants (i.e. '
                      'output from deblur or DADA2 denoising). They do not '
                      'have to be sorted in order of abundance.')},

    outputs=[('dbotu_table', FeatureTable[Frequency]),
            ('representative_sequences', FeatureData[Sequence])],

    output_descriptions={
        'dbotu_table': 'Feature table with sample counts for dbOTUs.',
        'representative_sequences': 'Representative sequences for each dbOTU.'},

    parameters={'gen_crit': qiime2.plugin.Float,
                'abund_crit': qiime2.plugin.Float,
                'pval_crit': qiime2.plugin.Float
    },

    parameter_descriptions={
        'gen_crit': ('Genetic criterion.'),
        'abund_crit': ('Abundance criterion.'),
        'pval_crit': ('P-value criterion.')
    },

)
