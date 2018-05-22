# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, Claire Duvallet.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name="dbotu_q2",
    version="0.0.1",
    packages=find_packages(),
    author="Claire Duvallet",
    author_email="duvallet@mit.edu",
    description="Distribution-based clustering",
    license='BSD-3-Clause',
    url="https://qiime2.org",
    entry_points={
        'qiime2.plugins':
        ['dbotu_q2=dbotu_q2.plugin_setup:plugin']
    },
    zip_safe=False,
    package_data={
        'dbotu_q2': ['citations.bib']
    }
)
