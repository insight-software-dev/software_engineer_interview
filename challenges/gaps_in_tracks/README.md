# Challenge: Gaps in Tracks

## Expected time of completion
20 minutes

## Context
In the railway industry, lines of tracks are defined in the form of ELR mileages. Mileages consist of the elr_code(VARCHAR), mileage_from(float) and mileage_to(float).
- ELR Code - is a 3-4 length string containing letters and numbers identifying Engineer's Line Reference https://en.wikipedia.org/wiki/Engineer%27s_Line_Reference
- mileage_from and mileage_to - are float values of miles starting from any particular point

Characteristics of ELR Mileages are:
- Mileages can overlap on the same ELR
- Mileages can have gaps on the same ELR
- Mileages don't need to start from 0

## Goal
- Provide a list of gaps in mileages grouped by ELR code in the format of i.e.
```
{
    "BOK1": [{
        "mileage_from": "1.450",
        "mileage_to": "5.120"
    }, ...]
}
```
- Attempt to do as much as possible using database queries.


## Where to start
Within the `challenges/gaps_in_tracks` you will find the data source for the mileages. To get access to the data you can either:
- Use Docker. Within `challenges/gaps_in_tracks` run `docker compose up -d`. This should start the MySQL server on port 3306. Details of access can be found in docker-compose.yml.
- Use the CSV file to load the data to another database or just load it up straight from the file

