Using Bio-Formats in .NET
=========================

OME does not currently provide a .NET implementation for Bio-Formats.
However, there are options you can use to read images from .NET via Bio-Formats:

Bioformats.NET6
---------------

The `Bioformats.NET6 <https://github.com/BiologyTools/BioFormatsNET6>`_ project provides Bio-Formats libraries converted to DLL, built with IKVM 8.7.1 Maven SDK for .NET6. To install add the below to your project file.:

.. parsed-literal::

    <PropertyGroup>
      <MavenAdditionalRepositories>ome=https://artifacts.openmicroscopy.org/artifactory/maven/;edu.ucar=https://maven.scijava.org/content/repositories/public/;</MavenAdditionalRepositories>
    </PropertyGroup> 
    <ItemGroup>
        <MavenReference Include="bioformats_package">
          <GroupId>ome</GroupId>
          <ArtifactId>bioformats_package</ArtifactId>
          <Version> |release| </Version>
        </MavenReference>
        <MavenReference Include="cdm-core">
          <GroupId>edu.ucar</GroupId>
          <ArtifactId>cdm-core</ArtifactId>
          <Version>5.3.3</Version>
        </MavenReference>
    </ItemGroup>

