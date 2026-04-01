# 2Dcompensate
A program to apply X and Y error compensation to G code files, created for Maslow 4 CNC.

This program was developed to compensate for positioning errors across the entire work area of a Maslow 4 CNC machine. Although the Maslow web UI includes settings for X and Y axis scaling factors, it has been found that those errors are not consistent for the entire work area. The approach used here relies on a user defined grid of error measurements to allow higher resolution compensation of a G code program, through the use of two dimensional interpolation. This technique is required because the error in each axis depends on the current position of the other.

The program comprises two tabs - one for the definition of the "error maps" for the X and Y axes, and another for application of those maps to the X and Y coordinates of a G code file, resulting in a compensated version of that file.



