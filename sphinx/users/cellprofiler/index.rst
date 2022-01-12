CellProfiler
============

`CellProfiler`_—developed by the `Broad Institute Imaging Platform`_—is
free open-source software designed to enable biologists without training
in computer vision or programming to quantitatively measure phenotypes
from thousands of images automatically. CellProfiler uses Bio-Formats to
read images from disk, as well as write movies.

Installation
------------

The CellProfiler distribution comes with Bio-Formats included, so no
further installation is necessary.

Upgrading
---------

It should be possible to use a newer version of Bio-Formats by replacing
the bundled **bioformats_package.jar** with a newer version.

-  For example, on Mac OS X, Ctrl+click the CellProfiler icon, choose
   :guilabel:`Show Package Contents`, and replace the following file:

   - :file:`Contents/Resources/bioformats/jars/bioformats_package.jar`

.. seealso::
    `CellProfiler`_
        Website of the CellProfiler software

    :doc:`/developers/python-dev`
        Section of the developer documentation describing the Python wrapper
        for Bio-Formats used by CellProfiler

.. _CellProfiler: http://cellprofiler.org/
.. _Broad Institute Imaging Platform: https://www.broadinstitute.org/imaging
