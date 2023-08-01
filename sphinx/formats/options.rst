Additional reader and writer options
====================================

Some readers and writers have additional options which can be used to inform
how Bio-Formats reads or writes files in that format.

Reader options
--------------

.. list-table::
   :header-rows: 1

   * - Format name
     - Option
     - Default
     - Description
   * - :doc:`cellsens-vsi`
     - ``cellsens.fail_on_missing_ets``
     - false
     - Throw an exception if an expected associated .ets file is missing
   * - :doc:`gatan-digital-micrograph`
     - ``gatan.split_montage``
     - true
     - Split montage image tiles across multiple planes
   * - :doc:`leica-lif`
     - ``leicalif.old_physical_size``
     - false
     - Ensure physical pixel sizes are compatible with versions <= 5.3.2
   * - :doc:`nikon-nis-elements-nd2`
     - ``nd2.chunkmap``
     - true
     - Use chunkmap table to read image offsets
   * - :doc:`olympus-scanr`
     - ``scanr.skip_missing_wells``
     - true
     - Ignore missing wells
   * - :doc:`ome-tiff`
     - ``ometiff.fail_on_missing_tiff``
     - true
     - Fail if a missing file is detected in a partial dataset
   * - :doc:`ventana-bif`
     - ``ventana.split_tiles``
     - false
     - Report each tile as a separate series
   * - :doc:`zeiss-czi`
     - ``zeissczi.attachments``
     - true
     - Include attachment images
   * - :doc:`zeiss-czi`
     - ``zeissczi.autostitch``
     - true
     - Automatically stitch tiled images
   * - :doc:`zeiss-czi`
     - ``zeissczi.trim_dimensions``
     - false
     - Trim XY dimensions to match those in ZEN
   * - :doc:`zeiss-czi`
     - ``zeissczi.relative_positions``
     - false
     - Use pixel position instead of the physical stage position

Usage
^^^^^

Reader options can be used via the command line with
:option:`showinf -option`, in ImageJ via the
:doc:`configuration window </users/imagej/features>`, or via the API using the
:javadoc:`DynamicMetadataOptions class <loci/formats/in/DynamicMetadataOptions.html>`.

Writer options
--------------

.. list-table::
   :header-rows: 1

   * - Format name
     - Option
     - Default
     - Description
   * - :doc:`ome-tiff`
     - ``ometiff.companion``
     - None
     - If set, OME-XML will be written to a companion file with a name
       determined by the option value
   * - :doc:`ome-tiff`
     - ``ometiff.preserve_creator``
     - false
     - If set to false, the OME-XML Creator attribute will be updated to include the current Bio-Formats version.
       This will overwrite any existing Creator in the input metadata.
       If set to true, the Creator attribute will only be updated if it wasn't previously set;
       any existing value will be preserved.
   * - :doc:`ome-xml`
     - ``omexml.preserve_creator``
     - false
     - If set to false, the OME-XML Creator attribute will be updated to include the current Bio-Formats version.
       This will overwrite any existing Creator in the input metadata.
       If set to true, the Creator attribute will only be updated if it wasn't previously set;
       any existing value will be preserved.
   * - :doc:`dicom`
     - ``dicom.dual_personality``
     - true
     - If set to true, DICOM files will be written as dual-personality DICOM/TIFF files which include TIFF metadata 
       as described in `Clunie DA. Dual-Personality DICOM-TIFF for Whole Slide Images: A Migration Technique for Legacy Software. 
       J Pathol Inform. 2019 Apr 3;10:12. doi: 10.4103/jpi.jpi_93_18. PMID: 31057981; PMCID: PMC6489422. 
       <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6489422/>`_.
       If set to false, the writing of DICOM files will revert back to the original plain DICOM files

Usage
^^^^^

Writer options can be used via the command line using
:option:`bfconvert -option`, or via the API using the
:javadoc:`DynamicMetadataOptions class <loci/formats/in/DynamicMetadataOptions.html>`.
