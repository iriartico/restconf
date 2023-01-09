#!/bin/bash

python3 state_restconf.py
python3 GigabitEthernet1.py
python3 GigabitEthernet2.py
python3 GigabitEthernet4.py 
python3 GigabitEthernet5.py 
python3 create_static_route.py
