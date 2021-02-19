Converting a file to different format
=====================================

The :command:`bfconvert` :doc:`command line tool <index>` can be used to convert
files between :doc:`supported formats </supported-formats>`.

:command:`bfconvert` with no options displays a summary of available options.

.. program:: bfconvert

To convert a file to single output file (e.g. TIFF):

::

  bfconvert /path/to/input output.tiff

The output file format is determined by the extension of the output file, e.g.
.tiff for TIFF files, .ome.tiff for OME-TIFF, .png for PNG.

.. option:: -option KEY VALUE

    Passes options expressed as key/value pairs::

      bfconvert -option key value /path/to/input /path/to/output

    e.g. additional writer options, see :doc:`/formats/options`::

      bfconvert -option ometiff.companion converted.companion.ome input.fake converted.ome.tiff

    .. versionadded:: 5.4.0

.. option:: -noflat

    Do not flatten resolutions into individual series. This option is mandatory
    to read images with pyramidal levels using the sub-resolution API and
    generate an output image with sub-resolutions. As of Bio-Formats 6.0.0,
    only the OME-TIFF output format properly supports this option::

      bfconvert -noflat /path/to/input output-first-series.ome.tiff

    .. versionadded:: 6.0.0

.. option:: -series SERIES

    All images in the input file are converted by default.  To convert only
    one series::

      bfconvert -series 0 /path/to/input output-first-series.tiff

.. option:: -timepoint TIMEPOINT

    To convert only one timepoint::

      bfconvert -timepoint 0 /path/to/input output-first-timepoint.tiff

.. option:: -channel CHANNEL

    To convert only one channel::

      bfconvert -channel 0 /path/to/input output-first-channel.tiff

.. option:: -z Z

    To convert only one Z section::

      bfconvert -z 0 /path/to/input output-first-z.tiff

.. option:: -range START END

    To convert images between certain indices (inclusive)::

      bfconvert -range 0 2 /path/to/input output-first-3-images.tiff

.. option:: -tilex TILEX, -tiley TILEY

    All images larger than 4096×4096 will be saved as a set of tiles if the
    output format supports doing so.  The default tile size is determined by
    the input format, and can be overridden like this::

      bfconvert -tilex 512 -tiley 512 /path/to/input output-512x512-tiles.tiff

    :option:`-tilex` is the width in pixels of each tile; :option:`-tiley` is
    the height in pixels of each tile.  The last row and column of tiles may
    be slightly smaller if the image width and height are not multiples of the
    specified tile width and height.  Note that specifying :option:`-tilex`
    and :option:`-tiley` will cause tiles to be written even if the image is
    smaller than 4096×4096.

    Also note that the specified tile size will affect performance.  If large
    amounts of data are being processed, it is a good idea to try converting a
    single tile with a few different tile sizes using the :option:`-crop`
    option. This gives an idea of what the most performant size will be.

.. option:: -crop X,Y,WIDTH,HEIGHT

    For very large images, it may also be useful to convert a small tile from
    the image instead of reading everything into memory. To convert the
    upper-left-most 512×512 tile from the images:

    ::

      bfconvert -crop 0,0,512,512 /path/to/file output-512x512-crop.tiff

    The parameter to :option:`-crop` is of the format ``x,y,width,height``.
    The (x, y) coordinate (0, 0) is the upper-left corner of the image;
    ``x + width`` must be less than or equal to the image width and
    ``y + height`` must be less than or equal to the image height.

Images can also be written to multiple files by specifying a pattern string
in the output file.  For example, to write one series, timepoint, channel, and
Z section per file::

  bfconvert /path/to/input output_series_%s_Z%z_C%c_T%t.tiff

``%s`` is the series index, ``%z`` is the Z section index, ``%c`` is the
channel index, and ``%t`` is the timepoint index (all indices begin at 0).

For large images in particular, it can also be useful to write each tile to
a separate file::

  bfconvert -tilex 512 -tiley 512 /path/to/input output_tile_%x_%y_%m.jpg

``%x`` is the row index of the tile, ``%y`` is the column
index of the tile, and ``%m`` is the overall tile index.  As above, all
indices begin at 0.  Note that if ``%x`` or ``%y`` is included in the file
name pattern, then the other must be included too.  The only exception is if
``%m`` was also included in the pattern.

Note for Windows Users: The command interpreter for batch files needs the ``%``
characters to be doubled in order to process the sequencing variables
correctly. So in Windows, the above example would read::

  bfconvert /path/to/input output_series_%%s_Z%%z_C%%c_T%%t.tif

.. option:: -compression COMPRESSION

    By default, all images will be written uncompressed.  Supported compression
    modes vary based upon the output format, but when multiple modes are
    available the compression can be changed using the :option:`-compression`
    option. For example, to use LZW compression in a TIFF file::

      bfconvert -compression LZW /path/to/input output-lzw.tiff

.. option:: -overwrite

    If the specified output file already exists, :program:`bfconvert` will
    prompt to overwrite the file.  When running :program:`bfconvert`
    non-interactively, it may be useful to always allow :program:`bfconvert` to
    overwrite the output file::

      bfconvert -overwrite /path/to/input /path/to/output

.. option:: -nooverwrite

    To always exit without overwriting::

      bfconvert -nooverwrite /path/to/input /path/to/output

.. option:: -nolookup

    To disable the conversion of lookup tables, leaving the output
    file without any lookup tables::

      bfconvert -nolookup /path/to/input /path/to/output

    .. versionadded:: 5.2.1

.. option:: -bigtiff

    This option forces the writing of a BigTiff file::

      bfconvert -bigtiff /path/to/input output.ome.tiff

    .. versionadded:: 5.1.2

    The :option:`-bigtiff` option is not necessary if a BigTiff extension is
    used for the output file, e.g.::

        bfconvert /path/to/input output.ome.btf

.. option:: -nobigtiff

    This option disables the automatic switching to BigTiff based upon the number of pixel bytes 
    (TIFF files larger than 4GB)::

      bfconvert -nobigtiff /path/to/input output.ome.tiff

    .. versionadded:: 6.4.0

    Using the :option:`-nobigtiff` will disable writing BigTiff when the output format is less than 4GB. 
    It will not be able to write standard Tiff files greater than 4GB. An example of when it might be 
    used would be when converting using a compression codec that reduces the size of the output file, e.g.:: 

        bfconvert -nobigtiff -compression LZW /path/to/input output.ome.btf

.. option:: -padded

    This option is used alongside a pattern string when writing an image to multiple files.
    When set this will enforce zero padding on the filename indexes set in the provided pattern string::

      bfconvert /path/to/input output_xy%sz%zc%ct%t.ome.tif -padded

    .. versionadded:: 5.2.2

.. option:: -pyramid-resolutions RESOLUTIONS
.. option:: -pyramid-scale SCALE

    When using :option:`-noflat` by default, each series of the converted file
    will contain the same number of resolutions as in the input file. The
    :option:`-pyramid-resolutions` option allows to set the number of
    expected resolutions in the output file for each series. If the target
    number of resolutions is greater than the actual number of sub-resolutions
    present in the input file, additional pyramidal levels will be calculated
    using the downsampling factor specified by the :option:`-pyramid-scale`
    option::

      bfconvert -noflat -pyramid-resolutions 4 -pyramid-scale 2 /path/to/input out.ome.tiff

    .. versionadded:: 6.0.0

.. option:: -cache

    This option will cache the initialized reader under the same directory as 
    the input file after initialization::

      bfconvert -cache /path/to/input output.ome.tiff

    .. versionadded:: 6.2.0

.. option:: -cache-dir DIRECTORY

    This option is to be used in conjunction with :option:`-cache`. When used 
    it specifies the directory to store the cached initialized reader. If unspecified, 
    the cached reader will be stored under the same folder as the image file::

      bfconvert -cache-dir /path/to/store/cached/reader /path/to/input output.ome.tiff

    .. versionadded:: 6.2.0

.. option:: -no-sas

    Do not preserve the OME-XML StructuredAnnotation elements::

      bfconvert -no-sas /path/to/input output.ome.tiff

    .. versionadded:: 6.2.0
