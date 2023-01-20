# Devtools for KiCAD.
Uses KiCAD environment variables to automatically retrieve project directory. Uses KiCAD project variables to automatically generate and find latest `version/revision/` directories within the project.

## Installation:
1. Clone the repo to `~/.local/share/kicad/6.0/3rdparty/plugins/kicad-devtools`
2. Look through the scripts in this library to make sure the paths are consistent with your directory setup.
3. In Eeschema, open the BOM generation interface and add `bom_auto-pkg.py` as a new BOM script.

## How to Use:
1. Generate gerbers and drill files from the PCBNew interface. This will automatically create the directories for the latest version and revision, as indicated by the project variables. These path variables are encoded and saved in the project configuration files that should be version controlled together with the rest of the project files.
2. Use the HTML BOM generator to create an assembly drawing. Place it in the `version/revision/` directory
3. User BOM auto packager to generate BOMs and compress the fabrication package with all the necessary files.


## BOM Tools:
Tools for generating BOMs from the Eeschema interface.

### Dependencies:
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
Generates two bills of materials: a grouped one `bom_grouped.csv` and a sorted ungrouped one `bom_sorted.csv`. The scripts to generate these BOMs are identical to the ones above. Runs `link_pkger.sh` to link the `gbr_pkger.sh` into the most advanced `[version]/[revision]` directory in `production/`, which in turn runs the `gbr_pkger.sh` to package up the mfg files.


## Gerber Tools:
Tools for compressing gerber files and BOMs into a fabrication package.
### `gbr_pkger.sh`
Packages the bom and gerber files into a .zip archive automatically baking version and revision numbers into the filename.

### `link_pkger.sh`
Creates a soft link to `gbr_pkger.sh` in the most advanced `[version]/[revision]` directory in `production/` and runs it to package up the mfg files.