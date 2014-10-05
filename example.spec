# Spec file for testing validation for example.py

regex username=[a-z_][a-z0-9_]{0,30}
range hour=0..24
enum  day=mon,tue,wed,thu,sat,sun

#./example.py --hour $hour
#./example.py --username $username
#./example.py --day $day
./example.py foo [ --day $day ] [ --hour $hour ]
