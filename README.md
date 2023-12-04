1. app1
   just run <br /> 
   vagrant up <br /> 
   vagrant provision <br /> 
   it will make two cumulus v4.3.0 virtuals box'es and configure bgp in between
2. app2
   just run <br /> 
   python3 ip.py <br /> 
   it will calculate if one subnet is hit by another
3. app1-rework
   start machines via test kitchen <br /> 
   kitchen create <br /> 
   it will make two cumulus v4.3.0 virtual box'es <br /> 
   kitchen converge <br /> 
   it will create bgp link between them <br /> 