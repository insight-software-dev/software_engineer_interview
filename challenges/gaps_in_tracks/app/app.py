from flask import Flask
import mysql.connector
import json

app = Flask(__name__)

config = {
        'user': 'root',
        'password': 'your_password',
        'host': 'db',
        'port': '3306',
        'database': 'your_database',
    }

query = (
    "WITH cte AS (SELECT elr_code, mileage_from, mileage_to, "
    "LAG (mileage_to, 1, null) OVER (PARTITION BY elr_code ORDER BY mileage_from ASC) AS previous_end, "
    "mileage_from - LAG (mileage_to, 1, null) OVER (PARTITION BY elr_code ORDER BY mileage_from ASC) AS difference "
    "FROM mileages) "
    "SELECT elr_code, previous_end AS mileage_from, mileage_from AS mileage_to FROM cte "
    "WHERE difference > 0.0 "
)

def get_elrs(config: dict, query: str) -> dict:
    """
    Fetch gaps in ELR data from the DB and read data into dictionary.
    """
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(query)
    results = {}
    for (elr_code, mileage_from, mileage_to,) in cursor:
        if elr_code in results:
            results[elr_code].append({"mileage_from": mileage_from, "mileage_to": mileage_to,})
        else:
            results[elr_code] = [{"mileage_from": mileage_from, "mileage_to": mileage_to,},]
    cursor.close()
    connection.close()
    return results


@app.route('/')
def index() -> str:
    """Basic view to check that service is runnign"""
    return "running"

@app.route('/elrs')
def elrs() -> str:
    """View to fetch gaps in ELR data formatted as a JSON string"""
    return json.dumps(get_elrs(config=config, query=query))

if __name__ == '__main__':
    app.run(host='0.0.0.0')