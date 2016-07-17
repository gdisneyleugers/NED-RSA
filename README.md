# NED-RSA
RSA NED Reconstruction Attack can attack any key from 128-1024. Private key reconstruction attack against RSA Public key. Certian N values are better than others, these N values will cause not optimal D values to be calculated. Thus arent vulnerable, this seems to be only 1 of 3 will have this strong N value.

#Setup: 
pip install gmpy primefac crypto

#To run:
python NED-RSA.py pub-key.pem

#Output:
  ----------------------------------------------------------------
  N: 13417933502929779524771058323761129441
  ----------------------------------------------------------------
  E: 65537
  ----------------------------------------------------------------
  P: 3568797732513430367
  ----------------------------------------------------------------
  Q: 3759790974054393023
  ----------------------------------------------------------------
  D: 2344662930490437997371731419749114865
  ----------------------------------------------------------------
  > -----BEGIN RSA PRIVATE KEY-----
  > MF4CAQACEAoYMzK1hT9UwaGx5lNz5+ECAwEAAQIQAcOQzr+hdRuMpL+cI5Nj8QII
  > NC11+H47ZL8CCDGG6qEhrrtfAggYBorYtj9g/wIIMGmPZJ6GLMUCCCKZfizk8eJR
  > -----END RSA PRIVATE KEY-----
  
#Compute Times on i7:
  - 10 Min (128)
  - 1 Hr (256)
  - 4 hr (512)
  - 16 hr (1024)


