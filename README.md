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

### `bom_auto-pkg.py`
Generates two bills of materials: a grouped one `bom_grouped.csv` and a sorted ungrouped one `bom_sorted.csv`. Runs `link_pkger.sh` to link the `gbr_pkger.sh` into the most advanced `[version]/[revision]` directory in production, which in turn runs the `gbr_pkger.sh` to package up the mfg files.


## Gerber Tools:

### `gbr_pkger.sh`
Packages the bom and gerber files into a .zip archive automatically baking version and revision numbers into the filename.

### `link_pkger.sh`
Creates a soft link to `gbr_pkger.sh` in the most advanced `[version]/[revision]` directory in `production/` and runs it to package up the mfg files.