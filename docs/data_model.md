## Activity

Activity creators can:
 * Define input fields required for a challenge entrant to "record" activity
 * Define whether an activity may be repeated, and if so at what frequency
 * Define the rewards associated with completing an activity
 * Define whether an activity requires challenge admin approval in order for the points to be remitted
 * Define whether points can be awarded on individual completion or if some group completion criteria is necessary


```json
{
    "id": "string",
    "challenge_id": "string",
    "name": "string",
    "record_rules": [ //configurable input fields 
        {
            "name": "string",
            "type": "string",
            "input_validation": {"???"},
            "required": "boolean"
        }, // rule object 1,
        {} // rule object 2, ...
    ],
    "repeat_rules": { // configurable repeat rules
        "repeats_allowed": "boolean",
        "repeat_frequency": "string",
    },
    "reward_rules": { // configurable reward rules
        "frequency_mutiplier"
    },
    "completion_criteria": {
        "team_completion": "boolean",
        "min_completion_percentage": "float"
    }
}
```

## Challenge
```json
{
    "id": "string",
    "name": "string",
    "owner_id": "string",
    "admins": [],
    "start_date": "datetime",
    "end_date": "datetime",
    "team_allowed": "boolean"
}
```

## Person
```json
    {
        "id": "string",
        "fname": "string",
        "lname": "string",
        "teams": [],
        "challenges": [],
        "activities": [
            {"activity_id": 1234,"points_awarded":10,"ts":"2020-09-08"}
        ]
    }
```

## Team
```json
{
    "id": "string",
    "team_name": "string",
    "owner_id": "string",
    "members": [],
    "challenges": [],
    "activities": [
        {
            "activity_id": 1234,
            "points_awarded": 10,
            "ts": "2020-09-08",
            "person_id": 123
        }
    ]
}
```