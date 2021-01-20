#!/usr/bin/env sh

git submodule update --init --recursive verification/OSVVM/OsvvmLibraries
./ghdl/scripts/vendors/compile-osvvm.sh \
  --all \
  --source $(dirname $0)/OsvvmLibraries/osvvm --output precompiled
