#!/bin/bash
set -e

outdir="postprocessed_proto_files"
mkdir -p "$outdir"

for inpath in terraform/docs/plugin-protocol/*.proto; do
  inname="$(basename "$inpath")"
  outname="$(echo "$inname" | sed 's/tfplugin\([0-9]\)\.\([0-9]\)/v\1_\2/')"
  outpath="$outdir/$outname"
  sed \
    -e 's/package tfplugin/package v/' \
    "$inpath" > "$outpath"
done
