# 2Dcompensate
A program to apply X and Y error compensation to G code files, created for Maslow 4 CNC.

This program was developed to compensate for positioning errors across the entire work area of a Maslow 4 CNC machine. Although the Maslow web UI includes settings for X and Y axis scaling factors, it has been found that those errors are not consistent for the entire work area. The approach used here relies on a user defined grid of error measurements to allow higher resolution compensation of a G code program, through the use of two dimensional interpolation. This technique is required because the error in each axis depends on the current position of the other.

The program comprises two tabs - one for the definition of the "error maps" for the X and Y axes, and another for application of those maps to the X and Y coordinates of a G code file, resulting in a compensated version of that file.

The "Error map" tab contains adjustable tables for the measured X and Y deviations from nominal at the intersections of grid lines. Those deviations are found by drawing or cutting a grid pattern onto the work area then measuring the horizontal (X) and vertical (Y) dimensions from the center lines to each intersection. In the example below, a 10" x 10" (254mm x 254mm) grid was used to cover a 96" x 48" work area. In use, error values for coordinates inside the grid will be interpolated; errors for values outside the grid will be extrapolated.

```
   -1016     -762     -508     -254      X 0      254      508      762      1016
 508  +--------+--------+--------+--------+--------+--------+--------+--------+
      |        |        |        |        |        |        |        |        |
 254  +--------+--------+--------+--------+--------+--------+--------+--------+
      |        |        |        |        |        |        |        |        |
Y 0   +--------+--------+--------+--------+--------+--------+--------+--------+
      |        |        |        |        |        |        |        |        |
-254  +--------+--------+--------+--------+--------+--------+--------+--------+
      |        |        |        |        |        |        |        |        |
-508  +--------+--------+--------+--------+--------+--------+--------+--------+
```

Note that the initial release of this program does not account for circular arc (i.e., G2 / G3) motion.

Multiple error map versions can be saved and later recalled.  The format of the error map file is simple:

In this example, errors were measured to the closest 1/32" on a 10" x 10" grid, drawn on 48" wide kraft paper with a pen inserted into a 3D printed holder* in place of the router collet.

```
X error map: mm
              -1016.0     -762.0     -508.0     -254.0        0.0      254.0      508.0      762.0     1016.0
     508.0          0          0          0          0          0          0          0          0    -1.5875
     254.0    -1.5875          0          0          0          0          0          0          0    -1.5875
       0.0  -0.793750          0          0          0          0          0          0          0    -1.5875
    -254.0  -0.793750          0          0          0          0          0          0          0  -0.793750
    -508.0    -1.5875          0          0          0          0          0          0   0.793750          0

Y error map: mm
              -1016.0     -762.0     -508.0     -254.0        0.0      254.0      508.0      762.0     1016.0
     508.0  -0.793750    -1.5875  -3.175000  -3.175000    -4.7625  -3.175000  -3.175000    -1.5875          0
     254.0          0  -0.793750    -1.5875    -1.5875  -2.381250    -1.5875    -1.5875  -0.793750          0
       0.0          0          0          0          0          0          0          0          0          0
    -254.0    -1.5875  -0.793750    -1.5875    -1.5875    -1.5875    -1.5875  -0.793750  -0.793750   0.793750
    -508.0    -1.5875  -2.381250  -3.175000  -3.175000  -3.175000  -3.175000  -2.381250    -1.5875          0
```

* The pen holder used was a remix of https://forums.maslowcnc.com/uploads/short-url/myx6xtKND4mVYCCKSlAYYUWbZNp.step
  Modified to fit a G22 pen refill, to eliminate the "cut down to 2.4" Overall Length" part! On Amazon:
  "GPCA GP22 Ink Refill Cartridges for Gel Pens, Medium Point Size, 3-Pack, Black"

Once the errors are characterized, use the "Compensate" tab to open and compensate a G code file.

"Open" will display a file browser to navigate to and select a G code file (*.gcode, *.nc or *.txt). If the "Compensate automatically" checkbox if checked, the file will be compensated using the current values on the "Error" tab, and saved with "_compensated" appended to the file name and included as a comment in the first line of the file.

"Verify calculations" will cause comments to be inserted in the file for each X and Y value modified, showing the claculation that was applied. "Show line numbers" will number the lines in the editor window. It will not output those line numbers to the compensated file.

The "Find", "Replace with", and "Replace all" buttons provide a very basic search and replace functionality.

"Save" will overwrite the listed file with the content of the editor window. It is not enabled unless changes are made.

The files made available here include:
   The Python (3.14) source code, compcalc.py
   The package requirements.txt
   A "Compcalc" folder, containing an executable (pyinstaller) version with all requirements
   
