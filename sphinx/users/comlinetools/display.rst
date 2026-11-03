Displaying images and metadata
==============================

The :command:`showinf` :doc:`command line tool <index>` can be used to show
the images and metadata contained in a file.

If no options are specified, :program:`showinf` displays a summary of
available options.

.. program:: showinf

To simply display images:

::

  showinf /path/to/file

All of the images in the first 'series' (or 5 dimensional stack) will be
opened and displayed in a simple image viewer.  The number of series, image
dimensions, and other basic metadata will be printed to the console.

.. option:: -noflat

    Do not flatten resolutions into individual series::

      showinf -noflat /path/to/file

.. option:: -series SERIES

    Displays a different series, for example the second one:

    ::

      showinf -series 1 /path/to/file

    Note that series numbers begin with 0.

.. option:: -resolution

    Displays a different resolution of the specified series.
    Only used with :option:`-noflat`.

    ::

      showinf -noflat -series 1 -resolution 1 /path/to/file

    Note that as with :option:`-series`, the resolution index
    starts with 0.

.. option:: -omexml

    Displays the OME-XML metadata for a file on the console:

    ::

      showinf -omexml /path/to/file

.. option:: -nopix

    Image reading can be suppressed if only the metadata is needed:

    ::

      showinf -nopix /path/to/file

.. option:: -option KEY VALUE

    Passes options expressed as key/value pairs::

      showinf -option key value /path/to/file

    e.g. additional reader options, see :doc:`/formats/options`::

      showinf -option leicalif.old_physical_size true /path/to/file

    .. versionadded:: 5.3.0

.. option:: -range START END

    A subset of images can also be opened instead of the entire stack, by
    specifying the start and end plane indices (inclusive):

    ::

      showinf -range 0 0 /path/to/file

    That opens only the first image in first series in the file.

.. option:: -crop X,Y,WIDTH,HEIGHT

    For very large images, it may also be useful to open a small tile from the
    image instead of reading everything into memory.  To open the
    upper-left-most 512×512 tile from the images:

    ::

      showinf -crop 0,0,512,512 /path/to/file

    The parameter to :option:`-crop` is of the format ``x,y,width,height``.
    The (x, y) coordinate (0, 0) is the upper-left corner of the image;
    ``x + width`` must be less than or equal to the image width and
    ``y + height`` must be less than or equal to the image height.

.. option:: -no-upgrade

    By default, :program:`showinf` will check for a new version of
    Bio-Formats.  This can take several seconds (especially on a slow internet
    connection); to save time, the update check can be disabled:

    ::

      showinf -no-upgrade /path/to/file

.. option:: -novalid

    Similarly, if OME-XML is displayed then it will automatically be validated.
    On slow or missing internet connections, this can take some time, and so
    can be disabled:

    ::

      showinf -novalid /path/to/file

.. option:: -validate

    Enforce OME-XML validation (opposite of :option:`-novalid`)::

      showinf -validate /path/to/file

.. option:: -nocore

    Most output can be suppressed:

    ::

      showinf -nocore /path/to/file

.. option:: -xmlversion OME_XML_VERSION

    Use the specified OME-XML schema version instead of the latest::

      showinf -xmlversion 2015-01 /path/to/input

.. option:: -xmlspaces INTEGER

    Use the specified number of spaces when indenting OME-XML for display.
    Defaults to 3.

    ::

      showinf -xmlspaces 4 -omexml /path/to/input

.. option:: -nousedfiles

    Do not print the list of files in the dataset.
    This can be helpful when working with large plates that store
    one plane per file.


    ::

      showinf -nousedfiles /path/to/input

.. option:: -nometa

    Do not read or print more than the minimum necessary metadata to read images::

      showinf -nometa /path/to/file

.. option:: -nofilter

    Do not replace unprintable or XML-invalid characters when converting metadata
    to OME-XML. This is rarely recommended.

    ::

      showinf -nofilter /path/to/file

.. option:: -thumbs

    Display thumbnail images instead of original image data::

      showinf -thumbs /path/to/file

.. option:: -minmax

    Calculate and report the minimum and maximum pixel values for each channel.
    This can cause significantly slower image read times.

    ::

      showinf -minmax /path/to/file

.. option:: -stitch

    Automatically try to group together input files with similar names::

      showinf -stitch /path/to/input

    If the list of input files to be grouped is already know, then using
    a :doc:`/formats/pattern-file` instead is recommended.

.. option:: -nogroup

    Do not look for additional input files to be grouped into the same dataset.
    If the specified input file cannot be read independently (i.e. the format
    strictly requires multiple files), then this option will do nothing::

      showinf -nogroup /path/to/input

.. option:: -separate

    Split RGB input images into separate channels::

      showinf -separate /path/to/input

.. option:: -expand

    If colormaps (lookup tables) are present for the input data,
    permanently apply them, creating RGB images::

      showinf -expand /path/to/input

.. option:: -merge

    Merge separate input channels into RGB images when possible::

      showinf -merge /path/to/input

.. option:: -no-sas

    Do not preserve the OME-XML StructuredAnnotation elements when displaying OME-XML::

      showinf -no-sas -omexml /path/to/input

.. option:: -normalize

    Similar to :option:`-autoscale`, adjusts pixel values to fit into the range [0-1].
    This is primarily needed to display float/double data without error.

    ::

      showinf -normalize /path/to/input

.. option:: -map

    Path to a file, which should be referred to by the name of the
    input file path. This is rarely used in practice, but can be helpful
    for certain tests::

      showinf -map /path/to/actual/input input-reference-name

.. option:: -omexml-only

    Displays the OME-XML alone:

    ::

      showinf -omexml-only /path/to/file

    This is particularly helpful when there are hundreds or thousands of
    series.

.. option:: -debug

    Enables debugging output if more information is needed:

    ::

      showinf -debug /path/to/file

.. option:: -trace

    Enables `TRACE`-level debugging output if more information than :option:`-debug` is needed:

    ::

      showinf -trace /path/to/file

.. option:: -fast

    Displays an image as quickly as possible. This is achieved by converting
    the raw data into a 8 bit RGB image::

      showinf -fast /path/to/file

    .. note::
       Due to the data conversion to a RGB image, using this option results in
       a loss of precision.

.. option:: -autoscale

    Adjusts the display range to the minimum and maximum pixel values::

      showinf -autoscale /path/to/file

    .. note::
       This option automatically sets the :option:`-fast` option and suffers
       from the same limitations.

.. option:: -cache

    Caches the reader under the same directory as the input file after
    initialization::

      showinf -cache /path/to/file

.. option:: -cache-dir DIR

    Specifies the base directory under which the reader should be cached::

      showinf -cache-dir /tmp/cachedir /path/to/file

.. option:: -swap DIMENSIONORDER

    Overrides the default input dimension order.
    This is used when dimension sizes are mixed up and/or planes appear
    out of order with default options::

      showinf -swap XYZTC /path/to/file

.. option:: -shuffle DIMENSIONORDER

    Overrides the default output dimension order.
    This is used when the dimension sizes are correct and planes are correctly ordered,
    but a different dimension order is needed::

      showinf -shuffle XYZTC /path/to/file

.. option:: -format FORMAT

    Specifies the reader to be used for opening the specified file. The utility
    will look for a reader named ``loci.formats.in.<FORMAT>Reader``. If the
    reader does not exist or no :option:`-format` option is passed, the file
    will be opened with ``loci.formats.in.ImageReader``::

      showinf -format APNG test.png

.. option:: -fill UNSIGNED_BYTE

    Sets the fill value to use for undefined pixels.
    Valid values are 0-255, with 0 representing a black pixel and 255 representing a white pixel.
    The value set here will be applied to all bytes in an undefined pixel, e.g. setting to 128 (0x80)
    on a uint16 image will result in a pixel value of 32896 (0x8080).
    The default fill value is typically 0, but some readers may have different defaults.

    .. versionadded:: 6.13.0

.. option:: -

    Batch process multiple files reading file names and any additional options
    line by line from stdin. For every line from stdin ``showinf`` is invoked
    as called from the command prompt, but substituting ``-`` with the stdin
    line.

    ::

      ls *.tiff | showinf -

    .. versionadded:: 8.0.0
