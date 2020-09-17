Managing memory in ImageJ/Fiji using Bio-Formats
================================================

When dealing with a large stack of images, you may receive a
warning like this:

.. image:: /images/memory_warning.jpg
   :align: center
   :alt: Memory warning

This means the allotted memory is less than what Bio-Formats needs to
load all the images. If you have a very large data set, you may have to:

-  Crop the view area
-  Open only a subset of images
-  Use Virtual Stack
-  Increase ImageJ/Fiji’s memory.


If your files contain JPEG or JPEG-2000 images, you may see this memory
warning even if your file size is smaller than the amount of allocated
memory. This is because compressed images like JPEG need to be
decompressed into memory before being displayed and require more memory
than their file size suggests. If you are having this issue, try
utilizing one of the memory management tools below.

Cropping the view area
----------------------

**Crop on Import** is useful if your images are very large and you are
only interested in one specific section of the stack you are importing.
If you select this feature, you will see a screen where you can enter
the height and width (in pixels) of the part of image you want to see.
Note that these measurements are from the top left corner of the image.

Opening only a subset of images
-------------------------------

The **Specify Range for Each Series** option is useful for viewing a
portion of a data set where all the plane images are encapsulated into
one file (e.g. the Zeiss LSM format). If your file has a large quantity
of images, you can specify which channels, Z-planes, and times you want
to load.

Use Virtual Stack
-----------------

**Virtual Stack** conserves memory by not loading specific images until
necessary. Virtual Stack does not contain a buffer and may produce
choppy animations.

Increasing ImageJ/Fiji’s memory
-------------------------------

Finally, you can also increase the amount of the computer memory devoted to
ImageJ/Fiji by selecting **Memory & Threads** under the **Edit** menu.

.. image:: /images/IncreaseMemory.jpg
   :align: center
   :alt: Fiji's Memory Allocation Menu

Generally, allocating more than 75% of the computer’s total memory will
cause ImageJ/Fiji to become slow and unstable.

**Please note** that, unlike the other two features, ImageJ/Fiji itself
provides this feature and not Bio-Formats. You can find out more about
this feature by looking at ImageJ’s
`documentation <https://imagej.nih.gov/ij/docs/menus/edit.html#options>`_.
