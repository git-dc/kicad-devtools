#! /bin/bash

p=$(dirname $PWD)
parent=${PWD##*/}
grandparent=${p##*/}
fname="$PWD/../../fab+assy_"$grandparent"_"$parent".zip"
echo "Packaging gerbers and BOMs into $fname"
cp $PWD/../../bom_sorted.csv $PWD/bom_sorted_"$grandparent"_"$parent".csv
cp $PWD/../../bom_grouped.csv $PWD/bom_grouped_"$grandparent"_"$parent".csv
zip -r $fname *
