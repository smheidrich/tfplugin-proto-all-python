#!/bin/bash
set -e

outdir="postprocessed_python_files"
mkdir -p "$outdir"

for inpath in generated_python_files/*.py*; do
  inname="$(basename "$inpath")"
  outname="$inname"
  outpath="$outdir/$outname"
  ( \
    #echo "from typing import Any"; \
    sed \
      -e 's/__slots__ = \[\]/__slots__: list[str] = []/' \
      -e 's/\([^s].\)_Mapping\([^[]\)/\1_Mapping[Any, Any]\2/g' \
      "$inpath" \
  ) > "$outpath"
done
