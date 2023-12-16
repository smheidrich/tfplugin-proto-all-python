#!/bin/bash
set -e
if [ ! -e terraform ]; then
  git clone --depth=1 --sparse --filter=blob:none https://github.com/hashicorp/terraform.git
  cd terraform
  git sparse-checkout set docs/plugin-protocol --cone
else
  cd terraform
  git pull --rebase
fi
