1. app1
   just run vagrant up
   vagrant provision
   it will make two cumulus v4.3.0 virtuals box'es and configure bgp in between
2. app2
   just run python3 ip.py
   it will calculate if one subnet is hit by another
3. app1-rework
   start machines via test kitchen
   kitchen create
   it will make two cumulus v4.3.0 virtual box'es
   kitchen converge
   it will create bgp link between them
