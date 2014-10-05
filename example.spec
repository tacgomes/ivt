# Spec file for testing validation for example.py

enum  verbosity=info,warn,error
range hour=0..24
range minsec=0..60
regex timezone=\w+
regex username=[a-z_][a-z0-9_]+

./example.py help
./example.py show-log [ --verbosity=$verbosity ]
./example.py show-log [ -v=$verbosity ]
./example.py set-time --hour=$hour --minute=$minsec --second=$minsec [ --timezone=$timezone ]
./example.py add-user --username=$username
