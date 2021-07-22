#!/usr/bin/env sh

git submodule update --init --recursive verification/OSVVM/OsvvmLibraries
$(dirname "$0")/compile-osvvm.py \
  --all \
  --source $(dirname $0)/OsvvmLibraries/osvvm --output precompiled
