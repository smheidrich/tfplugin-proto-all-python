#!/bin/bash
set -e
PROTOC_PYTHON="${PROTOC_PYTHON:-python3}"
INCLUDE="${INCLUDE:-postprocessed_proto_files}"
OUTPUT="${OUTPUT:-generated_python_files}"
PROTO_FILES_DIR="${PROTO_FILES_DIR:-$INCLUDE}"

mkdir -p "$OUTPUT"

for x in "$PROTO_FILES_DIR"/*.proto; do
"$PROTOC_PYTHON" -m grpc_tools.protoc \
  -I$INCLUDE \
  --python_out=$OUTPUT \
  --pyi_out="$OUTPUT" \
  --grpc_python_out=$OUTPUT \
  "$x"
done
