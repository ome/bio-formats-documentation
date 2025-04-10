***********************
Developer Documentation
***********************

The following sections describe various things that are useful to know when
working with Bio-Formats. It is recommended that you obtain the
Bio-Formats source by following the directions in the
:ref:`source-code` section. Referring to the :javadoc:`Javadocs <>` as you
read over these pages should help, as the notes will make more sense when you
see the API.

For a complete list of supported formats, see the Bio-Formats
:doc:`supported formats table </supported-formats>`.

For a few working examples of how to use Bio-Formats, see
:sourcedir:`these Github pages <components/formats-gpl/utils>` and the
:java_examples:`bio-formats-examples repository <>`.


Introduction to Bio-Formats
===========================

.. toctree::
    :maxdepth: 1

    overview
    building-bioformats
    components
    file-reader
    file-writer

Using Bio-Formats as a Java library
===================================

.. toctree::
    :maxdepth: 1

    java-library
    units
    export
    export2
    tiling
    wsi
    in-memory
    logging
    conversion
    matlab-dev
    python-dev
    r-dev
    dotnet-dev
    non-java-code

.. seealso::
   :doc:`/formats/options`

Using Bio-Formats as a native C++ library
=========================================

.. note:: See the `OME-Files C++ downloads page <https://downloads.openmicroscopy.org/latest/ome-files-cpp/>`_
    for more information.

Contributing to Bio-Formats
===========================

.. toctree::
    :maxdepth: 1

    code-formatting
    commit-testing
    generating-test-images
    reader-guide
    format-documentation
    service
    useful-scripts

See :report:`open Trac tickets for Bio-Formats <44>` and the various
`Trello boards <https://trello.com/b/4EXb35xQ/getting-started>`_ for
information on work currently planned or in progress.

For more general guidance about how to contribute to OME projects, see the 
:devs_doc:`Contributing developers documentation <index.html>`.
