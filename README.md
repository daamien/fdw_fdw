# fdw_fdw

a PostgreSQL Foreign Data Wrapper that returns the list of all the PostgreSQL Foreign Data Wrappers



## Quick Demo with docker 

```
docker run -p 65432:5432 -d daamien/fdw_fdw
```

Wait for a few seconds while the PostgreSQL instance is starting
The FDW data wrappers is already installed in the 'postgres' database
and you can directly write queries against the foreign table
called "wrappers" 

Like this:

```
psql -h 127.0.0.1 -p 65432 -U postgres -c "SELECT * FROM wrappers;"
```

## INSTALL

```
sudo apt-get install postgresql-9.5-python3-multicorn
sudo python3 setup.py install
```

