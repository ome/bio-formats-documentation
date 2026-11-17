Working with axis orientation metadata
======================================

Bio-Formats 9.0.0 introduces API to report axis orientation metadata, specifically anatomical orientations compliant with `NGFF RFC 4 <https://ngff.openmicroscopy.org/rfc/4>`_.
Future versions may expand upon this concept for non-anatomical orientations.

Any reader which chooses to report axis metadata does so by implementing the `IAxisOrientationReader` interface.
This interface contains a single method (`getAxisOrientations()`) which returns an array of `Orientation` objects, one per axis.
In most cases, the array length is 5; a longer length is possible if modulo axes are defined. The array order in all cases matches the dimension order
reported by `getDimensionOrder()` in `IFormatReader`.

An `Orientation` object contains both a type (`OrientationType`) and term (`OrientationTerm`).
`OrientationType` is an enum, which currently contains a single value (`ANATOMICAL`).
`OrientationTerm` is an interface, the only implementing class of which `AnatomicalOrientation`.
`AnatomicalOrientation` is also an enum, which encapsulates the vocabulary described in `NGFF RFC 4 <https://ngff.openmicroscopy.org/rfc/4/#controlled-vocabulary>`_.

Applications wishing to consume axis orientation metadata can check if the base reader used to open a particular file implements `IAxisOrientationReader`.
Note that `ImageReader` does not implement this interface, and so must be unwrapped first.

Formats which support axis orientation metadata are:

- :doc:`/formats/dicom`
- :doc:`/formats/analyze-75`
- :doc:`/formats/bruker-mri`
- :doc:`/formats/inveon`
- :doc:`/formats/minc-mri`
- :doc:`/formats/nifti`
- :doc:`/formats/varian-fdf`
- :doc:`/developers/generating-test-images`
