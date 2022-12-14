# REST API

In this repository, you can access two implementations of RESTful APIs, which are capable of storing raw measurements from sensors and retrieving data aggregates from 
these sensors upon request ( JWT for authentication, migrations "Flask-Migrate","alembic" are not yet being implemented (was not asked))  . There are two branches available for each. 


 - [fastapi](https://github.com/itsparsa/assignment/tree/fastapi)
 - [flask](https://github.com/itsparsa/assignment/tree/flask)
 
## Functionallity
###  inputs :
server will get the following attributes:

- Sensor ID
- Measurement type (e.g., temperature celsius or relative humidity)
- Timestamp of recording
- Numerical measurement value

And will store them in a database (PostgreSQL).

### outputs:
these API endpoints can to retrieve measurement aggregates
(time-series) for a given Sensor ID. with the following attributes:
-  Min value

-  Mean value
-  Max value
-  Timestamp of the aggregated datapoint 

based on :

- Sensor ID for which to return the data
- Measurement Type of the data to be returned
- whether 5 minute aggregates or hourly aggregates are being returned.
- starting time-frame for which the aggregates

## comparison 
### database 
In flask implementation I only accumulated the data which was sent to server. But for FastAPI, sensors are categorized into their type (e.g. sensors for temperature are in temperatureSenosr). Not only this will speed up the searching process but also it makes database extendable for some sensors that they have different type of value (e.g. image sensors value are in array form not float).

### speedwise
according to the insomnia app there FastAPI app is 20 ms faster than Flask app. ( I am still working to get better evidance ) 
