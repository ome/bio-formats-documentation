MATLAB
======

`MATLAB <https://www.mathworks.com/products/matlab.html>`_ is a high-level
language and interactive environment that facilitates rapid development
of algorithms for performing computationally intensive tasks.

Calling Bio-Formats from MATLAB is fairly straightforward, since MATLAB
has built-in interoperability with Java. We have created a
:sourcedir:`toolbox <components/formats-gpl/matlab>` for reading and writing
image files. Note the minimum recommended MATLAB version is R2017b.

.. note::

   It is possible to run Bio-Formats 6 on earlier MATLAB versions using a
   JVM version 8 or greater although using a different JVM than the one shipped
   with MATLAB can affect other functionalities. Please refer to the
   `MATLAB Answers <https://mathworks.com/matlabcentral/answers/index>`__
   for more information.

Installation
------------

Download the MATLAB toolbox from the Bio-Formats
:downloads:`downloads page <>`.
Unzip :file:`bfmatlab.zip` and add the unzipped :file:`bfmatlab` folder to
your MATLAB path.

Usage
-----

Please see :doc:`/developers/matlab-dev`
for usage instructions. If you intend to extend the existing .m files,
please also see the :doc:`developer page </developers/index>` for more
information on how to use Bio-Formats in general.

Performance
-----------

In our tests (MATLAB R14 vs. java 1.6.0\_20), the script executes at
approximately half the speed of our
:doc:`showinf command line tool </users/comlinetools/index>`, due to
overhead from copying arrays.

Troubleshooting
---------------

If you encounter an error trying to open JPEG-2000 data in MATLAB but the file
will open e.g. in Fiji using Bio-Formats, it may be due to conflicting
versions of JAI ImageIO in different JARs. As discussed on the component page,
:ref:`JAI ImageIO <forks-jai>` is no longer maintained and you will likely
need to remove the conflicting JAR(s) as a workaround.

Upgrading
---------

To use a newer version of Bio-Formats, overwrite the content of the
:file:`bfmatlab` folder with the :downloads:`newer version <>` of the
toolbox and restart MATLAB.

Alternative scripts
-------------------

Several other groups have developed their own MATLAB scripts that use
Bio-Formats, including the following:

- `<https://github.com/pramukta/bf-tools>`_
- `imread for multiple life science image file formats <http://www.mathworks.com/matlabcentral/fileexchange/32920-imread-for-multiple-life-science-image-file-formats>`_
