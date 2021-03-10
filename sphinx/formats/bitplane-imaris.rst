.. index:: Bitplane Imaris
.. index:: .ims

Bitplane Imaris
===============================================================================

Extensions: .ims


Owner: `Oxford Instruments <https://imaris.oxinst.com/>`_ (formerly Bitplane)

**Support**


BSD-licensed: |no|

Export: |no|

Officially Supported Versions: 2.7, 3.0, 5.5

Readers:

- ImarisHDFReader (:bfreader:`Source Code <ImarisHDFReader.java>`, :doc:`Supported Metadata Fields </metadata/ImarisHDFReader>`)
- ImarisTiffReader (:bfreader:`Source Code <ImarisTiffReader.java>`, :doc:`Supported Metadata Fields </metadata/ImarisTiffReader>`)
- ImarisReader (:bfreader:`Source Code <ImarisReader.java>`, :doc:`Supported Metadata Fields </metadata/ImarisReader>`)




We currently have:

* an Imaris (RAW) specification document (from no later than 1997 November 11, in HTML) 
* an Imaris 5.5 (HDF) specification document 
* Bitplane's bfFileReaderImaris3N code (from no later than 2005, in C++) 
* several older Imaris (RAW) datasets 
* one Imaris 3 (TIFF) dataset 
* several Imaris 5.5 (HDF) datasets
* `public sample images <https://downloads.openmicroscopy.org/images/Imaris-IMS/>`__

We would like to have:

* an Imaris 3 (TIFF) specification document 
* more Imaris 3 (TIFF) datasets

**Ratings**


Pixels: |Very good|

Metadata: |Very good|

Openness: |Very good|

Presence: |Fair|

Utility: |Fair|

**Additional Information**


- There are three distinct Imaris formats: 
    #. the old binary format (introduced in Imaris version 2.7) 
    #. Imaris 3, a TIFF variant (introduced in Imaris version 3.0) 
    #. Imaris 5.5, an HDF variant (introduced in Imaris version 5.5)
