# Devtools for KiCAD.

## BOM Tools:

The BOM tools have a dependency - a python file with netlist reader utilities. It can be copied from `/usr/share/kicad-nightly/plugins/kicad_netlist_reader.py`. [The path will probably change as KiCAD 6 comes out.]


### `bom_grouped.py`
Generates a bill of materials grouped by value and footprint, with the following fields:

 - Ref Designator
 - Qty
 - Qty+
 - Value
 - Footprint
 - Mfr PN
 - Description