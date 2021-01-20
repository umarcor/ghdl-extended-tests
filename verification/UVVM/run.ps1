git submodule update --init --recursive verification\UVVM\uvvm
& .\ghdl\scripts\vendors\compile-uvvm.ps1 `
  -All `
  -Source verification\UVVM\uvvm -Output precompiled
