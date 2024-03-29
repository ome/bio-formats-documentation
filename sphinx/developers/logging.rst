Logging
=======

Logging frameworks
------------------

Bio-Formats uses `SLF4J <http://www.slf4j.org>`_ as a logging API. SLF4J is a
facade and needs to be bound to a logging framework at deployment time. Two
underlying logging frameworks are currently supported by Bio-Formats. Bio-Formats 
does not impose any specific SLF4J binding on downstream consumers as per the 
recommended `SLF4J best practices <https://www.slf4j.org/manual.html#libraries>`_.
Some recommended bindings are as follows:

- `logback <http://logback.qos.ch/>`_ is the recommended framework and
  natively implements the SLF4J API. A logback version of 1.2.x is recommended as 
  Bio-Formats has a hard dependency for slf4j-api 1.7.30. This means that logback 
  versions 1.3.x and higher are not yet supported in Bio-Formats as they rely 
  on slf4j-api 2.x. 
- `log4j <http://logging.apache.org/log4j>`_ is the other logging framework
  supported by Bio-Formats and is primarily used in the
  :doc:`MATLAB environment <matlab-dev>`.

Examples of declaring these dependencies using Maven or Gradle are given in the 
`Bio-Formats examples repository <https://github.com/ome/bio-formats-examples>`_.

Initialization
--------------

The :common_javadoc:`DebugTools <loci/common/DebugTools.html>` class contains a
series of framework-agnostic methods for the initialization and control of the
logging system. This class uses reflection to detect the underlying logging
framework and delegate the method calls to either
:common_javadoc:`Log4jTools <loci/common/Log4jTools.html>` or
:common_javadoc:`LogbackTools <loci/common/LogbackTools.html>`.

The main methods are described below:

- ``DebugTools.enableLogging()`` will initialize the underlying logging 
  framework. This call will result in a no-op if logging has been initialized
  either via a binding-specific configuration file (see
  `logback configuration <http://logback.qos.ch/manual/configuration.html>`_)
  or via a prior call to ``DebugTools.enableLogging()``.

- ``DebugTools.enableLogging(level)`` will initialize the logging framework
  under the same conditions as described above and set the root logger level if
  the initialization was succesful.

- ``DebugTools.setRootLevel(level)`` will override the level of the root logger
  independently of how the logging system was initialized.

- ``DebugTools.enableIJLogging()`` (logback-only) will add an ImageJ-specific
  appender to the root logger.

.. versionchanged:: 5.2.0

  Prior to Bio-Formats 5.2.0, ``DebugTools.enableLogging(level)``
  unconditionally set the logging and root logger level. Use
  ``DebugTools.setRootLevel(level)`` to restore this behavior.
