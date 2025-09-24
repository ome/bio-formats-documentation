External file format readers
============================

Bio-Formats contains a file named :source:`readers.txt <components/formats-api/src/loci/formats/readers.txt>`
which records every recognized reader class name. This file is used by the main reader class
(:javadoc:`loci.formats.ImageReader <loci/formats/ImageReader.html>`) to associate a format reader
with a particular file.

For readers that are included in core Bio-Formats (i.e. the `ome/bioformats` repository on GitHub),
a line containing just the fully qualified class name is added, e.g.:

.. code-block::

  loci.formats.in.OMETiffReader         # tif

An optional comment can be added after the class name using `#`.

Readers that are not in `ome/bioformats` and which are not included in Bio-Formats releases can be
defined as "external" readers, e.g.:

.. code-block::

  loci.formats.in.ZarrReader[type=external]         # .zarr

This allows Bio-Formats to recognize a reader if it was installed separately,
but quietly ignore if it is not found.

When to use an external reader
------------------------------

The OME team often encourages new readers to be proposed as "external" under any of the following conditions:

- the newly introduced reader code is very large and/or complex
- native libraries or closed-source dependencies are required
- the reader covers an imaging domain which is unfamiliar to the OME team
- test data cannot be provided to the OME team
- the reader needs to be updated outside of the normal Bio-Formats release process

When considering a new reader, we suggest discussing with the OME team first before making substantial changes.

How to propose an external reader
---------------------------------

As indicated above, we suggest discussing with the OME team before investing significant time in a new reader.

At minimum, open a new pull request on `ome/bioformats` that updates `readers.txt` as indicated above,
including the following information:

- where to find the reader source code
- who is maintaining the external reader, and an acknowledgement that the OME team is not responsible for maintaining this reader
- where/how the reader will be released
- test data, if possible
- supporting documentation (issues, forum threads, etc.) indicating why this reader is necessary

If we are not able to test the proposed external reader due to missing test data or dependencies,
then we are unlikely to approve it.

.. seealso::

  `OME's Third Party Contribution and Interaction Policy <https://ome-contributing.readthedocs.io/en/latest/third-party-policy.html>`_

What external reader ownership involves
---------------------------------------

Developing an external reader means taking complete ownership and responsibility for
the development, maintenance, testing, and distribution of the reader. The OME team
will not review code, fix issues, or otherwise participate in the development or
release process. As a result, it is very important to have a maintenance and testing
plan that includes:

- where issues should be reported
- who is responsible for fixing issues and releasing new versions
- where/how to find new versions of the reader, e.g. a Fiji update site
