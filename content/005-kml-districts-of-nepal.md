Title: KML Districts of Nepal
Slug: kml-districts-of-nepal
Date: 2010-07-10 21:25:38
Tags: maps, Nepal, kml, gis
Category: Blog
Author: Vibek Raj Maurya
Email:  rvibek@gmail.com
Lang: 
Summary: The file basically overlays on top GoogleEarth and GoogleMap and it has very basic attributes as described in the schema below.

Since past few weeks I had been watching videos on extending [GoogleEarth](http://earth.google.com/" target="_blank) and KML at [Google Developer Youtube Channel](http://www.youtube.com/user/GoogleDeveloperDay). This weekend I finally manage to practice with [QuatumGIS](http://www.qgis.org/) and [MapWindow GIS](http://www.mapwindow.org/). 

I practised with the data downloaded from [ICIMOD](http://icimod.org" target="_blank), Nepal. And here is a KML file of districts of Nepal. The file basically overlays on top GoogleEarth and GoogleMap and it has very basic attributes as described in the schema below.

[Download KML (2.2MB)](https://docs.google.com/uc?id=0B8IiFn2ckr59OWUzZTRmZDItMTA1OS00OGE3LWE1ODMtMzc0ZWZjOWUxOGQ5&export=download&hl=en_GB)

Schema of above KML
```python
<Schema name="np_data" id="np_data">
 <SimpleField name="Name" type="string"></SimpleField>
 <SimpleField name="Description" type="string"></SimpleField>
 <SimpleField name="DISTRICT" type="string"></SimpleField>
 <SimpleField name="AREA_SQ" type="float"></SimpleField>
 <SimpleField name="AREA" type="float"></SimpleField>
 <SimpleField name="PERIMETER" type="float"></SimpleField>
 <SimpleField name="DIST2_DD_" type="float"></SimpleField>
 <SimpleField name="DIST2_DD_I" type="float"></SimpleField>
</Schema>
```