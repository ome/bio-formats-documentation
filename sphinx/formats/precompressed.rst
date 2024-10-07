Support for "precompressed" tiles
=================================

Some formats allow reading and/or writing "precompressed" tiles.
This feature is primarily intended for whole slide images, each of which may have thousands of tiles.
Data representing these tiles may be compressed, either lossily or losslessly, depending on the
file format, imaging modality, or acquisition configuration.

When reading, this allows for retrieving compressed bytes that are as close as possible
to what is actually stored in the file. Decompression (if necessary) is the responsibility
of the consumer.

When writing, compressed bytes instead of raw bytes can be provided to the writer,
such that the writer will just save the provided compressed bytes instead of recompressing.

See also :doc:`how to work with precompressed tiles in bfconvert </users/comlinetools/precompressed>`

.. _precompressed#readers:

Formats that support precompressed tile reading
-----------------------------------------------

* SVS (since 7.1.0)
* NDPI (since 8.0.0)
* DICOM (since 8.0.0)

.. _precompressed#writers:

Formats that support precompressed tile writing
-----------------------------------------------

* DICOM (since 7.1.0)
* TIFF (since 8.0.0)
* OME-TIFF (since 8.0.0)
