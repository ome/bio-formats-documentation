Using Bio-Formats as a Java library
===================================

Bio-Formats as a Maven, Gradle or Ivy dependency
------------------------------------------------

All released :file:`.jar` artifacts are published to and can be obtained from
the `OME Artifactory <http://artifacts.openmicroscopy.org/artifactory>`_.  The
"Client Settings" section of the Artifactory main page provides example code
snippets for inclusion into your Gradle, Maven or Ivy project, which will
enable the use of this repository.

.. versionchanged:: 6.12.0
As of Bio-Formats 6.12.0 consumers will have to directly declare a dependency for 
their chosen SLF4J logging framework. See :doc:`logging` for further details. 

Examples of getting started with Bio-Formats using Maven or Gradle are given
in the https://github.com/ome/bio-formats-examples repository.
`OMERO <https://github.com/ome/openmicroscopy>`_ uses Ivy to manage
its Java dependencies including Bio-Formats.

.. note::
  In order to retrieve the NetCDF dependency of Bio-Formats, it is necessary
  to configure the Unidata releases repository in addition to Maven Central and
  the OME artifactory in your :examples:`pom.xml`, :examples:`build.gradle` or
  :file:`ivy.xml` file.

Bio-Formats as a Java library
-----------------------------

Alternatively Bio-Formats can be used by including its component jar files.
You can :downloads:`download formats-gpl.jar <artifacts/formats-gpl.jar>` to
use it as a library. Just add :file:`formats-gpl.jar` to your :envvar:`CLASSPATH` or
build path. You will also need :file:`ome-common.jar` for common I/O functions,
:file:`ome-xml.jar` for metadata standardization, and a
`SLF4J <http://www.slf4j.org/>`_ binding for :doc:`logging`.

Dependencies
^^^^^^^^^^^^

The complete list of third-party dependencies for `formats-gpl.jar` is as follows:

.. list-table::
    :header-rows: 1

    * - Package
      - Maven name
      - License
    * - `JHDF5 v19.04.0 <https://unlimited.ethz.ch/display/JHDF/>`_
      - cisd:jhdf5:19.04.0
      - `Apache License v2.0`_
    * - `cisd base v18.09.0 <https://sissource.ethz.ch/sispub/base/>`_
      - cisd:base:18.09.0
      - `Apache License v2.0`_
    * - `commons-io v2.7 <https://commons.apache.org/proper/commons-io/>`_
      - commons-io:commons-io:2.7
      - `Apache License v2.0`_
    * - `commons-lang3 v3.10 <https://commons.apache.org/proper/commons-lang/>`_
      - org.apache.commons:commons-lang3:3.10
      - `Apache License v2.0`_
    * - `XMP Library for Java v6.1.11 <https://www.adobe.com/devnet/xmp.html>`_
      - com.adobe.xmp:xmpcore:6.1.11
      - `BSD License`_
    * - `JCommander v1.27 <http://jcommander.org/>`_
      - com.beust:jcommander:1.27
      - `Apache License v2.0`_
    * - `metadata-extractor v2.18.0 <https://github.com/drewnoakes/metadata-extractor>`_
      - com.drewnoakes:metadata-extractor:2.18.0
      - `Apache License v2.0`_
    * - `aircompressor v0.21 <https://github.com/airlift/aircompressor>`_
      - io.airlift:aircompressor:0.21
      - `Apache License v2.0`_
    * - `Kryo v4.0.2 <https://github.com/EsotericSoftware/kryo>`_
      - com.esotericsoftware.kryo:kryo:4.0.2
      - `BSD License`_
    * - `reflectasm v1.11.3 <https://github.com/EsotericSoftware/reflectasm>`_
      - com.esotericsoftware:reflectasm:1.11.3
      - `BSD 3-Clause`_
    * - `asm v5.0.4 <https://asm.ow2.io>`_
      - org.ow2.asm:asm:5.0.4
      - `BSD 3-Clause`_
    * - `MinLog v1.3 <https://github.com/EsotericSoftware/minlog>`_
      - com.esotericsoftware.minlog:minlog:1.3
      - `BSD License`_
    * - `Guava v29.0 <https://github.com/google/guava>`_
      - com.google.guava:guava:29.0-jre
      - `Apache License v2.0`_
    * - `JGoodies Common v1.7.0 <http://www.jgoodies.com/downloads/libraries/>`_
      - com.jgoodies:jgoodies-common:1.7.0
      - `BSD License`_
    * - `JGoodies Forms v1.7.2 <http://www.jgoodies.com/downloads/libraries/>`_
      - com.jgoodies:jgoodies-forms:1.7.2
      - `BSD License`_
    * - `Commons Lang v2.6 <http://commons.apache.org/lang/>`_
      - commons-lang:commons-lang:2.6
      - `Apache License v2.0`_
    * - `Commons Logging v1.2 <http://commons.apache.org/logging/>`_
      - commons-logging:commons-logging:1.2
      - `Apache License v2.0`_
    * - `NetCDF-Java Library v5.3.3 <https://www.unidata.ucar.edu/software/netcdf-java/v5.3/documentation.htm>`_
      - edu.ucar:cdm:5.3.3
      - `MIT-Style License`_
    * - `Joda time v2.2 <https://github.com/JodaOrg/joda-time>`_
      - joda-time:joda-time:2.2
      - `Apache License v2.0`_
    * - `JUnit v4.10 <https://junit.org/junit4/>`_
      - junit:junit:4.10
      - `Common Public License v1.0`_
    * - `BeanShell v2.0b4 <http://www.beanshell.org>`_
      - org.beanshell:bsh:2.0b4
      - `Sun Public License / LGPL`_
    * - `Hamcrest Core v1.2.1 <https://github.com/hamcrest/JavaHamcrest>`_
      - org.hamcrest:hamcrest-core:1.2.1
      - `BSD 3-Clause`_
    * - `Objenesis v2.5.1 <http://objenesis.org>`_
      - org.objenesis:objenesis:2.5.1
      - `Apache License v2.0`_
    * - `Perf4J v0.9.16 <https://github.com/perf4j/perf4j>`_
      - org.perf4j:perf4j:0.9.16
      - `Apache License v2.0`_
    * - `Native Library Loader v2.1.4 <https://github.com/scijava/native-lib-loader>`_
      - org.scijava:native-lib-loader:2.1.4
      - `BSD License`_
    * - `SLF4J API v1.7.30 <http://www.slf4j.org>`_
      - org.slf4j:slf4j-api:1.7.30
      - `MIT License`_
    * - `TestNG v6.8 <https://testng.org/doc/>`_
      - org.testng:testng:6.8
      - `Apache License v2.0`_
    * - `SnakeYAML v1.32 <https://bitbucket.org/snakeyaml/snakeyaml>`_
      - org.yaml:snakeyaml:1.32
      - `Apache License v2.0`_
    * - `Woolz v1.4.0 <http://www.emouseatlas.org/emap/analysis_tools_resources/software/woolz.html>`_
      - woolz:JWlz:1.4.0
      - `GPL v2`_
    * - `Xalan Java Serializer v2.7.2 <http://xml.apache.org/xalan-j>`_
      - xalan:serializer:2.7.2
      - `Apache License v2.0`_
    * - `Xalan Java v2.7.2 <http://xml.apache.org/xalan-j>`_
      - xalan:xalan:2.7.2
      - `Apache License v2.0`_
    * - `Xerces2 Java Parser v2.12.2 <http://xerces.apache.org/xerces2-j>`_
      - xerces:xercesImpl:2.12.2
      - `Apache License v2.0`_
    * - `XML Commons External Components XML APIs v1.4.01 <http://xerces.apache.org/xml-commons/components/external/>`_
      - xml-apis:xml-apis:1.4.01
      - `Apache License v2.0`_
    * - `minio v5.0.2 <https://min.io>`_
      - io.minio:minio:5.0.2
      - `AGPL v3`_
    * - `http-client-xml v1.20.0 <http://googleapis.github.io/google-http-java-client>`_
      - com.google.http-client:google-http-client-xml:1.20.0
      - `Apache License v2.0`_
    * - `http-client v1.20.0 <http://googleapis.github.io/google-http-java-client>`_
      - com.google.http-client:google-http-client:1.20.0
      - `Apache License v2.0`_
    * - `xpp3 v1.1.4c <https://github.com/aslom/xpp3>`_
      - xpp3:xpp3:1.1.4c
      - https://github.com/aslom/xpp3/blob/master/LICENSE.txt
    * - `okhttp3 v3.7.0 <https://square.github.io/okhttp/>`_
      - com.squareup.okhttp3:okhttp:3.7.0
      - `Apache License v2.0`_
    * - `okio v1.12.0 <https://square.github.io/okio/>`_
      - com.squareup.okio:okio:1.12.0
      - `Apache License v2.0`_
    * - `jaxb v2.3.0 <https://javaee.github.io/jaxb-v2/>`_
      - javax.xml.bind:jaxb-api:2.3.0
      -
    * - `json v20090211 <https://github.com/stleary/json-java>`_
      - org.json:json:20090211
      - https://github.com/stleary/JSON-java/blob/master/LICENSE
    * - `sqlite v3.28.0 <https://github.com/xerial/sqlite-jdbc>`_
      - org.xerial:sqlite-jdbc:3.28.0
      - `Apache License v2.0`_
    * - `failureaccess v1.0.1 <https://github.com/google/guava>`_
      - com.google.guava:failureaccess:1.0.1
      - `Apache License v2.0`_
    * - `listenablefuture v9999.0 <https://github.com/google/guava>`_
      - com.google.guava:listenablefuture:9999.0-empty-to-avoid-conflict-with-guava
      - `Apache License v2.0`_
    * - `jsr305 v3.0.2 <https://github.com/findbugsproject/findbugs>`_
      - com.google.code.findbugs:jsr305:3.0.2
      - `BSD 3-Clause`_
    * - `checker-qual v2.11.1 <https://checkerframework.org/>`_
      - org.checkerframework:checker-qual:2.11.1
      - `GPL v2`_
    * - `errorprone v2.3.4 <https://errorprone.info/>`_
      - com.google.errorprone:error_prone_annotations:2.3.4
      - `Apache License v2.0`_
    * - `j2objc-annotations v1.3 <https://developers.google.com/j2objc/>`_
      - com.google.j2objc:j2objc-annotations:1.3
      - `Apache License v2.0`_
    * - `httpservices v5.3.3 <https://www.unidata.ucar.edu/software/netcdf-java/v4.6/reference/httpservices.html>`_
      - edu.ucar:httpservices:5.3.3
      - `MIT-Style License`_
    * - `httpclient v4.5.9 <https://hc.apache.org/>`_
      - org.apache.httpcomponents:httpclient:4.5.9
      - `Apache License v2.0`_
    * - `commons-codec v1.11 <https://commons.apache.org/proper/commons-codec/>`_
      - commons-codec:commons-codec:1.11
      - `Apache License v2.0`_
    * - `httpmime v4.5.9 <https://hc.apache.org/>`_
      - org.apache.httpcomponents:httpmime:4.5.9
      - `Apache License v2.0`_
    * - `c3p0 v0.9.5.3 <https://www.mchange.com/projects/c3p0/>`_
      - com.mchange:c3p0:0.9.5.3
      - `Eclipse Public License v1.0`_
    * - `mchange-commons-java v0.2.15 <https://www.mchange.com/projects/mchange-commons-java/>`_
      - com.mchange:mchange-commons-java:0.2.15
      -
    * - `jackson-core v2.14.1 <https://github.com/FasterXML/jackson-core>`_
      - com.fasterxml.jackson.core:jackson-core:2.14.1
      - `Apache License v2.0`_
    * - `jackson-annotations v12.14.1 <https://github.com/FasterXML/jackson-annotations>`_
      - com.fasterxml.jackson.core:jackson-annotations:12.14.1
      - `Apache License v2.0`_
    * - `jackson-databind v2.14.1 <https://github.com/FasterXML/jackson-databind>`_
      - com.fasterxml.jackson.core:jackson-databind:2.14.1
      - `Apache License v2.0`_

The below are optional dependencies :

.. list-table::
    :header-rows: 1

    * - Package
      - Maven name
      - License
    * - `Logback Classic v1.2.9 <https://logback.qos.ch>`_
      - ch.qos.logback:logback-classic:1.2.9
      - `Eclipse Public License v1.0`_
    * - `Logback Core v1.2.9 <https://logback.qos.ch>`_
      - ch.qos.logback:logback-core:1.2.9
      - `Eclipse Public License v1.0`_

As described in :ref:`versioning-policy`, the minor version number of a
Bio-Formats release will always be increased if the version of a
non-OME/external dependency is bumped.

Dependency lists for any component can be generated by checking out the
code as described in :ref:`source-code` and then running::

    cd components/$COMPONENT_NAME
    mvn dependency:tree

.. _Apache License v2.0: https://spdx.org/licenses/Apache-2.0.html
.. _MIT License: https://spdx.org/licenses/MIT.html
.. _BSD 3-Clause: https://spdx.org/licenses/BSD-3-Clause.html
.. _Sun Public License / LGPL: http://www.beanshell.org/license.html
.. _Common Public License v1.0: https://spdx.org/licenses/CPL-1.0.html
.. _MIT-Style License: https://github.com/Unidata/thredds/blob/v4.3.22/cdm/license.txt
.. _BSD License: https://spdx.org/licenses/BSD-2-Clause.html
.. _Eclipse Public License v1.0: https://spdx.org/licenses/EPL-1.0.html
.. _GPL v2: https://spdx.org/licenses/GPL-2.0.html
.. _AGPL v3: https://spdx.org/licenses/AGPL-3.0-only.html


Examples of usage
-----------------

File reading and performance:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:source:`MultiFileExample <components/formats-gpl/utils/MultiFileExample.java>` -
Simple example of how to open multiple files simultaneously.

:source:`ParallelRead <components/formats-gpl/utils/ParallelRead.java>` -
Reads all files in given directory in parallel, using a separate thread for each.

:doc:`ReadWriteInMemory <in-memory>` -
Tests the Bio-Formats I/O logic to and from byte arrays in memory.

:java_examples:`OrthogonalReader <OrthogonalReader.java>` -
Reads image data in XZ and YZ order.

File writing:
^^^^^^^^^^^^^

:source:`MinimumWriter <components/formats-gpl/utils/MinimumWriter.java>` -
A command line utility demonstrating the minimum amount of metadata needed to
write a file.

:java_examples:`FileExport <FileExport.java>` -
Write a file in any supported output format.

:source:`TiledExport <components/formats-gpl/utils/TiledExportExample.java>` -
Shows how to convert a file one tile at a time, instead of one plane at a time (needed for very large images).

:java_examples:`FileExportSPW <FileExportSPW.java>` -
Write a file with plate (OME SPW) metadata.

File compression:
^^^^^^^^^^^^^^^^^

:source:`makeLZW <components/formats-gpl/utils/MakeLZW.java>` -
Converts the given image file to an LZW-compressed TIFF.

Metadata extract/print:
^^^^^^^^^^^^^^^^^^^^^^^

:source:`GetPhysicalMetadata <components/formats-gpl/utils/GetPhysicalMetadata.java>` -
Uses Bio-Formats to extract some basic standardized (format-independent) metadata.

:java_examples:`ReadPhysicalSize <ReadPhysicalSize.java>` -
Reads physical size information uses the units API to display in micrometers.

:source:`ImageInfo <components/bio-formats-tools/src/loci/formats/tools/ImageInfo.java>` -
A more involved command line utility for thoroughly reading an input file,
printing some information about it, and displaying the pixels
onscreen using the Bio-Formats viewer.

:source:`PrintTimestamps <components/formats-gpl/utils/PrintTimestamps.java>` -
A command line example demonstrating how to extract timestamps from a file.

:source:`PrintLensNA <components/formats-gpl/utils/PrintLensNA.java>` -
Uses Bio-Formats to extract lens numerical aperture in a format-independent manner from a dataset.

:source:`PrintROIs <components/formats-gpl/utils/PrintROIs.java>` -
A simple example of how to retrieve ROI data parsed from a file.

:java_examples:`SubResolutionExample <SubResolutionExample.java>` -
Demonstration of the sub-resolution API.

Metadata add/edit:
^^^^^^^^^^^^^^^^^^

:source:`EditImageName <components/formats-gpl/utils/EditImageName.java>` -
Edits the given file's image name (but does not save back to disk).

:source:`EditTiffComment <components/formats-gpl/utils/EditTiffComment.java>` -
Allows raw user TIFF comment editing for the given TIFF files.

:source:`writeMapAnnotations <components/formats-gpl/utils/writeMapAnnotationsExample.java>` -
Example method to write MapAnnotations to the ome-xml.

:source:`CommentSurgery <components/formats-gpl/utils/CommentSurgery.java>` -
Edits a TIFF ImageDescription comment, particularly the OME-XML comment found in OME-TIFF files.

Image converters:
^^^^^^^^^^^^^^^^^

:source:`ImageConverter <components/bio-formats-tools/src/loci/formats/tools/ImageConverter.java>` -
A simple command line tool for converting between formats.

:java_examples:`FileConvert <FileConvert.java>` -
Converts a file in any supported format to any supported output format.

:source:`ConvertToOmeTiff <components/formats-gpl/utils/ConvertToOmeTiff.java>` -
Converts the given files to OME-TIFF format.

:source:`WritePreCompressedPlanes <components/formats-gpl/utils/WritePrecompressedPlanes.java>` -
Writes the pixels from a set of JPEG files to a single TIFF. The pixel data is used as-is, 
so no decompression or re-compression is performed.

:java_examples:`GeneratePyramidResolutions <GeneratePyramidResolutions.java>` -
Convert a file containing a single large image to a pyramid OME-TIFF.

:java_examples:`TiledReaderWriter <TiledReaderWriter.java>` -
Convert a file to OME-TIFF one tile at a time.

:java_examples:`OverlappedTiledWriter <OverlappedTiledWriter.java>` -
Convert a file to OME-TIFF one tile at a time, when the image size is not a multiple of the tile size.

:java_examples:`SimpleTiledWriter <SimpleTiledWriter.java>` -
Convert a file to OME-TIFF using automatic tiling.

ImageJ plugins:
^^^^^^^^^^^^^^^

:source:`Simple_Read <components/bio-formats-plugins/utils/Simple_Read.java>` -
A simple ImageJ plugin demonstrating how to use Bio-Formats to read files into
ImageJ (see :doc:`/users/imagej/index`).

:source:`Read_Image <components/bio-formats-plugins/utils/Read_Image.java>` -
An ImageJ plugin that uses Bio-Formats to build up an image stack, reading
image planes one by one (see :doc:`/users/imagej/index`).

:source:`Mass_Importer <components/bio-formats-plugins/utils/Mass_Importer.java>` -
A simple plugin for ImageJ that demonstrates how to open all image files in a
directory using Bio-Formats, grouping files with similar names to avoiding
opening the same dataset more than once (see :doc:`/users/imagej/index`).

Image processing utilities:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:source:`SewTiffs <components/formats-gpl/utils/SewTiffs.java>` -
Stitches the first plane from a collection of TIFFs into a single file.

:source:`SumPlanes <components/formats-gpl/utils/SumPlanes.java>` -
Sums together the image planes from the given file,and saves the result to a 16-bit TIFF.


A Note on Java Web Start (bioformats\_package.jar vs. formats-gpl.jar)
----------------------------------------------------------------------

To use Bio-Formats with your Java Web Start application, we recommend
using **formats-gpl.jar** rather than **bioformats\_package.jar**—the latter
is merely a bundle of **formats-gpl.jar** plus all its optional
dependencies.

The **bioformats\_package.jar** bundle is intended as a convenience (e.g. to
simplify installation as an ImageJ plugin), but is by no means the only
solution for developers. We recommend using **formats-gpl.jar** as a
separate entity depending on your needs as a developer.

The bundle is quite large because we have added support for several
formats that need large helper libraries (e.g. Imaris' HDF-based
format). However, these additional libraries are optional; Bio-Formats
has been coded using reflection so that it can both compile and run
without them.

When deploying a JNLP-based application, using **bioformats\_package.jar**
directly is not the best approach, since every time Bio-Formats is
updated, the server would need to feed another 15+ MB JAR file to the
client. Rather, Web Start is a case where you should keep the JARs
separate, since JNLP was designed to make management of JAR dependencies
trivial for the end user. By keeping **formats-gpl.jar** and the
optional dependencies separate, only a <1 MB JAR needs to be updated
when **formats-gpl.jar** changes.

As a developer, you have the option of packaging **formats-gpl.jar**
with as many or as few optional libraries as you wish, to cut down on
file size as needed. You are free to make whatever kind of "stripped
down" version you require. You could even build a custom
**formats-gpl.jar** that excludes certain classes, if you like.

