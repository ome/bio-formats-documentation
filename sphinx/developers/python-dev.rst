Using Bio-Formats in Python
===========================

OME does not currently provide a Python implementation for Bio-Formats.
However, there are several options you can use to read images from Python via Bio-Formats:

AICSImageIO
-----------

The `AICSImageIO <https://allencellmodeling.github.io/aicsimageio/>`_ project
includes support for Bio-Formats:

.. code-block:: python

    from aicsimageio import AICSImage
    cells = AICSImage('/path/to/my/cells.ome.tif')

    import napari
    napari.view_image(cells.xarray_data)
    napari.run()

PyImageJ
--------

The `PyImageJ <https://pypi.org/project/pyimagej>`_ project enables use of
`ImageJ2 <https://imagej.net/software/imagej2>`_, which includes the
`SCIFIO <https://imagej.net/libs/scifio>`_ library, which wraps Bio-Formats.
In this way, you can open Bio-Formats-supported formats as NumPy arrays:

.. code-block:: python

    import imagej
    ij = imagej.init('sc.fiji:fiji')
    jcells = ij.io().open('/path/to/my/cells.ome.tif')
    cells = ij.py.from_java(jcells)

    import napari
    napari.view_image(cells)
    napari.run()

python-bioformats
-----------------

The :doc:`/users/cellprofiler/index` project has implemented a Python wrapper 
around Bio-Formats used by the CellProfiler software which can be installed 
using `pip`::

  pip install python-bioformats

.. seealso::
   https://pypi.org/project/python-bioformats
      Source code of the CellProfiler Python wrapper for Bio-Formats
