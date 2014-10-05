# Spec file for testing validation for example.py

regex username=[a-z_][a-z0-9_]{0,30}
range hour=0..24
enum  day=mon,tue,wed,thu,sat,sun

./example.py set-time --hour=$hour [ --day=$day ]
#./example.py adduser --username=$username
