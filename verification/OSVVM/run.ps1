git submodule update --init --recursive verification\OSVVM\OsvvmLibraries
& .\ghdl\scripts\vendors\compile-osvvm.ps1 `
  -All `
  -Source verification\OSVVM\OsvvmLibraries -Output precompiled
