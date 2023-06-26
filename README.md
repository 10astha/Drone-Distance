The drone
begins at position (0,0,0) and can move infinitely in any direction depending on how it is programmed. A
drone program is a string consisting of a sequence instructions, where each instruction is one of the following.

• +X: Move one unit in the direction of the positive X-axis.

• -X: Move one unit in the direction of the negative X-axis.

• +Y: Move one unit in the direction of the positive Y -axis.

• -Y: Move one unit in the direction of the negative Y -axis.

• +Z: Move one unit in the direction of the positive Z-axis.

• -Z: Move one unit in the direction of the negative X-axis.

• m(P), where m > 0 is an integer and P is a drone program: Execute program P m times.
For example,
• 2(+X+Y-Z) is equivalent to +X+Y-Z+X+Y-Z, moving the drone to (2, 2, −2) after traveling distance 6.

• 5(+X)10(-X) is equivalent to +X+X+X+X+X-X-X-X-X-X-X-X-X-X-X, moving the drone to (−5, 0, 0) after
traveling distance 15.

• 3(-Y2(+Z)) is equivalent -Y+Z+Z-Y+Z+Z-Y+Z+Z, moving the drone to (0, −3, 6) after traveling distance
9.

• +X+X+X+X4(+Y)2(+Z-Z) is equivalent to +X+X+X+X+Y+Y+Y+Y+Z-Z+Z-Z, moving the drone to (4, 4, 0)
after traveling distance 12.
