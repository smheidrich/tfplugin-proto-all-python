#!/bin/bash
set -e

outdir="tfplugin_proto"
mkdir -p "$outdir"
touch "$outdir/__init__.py"

for inpath in postprocessed_python_files/*.py*; do
  inname="$(basename "$inpath")"
  outname="$(echo "$inname" | sed -e 's/_pb2//' -e 's/tfplugin/v/')"
  outpath="$outdir/$outname"
  ( \
    sed \
      -e 's/import tfplugin\([0-9]_[0-9]\)_pb2/from . import v\1/' \
      "$inpath" \
  ) > "$outpath"
done
