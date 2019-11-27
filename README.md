# weather-api

This project contains several api endpoints displaying current average temperature. The temperature is pulled from 3 different weather stations.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Any Unix based system


### Run Unit tests
```
cd weather/test/
python test_getcurrentaveragetemperature.py -v

```

## Running Project 
You need to pass in two paramters when executing the binary for pass-as-a-service. The first parameter is the passwords file and the second parameter is the groups file.
```
cd weather-api/api/
python manage.py runserver
```

