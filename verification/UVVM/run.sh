#!/usr/bin/env sh

git submodule update --init --recursive verification/UVVM/uvvm
./ghdl/scripts/vendors/compile-uvvm.sh \
  --all \
  --source $(dirname $0)/uvvm --output precompiled
