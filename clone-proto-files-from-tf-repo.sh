#!/bin/bash
git clone --depth=1 --sparse --filter=blob:none https://github.com/hashicorp/terraform.git
cd terraform
git sparse-checkout set docs/plugin-protocol --cone
