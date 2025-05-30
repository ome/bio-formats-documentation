Version history
===============

8.2.0 (2025 May)
----------------

New file formats:

* Molecular Devices JDCE
    - Added support for datasets acquired on ImageXpress HCS.ai High-Content Screening System
    - Added support for datasets acquired on IN Cell Analyzer 2XXX/6XXXX series and converted into JDCE format by IN Carta® Image Analysis Software

File format fixes:

* ARF
    - improve type checking to prevent false positives
* Hamamatsu DCIMG
    - fix image stride in DCIMG version 1 and later (thanks to Zach Marin)
* Leica LIF
    - fix mapping of images to memory blocks containing pixel data
* Metamorph
    - warn if timestamp values are invalid or cannot be parsed
* MIAS
    - fix sorting of directory listings
* Prairie Technologies TIFF
    - add support for multi-page TIFFs (thanks to Michael Fox)
* ScanR
    - make sure the initialized file is placed first on the used file list
* Zeiss CZI
    - fix sub-block sizes in pyramid sub-resolutions (thanks to Jürgen Bohl)


Bio-Formats improvements:

* Fix Maven repository URLs to prevent build instability
* Prevent file appending when exporting via ImageJ plugin
* Fix color map array allocation in `bfopen` function in MATLAB toolbox
* Remove obsolete Python script for updating version metadata
* Fix several type conversion warnings raised by CodeQL, to prevent integer overflows

Component updates:

* `sqlite-jdbc` was upgraded to 3.49.1.0 to fix CVE-2023-32697 (thanks to Curtis Rueden)

8.1.1 (2025 March)
------------------

File format fixes:

* Imspector
    - fix `NumberFormatException` when reading timepoint count
* InCell
    - ignore timepoint configurations if a timelapse was not acquired
    - fix handling of channels with different Z sizes
    - add `incell.duplicate_missing_planes` option
* Metamorph
    - allow files to initialize when channel wavelengths are invalid
* Nikon ND2
    - fix pixel type detection for floating point multiposition data
* ScanR
    - fix exposure time reporting when field positions are missing
* Spider
    - fix type cast warning in image count calculation raised by CodeQL

Bio-Formats improvements:

* Remove unused and obsolete C++ and Javascript files
* Update GitHub Actions configuration to include CodeQL workflows
* Add options to `FakeReader` to create test data with instrument and channel wavelength metadata
* Ensure `getAvailableOptions()` in `IFormatReader` API returns the correct reader options

8.1.0 (2025 February)
---------------------

New file formats:

* Hamamatsu DCIMG
    - add a new reader for Hamamatsu .dcimg files (thanks to Zach Marin)

File format fixes:

* Evident/Olympus OIR
    - fix an issue with reading timestamp metadata
* Evident/Olympus VSI
    - fix ordering of used files list
* Fuji
    - fix ordering of used files list
* Imaris HDF
    - add caching and support for LZ4 compression (thanks to Marco Stucchi)
* Leica TCS
    - ensure all relevant files are included in used files list

Bio-Formats improvements:

* Remove `LOCI` entry from ImageJ plugins menu (thanks to Tiago Ferreira)
* Fix array endianness in `bfsave` MATLAB function
* Fix `-version`, `-debug`, `-trace`, and `-no-upgrade` options in `tiffcomment` command line tool

Component updates:

* `logback` was upgraded to 1.3.15
* `ome-codecs` was upgraded to 1.1.0
* `ome-common` was upgraded to 6.0.25
* `ome-metakit` was upgraded to 5.3.8
* `ome-model` was upgraded to 6.4.0

8.0.1 (2024 November)
---------------------

File format fixes:

* PerkinElmer Operetta
   - prevent directories from being included in the used files list
   - calculate physical Z size in micrometers, for improved readability

Bio-Formats improvements:

* Fix regression in `showinf` that prevented images from being displayed
* Add test to ensure that the initialized file is placed first on the used files list
* Include original metadata when exporting OME-TIFF via the Bio-Formats Exporter plugin for ImageJ

8.0.0 (2024 October)
--------------------

File format fixes and improvements:

* CV7000
   - allow TIFF files to be in a subdirectory

* DICOM
   - add support for reading precompressed tiles [1]_
   - improve image write performance [1]_
   - fix writing to DICOM when physical size units are missing from input data

* Evident/Olympus OIR
   - improve image read performance (thanks to Nicolas Chiaruttini)

* Hamamatsu NDPI
   - add support for reading precompressed tiles [1]_

* Leica LIF
   - fix file offset calculations for datasets with unstitched tiles

* OME-TIFF
   - improve image write performance
   - add support for writing precompressed tiles [1]_

* OME-XML
   - fix incorrect logical operators when checking image dimensions

* RCPNL
   - define objective metadata for lens ID 18112

* SDT
   - fix reading of files acquired with SPCM 9.90 (thanks to Chen Qian)

* Zeiss LSM
   - fix incorrect logical operators when setting channel colors

Bio-Formats improvements:

* Add a batch processing feature to `showinf` (thanks to Torsten Stöter)
* Update `bfconvert` to automatically detect the compression type when using `-precompressed` [1]_
* Fix autoscaling of `float` values in `AWTImageTools`
* ImageJ export plugin: fix handling of multi-channel datasets
* `JPEGTurboService` [1]_
   - add several new methods for retrieving tiles from a single JPEG stream
   - expand Javadocs for existing methods

Documentation updates:

* update all links to AwareSystems TIFF documentation to last version from Internet Archive
    - see `libtiff mailing list discussion <https://www.mail-archive.com/tiff@lists.osgeo.org/msg00421.html>`_ for context
* fix index of command-line tools
* add documentation for new batch processing feature in `showinf` (thanks to Torsten Stöter)
* add documentation for precompressed tiles feature [1]_
* several other fixes for broken links

Component updates:

* `ome-common` was upgraded to 6.0.24
* `cdm-core` was upgraded to 5.6.0

.. [1] This functionality was implemented through collaboration between Glencoe Software and `NCI Imaging Data Commons <https://datacommons.cancer.gov/repository/imaging-data-commons/>`_,
       and has been funded in whole or in part with Federal funds from the National Cancer Institute, National Institutes
       of Health, under Task Order No. HHSN26110071 under Contract No. HHSN2612015000031.

7.3.1 (2024 July)
-----------------

File format fixes and improvements:

* Aperio SVS
   - updated isThisType to reject files with a single IFD

* ICS (Image Cytometry Standard)
   - fixed a Null Pointer Exception when the image name is not set

* Imaris HDF
   - fixed handling of channels with an empty color attribute 

* PerkinElmer Columbus
   - updated to use micrometers instead of reference frame for positions

Bio-Formats improvements:

* fixed warnings across all components for Java 9+ 
    - Among other things, this includes changes to how double values are parsed from strings in many format readers.
      These changes are expected to be more lenient in allowing datasets with certain missing or invalid metadata
      values (e.g. objective magnifications, detector voltages) to be read without throwing an exception. This means
      that some datasets which failed to read in 7.3.0 may now suddenly work (or fail at a later point) with 7.3.1,
      without an intentional targetted fix for that format. For specific changes to format readers, please see
      https://github.com/ome/bioformats/pull/4182 and https://github.com/ome/bioformats/pull/4177.
* fixed a number of String comparisons

Documentation improvements:

* fixed a number of broken external links

7.3.0 (2024 April)
------------------

File format fixes and improvements:

* CellSens VSI
   - fixed an exception in CellSens 4.1 data by updating the handling of orphaned ets files (thanks to Edward Scanlon)

* DICOM
   - updated handling of nested sequences that include pixel data
   - removed a duplicate enum check in the DICOM writer

* OME-XML
   - reading an OME-XML file now populates the original metadata table

* PerkinElmer Columbus
   - added support for reading data with Z stacks (thanks to Tim Blackmore)

* Prairie Technologies TIFF
   - improved type checking for Prairie files

* SimplePCI
   - fixed handling of Z position metadata

Bio-Formats improvements:

* Bio-Formats is now compatible with Java 21 builds
* added a new `quality` option to `bfconvert` which enables the setting of the compression quality to be used. 
* when using the `channel` option in `bfconvert`, the unselected channels are now correctly removed from the OME-XML metadata
* added coverage of Apple M1 as part of the CI process
* added coverage of Java 21 builds as part of the CI process

Component updates:

* `ome-jai` was upgraded to 0.1.4
* `ome-stubs` was upgraded to 6.0.2
* `ome-mdbtools` was upgraded to 5.3.3
* `ome-common` was upgraded to 6.0.22
* `ome-poi` was upgraded to 5.3.9
* `ome-metakit` was upgraded to 5.3.7
* `ome-codecs` was upgraded to 1.0.3
* `ome-xml` was upgraded to 6.3.6
* `specification` was upgraded to 6.3.6

Documentation improvements:

* fixed a number of broken external links
* documented the new `quality` option in `bfconvert`

7.2.0 (2024 February)
---------------------

File format fixes and improvements:

* Aperio SVS
   - improved detection of label and macro images
   - thumbnails are now removed by default
   - added a new reader option `svs.remove_thumbnail` to control the thumbnail behaviour. By default 
     the option is true and thumbnails are removed. Setting the option to false will restore the previous 
     behavior and include thumbnails

* Imaris HDF
   - channel names are now correctly populated

* Olympus OIR
   - fixed an issue with channel ordering
   - prevent certain pixel blocks from being incorrectly skipped

* TIFF
   - dimension order is now marked as certain if metadata is read from ImageJ tag

* Zeiss CZI
   - improved well column indexing by using alternate sources for well identifiers when available
   - improved image naming, particularly for attachments
   - fixed a bug so that opening CZI compressed with ZSTD now allows access to pyramid levels (thanks to Stephan Wagner-Conrad)
   - fixed an integer arithmetic problem when calculating pyramid scales (thanks to Stephan Wagner-Conrad)

Bio-Formats improvements:

* JPEG handling no longer fails for non 4:4:4 JPEG (thanks to Can Gokhan Dogan)
* fixed a bug in the Bio-Formats Plugins configuration window when toggling the Nikon ND2 chunkmap option
* updated testing to add an additional check for image names when resolutions are not flattened

Documentation improvements:

* fixed a number of broken external links

7.1.0 (2023 December)
---------------------

API Additions

* ICompressedTileReader 
   - a new interface allowing for the reading of compressed bytes without decompression. Currently only 
     implemented by the SVSReader

* ICompressedTileWriter
   - a new interface allowing for the writing of precompressed bytes. Currently only implemented by the DICOM Writer

* IExtraMetadataWriter
   - a new interface enabling extra supplemental metadata to be set for inclusion in a writer. Currently only 
     implemented by the DICOM Writer

File format fixes and improvements:

* Aperio SVS
   - added implementation for the reading of compressed data without decompression using the new 
     ICompressedTileReader interface

* cellSens VSI
   - fixed handling of uncompressed BGR data

* CV7000
   - action index is now included in the channel name
   - Fluor will now be set on Channel when possible
   - for missing planes the default behavior has switched from returning a blank plane to returning the 
     first plane in the channel 
   - added a new reader option `cv7000.duplicate_missing_planes` to control the behavior for missing planes 

* DICOM
   - added implementation for the writing of precompressed data using the new ICompressedTileWriter interface
   - added implementation for the writing of extra supplemental metadata data using the new IExtraMetadataWriter 
     interface. Extra metadata can be provided in the form of a .json file 
   - This functionality was implemented through collaboration between Glencoe Software and `NCI Imaging Data Commons <https://datacommons.cancer.gov/repository/imaging-data-commons/>`_,
     and has been funded in whole or in part with Federal funds from the National Cancer Institute, National Institutes 
     of Health, under Task Order No. HHSN26110071 under Contract No. HHSN2612015000031.

* Photoshop TIFF
   - fixed plane reading with memoization

Bio-Formats improvements:

* fixed handling of JPEG Turbo service when the native library cannot be loaded, most notably for Apple Silicon 
  instances. An IOException will now be thrown by readers that require the library but the RunTimeException 
  introduced in 7.0.1 will no longer be thrown when the library is not required
* prevented unnecessary Lurawave debug error being printed (thanks to Can Gokhan Dogan)
* updated license headers for all Java sources of the OME-XML library
* added a new codec option `disableChromaSubsampling` along with implementation for the JPEG Codec (thanks to Peter Haub)
* updated github actions checkout version to v4 and build release on ubuntu 22.04
* json dependency moved from formats-gpl to formats-bsd
* TiffSaver now generates valid 4-channel RGBA images (thanks to Can Gokhan Dogan)
* added a new ` precompressed`  option to the bfconvert tool, enabling the conversion of precompressed tiles. 
  Currently only supported for converting from SVS to DICOM.
* added a new ` extra-metadata`  option to the bfconvert tool for providing supplemental metadata during conversion. 
  Currently only supported for writing to DICOM

Component updates:

* `slf4j-api` was upgraded to 2.0.9
* `logback-classic` was upgraded to 1.3.14
* `logback-core` was upgraded to 1.3.14
* `xalan` was upgraded to 2.7.3
* `com.google.guava` was upgraded to 32.0.0-jre
* `json` was upgraded to 20230227
* `ome-common` was upgraded to 6.0.21
* `ome-model` was upgraded to 6.3.4
* `ome-codecs` was upgraded to 1.0.1
* `ome-poi` was upgraded to 5.3.8
* `ome-metakit` was upgraded to 5.3.6

Documentation improvements:

* fixed a number of broken external links
* updated the bfconvert instructions to document new options
* added a new link for the external Bioformats.NET project

7.0.1 (2023 October)
--------------------

File format fixes and improvements:

* Amersham Biosciences Gel
   - improved format detection

* Aperio SVS
   - fixed a NullPointerException when attempting to read the magnification metadata
   - physical sizes and positions are now calculated for full resolution label and macro images
   - fixed a regression from Bio-Formats 6.8.0 which saw label and macro images incorrectly indexed

* DICOM
   - the DICOM writer will now throw an exception if the provided tiles don't match the 
     expected tile size

* Gatan DM3
   - fixed a StringIndexOutOfBoundsException when parsing acquisition mode

* Hamamatsu NDPI
   - corrected for potential integer overflow in stored restart marker tag

* IVision
   - improved the version and data type checks in isThisType

* Leica LIF
   - improved the exception handling if no images are found

* Olympus OIR
   - fixed issue with XML block reading that resulted in missing pixel blocks

* OME-TIFF
   - reader will now fail fast and throw a FormatException if an invalid file is found

* TIFF
   - a FormatException is now thrown for unsupported 64-bit int data
   - for all TIFF based formats the IFD entry offset is now checked before seeking

* TillVision
   - improved metadata parsing and detection of .pst files

* Ventana
   - fixed tile arithmetic for smallest resolutions

* Zeiss CZI
   - unified channel color parsing so that retrieving lookup tables now allows RGB and ARGB colors

Bio-Formats improvements:

* URLHandle will fall back to resetting stream if resetting to a mark fails
* an exception will now be thrown if the TurboJPEG library fails to load (thanks to Can Gokhan Dogan)
* fixed a Bio-Formats plugin bug when attempting to export a file after reducing the range of channels
* reviewed and updated a number of file headers
* updated GitHub Actions from checkout v2 to v3

Component updates:

* `ome-common` was upgraded to 6.0.20

Documentation improvements:

* fixed a number of broken external links
* updated the link to OME Model documentation
* migrated readthedocs configuration to version 2

7.0.0 (2023 August)
-------------------

Removal of deprecated components:

* Legacy ND2 Reader
   - The LegacyND2Reader and underlying components have been removed. This reader depended on an 
     outdated DLL which had not been built in years, was untested and fully superseded by the new
     NativeND2Reader. The existing NativeND2Reader has been renamed as ND2Reader and now acts as the 
     sole reader for the format. Support for the ND2 format will be unaffected and continue via this 
     newly renamed reader.

* Legacy QuickTime
   - The LegacyQT Reader, Writer and Tools have been removed. These classes depended on the external 
     QuickTime for Java library which is long obsolete. The existing NativeQTReader has been renamed 
     as QTReader and support for QuickTime is now limited to non legacy readers and writers.

* LuraWave Codec
   - The LuraWave Codec along with the LuraWaveService and associated components have been removed and 
     are no longer supported. This codec was dependent on a third-party proprietary library with a 
     license code. This may impact LuraWave compressed files for the Opera Flex format.

* Woolz
   - The Woolz Reader, Writer and Service have been removed and are no longer supported. The reader 
     and writer are untested and rely on an underlying library which has an unclear maintenance status.

File format fixes and improvements:

* DICOM
   - support has been added for the writing dual-personality of DICOM/TIFF. The DICOM 
     writer will now, by default, include TIFF metadata as described in 
     https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6489422/. These new dual-personality files can 
     be read either by the DICOM reader or can also be recognised as TIFF. A new option named
     `dicom.dual_personality` has been added to the DicomWriter. Setting this new option to false will 
     revert writing of DICOM files back to the original plain DICOM files. This functionality was 
     implemented through collaboration with `NCI Imaging Data Commons <https://datacommons.cancer.gov/repository/imaging-data-commons/>`_, and has been funded in whole or 
     in part with Federal funds from the National Cancer Institute, National Institutes of Health, 
     under Task Order No. HHSN26110071 under Contract No. HHSN2612015000031.

* PerkinElmer Opera Flex
   - reader will now ignore files in which the compression cannot be identified

* PerkinElmer Operetta
   - fixed an exception when reading null planes (thanks to Nicolas Chiaruttini)

Component updates:

* `ome-common` was upgraded to 6.0.19
* `ome-stubs` was upgraded to 6.0.1
* `ome-codecs` was upgraded to 1.0.0
* `native-lib-loader` was upgraded to 2.4.0 (thanks to Can Gokhan Dogan)

Documentation improvements:

* fixed a number of broken links

6.14.0 (2023 July)
------------------
Deprecation warnings:

* Legacy ND2 Reader
   - The LegacyND2Reader and underlying components have been marked as deprecated in preparation 
     for removal in the upcoming 7.0.0 major release of Bio-Formats. This reader depends on an outdated 
     DLL which has not been built in years, is untested and fully superseded by the new NativeND2Reader. 
     From Bio-Formats 7.0.0 onwards the existing NativeND2Reader will be renamed as ND2Reader and act as 
     the sole reader for the format. Support for the ND2 format will be unaffected and continue via this 
     newly renamed reader

* Legacy QuickTime
   - The LegacyQT Reader, Writer and Tools have been marked as deprecated in preparation for removal 
     in the upcoming 7.0.0 major release of Bio-Formats. These classes depended on the external QuickTime 
     for Java library which is long obsolete. From Bio-Formats 7.0.0 onwards the existing NativeQTReader 
     will be renamed as QTReader and support for QuickTime will be limited to non legacy readers and writers.

* LuraWave Codec
   - The LuraWave Codec along with the LuraWaveService and associated components have been marked as 
     deprecated in preparation for removal in the upcoming 7.0.0 major release of Bio-Formats. This codec 
     depends on a third-party proprietary library with a license code. Opera Flex is the format that is 
     most likely to be impacted by this change.

* Woolz
   - The Woolz Reader, Writer and Service have been marked as deprecated in preparation for removal 
     in the upcoming 7.0.0 major release of Bio-Formats. The reader and writer are untested and rely on 
     an underlying library which maintenance status is unclear

File format fixes and improvements:

* CV7000/CV8000
   - updated CV7000 isThisType test to improve performance by skipping extended type checking
   - reader now handles the use case where wells are recorded, but all files were removed
   - fixed channel indexing in scenarios where more channels are defined than acquired

* ICS (Image Cytometry Standard)
   - fixed an Illegal group reference exception when constructing slice label 

* KLB (Keller Lab Block)
   - fixed a bug with the reading of image planes in Z stacks

* MicroManager
   - updated handling of truncated files to prevent possible infinite loop and throw an exception

Bio-Formats improvements:

* updated handling of exceptions in Bio-Formats plugins to ensure readers are closed
* updated list of external readers to include new external 
  `ZeissQuickStartCZIReader <https://github.com/BIOP/quick-start-czi-reader>`_ (thanks to Nicolas Chiaruttini)
* updated top-level Git mailmap to normalize commit author variants
* added a new bf-unconfigured tool to the Bio-Formats toolbox. The new tool lists classes which 
  are not configured for testing as part of format reader tests
* replaced use tt tag in java docs with code tag

Documentation improvements:

* fixed a number of broken links
* migrated OME-Model documentation to Read the Docs
* added deprecation warnings to format pages of the affected components

Component updates:

* `ome-common` was upgraded to 6.0.17

6.13.0 (2023 April)
-------------------
File format fixes and improvements:

* Aperio SVS
   - removed broken special case path when there is only one (pyramidal) image 
     (thanks to Alexandr Virodov)

* Bio-Rad Gel
   - fixed pixel data offsets for cropped images

* cellSens VSI
   - improved tile decoding to fail faster on invalid tiles

* CellWorX/MetaXpress
   - fixed a bug when retrieving channel metadata when the files for the entire first 
     field are missing

* CV7000
   - extra folders mixed in with the plate data will now be ignored
   - corrected channel indexing if a subset of channels was acquired

* Lambert Instruments FLIM
   - added support for Fli 2.0 (thanks to Shaquille Louisa - Lambert Instruments)

* MetaMorph
   - prevented an exception when attempting to read metadata keys that don't exist

* MetaMorph TIFF
   - fixed a NullPointerException when there are missing stage positions

* MRC
   - the IMOD flag is now used to determine int8 or uint8 pixel type

* NIFTI
   - improved the performance for gzip-compressed files by reducing the number 
     of backwards seeks

* Nikon ND2
   - fixed an exception when reading blocks greater than 2GB

* OME-TIFF
   - file paths are now normalized rather than resolving symlinks

* Perkin Elmer Operetta
   - fixed series validation for single plane images (thanks to Alex Herbert)

* Zeiss CZI
   - improved the tile stitching when a pyramid does not exist

Bio-Formats improvements:

* added a new writer option `preserve_creator` for OME-TIFF and OME-XML writers. 
  When set to true the original OME/Creator attribute will be preserved by the writer. 
  If set to false, the OME Creator attribute will be updated to include the current 
  Bio-Formats version. Attribute is set to false by default.
* enabled the configuration of the fill value for undefined pixel values through new 
  API additions to IFormatReader. Two new methods (along with default implementations) 
  have been added for `setFillColor(Byte color)` and `Byte getFillColor()`, the default 
  value if undefined is 0.
* added a new `-fill` option to the command line tools, allowing a byte value to be 
  configured for use with undefined pixels (0-255)
* enabled the configuration of JPEG quality in the JPEGCodec using the existing quality 
  setting on `CodecOptions` (thanks to Peter Haub)
* improved JPEG performance by using in-memory cache in JPEGCodec (thanks to Pete Bankhead)
* made minor API updates to `Memoizer` to allow a null reader to be specified in the 
  constructors, in which case a new `ImageReader` will be wrapped
* prevented file leaks in FileStitcher by closing readers when setting the class list
* fixed exceptions in FileStitcher when a no-op file pattern is encountered
* updated GitHub Actions release process


Documentation improvements:

* updated the format page for MRC to clarify list of developers and add links to latest specifications
* added new developer documentation pages for Bioconductor RBioFormats 
* corrected one of the examples in the OME-TIFF specification page (thanks to Tom Boissonnet)
* updated the list of writer options to add documentation for new `preserve_creator` options
* updated the list of command line tools options to add documentation for new `fill` option
* version history and bug reporting are now linked from the main documentation page
* fixed a number of broken links
* updated the Li-Flim format page to add supported versions

Component updates:

* `ome-common` was upgraded to 6.0.16
* `ome-model` was upgraded to 6.3.3
* `ome-codecs` was upgraded to 0.4.5
* `imagej1` was upgraded to 1.54c
* `json` was upgraded to 20230227
* `kryo` was upgraded to 5.4.0
* `snakeyaml` was upgraded to 2.0
* `joda-time` was upgraded to 2.12.2
* `guava` was upgraded to 31.1-jre
* `jackson-annotations` was upgraded to 12.14.2
* `jackson-databind` was upgraded to 12.14.2

6.12.0 (2023 February)
----------------------

File format fixes and improvements:

* Lambert Instruments FLIM
   - added support for MSB 12 to 16 bit conversion (thanks to Shaquille Louisa - Lambert Instruments)

* Olympus cellSens VSI
   - corrected tile handling to respect tile origin metadata
   - pixel data will now only be read from ets files with the prefix `frame_`
     (funded by a partnership between Glencoe Software and Evident Scientific)

* Perkin Elmer Operetta/Harmony
   - plates containing 32-bit TIFF files will now return blank planes

* Zeiss CZI
   - fixed pyramid dimension calculation

Bio-Formats improvements:

* implemented full Java 17 support for Bio-Formats
* logback dependencies are now optional as per the SLF4J best practices (thanks to Curtis Rueden)
   - downstream consumers must now declare the specific SLF4J binding they wish to use
* CI build matrix updated to use Java versions 8, 11 and 17
* ant tasks switched to use Maven Artifact Resolver
* fixed a bug when decompressing using the Base64Codec
* added a new ImageJ macro example to Bio-Formats examples
* FakeReader now ensures correct dimension order for RGB image
* added new unit tests for FakeReader
* fixed min/max calculation for RGB data
* artifacts from the GitHub Actions build are now uploaded and archived for 30 days
* release artifacts are now generated via GitHub Actions
* fixed a number of small issues in OME-Model (thanks to Roger Leigh)

Documentation improvements:

* migrated Bio-Formats documentation to `Read the Docs <https://bio-formats.readthedocs.io/en/stable/>`_
* fixed and updated a number of links in documentation
* updated OME-Model links to comply with Sphinx 5 deprecation warnings
* updated GitHub Actions set-output to comply with deprecation warnings
* updated OME-TIFF documentation to add links to new sample dataset 
  `BBBC017 <https://downloads.openmicroscopy.org/images/OME-TIFF/2016-06/BBBC017/>`_

Component updates:

* `ome-metakit` was upgraded to 5.3.5
* `ome-common` was upgraded to 6.0.14
* `ome-codecs` was upgraded to 0.4.4
* `ome-model` was upgraded to 6.3.2
* `jackson-annotations` was upgraded to 12.14.1
* `jackson-databind` was upgraded to 12.14.1
* `aircompressor` was upgraded to 0.21


6.11.1 (2022 December)
----------------------

File format fixes and improvements:

* 3i SlideBook 7
   - refactored code to remove a false positive threat report in Fortinet

* DICOM
   - fixed handling of some datasets with multiple optical paths

* Leica SCN
   - fixed colour correction for datasets from SCN 400 models

* Olympus cellSens VSI
   - corrected the handling of exposure times

* TIFF
   - handle REFERENCE_BLACK_WHITE tag as an array of floats or ints

* Vectra QPTIFF
   - biomarker data in channel name will now be preserved

* Zeiss CZI
   - added support for plates with multiple fields

Bio-Formats improvements:

* updated the output command for GitHub actions

Documentation improvements:

* fixed a number of broken links
* added a link to public sample files for `Olympus-FluoView <https://downloads.openmicroscopy.org/images/Olympus-FluoView/>`_

Component updates:

* `snakeyaml` was upgraded to 1.3.2

6.11.0 (2022 October)
---------------------

File format fixes and improvements:

* Amira Mesh
   - fixed handling of files with empty key values

* InCell 1000/2000
   - improved calculation of plane count

* Nikon NIS-Elements ND2
   - fixed handling of chunk map skipping logic

* Olympus FluoView FV1000
   - fixed an exception when parsing double values in the metadata

* OME-TIFF
   - improved initialization performance for files with a large number of planes
   - enabled individual file reading for datasets with one file per series

* SimplePCI & HCImage
   - fixed physical size calculation to make use of magnification value

* TIFF
   - implemented Zstandard decompression for Tiff formats (thanks to Willem Pomp)

Bio-Formats improvements:

* updated pattern file handling to support a single file wrapped in a pattern file
* Bio-Formats plugin now closes underlying readers after an exception
* contrast will be retained when using VirtualImagePlus in the Bio-Formats plugin (thanks to Tomas Farago)
* fixed overwrite checking in bfconvert tool when output path is a pattern

Documentation improvements:

* fixed a number of broken links
* updated test image documentation to add note on on setting fake file channel colors
* added new public sample files for `Olympus-FluoView <https://downloads.openmicroscopy.org/images/Olympus-FluoView/>`_
* updated OME-TIFF sample files for `BBBC017 <https://downloads.openmicroscopy.org/images/OME-TIFF/2016-06/BBBC017/>`_

Component updates:

* `ome-codecs` was upgraded to 0.4.1
* `snakeyaml` was upgraded to 1.3.1

6.10.1 (2022 August)
--------------------

File format fixes and improvements:

* Hamamatsu NDPI
   - fixed handling of non number tags for files greater than 4GB in size

* OME-TIFF
   - improved performance of initializing a single file OME-TIFF datasets with a larger number of series

* TIFF (Tagged Image File Format)
   - fixed a ClassCastException when the SubfileType tag has the wrong type

* Zeiss CZI
   - scene names will now be taken into account when generating image names

Documentation improvements:

* fixed a number of broken links

Component updates:

* `ome-common` was upgraded to 6.0.13
* `ome-poi` was upgraded to 5.3.7
* `slf4j` was upgraded to 1.7.30
* `metadata-extractor` was upgraded to 2.18.0

6.10.0 (2022 May)
-----------------

New file formats:

* Slidebook 7
   - added support for reading SlideBook Format 7 from SlideBook 2021
     This functionality was implemented and contributed by Intelligent Imaging Innovations

File format fixes and improvements:

* CellWorX / MetaXpress
   - channel metadata will now be preserved for all channels by reading from each file

* Cellomics
   - marked the private Pattern field as transient to fix memo file generation with JDK17

* DeltaVision
   - fixed detection of incorrect XY tile counts

* Hitachi S-4800
   - enhanced format recognition and identification of datasets
   - corrected the units for physical sizes to nanometers instead of micrometers

* Nikon NIS-Elements ND2
   - improved metadata parsing, especially for objective data, timestamps, and exposure times

* PerkinElmer Operetta
   - improved checks for invalid TIFFs and supplemental metadata files
   - updated image names to make well names more readable

* TIFF (Tagged Image File Format)
   - fixed incorrect SampleValue metadata values

* Vectra QPTIFF
   - reader has been updated to support schema version 4 
   - funded by a partnership between Glencoe Software and Akoya Biosciences.

Bio-Formats improvements:

* updated automated testing to ensure files are initialized before all tests

Documentation improvements:

* fixed broken link in MIPAV documentation
* updated logback component version in developer docs
* updated link to View5D software
* added a new format page for Slidebook 7

Component updates:

* `ome-metakit` was upgraded to 5.3.4
* `ome-common` was upgraded to 6.0.9
* `ome-model` was upgraded to 6.3.1
* `ome-poi` was upgraded to 5.3.6
* `ome-codecs` was upgraded to 0.3.2
* `logback-core` was upgraded to 1.2.9
* `logback-classic` was upgraded to 1.2.9
* `xercesImpl` was upgraded to 2.12.2
* `xml-apis` was upgraded to 1.4.01
* `snakeyaml` 1.29 was added as a dependency

6.9.1 (2022 April)
------------------

File format fixes and improvements:

* DeltaVision
   - allowed partial planes to be read from truncated files

* MetaMorph
   - fixed a NumberFormatException when parsing double values in metdata

* OME-TIFF
   - performance improvements to reduce the number of open file handles during initialization

* PerkinElmer Operetta
   - performance improvements to speed up the reading of datasets (thanks to Nicolas Chiaruttini)

* Zeiss CZI
   - switched to a white background for brightfield data to better match Zeiss Zen software

* Zeiss LSM
   - fixed a bug that resulted in an incorrect pixel type for some floating point data

Bio-Formats improvements:

* removed the maven deploy step from workflows in forked repositories
* upgraded cdm dependency from 4.6.13 to cdm-core 5.3.3
* configurable sleep time in FakeReader moved to the end of initialization

Documentation improvements:

* DICOM format page updated with improved links for sample datasets, software, and specification
* updated guidelines for submitting sample datasets

6.9.0 (2022 February)
---------------------

New file formats:

* Leica LOF
   - added support for reading Leica LOF files.
     This functionality was implemented and contributed by Leica Microsystems

* Leica XLEF
   - added support for reading Leica XLEF files.
     This functionality was implemented and contributed by Leica Microsystems

File format fixes and improvements:

* FEI TIFF
   - fixed parsing of physical pixel sizes for Phenom data

* Imspector OBF
   - improved handling of deflate errors when opening older OBF files (thanks to Nils Gladitz)

* JPEG
   - performance improvements to reduce memory required to read tiles from large JPEGs

* Leica LIF
   - improved parsing of channel metadata (thanks to Zach Marin)

* Nikon NIS-Elements ND2
   -improved parsing of metadata tables with invalid characters

* OME-TIFF
   - performance improvements of tile read speeds for some pyramid OME-TIFFs

* PerkinElmer Operetta
   - enabled support for handling sparse planes

Bio-Formats improvements:

* added new API methods to FormatTools for creating well names
* added a swap option to bfconvert to override input dimension order (thanks to Roberto Calabrese)

Documentation improvements:

* new public sample files for `Leica XLEF <https://downloads.openmicroscopy.org/images/Leica-XLEF/>`_ (thanks to Leica Microsystems)
* added documentation for using the swap option with the command line tools
* updated the process for contributing sample files via `Zenodo <https://zenodo.org/>`_
* updated the link to NDP.view2 software on the Hamamatsu ndpi format page


6.8.1 (2022 January)
--------------------

File format fixes and improvements:

* Aperio SVS / Aperio AFI
   - improved handling of macro and label images when no image description is present

* cellSens VSI
   - added support for physicalSizeZ metadata

* Gatan Digital Micrograph DM4
   - fixed a FormatException when encountering null values in the metadata

Bio-Formats improvements:

* fixed a bug in TiffSaver which could result in an invalid TIFF when saving a file with tiling and compression (thanks to Pete Bankhead)
* made performance improvements to TIFF reading and writing (thanks to Pete Bankhead)

Security improvements:

* Updated use of the git:// protocol in POM as it has now been deprecated. See the `GitHub blog post <https://github.blog/2021-09-01-improving-git-protocol-security-github/>`_ for further details
* Removed the loci_tools from Bio-Formats builds due to log4j vulnerability, users should instead use bioformats_package.
  See the :secvuln:`OME security advisory <2021-SV4/>` for further details

6.8.0 (2021 December)
---------------------

New file formats:

* DICOM
   - added support for reading and writing DICOM whole slide images (DICOM WSI format).
     This functionality was implemented through collaboration with 
     `NCI Imaging Data Commons <https://datacommons.cancer.gov/repository/imaging-data-commons/>`_, 
     and has been funded in whole or in part with Federal funds from the National Cancer Institute,
     National Institutes of Health, under Task Order No. HHSN26110071 under Contract No. HHSN2612015000031

* Olympus omp2info 
   - Added a new reader for the Olympus tile format 
     provided through a partnership with Glencoe Software and OLYMPUS EUROPA SE & Co. KG

File format fixes and improvements:

* Amira Mesh
   - added support for Amira 3.0 keys

* Aperio SVS / Aperio AFI
   - improved handling of macro and label images

* AVI (Audio Video Interleave)
   - set fps from Pixels Time Increment when writing AVI files

* Nikon NIS-Elements ND2
   - updated parsing of newer ND2 files to resolve issues with incorrect 
     dimensions(thanks to Ilya Parmon)

* Olympus OIR
   - fixed a Null Pointer Exception for Laser Data ID

* OME-TIFF
   - fixed handling of partial datasets
   - added a new reader option ometiff.fail_on_missing_tiff to configure behaviour of partial dataset

* PerkinElmer Operetta
   - added support for Phenix v6 data

* TIFF
   - fixed non-sequential offset correction for TIFF files between 2 and 4 GB

* Zeiss CZI
   - added support for zstd compression. This feature will require FIJI users to additionally
     download the dependency io.airlift.aircompressor 0.18. (funded by a partnership between 
     Glencoe Software and ZEISS)

Bio-Formats improvements:

* updated the ordering of reader.txt
* `bfconvert` tool updated to use multiple of tile size granularity when writing (thanks to Jeremy Muhlich)
* added a new no-sequential option to enable writing in non sequential order

Component updates:

* `jhdf5` was upgraded to 19.04.0
* `commons-lang` 2.6 was added as a dependency
* `aircompressor` 0.18 was added as a dependency

Documentation improvements:

* updated page for using Bio-Formats in Python to add links for 
  AICSImageIO and PyImageJ (thanks to Curtis Rueden)

6.7.0 (2021 August)
-------------------

File format fixes and improvements:

* cellSens VSI
   - corrected offset checking to prevent seeking beyond EOF

* Deltavision
   - fixed a bug which resulted in an IndexOutOfBoundsException

* Hamamatsu ndpis
   - added support for channel names from NDP Shading Data

* Nikon NIS-Elements ND2
   - improved parsing of timestamp values (thanks to Ilya Parmon)
   - improved parsing of channel names and colors

* Olympus FluoView FV1000
   - fixed a bug with the handling of filter indexes

* OME-TIFF
   - resolution annotations now removed when resolutions are flattened
   - fixed handling of filesets with BinaryOnly across multiple folders

* PerkinElmer Operetta
   - channel colors now populated using emission wavelength

* TIFF
   - added support for Deflate compressed tiles/strips with lsb2msb order
   - prioritised units from TIFF tag over those from ImageJ comment

* Zeiss CZI
   - plates will now be correctly detected
   - added a new reader option ``zeissczi.relative_positions`` which when set to true 
     will change the PositionX and PositionY values stored in OME-XML to the pixel 
     position instead of the absolute physical stage position
   - added a new reader option ``zeissczi.trim_dimensions`` which when set to true will 
     use the pixel block metadata to trim XY dimensions to match those reported in ZEN

Bio-Formats improvements:
 
* the pattern reader now supports populating channel names from pattern tokens
* the channel filler will correctly reset bits per pixel if a lookup table is applied
* existing reader options are now registered in getAvailableOptions command
* improved performance of OME-XML validation (thanks to Nils Gladitz)
* added unit tests for the upgrade of custom attributes in OME-XML transforms

Documentation improvements:

* updated link to a 2005 publication about the OME data model
* bumped low level components `logback-core` and `logback-classic` to 1.2.0
* updated the licensing for BDV, KLB and CellH5 readers to BSD
* added documentation for additional reader options
* fixed a number of broken links

The below have been relicensed under the more permissive BSD-2 clause:

* Big Data Viewer reader
* Keller Lab Block reader
* CellH5 reader
* JHDF service
* Bio-Formats GNU Octave package
* Bio-Formats MATLAB functions

Component updates:

* `ome-model` was upgraded to 6.2.3
* `ome-common` was upgraded to 6.0.7
* `ome-poi` was upgraded to 5.3.4
* `ome-codecs` was upgraded to 0.3.1
* `ome-metakit` was upgraded to 5.3.3
* `logback` was upgraded to 1.2.0


6.6.1 (2021 March)
------------------

File format fixes and improvements:

* CV7000
   - fixed the channel-wise ordering of planes. The implementation changes to channel mapping 
     will require existing memo files to be regenerated for CV7000 datasets

* Hamamatsu NDPIS
   - transmittance values will now be used to pick valid channels if no wavelength present

* Leica SCN
   - updated position units from reference frame to nm
   - original metadata now populated correctly for all series 

* MetaMorph Stack
   - support added for parsing `NDInfoFile Version` to determined correct file suffix
   - improved detection of companion binary files

* MetaXpress
   - improved detection of thumbnail paths

* Nikon NIS-Elements ND2
   - made performance improvements to reduce memory usage when reading large datasets

* Olympus OIR
   - fixed a bug which resulted in blank planes when XML blocks end with CRLF

Documentation improvements:

* updated `bfconvert` documentation for using pattern string on Windows 
  (thanks to Nathanael Reveal)
* added a Fiji usage note to the Tecan Spark Cyto Workspace format page
* added references to the public Imaris IMS format specification page

Bio-Formats improvements:

* added support for `ChannelName` in Fake series tables


6.6.0 (2020 December)
---------------------

New file formats:

* Tecan Spark Cyto Workspace
   - Added a new reader for Tecan Spark Cyto workspace files, provided through a collaboration 
     between Tecan Trading and Glencoe Software

File format fixes and improvements:

* Applied Precision CellWorX / MetaXpress
   - support for CellWorX and MetaXpress has now been split into separate readers

* BD Pathway
   - plate row and column dimensions now being populated

* Bitmap
   - fixed offset calculation for files larger than 2 GB

* Cellomics
   - channel data now being parsed from companion .mdb file
   - corrected Plate/Well/Image mappings for sparse plates
   - plate size now calculated using the maximum row/column index
   - plate row and column dimensions now being populated

* Gatan Digital Micrograph DM4
   - fixed support for montages with single Z dimensions

* MetaMorph Stack
   - corrected laser indexes for multi series datasets

* MIAS (Maia Scientific)
   - plate row and column dimensions now being populated

* Nikon NIS-Elements ND2
   - fixed a null pointer exception when parsing metadata key value pairs

* Olympus ScanR
   - added functionality to handle missing wells through a new option ``scanr.skip_missing_wells``.
     By default the option is set to true and missing wells are skipped

* Olympus SIS TIFF
   - corrected parsing of pixel size values (thanks to Stephan Wagner-Conrad)
   - removed trailing null byte from imageName and channelName
   - improved formatting of the image reader

* PerkinElmer Opera Flex
   - plate row and column dimensions now being populated

* PerkinElmer Operetta
   - updated metadata files logic to skip plate folders

* PNG (Portable Network Graphics)
   - fixed an issue which resulted in a hanging call to `openBytes`

* Zeiss CZI
   - scene number is now correctly padded and indexes begin at 1

* Zeiss LSM
   - improved handling of cached plane variables

Documentation improvements:

* added new `OME-TIFF plate companion sample files <https://downloads.openmicroscopy.org/images/OME-TIFF/2016-06/plate-companion/>`_
* references to image index in the API documentation have been updated to plane index
* updated various links to follow the LOCI site migration
* fixed broken Javadoc links
* removed outdated references to mailing lists

Component updates:

* `ome-model` was upgraded to 6.2.2
* `ome-common` was upgraded to 6.0.6
* Memoizer version has been incremented meaning previous memo files are invalidated and 
  will be regenerated
* `kryo` dependency updated to 4.0.2
* Added new `sqlite-jdbc` version 3.28.0 dependency for the Tecan Spark Cyto Workspace format

Bio-Formats improvements:

* removed automatic file stitching from format reader tests
* improved stringency of ChannelName and ImageName testing
* improved reader detection for image conversion testing
* reviewed all instances of whitelist/blacklist
* introduced support for GitHub Actions
* improved handling of DynamicMetadataOptions on Windows
* introduced the ability to set metadata options using a `.bfoptions` file
* test-suite updated to handle new `.bfoptions` file


6.5.1 (2020 July)
-----------------

File format fixes and improvements:

* Aperio SVS / Aperio AFI
   - fixed a Null Pointer Exception when exposure time is not defined

* Big Data Viewer
   - corrected series indexes for non flattened multi resolution images

* Cellomics
   - physical sizes are now set for all series rather than just the first

* Imspector OBF
   - file format version and stack version are now recorded as part of global metadata

* MetaMorph
   - improved wavelength parsing using Metamorph XML or original metadata

* Mikroscan TIFF
   - stricter format recognition now used to prevent erroneous use of the reader

* Ventana BIF
   - added support for LEFT overlap direction (thanks to Joan Gibert)

* Zeiss CZI
   - fixed a bug to ensure Channel Illumination Type is not overridden by display settings

Documentation improvements:

* added link from OME-TIFF page to commercial partners page
* updated links for Biplane to now use Oxford Instruments
* fixed a number of broken hyperlinks in documentation

Component updates:

* `jxrlib` was upgraded to 0.2.4

Bio-Formats improvements:

* fixed a bug in `bfconvert` for multi-series files with varying image sizes
* removed the logging OMERO IDs passed to FormatReader and ImageReader


6.5.0 (2020 April)
------------------

File format fixes and improvements:

* Big Data Viewer
   - improved performance of tiled reading

* DeltaVision
   - implemented additional sanity check to header to ensure correct panel count

* DICOM
   - improved performance of initialization of multi-file datasets. Files spread across multiple 
     directories are now handled by a DICOMDIR file that groups the dataset

* Imspector OBF
   - added support for OBF Version 6 stacks (thanks to Nils Gladitz)
   - added support for OBF Version 4 stack flush points (thanks to Nils Gladitz)

* MetaMorph
   - ensured dimension metadata read from tags and/or .nd file rather than allowing the underlying 
     TIFF reader to treat each IFD as a series

* MetaXpress 
   - added support for single site HCS variant

* Zeiss CZI
   - fixed the position count when only one position is present and the starting index is greater than 0

* Various Readers
   - reviewed and updated readers to prevent potential cases of integer overflow

OME-Model updates:

* version of ``OME-Model`` has been updated to 6.1.0
* added support for Python 3.8 and make code-generation Python 3 only (thanks to Roger Leigh)
* added getters and setters for OME@Creator attribute for ome.xml metadata interfaces and implementations 
  (thanks to Nils Gladitz)
* removed unmaintained C++ OME-XML implementation (thanks to Roger Leigh)
* updated code-generation for building on Python 3.6, 3.7 (thanks to Roger Leigh)
* uncapped the Sphinx version for OME-Model documentation

Documentation improvements:

* fixed a number of broken links within the documentation
* added a new format page for MetaXpress
* added a reference to public OBF sample images in the format page

6.4.0 (2020 March)
------------------

File format fixes and improvements:

* Applied Precision CellWorX
   - added support for multiple Z sections

* DeltaVision
   - added and updated objective metadata based on values from softWoRx 7.2.0 (thanks to David Pinto)

* Hamamatsu NDPI
   - added support for JPEG-XR compression
   - added full support for files larger than 4 GB
   - improved support for a number of additional metadata tags
   - the Hamamatsu NDPI reader improvements are provided via work from Glencoe Software Inc.

* InCell
   - inverted Y coordinate in plane/field positions to correct stitching of tiles

* PerkinElmer Vectra QPTIFF
   - plane position values will now be populated on OME-XML

* TIFF
   - values for XPosition and YPosition in original metadata will now be more accurately stored as doubles
   - implemented a fix to prevent integer overflow when reading from a large tile greater than 2 GB

* Ventana BIF
   - improved handling of physical sizes for pre-stitched TIFFs

* Zeiss CZI
   - added a fix for uncompressed pixels incorrectly flagged as JPEG-XR
   - fixed a bug so that line-scans are now read correctly (thanks to Stephan Wagner-Conrad)
   - improved parsing of detector metadata

Bio-Formats tools improvements:

* added a new ``nobigtiff`` option to ``bfconvert`` to disable automatic switching to BigTiff based upon the 
  number of pixel bytes (TIFF files larger than 4GB). This may be useful when converting using a compression 
  codec so that the output file size is less than 4GB
* fixed a bug in ``xmlvalid`` tool to properly handle lowercasing of file names
* added new bfGetPlaneAtZCT function to MATLAB toolbox to retrieve a particular plane at a ZCT coordinate 
  (thanks to Mark Kittisopikul)
* added a new bfTestInRange helper function to MATLAB toolbox with improved performance and error handling 
  (thanks to Mark Kittisopikul)
* fixed a bug when using ``bfconvert`` on multi-series files with only a single timepoint, channel or Z slice selected

Bio-Formats API updates:

* version of ``jxrlib`` has been updated to 0.2.2
* version of ``ome-codecs`` has been updated to 0.3.0 which includes performance upgrades for 
  LZW compression (thanks to Alexander Popiel)
* moved JPEG-XR codec and service from ``formats-gpl`` to ``formats-bsd`` component
* TiffParser and TiffSaver have now been updated to implement Closeable
* added a documentation note to use one IFD instance per plane with ``saveBytes`` in ``TiffWriter``
* FormatWriter will now create output file's parent directory if needed
* FakeReader now allows for DeltaT to be set in INI file
* FakeReader now handles INI files in plates created by ``mkfake``
* fixed a number of deprecation warnings in various readers

6.3.1 (2019 December)
---------------------

File format fixes and improvements:

* ICS (Image Cytometry Standard)
   - prevented a potential error when writing ICS files with physical units which could not be converted

* Imspector OBF
   - fixed a bug with incorrect dimensions being parsed for some Imspector OBF files

* Leica LAS AF LIF (Leica Image File Format)
   - fixed a NullPointerException in some variants of the LIF file format

* TIFF
   - improved the performance of tiled writing

* Zeiss CZI
   - fixed issues with tile stitching and position size

Bio-Formats tools improvements:

* fixed a potential NullPointerException in SpringUtilities for Bio-Formats plugins (thanks to July Chen)
* updated URL for fetching ImageJ upgrades in ``ijview``
* fixed the XY coordinates for cropped images in ``bfconvert``
* fixed a bug when using a cropped multi-series file in ``bfconvert`` (thanks to Matthieu Moisse)
* fixed issues in ``bfconvert`` when writing separate tiles with additional options
* added documentation of tile output patterns to utility help in ``bfconvert``


6.3.0 (2019 October)
--------------------

File format fixes and improvements:

* Big Data Viewer
   - added support for parsing of physical sizes

* DeltaVision
   - added a new RCPNL reader which is a variant and split out of the DeltaVision format

* Hamamatsu NDPI
   - fixed population of the nominal magnification from the SourceLens TIFF tag

* ICS (Image Cytometry Standard)
   - fixed a bug when using tiles to read files from SVI-Huygens

* Imspector OBF
   - fixed an `IndexOutOfBoundsException` exception when using `DummyMetadata` (thanks to Nils Gladitz)

* JPEG 2000
   - added support for sub-resolutions

* Leica LIF
   - updated to parse attachments to determine if XY positions should be flipped or swapped

* MetaMorph
   - improved file name construction and plate detection logic

* Nikon ND2
   - updated to use floating point for 32 bit values

* OME-TIFF
   - reduced memory usage when reading files and memo file size for cached files

* PerkinElmer Operetta
   - improved handling of empty fields to prevent series from having X or Y set to 0

API updates:

* added `overwriteIFDValue` signature that takes an IFD offset to `TiffSaver`
* added a new `getRequiredDirectories` method to `FormatTools`
* new `FakeReader` keys added for `sleepOpenBytes` and `sleepInitFile`

Build updates:

* updated deployment mechanism for SNAPSHOT and Release to use Travis CI
* increased the strictness of AcquisitionDate checks in `FormatReaderTest`
* improved test coverage of companion file datasets

Component updates:

* `ome-common` was upgraded to 6.0.4
* updated `DateTools` to attempt to parse invalid dates with `Locale.US` 
* `DateTools` documentation updated to clarify expected units for timestamp passed to convertDate

Documentation improvements:

* added documentation for sleep options when generating test images
* fixed broken external links in documentation
* corrected suffixes used for JPEG 2000


6.2.1 (2019 August)
-------------------

File format fixes and improvements:

* Applied Precision CellWorX
   - corrected plane positions for series index > 0 rather than reusing positions from the first series

* DeltaVision
   - added objective info for new Applied Precision 100X/1.4 lensID
   - updated so that date from dv file will override log file date to avoid locale-dependent dates

* Leica LAS AF LIF (Leica Image File Format)
   - fixed units and indexing for tile-based plane positions

* TIFF
   - fixed a potential exception in MinimalTiffReader when the TIFF is stored using very 
     large tile/strip dimensions

* Zeiss CZI
   - fixed a potential index out of bounds exception when populating positions

Bug fixes and improvements:

* `bfconvert` has been updated so that when the dimensions of a sub-resolution are smaller than the 
  requested tile size then they default to the size of the sub-resolution

* fixed a bug in the execution of `bfsave` in the GNU Octave environment

Codec updates:

* `ome-codecs` was upgraded to 0.2.5

* JPEG codec updated to reduce decompression time for 8-bit RGB images

* Huffman codec updated to allow the decoding tree to go all the way down to the 16-bit depth required 
  by the standard (thanks to Aaron Avery)

* Lossless JPEG codec updated to provide better compliance with the LJPEG standard (thanks to Aaron Avery)

Documentation improvements:

* added instructions for building Bio-Formats with IntelliJ IDEA
* corrected command-line tools documentation for the novalid and noncore options
* updated broken links to Barre's Medical Imaging Samples
* updated the imagej.net link for Zeiss LSM toolbox plugin
* added links to public sample files for the following formats: 
   - `Big Data Viewer <https://downloads.openmicroscopy.org/images/BDV/>`_
   - `CellWorX <https://downloads.openmicroscopy.org/images/CellWorX/>`_
   - `CellH5 <https://downloads.openmicroscopy.org/images/CellH5/>`_
   - `PerkinElmer Opera Flex <https://downloads.openmicroscopy.org/images/Flex/>`_
   - `Gatan DM3 <https://downloads.openmicroscopy.org/images/Gatan/>`_
   - `Image Cytometry Standard <https://downloads.openmicroscopy.org/images/ICS/>`_
   - `Keller Lab Block <https://downloads.openmicroscopy.org/images/KLB/>`_
   - `PerkinElmer Columbus <https://downloads.openmicroscopy.org/images/PerkinElmer-Columbus/>`_
   - `Ventana BIF <https://downloads.openmicroscopy.org/images/Ventana/>`_
   - `Zeiss-CZI <https://downloads.openmicroscopy.org/images/Zeiss-CZI/>`_


6.2.0 (2019 July)
-----------------

New file formats:

* Mikroscan TIFF
   - a new reader for Mikroscan TIFF files has been contributed with thanks to 
     Jim Crowe, Mikroscan Technologies, Inc.

* Ventana BIF
   - added a new reader for Ventana BIF files which has been commissioned via Glencoe Software

File format fixes and improvements:

* Cellomics
   - fixed indexing for plates with a single well or missing fields

* DeltaVision
   - added support for the reading of the new panel count field 
     (provided through a collaboration between GE Healthcare and Glencoe Software Inc.)

* PerkinElmer Operetta
   - images with smaller XY dimensions than all other TIFF files in dataset will now be padded

* TIFF
   - updated functionality for overwriting IFD values to ensure that previous value 
     is completely overwritten and no orphaned tags are left

* Zeiss CZI
   - expanded support for auto-stitching of tiles

Bug fixes and improvements:

* added ``-cache``, ``-cache-dir`` and ``-no-sas`` options to ``bfconvert`` tool

* deprecated broken TRUNK and DAILY builds from upgrade checker

* disabled Oracle JDK from Travis CI checks

Documentation improvements:

* fixed broken link for discontinued Dcraw software

* updated links for Zeiss formats

6.1.1 (2019 June)
-----------------

File format fixes and improvements:

* DeltaVision
   - added new lens definitions associated with `rcpnl` files

* Gatan Digital Micrograph (DM3/DM4)
   - now parsing the `Montage` tag to determine if tiles are present

* Leica LAS AF LIF (Leica Image File Format)
   - added fix to correctly read scale from polygon regions of interest (thanks to Sean Warren)

* PerkinElmer Columbus 
   - improved handling of truncated TIFF files to return blank planes

* PerkinElmer Opera Flex
   - plate barcodes are now used to improve grouping and handling of truncated files

* TIFF (Tagged Image File Format)
   - improved parsing times for images stored as uncompressed contiguous strips

* Zeiss CZI
   - improved plane position metadata for many CZI datasets

Automated test changes:

* format reader tests have been updated to handle PerkinElmer Columbus 
  datasets with flex files

Documentation improvements:

* added help for missing options in ``bfconvert`` command line tool

6.1.0 (2019 May)
----------------

New file formats:

* BDV
   - added a new reader for Big Data Viewer files

File format fixes and improvements:

* Applied Precision CellWorX
   - improved handling of thumbnail files

* DeltaVision
   - updated handling of `rcpnl` files to treat each file as a single timepoint

* FakeReader
   - removed `header` key from original metadata

* Hamamatsu VMS
   - removed `header` key from original metadata

* Hitachi S-4800
   - removed `header` key from original metadata

* ICS (Image Cytometry Standard)
   - fixed an issue reading .ics/.ids files written by SVI Huygens (thanks to Jan Eglinger)

* Imaris IMS
   - fixed issues with newer files which had been failing due to older `netcdf` version

* JPEG
   - improved the reading of EXIF data

* Lambert Instruments FLIM
   - added support for packed UINT12 datatype (thanks to Johan Herz)

* LEO
   - fixed a bug with the parsing of physical sizes
   - improved support for additional global metadata fields

* Olympus OIR
   - fixed a bug which would show empty pixels when more than 1000 timepoints

Automated test changes:

* added additional tests for HCS/SPW datasets to ensure Plate, PlateAcquisition, Well, 
  WellSample, and WellSample position values are configured where present
* added a new `file-leak-detector` test to flag potential memory leaks

Bio-Formats API changes:

* ``ImageConverter`` as used in ``bfconvert`` command line tool is now public
* made ``ImageReader`` more defensive against exceptions thrown when determining reader type
* fixed an issue when performing a non-sequential write for multi-resolution TIFF files

Component changes:

* `ome-common` was upgraded to 6.0.3
* `perf4j` was upgraded to 0.9.16
* removed `Guava` dependency which will be pulled transitively from the 
  upstream `ome-common` dependency
* `jhdf5` was upgraded to 14.12.6
* `metadata-extractor` was upgraded to 2.11.0
* `xercesImpl` version 2.8.1 was added as it is no longer a dependency of `metadata-extractor`
* `netcdf` was upgraded to 4.6.13

6.0.1 (2019 March)
------------------

File format fixes and improvements:

* cellSens VSI
   - improved tag parsing resulting in fixes for missing or incorrect metadata

* Hamamatsu ndpi
   - improved handling of variants where a constituent NDPI has no wavelength

* LaVision Imspector
   - fixed a potential NullPointerException when 'xyz-Table Z Resolution' is false

* NRRD (Nearly Raw Raster Data)
   - added support for raw GZIP-compressed data files

* Olympus OIR
   - fix to ensure file path is normalized which fixes detection on Windows

* TIFF
   - improved handling of direct tile copying to prevent invalid images
   - improved handling of tiles in scenarios of an invalid offset or byte count of 0

Documentation improvements:
   - added documentation for -noflat option to the showinf and bfconvert users pages
   - updated recommended minimal MATLAB version to R2017b
   - documented support for MATLAB versions prior to R2017b
   - links to MicroCT public datasets now point to the public archive rather than directly 
     to the zip file

6.0.0 (2019 February)
---------------------

Bio-Formats API changes:

* Java 8 is now the minimum supported version
* Sub-resolution reading:

   - added ``MetadataList`` and ``CoreMetadataList`` classes
   - added a new ``SubResolutionFormatReader`` abstract class for handling
     pyramidal format readers
   - updated all pyramid format readers to use ``SubResolutionFormatReader``
   - deprecated ``getCoreMetadataList``, ``seriesToCoreIndex``, 
     ``coreIndexToSeries``, ``getCoreIndex`` and ``setCoreIndex`` in
     ``IFormatWriter``
* Added a new ``IPyramidHandler`` interface with the resolution getter methods
* Sub-resolution writing changes:

   - ``IFormatWriter`` now extends ``IPyramidHandler`` (breaking)
   - added ``setResolutions`` and ``getResolutions`` methods to
     ``IFormatWriter`` (breaking)
   - added examples of using the sub-resolution writing API
* Tiled writing API changes:

   - updated ``IFormatWriter`` to use ``setTileSizeX(0)`` and
     ``setTileSizeY(0)`` as a way to disable tiling (breaking)
   - updated ``FormatWriter`` set 0 as the default values of ``getTileSizeX()``
     and ``getTileSizeY`` (breaking)
* ``IFormatWriter.getCompressionTypes`` now returns the types for the selected
  writer only
* Metadata handling:

   - added getter methods to ``MetadataTools`` for retrieving OME
     enumerations by value
   - deprecated OME enumeration getter methods in ``FormatReader``
* Refactor ``FilePatternReader`` logic in a new ``WrappedReader`` abstract class

New file formats:

* KLB

   - added a new reader for Keller Lab Block (KLB) files

* CV7000

   - added a new reader for Yokogawa CV7000 datasets

* GE MicroCT

   - added a new reader for GE MicroCT datasets

File format fixes and improvements:

* Aperio SVS/AFI

   - removed pyramidal resolutions of mismatching pixel types
   - fixed exposure times, improved image naming of AFI datasets
   - displayed original metadata keys for each channel of AFI datasets
   - added support for multiple Z sections

* DICOM

   - improved file grouping and file-to-series mapping for multi-file datasets

* Fake

   - added support for multi-resolution test images
   - now populating WellSample positions when present using Plane data

* Gatan Digital Micrograph

   - adjusted endianness and record byte count for long values
   - allowed ROIs to be stored in DocumentObjectList groups
   - no longer creating an empty ROI when an unsupported shape type is encountered

* Image Pro

   - added support for Image Pro Plus .ips set

* GE InCell

   - added support for parsing minimum and maximum pixel values

* Lambert Instruments FLIM

   - fixed an integer overflow error with large files (thanks to Rolf Harkes)

* Leica LIF

   - unified metadata parsing to use ``DataTools.parseDouble``

* Leica SCN

   - improved support for Versa datasets

* Micro-Manager

   - improved handling of very large :file:`*_metadata.txt` files
   - prevented ``NumberFormatException`` for invalid double values
   - add support for parsing `ChannelColor` from :file:`*_metadata.txt` files

* Metamorph

   - added support for multi-dimensional .scan dataset created from
     Scan Slide (thanks to Jeremy Muhlich)

* MRC (Medical Research Council)

   - fixed endian detection for old-style headers

* Nikon ND2

   - prevented integer overflow when reading chunkmaps from files larger than
     2GB
   - fixed handling of duplicate and incomplete exposure time lists
   - fixed chunk map handling when CustomData blocks are between ImageDataSeqs

* OME-TIFF

   - added support for reading OME-TIFF with pyramidal resolutions stored as
     SubIFDs
   - added support for writing OME-TIFF with pyramidal resolutions
   - added support for companion OME-TIFF filesets where TIFF does not link
     back to the metadata file
   - improved handling of missing planes in TiffData

* PerkinElmer Operetta

   - improved support to handle datasets generated by the Harmony software

* TIFF

   - split IFDs into separate series if the dimensions or pixel type mismatch
   - restricted use case for legacy TIFF JAI reader
   - fixed a bug with FillOrder which resulted in 0 pixel values

* Zeiss CZI

   - reduced duplicate original metadata when reading a pyramid file

* Zeiss TIFF

   - added support for AVI files acquired with Keyence software

* Zeiss ZVI

   - reuse stream for sequential calls to ``openBytes`` on the same plane

* updated all pyramidal format readers to consume ``SubResolutionReader``
* updated all readers to consume ``MetadataTools`` getter to retrieve enumerations
* reviewed all readers and plugins to close open instances of
  ``RandomAccessInputStream``
* fixed some deprecation warnings in a number of readers
* for RGB images using ``ChannelSeparator`` all channel metadata is now copied instead of just names

ImageJ plugin improvements:

* updated the updater message in the Fiji plugin (thanks to Jan Eglinger)
* disabled LUT writing for any plane that has a default grayscale lookup table
* added macro option to always skip LUT writing

MATLAB toolbox improvements:

* improved performance of bfGetPlane by removing an unnecessary data copy (thanks to Cris Luengo)

Command-line tools improvements:

* ``bfconvert`` utility

   - added ``-no-flat`` option to the command-line tools to convert files with 
     sub-resolutions
   - added ``-pyramid-scale`` and ``-pyramid-resolutions`` options to
     generate sub-resolutions during conversion
   - removed ``Plate`` elements when ``-series`` is passed as an option
   - extended usage to describe available formats, extensions and compressions

* ``xmlvalid`` utility

   - added new ``validate`` methods to ``loci.formats.tools.XMLValidate`` returning
     the validation status
   - added a return code to ``xmlvalid``


Component changes:

* `ome-common` was upgraded to 6.0.0
* `ome-codecs` was upgraded to 0.2.3
* `ome-model` was upgraded to 6.0.0

Automated test changes:

* added ``testng.allow-missing`` property allowing to skip unconfigured filesets
* added ``testUnflattenedSaneOMEXML`` to compare series count to OME-XML images
  count when resolution flattening is disabled
* added ``test-equivalent`` target to compare pixel data between two files
* added support for storing resolution index and resolution count in the
  configuration files used for automated testing
* tests now fail when a configured file throws UnknownFormatException

Documentation improvements:

* fixed the :command:`xmlvalid` documentation page (thanks to Kouichi C. Nakamura)
* improved the memory section of the MATLAB documentation page (thanks to Kouichi C. Nakamura)
* extended ``IFormatReader`` Javadocs to reflect the reader guide
* added reference to current Adobe TIFF specification
* switched to image.sc as the reference location for public feedback

5.9.2 (2018 September 03)
-------------------------

File format fixes and improvements:

* AVI
   - added support for AVI files acquired with Keyence software
* Gatan
   - fixed a bug when reading a file with an empty tag of type 23
* Deltavision
   - extended the objective metadata support (thanks to David Pinto)
* MRC
   - fixed the reading of MRC files generated with FEI EPU software
* Zeiss LSM
   - improved the channel color detection for SIM data

Component changes:

All OME dependencies were upgraded mostly with build changes and documentation
improvements:

* ome-common was upgraded from 5.3.2 to 5.3.6
* ome-poi was upgraded from 5.3.1 to 5.3.3
* ome-mdbtools was upgraded from 5.3.1 to 5.3.3
* ome-jai was upgraded from 0.1.0 to 0.1.3
* ome-codecs was upgraded from 0.2.0 to 0.2.2
* ome-stubs was upgraded from 5.3.0 to 5.3.2
* ome-model was upgraded from 5.5.4 to 5.6.3

Documentation improvements:

* added links to public sample files for Imaris IMS, DICOM, Leica-SCN, LEO, MRC, PNG, TIFF and Trestle formats

5.9.1 (2018 August 14)
----------------------

File format fixes and improvements:

* Olympus OIR
   - fixed a bug to prevent incorrect files from being read when multiple datasets are in 
     the same location
* LEO
   - updated parsing of metadata values for image pixel size, working distance, filament, EHT 
     and date (thanks to David Mankus)
* DeltaVision
   - reader can now detect up to 12 channels
* Micro-Manager
   - now logs a warning when an image is acquired with an unsupported version

Documentation improvements:

* added QuPath to the list of visualization and analysis applications
* updated the link to the i3dcore library
* updated the link to Slidebook
* improved MATLAB documentation with information on Java heap memory preferences (thanks to Kouichi C. Nakamura)
* corrected a number of permanently redirected URLs in the component and format pages

5.9.0 (2018 July 3)
-------------------

File format fixes and improvements:

* MetaMorph
   - fixed a ``NullPointerException`` when a stage label is not present
   - ensured that reported domain is now consistent with the existence of a Plate in OME-XML
   - fixed Metamorph RGB series channel count (thanks to Jeremy Muhlich)
* Leica LIF
   - improved handling of dimension order for non-RGB channels
* Imspector OBF
   - added support for FLIM datasets
* Inveon
   - updated to attempt to locate renamed data files
* Volocity
   - expanded image names to include the stack parent names
* Olympus OIR
   - added a fix for slow tag reading and a potential infinite loop
* TIFF
   - added support in ``TiffWriter`` for the writing of DEFLATE (zlib) compression
   - deprecated ``getIFDs()`` in ``TiffParser`` and added ``getMainIFDs()`` and ``getSubIFDs()``
* Zeiss CZI
   - fixed an issue with big images when tiling is present but a pyramid is not
* Nikon NIS-Elements ND2
   - prevented integer overflow exception when reading a tile from a large image
* Amersham Biosciences Gel
   - prevented overflow issue when reading unsigned integer values
* Cellomics
   - fixed indexing when the field counts are variable
* Trestle
   - updated to ensure consistent ordering of used files

Bug fixes and improvements:

* enabled building and testing with Java 9 and 10
* added CI testing with Java 10 on AppVeyor and Travis
* removed Java 7 from Appveyor matrix
* updated a number of Maven plugins to current versions
* corrected warnings in Maven configuration in sub-components 
* added a warning to clarify the behavior when passing metadata with ``dimensionOrder`` in ``bfsave`` as 
  part of the Bio-Formats MATLAB toolbox (thanks to Jonathan Armond)
* improved robustness in the detection of patterns as part of the file stitching
* fixed a bug relating to dimension order in the Bio-Formats plugins Exporter
* fixed download URLs in Bio-Formats command-line tools
* updated use of ``static final`` to match Oracle's recommendations and convention
* disabled upgrade checker when running unit tests
* added support to data repo test suite for unconfigured tests

Documentation improvements:

* fixed unstable links flagged by automated link checking
* begun adding testing for breakages to memo files
* clarified ordering expectation in ``getUsedFiles`` Javadocs
* added documentation for dimensionOrder in bfsave with the :doc:`MATLAB toolbox </developers/matlab-dev>`
* fixed broken links in previous release notes
* expanded documentation for command-line tools to cover undocumented :doc:`options </users/comlinetools/display>` 
  and :doc:`environment variables </users/comlinetools/index>`
* added a new license/copyright section to the :doc:`About Bio-Formats </about/index>` page
* updated the public format page for the Vectra QPTIFF format 

5.8.2 (2018 April 23)
---------------------

File format fixes and improvements:

* JPEG
   - large images with no restart markers now revert to using ``DefaultJPEGReader`` for improved decoding
* Micro-Manager
   - when available ``PositionName`` will be parsed and used as the image name
* Hamamatsu ndpi
   - updated image names to be more meaningful when resolutions are not flattened
* InCell 2000/6000
   - fixed an ``IllegalArgumentException`` and improved well and field indexing
* AVI
   - fixed a bug with padding for RGB images
* NIfTI
   - the ``nDimensions`` field is now used to read additional dimensions when size is greater than 4
* PerkinElmer Opera Flex
   - fixed a bug which resulted in an incorrect field count
* Zeiss CZI
   - improved handling of files with no extension

Bug fixes and improvements:

* an error message is now logged by ``ImageReader`` when finding a reader for an empty file
* added a new protected helper method to ``Memoizer`` to check if a directory is writable
* improved the rounding of ``PlanePosition`` values for data repo configuration testing
* prevented a null pointer exception when retrieving plane exposure time using Bio-Formats ImageJ 
  macro extensions
* updated ``MinMaxCalculator`` to account for unflattened multi resolution images

Documentation improvements:

* decoupled the Bio-Formats documentation to the new 
  `ome/bio-formats-documentation GitHub repository <https://github.com/ome/bio-formats-documentation>`_
* updated :doc:`Adding format/reader documentation </developers/format-documentation>` for the new 
  decoupled workflow
* improved link checking in automated builds

5.8.1 (2018 March 22)
---------------------

File format fixes and improvements:

* TIFF
   - updated TiffWriter so that planes will no longer be split when using non-standard
     SamplesPerPixel e.g. images with 2 or 4 samples per pixel. This will ensure the ``TiffData``
     elements represent the structure specified by the user. If users wish to split planes the 
     ``ChannelSeparator`` and ``bfconvert`` provide the means to do this explicitly
   - updated TiffWriter to use the correct logic for index checking when writing tiled images
   - fixed a ``ClassCastException`` when the ``NEW_SUBFILE_TYPE`` tag has a non-standard type
     or count such that the value is not inlined
   - updated to also check the last IFD for an ImageJ comment in the scenario that the image has 
     been processed by other software
* NRRD (Nearly Raw Raster Data)
   - added support for ``space directions`` and ``space units`` fields added in version 4
* Evotec/PerkinElmer Opera Flex
   - updated to read rather than calculate image offsets when a single tile is used

Bug fixes and improvements:

* limited the number of exceptions in the Bio-Formats plugins exporter when an unsupported pixel 
  type is found
* fake test images now allow for per-plane ExposureTime{X,Y,Z} and Position{X,Y,Z} keys in the INI file
  (for further details see the documentation for :doc:`Generating test images </developers/generating-test-images>`)
* file patterns now have expanded support for multi-channel pyramids, allowing for the matching of 
  at least two channels rather than three, and the stitching of files containing a pyramid has also been fixed

Documentation improvements:

* improved testing of external links

5.8.0 (2018 February 21)
------------------------

New file formats:

* Ionpath MIBI
   - added a new reader to support the reading of Ionpath Multiplexed Ion Beam Imaging (MIBI)
     files (thanks to Rachel Finck)
* PerkinElmer Vectra QPTIFF
   - added support for PerkinElmer Vectra QPTIFF files (The QPTIFF Bio-Formats reader is provided 
     through a collaboration between PerkinElmer, Inc and Glencoe Software Inc.)

File format fixes and improvements:

* cellSens VSI
   - added support for lossless JPEG compression
* Imspector OBF
   - improved the parsing of OBF files with embedded OME-XML metadata (thanks to Bjoern Thiel)
* Leica LIF
   - companion metadata files are now attached if present
* Micro-Manager
   - fixed a bug related to the parsing of the metadata closing block
* NRRD (Nearly Raw Raster Data)
   - added support for GZIP pixel stream contained within a .nrrd file
* Olympus OIR
   - added support for multi-file datasets
* OME-TIFF
   - when files are ungrouped the dimensions are corrected by checking the indexes for each
     associated TiffData
* PerkinElmer Operetta
   - added support for additional metadata fields such as ``Instrument``, ``Wavelength``
     and ``Exposure time``
* TIFF
   - fixed a bug when printing IFD values of type ``OnDemandLongArray``
   - fixed a bug when writing tile sizes for multi-series images
* Zeiss CZI
   - when Z positions are not enumerated then values are calculated from a Z step
   - metadata for DisplaySetting will now be preserved in the original metadata table

Bug fixes and improvements:

* removed unused ScreenReader in preparation for migrating it to be an external reader
* fixed a bug with the generation of thumbnails in Bio-Formats plugins
* updated the Maven POM to unify component version property names
* tile size is now reported in the core metadata when using the showinf tool
* added ``setFilePatternIds`` to ``ImporterOptions`` for use with Bio-Formats plugins
* improved the precision of format identification for MRC, I2I, and Zeiss LSM

Documentation improvements:

* fixed and updated a number of external documentation links
* added links to `public NRRD samples <https://downloads.openmicroscopy.org/images/NRRD/>`_

5.7.3 (2018 January 11)
-----------------------

File format fixes and improvements:

* TIFF
   - fixed a NullPointerException when reading a TIFF file from the root system directory
   - improved support for large images that are stored as a single uncompressed tile with 
     multiple interleaved channels
* MRC (Medical Research Council)
   - added support in original metadata for the fields ``ISPG`` and ``Is data cube``
* TillPhotonics TillVision
   - directory listings for .pst files are now sorted
* MetaMorph
   - directory listings are now sorted during file initialization
* Amira Mesh
   - now supports ``Avizo`` in the file header in addition to the existing support for ``AmiraMesh``
* Becker & Hickl SPCImage
   - added a fix for IllegalArgumentException when reading files with compressed data
* Zeiss CZI
   - fixed an IndexOutOfBoundsException when creating ROI objects

Bug fixes and improvements:

* removed unused target utils-formats-api from ant build
* automated Memoizer tests updated to use UUID for generating unique memo file directories
* detect and fix Findbugs' ``SBSC_USE_STRINGBUFFER_CONCATENATION`` using StringBuilder
* configuration files for the automated test suite now use raw physical size rather than formatted size
* added first version of Dockerfile for running the automated test suite standalone

Documentation improvements:

* added a :source:`support <SUPPORT.md>` page to the Bio-Formats project
* updated reference URLs for the Aperio ImageScope and Micro-Manager
* documented issues with conflicts in the :ref:`JAI ImageIO component <forks-jai>`
* clarified the default values of HCS keys for fake images in the documentation for 
  :doc:`Generating test images </developers/generating-test-images>`
* corrected external links which failed automatic link checking

5.7.2 (2017 November 21)
------------------------

File format fixes and improvements:

* Nikon ND2
  - fixed a bug which would use the incorrect channel count for small-sized single channel images
* MetaMorph TIFF
   - changed the reader's behaviour to populate exposure times for all planes when only a 
     single exposure time is defined
* DeltaVision
   - improved parsing of the associated log files to add additional key value 
     pairs to global metadata
* EPS (Encapsulated PostScript)
   - fixed an exception when reading pixel data in cases with embedded TIFF
* GIF
   - fixed a bug to display the correct data when reading planes out of order

Bug fixes and improvements:

* fixed failures with Ant build from a clean Maven repository by updating Maven repositories 
  to use HTTPS rather than HTTP
* now using safe version checking for Bio-Formats plugins to prevent a bug with Java 9
* updated the JPEG-XR codec to allow either interleaved or non-interleaved data to be returned

Documentation improvements:

* added clarification regarding Bio-Formats version requirements for using Java 7 or above
* updated download links to latest Bio-Formats release version
* updated the link to the most active fork of JAI ImageIO
* fixed a number of external broken links
* added a Trello link for contributing external developers
* added a link to the page :doc:`Adding format/reader documentation pages</developers/format-documentation>` 
  to help those contributing to the documentation or supported formats pages
* the :doc:`Bio-Rad Gel</formats/bio-rad-gel>` page has been updated to add a link to biorad1sc_reader, 
  an external python implementation (thanks to Matthew Clapp)

5.7.1 (2017 September 20)
-------------------------

File format fixes and improvements:

* Nikon NIS-Elements ND2
   - improved parsing of Z position values
* LaVision Imspector
   - corrected the value of time per FLIM channel
   - fixed a bug which saw the Z and T dimensions swapped
   - fixed a divide by zero exception
   - added a fix for incorrect time-base and number of channels
* TIFF
   - added support for handling files with a FillOrder of 2 in which the bits in each 
     byte are reversed
   - improved support for multi-channel ImageJ TIFF files greater than 4GB in size

Performance improvements:

* improved TIFF performance by using non-regexp String replacement (thanks to Thushara Wijeratna)
* improved TIFF handling of Strings for large metadata (thanks to T. Alexander Popiel)

Documentation improvements:

* updated documentation to reference support for ImageJ TIFFs
* added links to format options page to user and developer index pages

5.7.0 (2017 September 4)
------------------------

File format fixes and improvements:

* Imaris HDF
   - fixed resolution problems in which dimensions and resolution order were incorrectly 
     calculated (thanks to Eliana Andreica)
* Nikon NIS-Elements ND2
   - fixed a bug in offset calculation when native chunk map is being used
* MetaMorph
   - corrected delta T and position Z values for multi-channel images when channels are 
     split across multiple files
* Amnis FlowSight
   - better handling of exceptions in isThisType method (thanks to Claire McQuin)
* PicoQuant Bin
   - better handling of exceptions in isThisType method (thanks to Claire McQuin)

Bug fixes and improvements:

* reviewed and corrected URLs throughout the Bio-Formats source code
* updated Bio-Formats Macro Extensions list with a missing function
* added a new option in Bio-Formats plugins to configure the slice label display using patterns

Documentation improvements:

* added new format page for :doc:`OMERO Pyramid</formats/omero-pyramid>`
* updated the developer page for :doc:`Working with whole slide images</developers/wsi>`
* added new page for configuring options in :doc:`Bio-Formats plugins</users/imagej/options>`
* updated documentation sidebar to enable navigation of previous versions

5.6.0 (2017 August 14)
----------------------

File format fixes and improvements:

* Zeiss CZI
   - added support for images from Elyra PALM system
   - prevented a potential infinite loop when a scene with a pyramid is missing
* cellSens VSI
   - a new option has been added to throw an exception rather than logging a 
     warning if .ets file is missing. The option, ``cellsens.fail_on_missing_ets``,
     can be used via the MetadataOptions API, as a parameter in the command 
     line tools or via the Bio-Formats configuration dialog in ImageJ
* MetaMorph Stack (STK)
   - fixed an error with HCS style datasets always returning the first plane 
     regardless of the requested index
   - updated to use stage labels starting with ``Scan`` to detect when a whole plate 
     is saved in a single .stk file
   - fixed a bug for ``ArrayIndexOutOfBoundsException`` when an image contains 
     a single Z plane
* Gatan Digital Micrograph
   - added support for Z stacks and ROIs
   - fixed several bugs in tag parsing
* PerkinElmer Operetta
   - ensure TIFF files exist before reading
* JPEG
   - support added for images with more than ``Integer.MAX_VALUE`` pixels

Bug fixes and improvements:

* JPEGTileDecoder
   - class now implements AutoCloseable to prevent resource leaks
* Bio-Formats Plugin
   - improved performance when using options to concatenate multiple series together
* TiffSaver
   - made performance improvements to prevent the writing of a new IFD for each tile, 
     resulting in significant file size reductions for images with a large quantity of tiles

Documentation improvements:

* updated website and URL links for new `OME Website <https://www.openmicroscopy.org>`_ website
* added missing :doc:`Andor SIF</formats/andor-sif>` to supported formats page
* added a new page :doc:`Working with whole slide images</developers/wsi>` outlining the API support 
  for pyramids/resolutions
* fixed broken documentation links for external resources which are no longer available
* updated the style of Sphinx documentation

Component architecture changes/decoupling:

* decoupled image encoding and decoding routines to the new
  `ome/ome-codecs GitHub repository <https://github.com/ome/ome-codecs>`_
  and consumed as 'org.openmicroscopy:ome-codecs' artifact from Maven Central
* removed components/forks/jai - decoupled to the new
  `ome/ome-jai GitHub repository <https://github.com/ome/ome-jai>`_
  and consumed as part of 'org.openmicroscopy:ome-jai' artifact from Maven Central
* replaced components/formats-api/codecs classes with wrappers around 'org.openmicroscopy:ome-codecs'
* replaced components/formats-bsd/codecs classes with wrappers around 'org.openmicroscopy:ome-codecs'

Updated build system:

* ant now removes the build files of the bundles during 'clean' to prevent a mix of dependencies

5.5.3 (2017 July 5)
-------------------

File format fixes and improvements:

* Zeiss CZI
   - fix to store Bézier ROIs as polygons, using the control points for the set 
     of Bézier curves to form an approximation of the ROI
   - improved parsing of stage positions in metadata
   - improved parsing of detector gain values
   - removed OME-XML validation errors by fixing potential for duplicate detector IDs
   - removed invalid XML failures for Modulo label elements
   - time increment metadata now populated on ``Pixels`` element
   - fix to deal with consecutive empty planes in a series (thanks to Nicholas Trahearn)
* DICOM
   - no longer allow core metadata to be modified when determining if files belong to a 
     DICOM dataset
* Nikon NIS-Elements ND2
   - fixed calculation for scanline padding
* Kodak BIP
   - stricter file type checking enforced by no longer relying only on the file suffix
* MINC MRI
   - improved parsing of metadata by correcting units for physical sizes, pixel type and 
     capturing XYZ plane positions in OME-XML
* Bio-Rad Gel
   - fixed the width of pixel data offset field
* DeltaVision
   - improved accuracy of format detection checking for input streams
* Andor SIF
   - fixed support for cropped images by parsing bounding box of the stored image

Documentation improvements:

* Olympus cellSens VSI updated to include list of available specifications

5.5.2 (2017 June 15)
--------------------

File format fixes and improvements:

* Olympus FluoView FV1000
   - fix for ``java.lang.ArrayIndexOutOfBoundsException`` caused by filter names
     of "---" (thanks to Stefan Helfrich)
   - refactored channel metadata population and increased usage of ``DataTools`` utility functions
* Zeiss CZI
   - fixed detection of Z line scans that caused incorrect dimensions in certain filesets
   - improved exception handling of truncated/invalid files 
* Veeco AFM
   - fixed reading of tiled images
* Hamamatsu ndpi
   - prevented potential memory leak by ensuring all ``TiffParser`` 
     streams are closed

Bug fixes:

* OMEXMLServiceImpl
   - improved exception handling to deal with potential ``java.lang.NullPointerException`` 
     when unable to locate OME-XML version while attempting to transform to the latest version

Documentation improvements:

* updated documentation to be compatible with the latest version of Sphinx 1.6
* fixed the usage/references of the option markup in documentation
* fixed the table in the Micro-Manager user page
* updated metadata ratings for supported formats

Updated build system:

* OME-Model version bump
   - the ome-model component has been updated to 5.5.4 which includes improvements to 
     performance, documentation and the C++ model implementation

5.5.1 (2017 May 25)
-------------------

File format improvements:

* CellH5
   - fix for ``HDF5SymbolTableException`` when recycling an IFormatReader to reopen 
     another CellH5 file
   - bug fix related to opening of subsets of CellH5 files, namely 
     ``openBytes(r, no, x, y, w, h)`` for y>0
* Zeiss CZI
   - fix pyramid resolution indexing for pyramids of different depths
   - fix for incorrect channel names and colors
* Zeiss AxioVision ZVI
   - correct parsing of epoch for Zeiss TIFF and Zeiss ZVI

Bug fixes:

* Command line tools 
   - fix for ``java.lang. NegativeArraySizeException`` caused by incorrect dimensions 
     when using showinf via command line with options set to autoscale and crop
* Format tools 
   - fix for ``java.lang. IndexOutOfBoundsException`` when using ``getFilename`` with an 
     image containing multiple samples per pixel channels and a single effective channel

Updated build system:

* Autogen jobs
   - fix for ``gen-meta-support`` to locate available ``org.openmicroscopy:ome-xml`` 
     sources from the Maven repository following the decoupling of the model components
* FileHandleTest
   - exclude JHDF5 native libraries from ``FileHandleTest`` to enable CellH5 files to be 
     included in daily tests

Documentation improvements:

* added a new example file for reading and writing of XZ and YZ orthogonal planes

5.5.0 (2017 May 8)
------------------

New file formats:

* Olympus OIR
   - added support for :doc:`Olympus .oir </formats/olympus-oir>` data  (funded by a 
     partnership between Glencoe Software and OLYMPUS EUROPA SE & Co. KG)
* PerkinElmer Columbus
   - added support for :doc:`PerkinElmer Columbus </formats/perkinelmer-columbus>` data

File format improvements:

* Andor Bio-Imaging Division (ABD) TIFF
   - fixed acquisition date format from ``MM/dd/yyyy`` to ``dd/MM/yyyy``
* Nikon NIS-Elements ND2
   - corrected logic used to determined ``PixelType`` by parsing uiBpc tags
* Hamamatsu ndpi
   - improved handling of channels in  NDPIS datasets (thanks to Manuel Stritt)
* Imspector OBF
   - fix for ``SAXParseException`` when description field in metadata is empty

Documentation improvements:

* added links to public sample files for Cellomics
* added links to public sample files for InCell 3000

5.4.1 (2017 April 13)
---------------------

File format improvements:

* MIAS (Maia Scientific)
   - added a fix for a possible exception when image files are not found under 
     channel-specific subdirectories
* BD Pathway
   - added fix to check if ``Experiment.exp`` is a directory or an experiment file
* Imspector OBF
   - enabled forward compatibility for future versions, as the OBF format is backwards 
     compatible (thanks to Bjoern Thiel)

Documentation improvements:

* updated external homepage link for FocalPoint
* removed Imago from list of visualization and analysis applications as it is no
  longer available from the Mayachitra website
* added links to public sample files for Hamamatsu NDPI and Hamamatsu VMS
* listed OpenSlide as available software for supported formats
* added a new developer page detailing in-memory reading and writing
* updated the Bio-Formats API versioning policy, which now follows strict 
  semantic versioning
* a new options page has been added, detailing the usage of configurable format-specific 
  options for readers and writers. Links to the available options are also included under 
  the relevant supported formats

5.4.0 (2017 March 21)
---------------------

File format improvements:

* DICOM
   - added support for DICOMDIR files, which allow multiple DICOM files in a 
     single directory to be opened as a single dataset
   - plane position values for values X, Y and Z are now being set in OME-XML
   - correctly read the physical size X and Y values based on the available 
     `specification <http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_10.7.html#sect_10.7.1.3>`_
* Nikon NIS-Elements ND2
   - performance improvements based on reading chunkmap. Processing of the
     chunkmap can be disabled via the MetadataOptions API using the boolean
     option ``nativend2.chunkmap``. For ImageJ users this option can be
     accessed via a checkbox in the Nikon ND2 section of the Bio-Formats
     configuration dialog
     :menuselection:`Plugins --> Bio-Formats --> Bio-Formats Plugins Configuration` (thanks to Christian Sachs)
* OME-TIFF
   - added an option to save an OME-TIFF dataset as a binary TIFF and
     companion XML. This can be used via the bfconvert command line tool by
     setting the value of option ``ometiff.companion`` to the name of the
     companion file to use. For example ``bfconvert -option ometiff.companion
     outputFile.companion.ome inputFile.tiff outputFile.ome.tiff``
* CellVoyager
   - metadata fixes specifically the naming of plates. Additional refactoring
     of the reader for general maintainability
* Gatan Digital Micrograph
   - previously missing Image-Instrument reference has been added to OME-XML
* TiffSaver
   - ensure open resources are closed under all possible scenarios
* Zeiss CZI
   - improved performance of large uncompressed images. When tiles from a
     large uncompressed image with no internal tiling are requested, only the
     specific tile specified in the call to ``openBytes`` is read from disk,
     instead of the entire image being read and then copied
* Zeiss AxioVision ZVI (Zeiss Vision Image)
   - ensure that the ``bitsPerPixel`` field is always set to match the final
     pixel type, and populate any channel colors that were parsed in the
     metadata. The bits per pixel update should only affect ``uint16`` or 
     ``int16`` files where the acquisition bit depth is not a multiple of 8, 
     and the RGB channel count is greater than 1

Updated build system:

* updated dependency for NetCDF to 4.3.22
* updated copyright headers from 2016 to 2017 and reviewed and fixed any incorrect 
  header descriptions
* documentation has been migrated to use ``.rst`` file format for Sphinx files
* reviewed and cleaned up warnings such as unused variables and imports
* added CellVoyager datasets to automated testing via continuous integration
* unified the semantics for creating temporary directories within unit tests

Documentation improvements:

* fixed link for PerkinElmer UltraVIEW system
* fixed links for NIfTI public specification and data sets
* available software for Hamamatsu ndpi has been updated from NDP.view to NDP.view2

5.3.4 (2017 February 21)
------------------------

Bug fixes:

* ImageJ
   - fix for a NullPointerException when exporting images that were not opened via 
     the Bio-Formats importer, and thus do not have a complete OMEXMLMetadata store

* Java 1.9
   - fix compile and runtime errors to enable building with Java 1.9

* ECAT7
   - update to add support for different versions of ECAT7 files (thanks to Torsten Stöter)

Updated build system:

* updated dependency for `ome-model <https://github.com/ome/ome-model>`_ in the POM to 
  version 5.4.0. This allows for improved ROI handling by enabling support for Shape 
  objects with Transform attributes. OME-XML schema version remains unchanged as 
  :model_doc:`OME schema 2016-06 <schemas/june-2016-2.html>`

Documentation improvements:

* new public sample files added for ECAT7 (thanks to Torsten Stöter)
* new public sample files added for Leica LIF (thanks to Michael Goelzer)
* new specification document (Version 3.2) for Leica LIF
* updated links to OMERO documentation as a result of decoupling

5.3.3 (2017 February 2)
-----------------------

Bug fixes:

* ImageJ
   - fix for issue when exporting from an ImagePlus that represents signed 
     data. The pixel type will now remain unchanged as will the pixel values 
     which had previously been scaled incorrectly

* Command line tools 
   - fix for ``java.lang.IllegalArgumentException`` when using bfconvert via command line 
     with option set to only convert a single time-point, channel or Z section

* Tiff writing 
   - using TiffWriter to write tiled images now supports the writing of 
     BigTIFF datasets

File format fixes:

* Applied Precision CellWorX
   - fix to now display the correct plate name and dimensions

* NIFTI
   - a few fixes for problems with byte alignment when reading non-core 
     metadata from NIFTI headers

* Leica LIF
   - added support for timestamps of LIF files created with LAS AF 3.1 or 
     newer. In the case of a halted acquisition only non-null timestamps are 
     stored in the OME metadata (thanks to Michael Goelzer)
   - the physical pixel height and width were incorrectly calculated by 
     dividing by the number of pixels. This has now been corrected to match 
     the official Leica LIF specification documents by dividing by the number 
     of pixels minus one (thanks to Michael Goelzer)
   - for backwards compatibility an option to preserve pre-5.3.3 physical sizes 
     has been added. This can be set either via command line tools, through 
     the API with the ``loci.formats.in.DynamicMetadataOptions`` class, or in the Bio-Formats 
     plugin configuration in ImageJ

* Improvision TIFF
   - channel colors are now being read and if present set correctly in image metadata

* MetaMorph
   - fix for ``java.lang.OutOfMemoryError`` exceptions when reading large Metamorph TIFF plates

Updated build system:

* version history file added to MATLAB bundle as NEWS.rst
* increased TiffWriter test coverage
* added test coverage framework for command line tools including new ImageConverterTest 

Documentation improvements:

* improved documentation and new examples for using tiled writing
* updated developer documentation for use of Bio-Formats as a Maven, Gradle 
  or Ivy dependency
* documentation for Leica LIF bug fixes and use of backward compatibility options
* fixes for a number of broken links

5.3.2 (2017 January 9)
----------------------

Bug fixes:

* ImageJ
   - fixed race condition when opening multiple series from a dataset, as
     introduced by thumbnail loading changes in 5.3.0
   - updated thumbnail generation to be faster for datasets containing an
     image pyramid

* Metamorph
   - updated to read the refractive index and set ``RefractiveIndex`` on
     ``ObjectiveSettings`` in the generated OME-XML (thanks to Marc Bruce)

* Metamorph TIFF
   - fixed Z and channel dimension counts when each channel has a unique Z position
   - updated to read the emission wavelength and set ``EmissionWavelength`` on
     ``LightSourceSettings`` in the generated OME-XML

* QuickTime
   - fixed incorrect image data when reading of tiles from single channel files

* file grouping
   - fixed handling of ``loci.formats.in.MetadataOptions`` objects by the
     ``loci.formats.FileStitcher`` reader

Documentation improvements:

* fixed extensions listed for Zeiss TIFF
* simplified markdown for creating tables

5.3.1 (2016 December 19)
------------------------

File format fixes:

* TIFF
   - fixed invalid IFD values when writing TIFF or OME-TIFF files with 
     Bio-Formats 5.3.0. This bug affected the writing of TIFF and OME-TIFF 
     via client code using ``loci.formats.TiffWriter``, converting to a TIFF 
     or OME-TIFF using 'bfconvert' command line tool or exporting to TIFF or 
     OME-TIFF using ImageJ/FIJI Bio-Formats exporter.

5.3.0 (2016 December 12)
------------------------

New features/API:

* added support for JPEG-XR compressed CZI data (funded by a
  `partnership between Glencoe Software and ZEISS <http://glencoesoftware.com/pressreleases/2016-08-30-glencoe-software-zeiss-partner-open-source-file-reader-whole-slide.html>`_), adding 'ome:jxrlib' as a new dependency
  of Bio-Formats
* improved tile-based image writing
    - added new methods to the ``loci.formats.IFormatWriter`` interface
      allowing to set and retrieve the tile along the X and Y dimensions
    - added default implementations to the ``loci.formats.FormatWriter``
      abstract class defaulting to the entire image width/height
    - added functionality to ``loci.formats.TiffWriter`` adding support for
      tiled images writing for TIFF and derived formats like OME-TIFF
    - added developer documentation and samples for tiled reading/writing
* added a new ``MetadataOptions`` implementation supporting arbitrary key/value
  pairs
* updated the display command line utility to support passing key/value
  options using :option:`showinf -option`
* added two options to the CZI reader to disable autostitching and exclude
  pyramid file attachments. Added new checkboxes to the CZI configuration
  interface of the ImageJ plugin to activate these options

Bug fixes/deprecations:

* deprecated ``loci.formats.meta.MetadataConverter`` in favor of
  ``ome.xml.meta.MetadataConverter``
* updated method deprecated in Octave 4.2.0 (thanks to Carnë Draug)
* OME-XML
    - fixed handling of Mask BinData elements

Component architecture changes/decoupling:

* removed formats-common component - now decoupled to the new
  `ome/ome-common-java GitHub repository <https://github.com/ome/ome-common-java>`_
  and consumed as 'org.openmicroscopy:ome-common' artifact from Maven
  Central
* removed ome-poi component - now decoupled to the new
  `ome/ome-poi GitHub repository <https://github.com/ome/ome-poi>`_
  and consumed as 'org.openmicroscopy:ome-poi' artifact from Maven Central
* removed specification, xsd-fu and ome-xml components - now decoupled to the
  new `ome/ome-model GitHub repository <https://github.com/ome/ome-model>`_
  and consumed as 'org.openmicroscopy:{specification,ome-xml}'
  artifacts from Maven Central
* removed mdbtools component - now decoupled to the new
  `ome/ome-mdbtools GitHub repository <https://github.com/ome/ome-mdbtools>`_
  and consumed as 'org.openmicroscopy:ome-mdbtools' artifact from Maven
  Central
* removed stubs components - now decoupled to the new
  `ome/ome-stubs GitHub repository <https://github.com/ome/ome-stubs>`_ and
  consumed as 'org.openmicroscopy:{lwf-stubs,mipav-stubs}' artifacts from
  Maven Central
* removed metakit component - now decoupled to the new
  `ome/ome-metakit GitHub repository <https://github.com/ome/ome-metakit>`_
  and consumed as 'org.openmicroscopy:metakit' artifacts from
  Maven Central
* updated developer documentation for the decoupled components

Updated build system:

* dropped embedded JARs and now use the Maven Ant Tasks plugin to unify the
  dependencies using the POM
* improved Ant JAR and bundle target
* dropped deprecated osgi targets, OME Tools bundle and ome-jxr component
* removed PDF generation from the docs-sphinx target
* added version number to Javadoc zip bundle name
* migrated unit tests out of test-suite into formats-bsd
* fixed test-suite targets, paths and symlink handling
* fixed test-metadata and migrated it into test-suite
* fixed mismatch between ``ND2HandlerTest`` package and location
* cleaned up test-build to remove obsolete and decoupled components
  and folders
* simplified Travis build
* POM repositories clean-up to reduce complexity and use Maven Central as the
  first location to look for dependencies
* now storing all versions in the top-level POM
* updated build versioning from Maven by unified versioning strategy,
  reviewing meta information stored in the manifests of each JAR and
  introspecting this information in the ``FormatTools`` API to retrieve
  version and revision numbers
* updated developer documentation on updated build system

5.2.4 (2016 October 18)
-----------------------

Java bug fixes:

* OME-TIFF
   - fixed regression when populating plane metadata
* CZI
   - populated series metadata with the scene/position information

5.2.3 (2016 October 5)
----------------------

Java bug fixes:

* CZI
   - fixed imageCount for RGB images
* ICS writing
   - fixed ordering of image dimensions
* DeltaVision
   - fixed reading of large time dimensions

Command-line tools improvements:

* :file:`bftools.zip` now includes the version history as :file:`NEWS.rst`
  (thanks to Gerhard Burger)

Code clean-up/improvements:

* switched to `String.indexOf(int)` in GPL-licensed reader code so that a
  simpler library method can be used
* strings now extended with characters where possible
* completed deprecation of `DataTools.sanitizeDouble()`
* deprecated unused OSGi and ome-tools bundle build targets

OME-XML changes/improvements:

* bumped schema version number to 2 (schema namespace left unchanged)
* added acquisition modes `BrightField`, `SweptFieldConfocal` and `SPIM`
* added parsing for Laser Scan Confocal and Swept Field Confocal

Documentation improvements:

* documented versioning policy
* clarified supported versions for Micro-Manager and Olympus ScanR files

5.2.2 (2016 September 13)
-------------------------

Java bug fixes and improvements:

* fixed a regression in which the DataTools number parsing API would not be
  thread-safe anymore
* InCell
   - improved handling of Analyzer 2000 datasets to find TIFF files
* FV1000
   - fixed preview names ordering
* OME-TIFF
   - enabled all BigTIFF extensions
* various code cleanup across the Java code
* added test coverage for all example codes in the developer documentations
* added tests covering the semantics of the INI parser

ImageJ bug fixes and improvements:

* fixed a bug in ImageJ when swapping dimensions of an image with multiple
  series of different dimensions
* added an option to the exporter to pad filename indexes with zeros

Command-line tools improvements:

* allowed the binaries to be symlinked (thanks to Gerhard Burger)
* added an option to bfconvert to pad filename indexes with zeros

5.2.1 (2016 August 25)
----------------------

Java bug fixes:

* Zeiss CZI
   - fixed NumberFormatException when the position object is not null but the
     values of child are null
* SimplePCI
   - made IniParser less stringent to allow reading of imperfectly formatted
     TIFF description headers
* fixed stitching of file patterns in ImageJ to remove duplication of
  directory names in the file path
* added an option to bfconvert to allow creation of OME-TIFF without lookup
  tables
* addition of MetadataOnly elements containing no BinData or TiffData now
  handled via MetadataTools API in ImageInfo
* example code in developer docs is now tested via a new Maven module

5.2.0 (2016 August 18)
----------------------

Java format support improvements are listed below.

†Denotes a major breaking change to the reader (typically modification of core
metadata). Code changes or re-import may be necessary in ImageJ/FIJI and
OMERO.

* added support (and public sample files) for
  :doc:`Becker & Hickl .spc FIFO </formats/becker-hickl-fifo>` data
* added support for :doc:`Princeton Instruments .spe </formats/princeton-instruments-spe>` data
* bug fixes for many formats including:
   - CellSens VSI†
       - fixes for correctly reading dimensions
   - FlowSight
       - fixes to infer channel count from channel names (thanks to Lee
         Kamentsky)
   - Hamamatsu VMS†
       - fixed dimensions of full-resolution images
   - ICS writing
       - fixed dimension population for split files
   - Kodak BIP
       - fixed handling of CCD temperature stored in hexadecimal
   - Leica LIF
       - fixed incorrect plane offsets for large multi-tile files
   - LiFlim
       - fixed ``ExposureTime`` check and units usage
   - Micro-Manager
       - fixed handling of large datasets saved as image stacks and split
         over multiple files
       - added user documentation for file saving options
   - MRC and Spider
       - fixed format type checking
   - Nifti
       - fixed ``planeSize`` to prevent crashes when loading large files
         (thanks to Christian Niedworok)
       - added support for gzipped compressed .nii.gz files (thanks to Eric
         Barnhill)
       - added public samples and updated documented supported file extensions
   - OME-TIFF
       - fixed ``Plane`` population errors
       - fixed ``NullPointerException`` when closing reader for partial
         multi-file filesets
       - reduced buffer size for ``RandomAccessInputStreams`` to improve
         performance
       - deprecated ``getMetadataStoreForConversion`` and
         ``getMetadataStoreForDisplay`` methods
   - OME-XML
       - fixed metadata store
   - PicoQuant
       - updated reader to always buffer data
   - PNG writing
   - SDT
       - performance improvements for loading of large files
   - Slidebook
       - Slidebook6Reader is now completely external and fully maintained by
         3i (see http://www.openmicroscopy.org/info/slidebook) and is
         specified as such in the :file:`readers.txt` configuration file
   - SVS
       - fixed ``NumberFormatException``
   - Tiff
       - fixed integer overflow to read resolutions correctly
       - fixed handling of tiled images with tile width less than 64
   - Zeiss CZI
       - fixed timestamp indexing when multiple separate channels are present
       - improved slide support - slides are now detected as a complete
         full-resolution image (instead of each tile being a separate series)
         and pyramid sub-resolutions and label/overview images are also
         detected
   - Zeiss LSM
       - fixed ``Plane`` population errors
   - Zeiss ZVI†
       - reworked image ordering calculation to allow for tiles


Top-level Bio-Formats API changes:

* Java 1.7 is now the minimum supported version
* the native-lib-loader dependency has been bumped to version 2.1.4
* the xalan dependency has been bumped to version 2.7.2
* all the ome.jxr classes have been deprecated to make clear that there is no
  JPEG-XR support implemented in Bio-Formats as yet
* the DataTools API has been extended to add a number of utility functions to:
   - account for decimal separators in different locales
   - parse a ``String`` into ``Double``, ``Float``, ``Integer`` etc
   - handle ``NumberFormatException`` thrown when parsing Unit tests
* the Logging API has been updated to respect logging frameworks
  (log4j/logback) initialized via a binding-specific configuration file and
  to prevent ``DebugTools.enableLogging(String)`` from overriding initialized
  logger levels (see :doc:`/developers/logging` for more information)
* helper methods have been added to FormatTools allowing a stage position to
  be formatted from an input ``Double`` and an input unit
* the Formats API has also been updated to add a new validate property to
  ``MetadataOptions`` and support for ``MetadataOptions`` has been moved to
  FormatHandler level to allow it to be used by both Readers and Writers
* initial work on `Reader discoverability <https://github.com/ome/design/issues/42>`_
  extended the ClassList API to allow the :file:`readers.txt` configuration
  file to be annotated using key/value pairs to mark optional Readers and
  specify additional per-Reader options

Other general improvements include:

* improved performance of ``getUsedFiles``
* fixes for ``FilePatternBlock``, ``AxisGuesser``, ``FilePattern``
* fixes for the detection of CSV pattern blocks by ``FilePatternBlock``
* :file:`bioformats_package.jar` now includes bio-formats-tools as a
  dependency so ``ImageConverter``, ``ImageFaker`` and ``ImageInfo`` classes
  are included in the bundle
* the JACE C++ implementation has been decoupled as it does not function with
  Java 1.8 (see `legacy repo <https://github.com/ome/bio-formats-jace>`_)
* ImageJ fixes
   - to allow reader delegation when a legacy reader is enabled
     but not working
   - to allow ROIs to be imported to the ImageJ ROI manager or added to a new
     overlay
* MATLAB fixes
   - improved integration with Octave (thanks to Carnë Draug)
   - added logging initialization
* Command-line tools fixes
   - upgrade check no longer run when passing -version
   - common methods refactoring
   - showinf improvements to preload format
   - tiffcomment now warns that it requires an ImageDescription tag to be
     present in the TIFF file
* added many automated tests and improved FakeReader testing framework
* documentation improvements include:
   - clarifying status of legacy Quicktime and ND2 readers
   - noting that the Gatan reader does not currently support stacks
   - more Java examples added to the developer documentation
   - new units page for developers

The Data Model version 2016-06 has been released to introduce
`Folders <http://blog.openmicroscopy.org/data-model/future-plans/2016/05/23/folders-upcoming/>`_,
and to simplify both the graphical aspects of the model and code generation.
Full details are available in the
:model_doc:`OME Model and Formats Documentation <schemas/june-2016.html>`.
OME-XML changes include:

* `Map` is now a complexType rather than an element and `MapPairs` has been
  dropped
* extended enum metadata has been introduced to better support units
* `Shape` and `LightSource` are now complexTypes rather than elements
* BinData has been added to code generation to handle raw binary data
* various code generation improvements to:
   - simplify and standardize the generation process
   - remove a number of hard-coded exceptional cases allowing for easier
     maintenance and growth
   - allow for genuine abstract model types and enable C++ model
     implementation
* updated OME-XML and OME-TIFF public sample files

The Bio-Formats C++ native implementation has been decoupled from
the Java codebase and will be released as
`OME-Files C++ <https://downloads.openmicroscopy.org/ome-files-cpp/>`_ from now
on, with the exception of OME-XML which is still within Bio-Formats at present
(there is a plan to decouple both the Java and the C++ versions of OME-XML in
future).

The following components have had their licensing updated to Simplified
(2-clause) BSD:

* XSL transforms
* specification code
* xsd-fu Python code


5.1.10 (2016 May 9)
-------------------

Java bug fixes:

* fixed warnings being thrown for ImageJ and other non-FIJI users on Windows
  (these warnings were triggered by the removal of the 3i Slidebook DLLs from
  the source code repository in Bio-Formats 5.1.9 and should now only be
  triggered when opening Slidebook files without the update site enabled -
  http://www.openmicroscopy.org/info/slidebook)
* a fix in the ImageJ plugin for files grouped using the "Dimensions" option
* a fix for writing TIFF files in tiles


5.1.9 (2016 April 14)
---------------------

* Java bug fixes, including:
   - SDT
       - fixed width padding calculation for single-pixel image
   - Deltavision
       - fixed the parsing of the new date format
       - added support for parsing and storing the working distance in native units
   - Micromanager
       - cleaned up JSON metadata parsing
   - Olympus Fluoview
       - fixed null pointer exceptions while parsing metadata
   - Leica LIF
       - fixed large multi-tiled files from having incorrect plane offsets after the 2GB mark
   - EM formats (MRC and Spider)
       - added native length support for EM readers
   - Gatan
       - fixed erroneous metadata parsing
       - added support for parsing and storing the physical sizes in native units
   - OME-TIFF
       - improved handling of OME-TIFF multi-file fileset’s with partial metadata blocks
   - Nikon ND2
       - fixed the parsing of emission wavelength
   - Olympus CellR (APL)
       - fixed multiple parsing issues with the mtb file
   - SlideBook
       - removed slidebook dlls from Bio-Formats repository
       - http://www.openmicroscopy.org/info/slidebook
   - Zeiss CZI
       - fixed parsing of files with multiple mosaics and positions

* Documentation updates, including:
   - improved documentation for the export of BigTIFFs in ImageJ

* C++:
   - no changes.


5.1.8 (2016 February 15)
------------------------

* Java bug fixes, including:
   - FEI TIFF
       - fixed stage position parsing and whitespace handling (thanks to Antoine Vandecreme)
   - Pyramid TIFF
       - fixed tile reading when a cache (.bfmemo) file is present
   - MicroManager
       - updated to parse JSON data from tags 50839 and 51123
       - fixed to detect :file:`*_metadata.txt` files in addition to :file:`metadata.txt`
         files
       - fixed to handle datasets with each stack in a single file
   - OME-XML
       - updated to make .ome.xml an official extension
   - OME-TIFF
       - fixed to ignore invalid BinaryOnly elements
   - TIFF
       - fixed caching of BigTIFF files
   - Slidebook
       - fixed handling of montages in Slidebook6Reader (thanks to Richard Myers)
   - Performance improvement for writing files to disk (thanks to Stephane Dallongeville)
   - Build system
       - fixed Maven POMs to reduce calls to artifacts.openmicroscopy.org
       - fixed bioformats_package.jar to include the loci.formats.tools
         package
* Documentation updates, including:
   - updated format pages to include links to example data
   - clarified description of Qu for MATLAB (thanks to Carnë Draug)
   - added installation instructions for Octave (thanks to Carnë Draug)
* C++:
   - Bugfixes to the OME-TIFF writer to correct use of the metadata store with
     multiple series
   - Ensure file and writer state consistency upon close failure

5.1.7 (2015 December 7)
-----------------------

* Java bug fixes, including:
   - Prevent physical pixel sizes from being rounded to 0, for all formats
   - Metamorph
       - fixed calculation of Z step size
       - fixed detection of post-processed dual camera acquisitions (thanks to Mark Kittisopikul)
   - OME-XML
       - fixed XML validation when an 'xmlns' value is not present (thanks to Bjoern Thiel)
   - MINC
       - fixed endianness of image data
   - Andor/Fluoview TIFF
       - fixed calculation of Z step size
   - MATLAB
       - improved performance by reducing static classpath checks (thanks to Mark Kittisopikul)
   - Gatan
       - fixed physical size parsing in non-English locales
   - Automated testing
       - fixed handling of non-default physical size and plane position units
* Documentation updates, including:
   - updated MapAnnotation example to show linkage of annotations to images
* C++:
   - no changes, released to keep version numbers in sync with Bio-Formats Java


5.1.6 (2015 November 16)
------------------------

* Java bug fixes, including:
   - Updated to use native units for following formats:
       - IMOD
       - Analyze
       - Unisoku
       - Olympus CellR (APL)
   - Metamorph TIFF
       - fixed handling of multi-line descriptions
       - added support for dual camera acquisitions
   - Zeiss LMS
       - fixed exception in type detection
   - Zeiss CZI
       - fixed detection of line scan Airyscan data
   - Slidebook
       - fixed calculation of physical Z size
   - ImageJ plugins
       - fixed handling of non-default units
       - fixed setting of preferences via macros
   - Automated testing
       - fixed handling of non-default units for physical sizes and timings
* C++ changes, including:
   - allow relocatable installation on Windows
   - reduce time required for debug builds
* Documentation updates, including:
   - addition of "Multiple Images" column to the supported formats table
   - addition of a MapAnnotation example

5.1.5 (2015 October 12)
-----------------------

* Java bug fixes, including:
   - ImageJ plugins
       - fixed use of "Group files..." and "Open files individually" options
       - fixed placement of ROIs
       - fixed size of the "About Plugins > Bio-Formats Plugins" window
   - xsd-fu (code generation)
       - removed OMERO-specific logic
   - Metamorph
       - fixed physical Z size calculation
   - Gatan DM3/DM4
       - fixed physical pixel size parsing
   - BMP
       - added support for RLE compression
   - DICOM
       - updated to respect the WINDOW_CENTER tag
       - fixed image dimensions when multiple sets of width and height values
         are present
   - Fluoview and Andor TIFF
       - fixed physical Z size calculation
   - Imspector OBF
       - updated to parse OME-XML metadata (thanks to Bjoern Thiel)
* C++ changes:
   - TIFF strip/tile row and column calulations corrected to compute
     the correct row and column count
   - Several compiler warnings removed (false positive warnings in
     third-party headers disabled, and additional warnings fixed)
   - It is now possible to build with Boost 1.59 and compile with a
     C++14 compiler
* The source release is now provided in both tar.xz and zip formats
* Documentation updates, including:
   - substantial updates to the format pages
       - improved linking of reader/writer classes to each format page
       - improved supported metadata pages for each format
       - updated format page formatting for clarity
       - added developer documentation for adding and modifying format pages

5.1.4 (2015 September 7)
------------------------

* Bug fixes, including:
   - Command line tools
       - fixed display of usage information
   - Automated testing
       - fixed problems with symlinked data on Windows
       - added unit tests for checking physical pixel size creation
   - Cellomics
       - fixed reading of sparse plates
   - SlideBook
       - fixed a few lingering issues with native library packaging
   - SimplePCI/HCImage TIFF
       - fixed bit depth parsing for files from newer versions of HCImage
   - SimplePCI/HCImage .cxd
       - fixed image dimensions to allow for extra padding bytes
   - Leica LIF
       - improved reading of image descriptions
   - ICS
       - fixed to use correct units for timestamps and physical pixel sizes
   - MicroManager
       - fixed to use correct units for timestamps
   - Gatan .dm3/.dm4
       - fixed problems with reading double-precision metadata values
   - Hamamatsu NDPI
       - fixed reading of mask images
   - Leica .lei
       - fixed reading of bit depth and endianness for datasets that were modified after
         acquisition
   - FEI TIFF
       - updated to read metadata from files produced by FEI Titan systems
   - QuickTime
       - fixed to handle planes with no stored pixels
   - Leica .scn
       - fixed reading of files that contain fewer images than expected
   - Zeiss .czi
       - fixed channel colors when an alpha value is not recorded
       - fixed handling of pre-stitched image tiles
   - SDT
       - added support for Zip-compressed images
   - Nikon .nd2
       - fixed to read image dimensions from new non-XML metadata
   - OME-XML
       - fixed writing of integer metadata values
* Native C++ updates:
   - completed support for building on Windows
* Documentation updates, including:
   - updated instructions for running automated data tests
   - clarified JVM versions currently supported

5.1.3 (2015 July 21)
--------------------

* Native C++ updates:
   - Added cmake superbuild to build core dependencies (zlib, bzip2, png, icu, xerces, boost)
   - Progress on support for Windows
* Bug fixes, including:
   - Fixed segfault in the `showinf` tool used with the C++ bindings
   - Allow reading from https URLs
   - ImageJ
       - improved performance of displaying ROIs
   - Command line tools
       - fixed bfconvert to correctly create datasets with multiple files
   - Metamorph
       - improved detection of time series
       - fixed .nd datasets with variable Z and T counts in each channel
       - fixed .nd datasets that contain invalid TIFF/STK files
       - fixed dimensions when the number of planes does not match the recorded
         Z, C, and T sizes
   - SlideBook
       - improved native library detection (thanks to Richard Myers)
   - JPEG
       - fixed decompression of lossless files with multiple channels (thanks to Aaron Avery)
   - Imspector OBF
       - updated to support version 2 files (thanks to Bjoern Thiel)
   - Imspector MSR
       - improved detection of Z stacks
   - PerkinElmer Opera Flex
       - improved handling of multiple acquisitions of the same plate
   - Zeiss CZI
       - fixed error when opening single-file datasets whose names contained
         "("  and ")"
   - TIFF
       - improved speed of reading files with many tiles
   - AVI
       - updated to read frame index (idx1) tables
   - Nikon ND2
       - fixed channel counts for files with more than 3 channels
   - PNG
       - fixed decoding of interlaced images with a width or height that is not a multiple of 8
   - PSD
       - improved reading of compressed images
* Documentation improvements, including:
    - updated instructions for writing a new file format reader
    - updated usage information for command line tools
    - new Javadocs for the `MetadataStore` and `MetadataRetrieve` interfaces


5.1.2 (2015 May 28)
-------------------

* Added OME-TIFF writing support to the native C++ implementation
* OME-TIFF export: switch to BigTIFF if .ome.tf2, .ome.tf8, or .ome.btf
  extensions are used
* Improved MATLAB developer documentation
* Added SlideBook reader that uses the SDK from 3I (thanks to Richard Myers
  and `3I - Intelligent Imaging Innovations <https://www.intelligent-imaging.com>`_)
* Preliminary work to make MATLAB toolbox work with Octave
* Many bug fixes, including:
    - ImageJ
        - fixed regression in getPlanePosition* macro extension methods
        - fixed display of composite color virtual stacks
    - Nikon ND2
        - improved parsing of plane position and timestamp data
    - TIFF
        - reduced memory required to read color lookup tables
    - Zeiss LSM
        - improved parsing of 16-bit color lookup tables
    - Zeiss CZI
        - fixed ordering of original metadata table
        - fixed reading of large pre-stitched tiled images
    - AIM
        - fixed handling of truncated files
    - Metamorph/MetaXpress TIFF
        - improved UIC1 metadata tag parsing

5.1.1 (2015 April 28)
---------------------

* Add TIFF writing support to the native C++ implementation
* Fixed remaining functional differences between Windows and Mac/Linux
* Improved performance of ImageJ plugin when working with ROIs
* TIFF export: switch to BigTIFF if .tf2, .tf8, or .btf extensions are used
* Many bug fixes, including:
    - fixed upgrade checking to more accurately report when a new version is
      available
    - Zeiss CZI
        - fixed ordering of multiposition data
        - improved support for RGB and fused images
    - Nikon ND2
        - improved ordering of multiposition data
    - Leica LIF
        - improved metadata validity checks
        - improved excitation wavelength detection
    - Metamorph STK/TIFF
        - record lens numerical aperture
        - fixed millisecond values in timestamps
    - Gatan DM3
        - correctly detect signed pixel data
    - Imaris HDF
        - fix channel count detection
    - ICS export
        - fix writing of files larger than 2GB

5.1.0 (2015 April 2)
---------------------

* Improvements to performance with network file systems
* Improvements to developer documentation
* Initial version of native C++ implementation
* Improved support for opening and saving ROI data with ImageJ
* Added support for :doc:`CellH5 </formats/cellh5>` data (thanks to Christoph Sommer)
* Added support for :doc:`Perkin Elmer Nuance </formats/perkinelmer-nuance>` data (thanks to Lee Kamentsky)
* Added support for :doc:`Amnis FlowSight </formats/amnis-flowsight>` data (thanks to Lee Kamentsky and Sebastien Simard)
* Added support for :doc:`Veeco AFM </formats/veeco-afm>` data
* Added support for :doc:`Zeiss .lms </formats/zeiss-axio-csm>` data (not to be confused with .lsm)
* Added support for :doc:`I2I </formats/i2i>` data
* Added support for writing Vaa3D data (thanks to Brian Long)
* Updated to :model_doc:`OME schema 2015-01 </schemas/january-2015.html>`
* Update RandomAccessInputStream and RandomAccessOutputStream to read and write bits
* Many bug fixes, including:
    - Leica SCN
        - fix pixel data decompression
        - fix handling of files with multiple channels
        - parse magnification and physical pixel size data
    - Olympus/CellSens .vsi
        - more thorough parsing of metadata
        - improved reading of thumbnails and multi-resolution images
    - NDPI
        - fix reading of files larger than 4GB
        - parse magnification data
    - Zeiss CZI
        - improve parsing of plane position coordinates
    - Inveon
        - fix reading of files larger than 2 GB
    - Nikon ND2
        - many improvements to dimension detection
        - many improvements to metadata parsing accuracy
        - update original metadata table to include PFS data
    - Gatan DM3
        - fix encoding when parsing metadata
        - fix physical pixel size parsing
    - Metamorph
        - fix off-by-one in metadata parsing
        - fix number parsing to be independent of the system locale
    - JPEG
        - parse EXIF data, if present (thanks to Paul Van Schayck)
    - OME-XML/OME-TIFF
        - fix handling of missing image data
    - PrairieView
        - improved support for version 5.2 data (thanks to Curtis Rueden)
    - DICOM
        - fix dimensions for multi-file datasets
        - fix pixel data decoding for files with multiple images
    - PNG
        - reduce memory required to read large images
    - Imspector OBF
        - fix support for version 5 data (thanks to Bjoern Thiel)
    - PCORAW
        - fix reading of files larger than 4 GB
    - AIM
        - fix reading of files larger than 4 GB
    - MRC
        - add support for signed 8-bit data
    - Fix build errors in MIPAV plugin
    - ImageJ
        - fix export from a script/macro
        - fix windowless export
        - allow exporting from any open image window
        - allow the "Group files with similar names" and "Swap dimensions"
          options to be used from a script/macro
    - bfconvert
        - fix writing each channel, Z section, and/or timepoint to a separate file
        - add options for configuring the tile size to be used when saving images

5.0.8 (2015 February 10)
------------------------

* No changes - release to keep version numbers in sync with OMERO

5.0.7 (2015 February 5)
-----------------------

* Several bug fixes, including:
    - ND filter parsing for DeltaVision
    - Timepoint count and original metadata parsing for Metamorph
    - Build issues when Genshi or Git are missing
    - LZW image decoding

5.0.6 (2014 November 11)
------------------------

* Several bug fixes, including:
    - Pixel sign for DICOM images
    - Image dimensions for Zeiss CZI and Nikon ND2
    - Support for Leica LIF files produced by LAS AF 4.0 and later

5.0.5 (2014 September 23)
-------------------------

* Documentation improvements
* Support for non-spectral Prairie 5.2 datasets

5.0.4 (2014 September 3)
------------------------

* Fix compile and runtime errors under Java 1.8
* Improvements to Nikon .nd2 metadata parsing
* Added support for PicoQuant .bin files (thanks to Ian Munro)

5.0.3 (2014 August 7)
---------------------

* Many bug fixes for Nikon .nd2 files
* Several other bug fixes, including:
    - LZW image decoding
    - Stage position parsing for Zeiss CZI
    - Exposure time units for ScanR
    - Physical pixel size units for DICOM
    - NDPI and Zeiss LSM files larger than 4GB
    - Z and T dimensions for InCell 6000 plates
    - Export of RGB images in ImageJ
* Improved metadata saving in MATLAB functions

5.0.2 (2014 May 28)
-------------------

* Many bug fixes for Zeiss .czi files
* Several other bug fixes, including:
    - Gatan .dm3 units and step count parsing
    - Imspector .msr 5D image support
    - DICOM reading of nested tags
* Update native-lib-loader version (to 2.0.1)
* Updates and improvements to user documentation

5.0.1 (2014 Apr 7)
------------------

* Added image pyramid support for CellSens .vsi data
* Several bug fixes, including:
    - Woolz import into OMERO
    - Cellomics file name parsing (thanks to Lee Kamentsky)
    - Olympus FV1000 timestamp support (thanks to Lewis Kraft and Patrick Riley)
    - (A)PNG large image support
    - Zeiss .czi dimension detection for SPIM datasets
* Performance improvements for Becker & Hickl .sdt file reading
  (thanks to Ian Munro)
* Performance improvements to directory listing over NFS
* Update slf4j and logback versions (to 1.7.6 and 1.1.1 respectively)
* Update jgoodies-forms version (to 1.7.2)

5.0.0 (2014 Feb 25)
-------------------

* New bundled 'bioformats_package.jar' for ImageJ
* Now uses logback as the slf4j binding by default
* Updated component names, .jar file names, and Maven artifact names
* Fixed support for Becker & Hickl .sdt files with multiple blocks
* Fixed tiling support for TIFF, Hamamatsu .ndpi, JPEG, and Zeiss .czi files
* Improved continuous integration testing
* Updated :doc:`command line documentation </users/comlinetools/index>`

5.0.0-RC1 (2013 Dec 19)
-----------------------

* Updated Maven build system and launched new Artifactory repository
  (https://artifacts.openmicroscopy.org)
* Added support for:
   - :doc:`Bio-Rad SCN </formats/bio-rad-scn>`
   - :doc:`Yokogawa CellVoyager </formats/cellvoyager>` (thanks to
     Jean-Yves Tinevez)
   - :doc:`LaVision Imspector </formats/lavision-imspector>`
   - :doc:`PCORAW </formats/pcoraw>`
   - Woolz (thanks to Bill Hill)
* Added support for populating and parsing ModuloAlong{Z, C, T} annotations
  for FLIM/SPIM data
* Updated netCDF and slf4j version requirements - netCDF 4.3.19 and
  slf4j 1.7.2 are now required
* Updated and improved :doc:`MATLAB users </users/matlab/index>` and
  :doc:`developers </developers/matlab-dev>` documentation
* Many bug fixes including for Nikon ND2, Zeiss CZI, and CellWorX formats

5.0.0-beta1 (2013 June 20)
--------------------------

* Updated to :model_doc:`2013-06 OME-XML schema <>`
* Improved the performance in tiled formats
* Added caching of Reader metadata using
  https://github.com/EsotericSoftware/kryo
* Added support for:
   - :doc:`Aperio AFI </formats/aperio-afi>`
   - :doc:`Inveon </formats/inveon>`
   - :doc:`MPI-BPC Imspector </formats/imspector-obf>`
* Many bug fixes, including:
   - Add ZEN 2012/Lightsheet support to Zeiss CZI
   - Improved testing of autogenerated code
   - Moved OME-XML specification into Bio-Formats repository

4.4.10 (2014 Jan 15)
--------------------

* Bug fixes including CellWorx, Metamorph and Zeiss CZI
* Updates to MATLAB documentation

4.4.9 (2013 Oct 16)
-------------------

* Many bug fixes including improvements to support for ND2 format
* Java 1.6 is now the minimum supported version; Java 1.5 is no longer 
  supported

4.4.8 (2013 May 2)
------------------

* No changes - release to keep version numbers in sync with OMERO

4.4.7 (2013 April 25)
---------------------

* Many bug fixes to improve support for more than 20 formats
* Improved export to multi-file datasets
* Now uses slf4j for logging rather than using log4j directly, enabling other 
  logging implementations to be used, for example when Bio-Formats is used as 
  a component in other software using a different logging system.

4.4.6 (2013 February 11)
------------------------

* Many bug fixes
* Further documentation improvements

4.4.5 (2012 November 13)
------------------------

* Restructured and improved documentation
* Many bug fixes, including:
   - File grouping in many multi-file formats
   - Maven build fixes
   - ITK plugin fixes

4.4.4 (2012 September 24)
-------------------------

* Many bug fixes

4.4.2 (2012 August 22)
----------------------

* Security fix for OMERO plugins for ImageJ

4.4.1 (2012 July 20)
--------------------

* Fix a bug that prevented BigTIFF files from being read
* Fix a bug that prevented PerkinElmer .flex files from importing into OMERO

4.4.0 (2012 July 13)
--------------------

* Many, many bug fixes
* Added support for:
   - .nd2 files from Nikon Elements version 4
   - PerkinElmer Operetta data
   - MJPEG-compressed AVIs
   -  MicroManager datasets with multiple positions
   - Zeiss CZI data
   - IMOD data

4.3.3 (2011 October 18)
-----------------------

* Many bug fixes, including:
   - Speed improvements to HCImage/SimplePCI and Zeiss ZVI files
   - Reduce memory required by Leica LIF reader
   - More accurately populate metadata for Prairie TIFF datasets
   - Various fixes to improve the security of the OMERO plugin for ImageJ
   - Better dimension detection for Bruker MRI datasets
   - Better thumbnail generation for histology (SVS, NDPI) datasets
   - Fix stage position parsing for Metamorph TIFF datasets
   - Correctly populate the channel name for PerkinElmer Flex files

4.3.2 (2011 September 15)
-------------------------

* Many bug fixes, including:
   - Better support for Volocity datasets that contain compressed data
   - More accurate parsing of ICS metadata
   - More accurate parsing of cellSens .vsi files
* Added support for a few new formats
   - .inr
   - Canon DNG
   - Hitachi S-4800
   - Kodak .bip
   - JPX
   - Volocity Library Clipping (.acff)
   - Bruker MRI
* Updated Zeiss LSM reader to parse application tags
* Various performance improvements, particularly for reading/writing TIFFs
* Updated OMERO ImageJ plugin to work with OMERO 4.3.x

4.3.1 (2011 July 8)
-------------------

* Several bug fixes, including:
   - Fixes for multi-position DeltaVision files
   - Fixes for MicroManager 1.4 data
   - Fixes for 12 and 14-bit JPEG-2000 data
   - Various fixes for reading Volocity .mvd2 datasets
* Added various options to the 'showinf' and 'bfconvert' command line tools
* Added better tests for OME-XML backwards compatibility
* Added the ability to roughly stitch tiles in a multi-position dataset

4.3.0 (2011 June 14)
--------------------

* Many bug fixes, including:
   - Many fixes for reading and writing sub-images
   - Fixes for stage position parsing in the Zeiss formats
   - File type detection fixes
* Updated JPEG-2000 reading and writing support to be more flexible
* Added support for 9 new formats:
   - InCell 3000
   - Trestle
   - Hamamatsu .ndpi
   - Hamamatsu VMS
   - SPIDER
   - Volocity .mvd2
   - Olympus SIS TIFF
   - IMAGIC
   - cellSens VSI
* Updated to 2011-06 OME-XML schema
* Minor speed improvements in many formats
* Switched version control system from SVN to Git
* Moved all Trac tickets into the OME Trac: https://trac.openmicroscopy.org
* Improvements to testing frameworks
* Added Maven build system as an alternative to the existing Ant build system
* Added pre-compiled C++ bindings to the download page

4.2.2 (2010 December 6)
-----------------------

* Several bug fixes, notably:
   - Metadata parsing fixes for Zeiss LSM, Metamorph STK, and FV1000
   - Prevented leaked file handles when exporting to TIFF/OME-TIFF
   - Fixed how BufferedImages are converted to byte arrays
* Proper support for OME-XML XML annotations
* Added support for SCANCO Medical .aim files
* Minor improvements to ImageJ plugins
* Added support for reading JPEG-compressed AVI files

4.2.1 (2010 November 12)
------------------------

* Many, many bug fixes
* Added support for 7 new formats:
   - CellWorX .pnl
   - ECAT7
   - Varian FDF
   - Perkin Elmer Densitometer
   - FEI TIFF
   - Compix/SimplePCI TIFF
   - Nikon Elements TIFF
* Updated Zeiss LSM metadata parsing, with generous assistance from Zeiss, FMI, and MPI-CBG
* Lots of work to ensure that converted OME-XML validates
* Improved file stitching functionality; non-numerical file patterns and limited regular expression-style patterns are now supported

4.2.0 (2010 July 9)
-------------------

* Fixed many, many bugs in all aspects of Bio-Formats
* Reworked ImageJ plugins to be more user- and developer-friendly
* Added many new unit tests
* Added support for approximately 25 new file formats, primarily in the SPM domain
* Rewrote underlying I/O infrastructure to be thread-safe and based on Java NIO
* Rewrote OME-XML parsing/generation layer; OME-XML 2010-06 is now supported
* Improved support for exporting large images
* Improved support for exporting to multiple files
* Updated logging infrastructure to use slf4j and log4j

4.1.1 (2009 December 3)
-----------------------

* Fixed many bugs in popular file format readers

4.1 (2009 October 21):

* Fixed many bugs in most file format readers
* Significantly improved confocal and HCS metadata parsing
* Improved C++ bindings
* Eliminated references to Java AWT classes in core Bio-Formats packages
* Added support for reading Flex datasets from multiple servers
* Improved OME-XML generation; generated OME-XML is now valid
* Added support for Olympus ScanR data
* Added OSGi information to JARs
* Added support for Amira Mesh files
* Added support for LI-FLIM files
* Added more informative exceptions
* Added support for various types of ICS lifetime data
* Added support for Nikon EZ-C1 TIFFs
* Added support for Maia Scientific MIAS data

4.0.1 (2009 June 1)
-------------------

* Lots of bug fixes in most format readers and writers
* Added support for Analyze 7.1 files
* Added support for Nifti files
* Added support for Cellomics .c01 files
* Refactored ImageJ plugins
* Bio-Formats, the common package, and the ImageJ plugins now require Java 1.5
* Eliminated native library dependency for reading lossless JPEGs
* Changed license from GPL v3 or later to GPL v2 or later
* Updated Olympus FV1000, Zeiss LSM, Zeiss ZVI and Nikon ND2 readers to parse
  ROI data
* Added option to ImageJ plugin for displaying ROIs parsed from the chosen
  dataset
* Fixed BufferedImage construction for signed data and unsigned int data

4.0.0 (2009 March 3)
--------------------

* Improved OME data model population for Olympus FV1000, Nikon ND2, Metamorph
  STK, Leica LEI, Leica LIF, InCell 1000 and MicroManager
* Added TestNG tests for format writers
* Added option to ImageJ plugin to specify custom colors when customizing
  channels
* Added ability to upgrade the ImageJ plugin from within ImageJ
* Fixed bugs in Nikon ND2, Leica LIF, BioRad PIC, TIFF, PSD, and OME-TIFF
* Fixed bugs in Data Browser and Exporter plugins
* Added support for Axon Raw Format (ARF), courtesy of Johannes Schindelin
* Added preliminary support for IPLab-Mac file format

2008 December 29
----------------

* Improved metadata support for DeltaVision, Zeiss LSM, MicroManager, and Leica
  LEI
* Restructured code base/build system to be component-driven
* Added support for JPEG and JPEG-2000 codecs within TIFF, OME-TIFF and OME-XML
* Added support for 16-bit compressed Flex files
* Added support for writing JPEG-2000 files
* Added support for Minolta MRW format
* Added support for the 2008-09 release of OME-XML
* Removed dependency on JMagick
* Re-added caching support to data browser plugin
* Updated loci.formats.Codec API to be more user-friendly
* Expanded loci.formats.MetadataStore API to better represent the OME-XML model
* Improved support for Nikon NEF
* Improved support for TillVision files
* Improved ImageJ import options dialog
* Fixed bugs with Zeiss LSM files larger than 4 GB
* Fixed minor bugs in most readers
* Fixed bugs with exporting from an Image5D window
* Fixed several problems with virtual stacks in ImageJ

2008 August 30
--------------

* Fixed bugs in many file format readers
* Fixed several bugs with swapping dimensions
* Added support for Olympus CellR/APL files
* Added support for MINC MRI files
* Added support for Aperio SVS files compressed with JPEG 2000
* Added support for writing OME-XML files
* Added support for writing APNG files
* Added faster LZW codec
* Added drag and drop support to ImageJ shortcut window
* Re-integrated caching into the data browser plugin

2008 July 1
-----------

* Fixed bugs in most file format readers
* Fixed bugs in OME and OMERO download functionality
* Fixed bugs in OME server-side import
* Improved metadata storage/retrieval when uploading to and downloading from
  the OME Perl server
* Improved Bio-Formats ImageJ macro extensions
* Major updates to MetadataStore API
* Updated OME-XML generation to use 2008-02 schema by default
* Addressed time and memory performance issues in many readers
* Changed license from LGPL to GPL
* Added support for the FEI file format
* Added support for uncompressed Hamamatsu Aquacosmos NAF files
* Added support for Animated PNG files
* Added several new options to Bio-Formats ImageJ plugin
* Added support for writing ICS files

2008 April 17
-------------

* Fixed bugs in Slidebook, ND2, FV1000 OIB/OIF, Perkin Elmer, TIFF, Prairie,
  Openlab, Zeiss LSM, MNG, Molecular Dynamics GEL, and OME-TIFF
* Fixed bugs in OME and OMERO download functionality
* Fixed bugs in OME server-side import
* Fixed bugs in Data Browser
* Added support for downloading from OMERO 2.3 servers
* Added configuration plugin
* Updates to MetadataStore API
* Updates to OME-XML generation - 2007-06 schema used by default
* Added support for Li-Cor L2D format
* Major updates to TestNG testing framework
* Added support for writing multi-series OME-TIFF files
* Added support for writing BigTIFF files

2008 Feb 12
-----------

* Fixed bugs in QuickTime, SimplePCI and DICOM
* Fixed a bug in channel splitting logic

2008 Feb 8
----------

* Many critical bugfixes in format readers and ImageJ plugins
* Newly reborn Data Browser for 5D image visualization
    + some combinations of import options do not work yet

2008 Feb 1
----------

* Fixed bugs in Zeiss LSM, Metamorph STK, FV1000 OIB/OIF, Leica LEI, TIFF,
  Zeiss ZVI, ICS, Prairie, Openlab LIFF, Gatan, DICOM, QuickTime
* Fixed bug in OME-TIFF writer
* Major changes to MetadataStore API
* Added support for JPEG-compressed TIFF files
* Added basic support for Aperio SVS files
    + JPEG2000 compression is still not supported
* Improved "crop on import" functionality
* Improvements to bfconvert and bfview
* Improved OME-XML population for several formats
* Added support for JPEG2000-compressed DICOM files
* EXIF data is now parsed from TIFF files

2007 Dec 28
-----------

* Fixed bugs in Leica LEI, Leica TCS, SDT, Leica LIF,
  Visitech, DICOM, Imaris 5.5 (HDF), and Slidebook readers
* Better parsing of comments in TIFF files exported from ImageJ
* Fixed problem with exporting 48-bit RGB data
* Added logic to read multi-series datasets spread across multiple files
* Improved channel merging in ImageJ - requires ImageJ 1.39l
* Support for hyperstacks and virtual stacks in ImageJ - requires ImageJ 1.39l
* Added API for reading directly from a byte array or InputStream
* Metadata key/value pairs are now stored in ImageJ's "Info" property
* Improved OMERO download plugin - it is now much faster
* Added "open all series" option to ImageJ importer
* ND2 reader based on Nikon's SDK now uses our own native bindings
* Fixed metadata saving bug in ImageJ
* Added sub-channel labels to ImageJ windows
* Major updates to 4D Data Browser
* Minor updates to automated testing suite

2007 Dec 1
----------

* Updated OME plugin for ImageJ to support downloading from OMERO
* Fixed bug with floating point TIFFs
* Fixed bugs in Visitech, Zeiss LSM, Imaris 5.5 (HDF)
* Added alternate ND2 reader that uses Nikon's native libraries
* Fixed calibration and series name settings in importer
* Added basic support for InCell 1000 datasets

2007 Nov 21
-----------

* Fixed bugs in ND2, Leica LIF, DICOM, Zeiss ZVI, Zeiss LSM, FV1000 OIB,
  FV1000 OIF, BMP, Evotec Flex, BioRad PIC, Slidebook, TIFF
* Added new ImageJ plugins to slice stacks and do "smart" RGB merging
* Added "windowless" importer plugin
    + uses import parameters from IJ_Prefs.txt, without prompting the user
* Improved stack slicing and colorizing logic in importer plugin
* Added support for DICOM files compressed with lossless JPEG
    + requires native libraries
* Fixed bugs with signed pixel data
* Added support for Imaris 5.5 (HDF) files
* Added 4 channel merging to importer plugin
* Added API methods for reading subimages
* Major updates to the 4D Data Browser

2007 Oct 17
-----------

* Critical OME-TIFF bugfixes
* Fixed bugs in Leica LIF, Zeiss ZVI, TIFF, DICOM, and AVI readers
* Added support for JPEG-compressed ZVI images
* Added support for BigTIFF
* Added importer plugin option to open each plane in a new window
* Added MS Video 1 codec for AVI

2007 Oct 1
----------

* Added support for compressed DICOM images
* Added support for uncompressed LIM files
* Added support for Adobe Photoshop PSD files
* Fixed bugs in DICOM, OME-TIFF, Leica LIF, Zeiss ZVI,
  Visitech, PerkinElmer and Metamorph
* Improved indexed color support
* Addressed several efficiency issues
* Fixed how multiple series are handled in 4D data browser
* Added option to reorder stacks in importer plugin
* Added option to turn off autoscaling in importer plugin
* Additional metadata convenience methods

2007 Sept 11
------------

* Major improvements to ND2 support; lossless compression now supported
* Support for indexed color images
* Added support for Simple-PCI .cxd files
* Command-line OME-XML validation
* Bugfixes in most readers, especially Zeiss ZVI, Metamorph, PerkinElmer and
  Leica LEI
* Initial version of Bio-Formats macro extensions for ImageJ

2007 Aug 1
----------

* Added support for latest version of Leica LIF
* Fixed several issues with Leica LIF, Zeiss ZVI
* Better metadata mapping for Zeiss ZVI
* Added OME-TIFF writer
* Added MetadataRetrieve API for retrieving data from a MetadataStore
* Miscellaneous bugfixes

2007 July 16
------------

* Fixed several issues with ImageJ plugins
* Better support for Improvision and Leica TCS TIFF files
* Minor improvements to Leica LIF, ICS, QuickTime and Zeiss ZVI readers
* Added searchable metadata window to ImageJ importer

2007 July 2
-----------

* Fixed issues with ND2, Openlab LIFF and Slidebook
* Added support for Visitech XYS
* Added composite stack support to ImageJ importer

2007 June 18
------------

* Fixed issues with ICS, ND2, MicroManager, Leica LEI, and FV1000 OIF
* Added support for large (> 2 GB) ND2 files
* Added support for new version of ND2
* Minor enhancements to ImageJ importer
* Implemented more flexible logging
* Updated automated testing framework to use TestNG
* Added package for caching images produced by Bio-Formats

2007 June 6
-----------

* Fixed OME upload/download bugs
* Fixed issues with ND2, EPS, Leica LIF, and OIF
* Added support for Khoros XV
* Minor improvements to the importer

2007 May 24
-----------

* Better Slidebook support
* Added support for Quicktime RPZA
* Better Leica LIF metadata parsing
* Added support for BioRad PIC companion files
* Added support for bzip2-compressed files
* Improved ImageJ plugins
* Native support for FITS and PGM

2007 May 2
----------

* Added support for NRRD
* Added support for Evotec Flex (requires LuraWave Java SDK with license code)
* Added support for gzip-compressed files
* Added support for compressed QuickTime headers
* Fixed QuickTime Motion JPEG-B support
* Fixed some memory issues (repeated small array allocations)
* Fixed issues reading large (> 2 GB) files
* Removed "ignore color table" logic, and replaced with Leica-specific solution
* Added status event reporting to readers
* Added API to toggle metadata collection
* Support for multiple dimensions rasterized into channels
* Deprecated reader and writer methods that accept the 'id' parameter
* Deprecated IFormatWriter.save in favor of saveImage and saveBytes
* Moved dimension swapping and min/max calculation logic to delegates
* Separate GUI logic into isolated loci.formats.gui package
* Miscellaneous bugfixes and tweaks in most readers and writers
* Many other bugfixes and improvements

2007 Mar 16
-----------

* Fixed calibration bugs in importer plugin
* Enhanced metadata support for additional formats
* Fixed LSM bug

2007 Mar 7
----------

* Added support for Micro-Manager file format
* Fixed several bugs -- Leica LIF, Leica LEI, ICS, ND2, and others
* Enhanced metadata support for several formats
* Load series preview thumbnails in the background
* Better implementation of openBytes(String, int, byte[]) for most readers
* Expanded unit testing framework

2007 Feb 28
-----------

* Better series preview thumbnails
* Fixed bugs with multi-channel Leica LEI
* Fixed bugs with "ignore color tables" option in ImageJ plugin

2007 Feb 26
-----------

* Many bugfixes: Leica LEI, ICS, FV1000 OIB, OME-XML and others
* Better metadata parsing for BioRad PIC files
* Enhanced API for calculating channel minimum and maximum values
* Expanded MetadataStore API to include more semantic types
* Added thumbnails to series chooser in ImageJ plugin
* Fixed plugins that upload and download from an OME server

2007 Feb 7
----------

* Added plugin for downloading images from OME server
* Improved HTTP import functionality
* Added metadata filtering -- unreadable metadata is no longer shown
* Better metadata table for multi-series datasets
* Added support for calibration information in Gatan DM3
* Eliminated need to install JAI Image I/O Tools to read ND2 files
* Fixed ZVI bugs: metadata truncation, and other problems
* Fixed bugs in Leica LIF: incorrect calibration, first series labeling
* Fixed memory bug in Zeiss LSM
* Many bugfixes: PerkinElmer, DeltaVision, Leica LEI, LSM, ND2, and others
* IFormatReader.close(boolean) method to close files temporarily
* Replaced Compression utility class with extensible Compressor interface
* Improved testing framework to use .bioformats configuration files

2007 Jan 5
----------

* Added support for Prairie TIFF
* Fixed bugs in Zeiss LSM, OIB, OIF, and ND2
* Improved API for writing files
* Added feature to read files over HTTP
* Fixed bugs in automated testing framework
* Miscellaneous bugfixes

2006 Dec 22
-----------

* Expanded ImageJ plugin to optionally use Image5D or View5D
* Improved support for ND2 and JPEG-2000 files
* Added automated testing framework
* Fixed bugs in Zeiss ZVI reader
* Miscellaneous bugfixes

2006 Nov 30
-----------

* Added support for ND2/JPEG-2000
* Added support for MRC
* Added support for MNG
* Improved support for floating-point images
* Fixed problem with 2-channel Leica LIF data
* Minor tweaks and bugfixes in many readers
* Improved file stitching logic
* Allow ImageJ plugin to be called from a macro

2006 Nov 2
----------

* Bugfixes and improvements for Leica LIF, Zeiss LSM, OIF and OIB
* Colorize channels when they are split into separate windows
* Fixed a bug with 4-channel datasets

2006 Oct 31
-----------

* Added support for Imaris 5 files
* Added support for RGB ICS images

2006 Oct 30
-----------

* Added support for tiled TIFFs
* Fixed bugs in ICS reader
* Fixed importer plugin deadlock on some systems

2006 Oct 27
-----------

* Multi-series support for Slidebook
* Added support for Alicona AL3D
* Fixed plane ordering issue with FV1000 OIB
* Enhanced dimension detection in FV1000 OIF
* Added preliminary support for reading NEF images
* Added option to ignore color tables
* Fixed ImageJ GUI problems
* Fixed spatial calibration problem in ImageJ
* Fixed some lingering bugs in Zeiss ZVI support
* Fixed bugs in OME-XML reader
* Tweaked ICS floating-point logic
* Fixed memory leaks in all readers
* Better file stitching logic

2006 Oct 6
----------

* Support for 3i SlideBook format (single series only for now)
* Support for 16-bit RGB palette TIFF
* Fixed bug preventing import of certain Metamorph STK files
* Fixed some bugs in PerkinElmer UltraView support
* Fixed some bugs in Leica LEI support
* Fixed a bug in Zeiss ZVI support
* Fixed bugs in Zeiss LSM support
* Fixed a bug causing slow identification of Leica datasets
* Fixed bugs in the channel merging logic
* Fixed memory leak for OIB format
* Better scaling of 48-bit RGB data to 24-bit RGB
* Fixed duplicate channels bug in "open each channel in a separate window"
* Fixed a bug preventing PICT import into ImageJ
* Better integration with HandleExtraFileTypes
* Better virtual stack support in Data Browser plugin
* Fixed bug in native QuickTime random access
* Keep aspect ratio for computed thumbnails
* Much faster file stitching logic

2006 Sep 27
-----------

* PerkinElmer: support for PE UltraView
* Openlab LIFF: support for Openlab v5
* Leica LEI: bugfixes, and support for multiple series
* ZVI, OIB, IPW: more robust handling of these formats (eliminated
  custom OLE parsing logic in favor of Apache POI)
* OIB: better metadata parsing (but maybe still not perfect?)
* LSM: fixed a bug preventing import of certain LSMs
* Metamorph STK: fixed a bug resulting in duplicate image planes
* User interface: use of system look & feel for file chooser dialog
  when available
* Better notification when JAR libraries are missing

2006 Sep 6
----------

* Leica LIF: multiple distinct image series within a single file
* Zeiss ZVI: fixes and improvements contributed by Michel Boudinot
* Zeiss LSM: fixed bugs preventing the import of certain LSM files
* TIFF: fixed a bug preventing import of TIFFs created with Bio-Rad software

2006 Mar 31
-----------

* First release
