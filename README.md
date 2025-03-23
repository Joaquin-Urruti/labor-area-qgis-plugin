# Calculate Worked Area

This is a plugin that takes as input a point layer loaded in QGIS with information about a labor done with agricultural machinery, and returns as output a polygon with the work surface.

![captura_qgis](captura_qgis.png)

Parameters:
- Input: a point layer
- Working width: the width of the machine
- Extra distance: a distance used to remove unwanted holes in the result
- Simplification level: to remove buffer point artifacts in the output
- Output path