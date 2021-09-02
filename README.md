# Devtools for KiCAD.

## BOM Tools:

The BOM tools have a dependency - a python file with netlist reader utilities. It can be copied from `/usr/share/kicad-nightly/plugins/kicad_netlist_reader.py`. [The path will probably change as KiCAD 6 comes out.]


### `bom_grouped.py`
Generates a bill of materials. Components and sorted by ref, and are grouped by value and footprint. The following fields are provided:

 - Ref
 - Qty
 - Value
 - Footprint
 - Mfr PN
 - Description

### `bom_sorted.py`
Generates a bill of materials. Components are sorted by ref, and are not grouped (one per line). The following fields are provided:

 - Ref
 - Qty
 - Value
 - Footprint
 - Mfr PN
 - Description


## Gerber Tools:

### `gbr_packager.sh`
Packages the bom and gerber files into a .zip archive automatically baking version and revision numbers into the filename.