# ev3-prothonics
Lego Ev3 Mindstorms robot project that uses SWI-Prolog to perform reasoning with the support of Prothonics.
(University of L'Aquila, Intelligence Systems and Robotics Laboratory Course - 2020)

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


To install dependencies on ev3dev-stretch, `sudo apt install python3-*` recommended. 
If pip needs to be used, than it's recommended to use it with `sudo python3 -m pip install pyswip` instead of `pip install`.


## Usage

This code only designed to work with Lego Mindstorms EV3 robots. In order to run it, clone the repository to robot, then run:

```sh
$ python3 main.py
```
## Contact

  - Dila Aslan - https://github.com/dilaaslan3
  - Mustafa Yumurtacı https://github.com/mstfymrtc


## Licence

Distributed under the Apache License 2.0. See ``LICENSE`` for more information.


