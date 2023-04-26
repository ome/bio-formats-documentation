R
=

OME does not currently provide an R implementation for Bio-Formats.
However, there are options provided by the community:

Bioconductor RBioFormats
-------------------------

`Bioconductor`_ is a project to develop, support, and disseminate free open 
source software that facilitates rigorous and reproducible analysis of data 
from current and emerging biological assays. Most Bioconductor components are 
distributed as R packages, this includes RBioFormats. RBioFormats is an R package 
which interfaces the OME Bio-Formats Java library to allow reading of proprietary 
microscopy image data and metadata.

Installation
------------

To install this package, start R (version "4.3") and enter::

    if (!require("BiocManager", quietly = TRUE))
      install.packages("BiocManager")

    # The following initializes usage of Bioc devel
    BiocManager::install(version='devel')

    BiocManager::install("RBioFormats")

Documentation
-------------

To view documentation for the version of this package installed in your system, 
start R and enter::

    browseVignettes("RBioFormats")

.. seealso::
    `RBioFormats`_
        Website for the RBioFormats package

    :doc:`/developers/r-dev`
        Section of the developer documentation describing the R wrapper
        for Bio-Formats used by RBioFormats

.. _Bioconductor: https://bioconductor.org
.. _RBioFormats: https://bioconductor.org/packages/devel/bioc/html/RBioFormats.html
