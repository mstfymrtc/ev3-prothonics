# ev3-prothonics
Lego Ev3 Mindstorms robot project that uses SWI-Prolog to perform reasoning with support of Prothonics.

# Features

  - Determines the color of front, right and left tiles with color sensors
  - Perform reasoning by SWI-Prolog with color sensor values as input
  - Always looks for food (aka. green tile), stay away from obstacles (aka. red tile)
  - Performs movement according to decisions given by SWI-Prolog

## Dependencies

1. [Numpy](https://numpy.org/)
2. [SWI-Prolog](https://www.swi-prolog.org/)
3. [Pyswip](https://github.com/yuce/pyswip)
4. [Prothonics](https://github.com/agnsal/prothonics)


To install numpy, swi-prolog and pyswip ev3dev-stretch, using `sudo apt install python3-*` command is recommended instead of pip3. 

Pyswip has to be installed using `sudo python3 -m pip install pyswip`, because only `pip` or `pip3` command on ev3dev-strecth might not work efficienly.

## Usage

This code only designed to work with Lego Mindstorms EV3 robots. In order to run it, clone the repository to robot, then run:

```sh
$ python3 main.py
```
## Contact

Dila Aslan - github.com/dilaaslan3
Mustafa Yumurtacı github.com/mstfymrtc


## Licence

Distributed under the Apache License 2.0. See ``LICENSE`` for more information.


