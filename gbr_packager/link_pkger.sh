#! /bin/bash

## Links the gerber packager into the most recent revision directory and runs it to package up production files.

prj_path=$1
ver_val=$(/bin/ls $prj_path -v | tail -n1)
rev_val=$(/bin/ls $prj_path$ver_val"/" -v | tail -n1)
rev_path=$prj_path$ver_val"/"$rev_val"/"
echo "Soft linking the gbr packager into $rev_path"
ln -sf $HOME/.local/share/kicad/7.0/3rdparty/plugins/kicad-devtools/gbr_packager/gbr_pkger.sh $rev_path/gbr_pkger.sh
cd $rev_path && /bin/bash $PWD/gbr_pkger.sh
