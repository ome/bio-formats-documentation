Using Bio-Formats in R
======================

OME does not currently provide an R implementation for Bio-Formats.
However, there are options provided by the community:

Bioconductor RBioFormats
-------------------------

The `RBioFormats <https://bioconductor.org/packages/devel/bioc/html/RBioFormats.html>`_ 
project from Bioconductor provides an R package which interfaces the OME Bio-Formats Java library 
to allow reading of proprietary microscopy image data and metadata.:

.. code-block::

    if (!require("BiocManager", quietly = TRUE))
      install.packages("BiocManager")

    # The following initializes usage of Bioc devel
    BiocManager::install(version='devel')

    BiocManager::install("RBioFormats")


    # To view documentation for the version of this package installed in your system
    browseVignettes("RBioFormats")

For further details and examples of how to use the package, please see the `API documentation <https://bioconductor.org/packages/devel/bioc/vignettes/RBioFormats/inst/doc/RBioFormats.html>`_ 