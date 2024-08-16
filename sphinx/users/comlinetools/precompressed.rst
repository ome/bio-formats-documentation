"Precompressed" tiles
=====================

Some formats allow reading and/or writing "precompressed" tiles.
This feature is primarily intended for whole slide images, each of which may have thousands of tiles.
Data representing these tiles may be compressed, either lossily or losslessly, depending on the
file format, imaging modality, or acquisition configuration.

When reading, this allows for retrieving compressed bytes that are as close as possible
to what is actually stored in the file. Decompression (if necessary) is the responsibility
of the consumer.

When writing, compressed bytes instead of raw bytes can be provided to the writer,
such that the writer will just save the provided compressed bytes instead of recompressing.

This feature is primarily exposed in the :program:`bfconvert` command, using the `-precompressed` option.
When the `-precompressed` option is used, best results are obtained by:

* using the `-noflat` option
* _not_ using the `-compression` option (this can work, but may force tile recompression)
* _not_ using the `-tilex` or `-tiley` options (this can work, but may force tile recompression)

There are several advantages to using the "precompressed" feature for formats that support it:

* faster tile read and write times, as no tile compression/decompression needs to be performed
* no change in compression quality
* very little change in file sizes between input and output data

There are also a few disadvantages:

* tile sizes cannot be changed during conversion
* compression type cannot be changed during conversion
* input and output format must support same compression type and tile size
* not all formats supported by Bio-Formats currently allow reading/writing precompressed tiles
* tools other than :program:`bfconvert` do not currently make use of the precompressed tile API

Formats that support precompressed tile reading:

* SVS (since 7.1.0)
* NDPI (forthcoming: https://github.com/ome/bioformats/pull/4181)
* DICOM (forthcoming: https://github.com/ome/bioformats/pull/4190)

Formats that support precompressed tile writing:

* DICOM (since 7.1.0)
* TIFF (forthcoming: https://github.com/ome/bioformats/pull/4190)
* OME-TIFF (forthcoming: https://github.com/ome/bioformats/pull/4190)

For additional discussion of the "precompressed" tiles feature, see:

* https://forum.image.sc/t/vsi-to-dcm-file-conversion/98249/5
* https://forum.image.sc/t/exporting-a-dicom-stack/99400
