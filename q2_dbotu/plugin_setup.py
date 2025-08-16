# ----------------------------------------------------------------------------
# Copyright (c) 2016, Claire Duvallet.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin import Citations, Plugin, Float
from q2_types.feature_table import FeatureTable, Frequency
from q2_types.feature_data import FeatureData, Sequence

from q2_dbotu import __version__
from q2_dbotu._methods import call_otus

citations = Citations.load("citations.bib", package="q2_dbotu")

plugin = Plugin(
    name="dbotu",
    version=__version__,
    website="https://github.com/cduvallet/q2-dbotu",
    package="q2_dbotu",
    description="Distribution-based clustering",
    short_description="Distribution-based clustering",
    citations=[citations['olesen2017dbotu3']]
)

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

    parameters={'gen_crit': Float,
                'abund_crit': Float,
                'pval_crit': Float
    },

    parameter_descriptions={
        'gen_crit': ('Genetic criterion.'),
        'abund_crit': ('Abundance criterion.'),
        'pval_crit': ('P-value criterion.')
    },

)
