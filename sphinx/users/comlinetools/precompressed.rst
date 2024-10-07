"Precompressed" tiles
=====================

See first :doc:`an overview of what precompressed tiles are and which formats support them </formats/precompressed>`.

This feature is primarily exposed in the :program:`bfconvert` command, using the `-precompressed` option.
When the `-precompressed` option is used, best results are obtained by:

* using the `-noflat` option
* **not** using the `-compression` option (this can work, but may force tile recompression)
* **not** using the `-tilex` or `-tiley` options (this can work, but may force tile recompression)

There are several advantages to converting using the "precompressed" feature for formats that support it:

* faster tile read and write times, as no tile compression/decompression needs to be performed
* no change in compression quality
* very little change in file sizes between input and output data

There are also a few disadvantages:

* tile sizes cannot be changed during conversion
* compression type cannot be changed during conversion
* input and output format must support same compression type and tile size
* the input format must have precompressed tile reading support (see :ref:`the list of supported readers <precompressed#readers>`)
* the output format must have precompressed tile writing support (see :ref:`the list of supported writers <precompressed#writers>`)
* command-line tools other than :program:`bfconvert` do not currently make use of the precompressed tile API

For additional discussion of the "precompressed" tiles feature, see:

* https://forum.image.sc/t/vsi-to-dcm-file-conversion/98249/5
* https://forum.image.sc/t/exporting-a-dicom-stack/99400
