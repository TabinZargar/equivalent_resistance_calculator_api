
Equivalent Resistance API

This Django API calculates the equivalent resistance of a circuit described in JSON format. Using Django REST framework, the API accepts nodes and connections and returns the equivalent resistance between specified input and output nodes.


API Usage

Endpoint: /api/calculate/  
Method: POST  
Request Body: JSON

JSON Input Example

{
    "nodes": ["A", "B", "C", "D", "E", "F"],
    "connections": [
        {"start": "A", "end": "C", "resistance": 20},
        {"start": "C", "end": "D", "resistance": 30},
        {"start": "D", "end": "E", "resistance": 40},
        {"start": "D", "end": "F", "resistance": 10},
        {"start": "C", "end": "F", "resistance": 60},
        {"start": "F", "end": "E", "resistance": 50},
        {"start": "E", "end": "B", "resistance": 80}
    ],
    "input_node": "A",
    "output_node": "B"
}

Response Example

{
    "equivalent_resistance": <calculated_value>
}

Running the Server

Start the Django server with:
```
python manage.py runserver
```

