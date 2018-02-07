Exporting files using Bio-Formats
=================================

This guide pertains to version 4.2 and later.

Basic conversion
----------------

The first thing we need to do is set up a reader:

::

      // create a reader that will automatically handle any supported format
      IFormatReader reader = new ImageReader();
      // tell the reader where to store the metadata from the dataset
      MetadataStore metadata;

      try {
        ServiceFactory factory = new ServiceFactory();
        OMEXMLService service = factory.getInstance(OMEXMLService.class);
        metadata = service.createOMEXMLMetadata();
      }
      catch (DependencyException exc) {
        throw new FormatException("Could not create OME-XML store.", exc);
      }
      catch (ServiceException exc) {
        throw new FormatException("Could not create OME-XML store.", exc);
      }

      reader.setMetadataStore(metadata);
      // initialize the dataset
      reader.setId("/path/to/file");

Now, we set up our writer:

::

      // create a writer that will automatically handle any supported output format
      IFormatWriter writer = new ImageWriter();
      // give the writer a MetadataRetrieve object, which encapsulates all of the
      // dimension information for the dataset (among many other things)
      OMEXMLService service = factory.getInstance(OMEXMLService.class);
      writer.setMetadataRetrieve(service.asRetrieve(reader.getMetadataStore()));
      // initialize the writer
      writer.setId("/path/to/output/file");

Note that the extension of the file name passed to 'writer.setId(…)'
determines the file format of the exported file.

Now that everything is set up, we can start writing planes:

::

      for (int series=0; series<reader.getSeriesCount(); series++) {
        reader.setSeries(series);
        writer.setSeries(series);

        for (int image=0; image<reader.getImageCount(); image++) {
          writer.saveBytes(image, reader.openBytes(image));
        }
      }

Finally, make sure to close both the reader and the writer. Failure to
do so can cause:

-  file handle leaks
-  memory leaks
-  truncated output files

Fortunately, closing the files is very easy:

::

      reader.close();
      writer.close();

Converting to multiple files
----------------------------

The recommended method of converting to multiple files is to use a
single IFormatWriter, like so:

::

      // you should have set up a reader as in the first example
      ImageWriter writer = new ImageWriter();
      OMEXMLService service = factory.getInstance(OMEXMLService.class);
      writer.setMetadataRetrieve(service.asRetrieve(reader.getMetadataStore()));
      // replace this with your own filename definitions
      // in this example, we're going to write half of the planes to one file
      // and half of the planes to another file
      String[] outputFiles =
        new String[] {"/path/to/file/1.tiff", "/path/to/file/2.tiff"};
      writer.setId(outputFiles[0]);

      int planesPerFile = reader.getImageCount() / outputFiles.length;
      for (int file=0; file<outputFiles.length; file++) {
        writer.changeOutputFile(outputFiles[file]);
        for (int image=0; image<planesPerFile; image++) {
          int index = file * planesPerFile + image;
          writer.saveBytes(image, reader.openBytes(index));
        }
      }

      reader.close();
      writer.close();

The advantage here is that the relationship between the files is
preserved when converting to formats that support multi-file datasets
internally (namely OME-TIFF). If you are only converting to graphics
formats (e.g. JPEG, AVI, MOV), then you could also use a separate
IFormatWriter for each file, like this:

::

      OMEXMLService service = factory.getInstance(OMEXMLService.class);
      // again, you should have set up a reader already
      String[] outputFiles = new String[] {"/path/to/file/1.avi", "/path/to/file/2.avi"};
      int planesPerFile = reader.getImageCount() / outputFiles.length;
      for (int file=0; file<outputFiles.length; file++) {
        ImageWriter writer = new ImageWriter();
        writer.setMetadataRetrieve(service.asRetrieve(reader.getMetadataStore()));
        writer.setId(outputFiles[file]);
        for (int image=0; image<planesPerFile; image++) {
          int index = file * planesPerFile + image;
          writer.saveBytes(image, reader.openBytes(index));
        }
        writer.close();
      }

Known issues
------------

`List of Trac tickets
<https://trac.openmicroscopy.org/ome/query?status=accepted&status=new&status=reopened&keywords=~export&component=Bio-Formats&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&order=priority>`_
