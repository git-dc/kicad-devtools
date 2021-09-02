#
# Example python script to generate a BOM from a KiCad generic netlist
#
# Example: Sorted and Grouped CSV BOM
#

"""
    @package
    Output: CSV (comma-separated)
    Grouped By: Value, Footprint
    Sorted By: Ref
    Fields: Ref, Qty, Value, Footprint, Mfr PN, Description

    Command line:
    python "pathToFile/bom_grouped.py" "%I" "%O.csv"
"""

# Import the KiCad python helper module and the csv formatter
import kicad_netlist_reader
import csv
import sys

# A helper function to convert a UTF8/Unicode/locale string read in netlist
# for python2 or python3
def fromNetlistText( aText ):
    if sys.platform.startswith('win32'):
        try:
            return aText.encode('utf-8').decode('cp1252')
        except UnicodeDecodeError:
            return aText
    else:
        return aText

# Generate an instance of a generic netlist, and load the netlist tree from
# the command line option. If the file doesn't exist, execution will stop
net = kicad_netlist_reader.netlist(sys.argv[1])

# Open a file to write to, if the file cannot be opened output to stdout
# instead
try:
    fname = "/".join(sys.argv[2].strip().split("/")[:-1])+"/production/bom_grouped.csv"
    print("BOM file location:", fname)
    f = open(fname, 'w')
except IOError:
    e = "Can't open output file for writing: " + sys.argv[2]
    print(__file__, ":", e, sys.stderr)
    f = sys.stdout

# Create a new csv writer object to use as the output formatter
out = csv.writer(f, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)

# Output a set of rows for a header providing general information
# out.writerow(['Source:', net.getSource()])
# out.writerow(['Date:', net.getDate()])
# out.writerow(['Tool:', net.getTool()])
# out.writerow( ['Generator:', sys.argv[0]] )
# out.writerow(['Component Count:', len(net.components)])
# out.writerow(['Ref', 'Qnty', 'Value', 'Cmp name', 'Footprint', 'Description', 'Vendor'])
out.writerow(['Ref', 'Qty', 'Value', 'Footprint', 'Mfr PN', 'Description'])


# Get all of the components in groups of matching parts + values
# (see ky_generic_netlist_reader.py)
grouped = net.groupComponents()

# Output all of the component information
for group in grouped:
    refs = ""
    pns_list = []
    part_numbers = ""
    
    # Add the reference of every component in the group and keep a reference
    # to the component so that the other data can be filled in once per group
    for component in group:
        refs += fromNetlistText( component.getRef() ) + ", "
        new_pn = fromNetlistText( component.getField("Mfr PN") )
        if new_pn not in pns_list:
            pns_list.append(new_pn)
        part_numbers = ", ".join(pns_list)
        c = component

    # Fill in the component groups common data
    out.writerow([refs, len(group),
        fromNetlistText( c.getValue() ),
        fromNetlistText( c.getFootprint() ),
        part_numbers,
        fromNetlistText( c.getDescription() )])


