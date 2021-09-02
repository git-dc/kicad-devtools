#! /bin/bash

p=$(dirname $PWD)
parent=${PWD##*/}
grandparent=${p##*/}
fname="fab+assy_files_"$grandparent"_"$parent".zip"
echo $fname
cp ../../bom_sorted.csv ./
cp ../../bom_grouped.csv ./
zip -r $fname *
rm bom_sorted.csv
rm bom_grouped.csv
