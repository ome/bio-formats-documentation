# -*- coding: utf-8 -*-
#
# Bio-Formats documentation build configuration file, created by
# sphinx-quickstart on Wed Aug 29 15:42:49 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import re
import subprocess

def popen(args, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
        copy = os.environ.copy()
        shell = (sys.platform == "win32")
        return subprocess.Popen(args,
                env=copy,
                stdin=stdin,
                stdout=stdout,
                stderr=stderr,
                shell=shell)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.)
extensions = ['sphinx.ext.extlinks']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.txt'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Bio-Formats'
title = project +u' Documentation'
author = u'The Open Microscopy Environment'
copyright = u'2000-2012, ' + author

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
try:
    if "BF_RELEASE" in os.environ:
        release = os.environ.get('BF_RELEASE')
    else:
        p = popen(['git','describe'])
        tag = p.communicate()
        split_tag = re.split("^(v)?(.*?)(-[0-9]+)?((-)g(.*?))?$",tag[0])
        # The full version, including alpha/beta/rc tags.
        release = split_tag[2]
    split_release =  re.split("^([0-9]\.[0-9])(\.[0-9]+)(.*?)$",release)
    # The short X.Y version.
    version = split_release[1]
except:
    version = 'UNKNOWN'
    release = 'UNKNOWN'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

if "OMERODOC_URI" in os.environ:
    omerodoc_uri = os.environ.get('OMERODOC_URI')
else:
    omerodoc_uri = 'http://www.openmicroscopy.org/site/support/omero4/'


if "SOURCE_BRANCH" in os.environ:
    source_branch = os.environ.get('SOURCE_BRANCH')
else:
    source_branch = 'develop'

extlinks = {
    'wiki' : ('http://trac.openmicroscopy.org.uk/ome/wiki/'+ '%s', ''),
    'ticket' : ('http://trac.openmicroscopy.org.uk/ome/ticket/'+ '%s', '#'),
    'snapshot' : ('http://cvs.openmicroscopy.org.uk/snapshots/'+ '%s', ''),
    'plone' : ('http://www.openmicroscopy.org/site/'+ '%s', ''),
    'oo' : ('http://www.openmicroscopy.org/' + '%s', ''),
    'doi' : ('http://dx.doi.org/' + '%s', ''),
    'source' : ('https://github.com/openmicroscopy/bioformats/blob/' + source_branch + '/' + '%s', ''),
    'javadoc' : ('http://hudson.openmicroscopy.org.uk/job/OMERO/javadoc/' + '%s', ''),
    'jenkins' : ('http://hudson.openmicroscopy.org.uk/' + '%s', ''),
    'mailinglist' : ('http://lists.openmicroscopy.org.uk/mailman/listinfo/' + '%s', ''),
    'forum' : ('http://www.openmicroscopy.org/community/' + '%s', ''),
    'omerodoc': (omerodoc_uri + '%s', '')
    }

rst_epilog = """
.. _Hibernate: http://www.hibernate.org
.. _ZeroC: http://www.zeroc.com
.. _Ice: http://www.zeroc.com
.. _OME-TIFF: https://www.openmicroscopy.org/site/support/file-formats/ome-tiff
.. _OME-XML: http://www.openmicroscopy.org/site/support/file-formats/the-ome-xml-file

.. |Poor| image:: /images/crystal-1.png
.. |Fair| image:: /images/crystal-2.png
.. |Good| image:: /images/crystal-3.png
.. |Very Good| image:: /images/crystal-4.png
.. |Outstanding| image:: /images/crystal-5.png
.. |no| image:: /images/crystal-no.png
.. |yes| image:: /images/crystal-yes.png

"""

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = { '**' : ['globaltoc.html', 'pagetoc.html',  'searchbox.html', 'sourcelink.html'] }

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Bio-Formatsdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
target = project + '-' + release + '.tex'
latex_documents = [
  (master_doc, target, title, author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = True

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
latex_show_urls = 'footnote'

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'OMERO', title, author, 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, project, title, author, 'omedocs', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# -- Options for the linkcheck builder ----------------------------------------

# Regular expressions that match URIs that should not be checked when doing a linkcheck build
linkcheck_ignore = ['http://www.openmicroscopy.org/site/support/faq']
