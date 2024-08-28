# Welcome to the technical challanges

## Context
In the railway industry, lines of tracks are defined in the form of ELR mileages. Mileages consist of the elr_code(VARCHAR), mileage_from(float) and mileage_to(float).
- ELR Code - is a 3-4 length string containing letters and numbers identifying Engineer's Line Reference https://en.wikipedia.org/wiki/Engineer%27s_Line_Reference
- mileage_from and mileage_to - are float values of miles starting from any particular point

Characteristics of the ELR Mileages are:
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
Within the `challanges/gaps_in_tracks` you will find the data source for the mileages. To get access to the data you can either:
- Use Docker. Within `challanges/gaps_in_tracks` run `docker compose up -d`. This should start the MySQL server on port 3306. Details of access can be found in docker-compose.yml.
- Use CSV file to load to other database or just load it up straight from file.

## Submission
- Duplicate this repository into a new private GitHub repository
- Add "jacekgdudek" as a collaborator
- Once the excercise is complete, create a PR with changes
- You can use any programming language of your choice



