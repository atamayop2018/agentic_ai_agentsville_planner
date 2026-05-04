import re
from pathlib import Path
path = Path('project_starter.ipynb')
text = path.read_text()

replacements = [
    (
        'api_key="**********",  # <--- TODO: Fill in your Vocareum API key here',
        'api_key="voc-1660414188160736498335769eab69e125a30.53769569",  # <--- Vocareum API key'
    ),
    (
        '    # TODO: Fill in the the missing fields for the VacationInfo class\n    "**********"\n    "**********"\n    "**********"\n    "**********"\n    "**********"',
        '    travelers: List[Traveler]\n    destination: str\n    date_of_arrival: datetime.date\n    date_of_departure: datetime.date\n    budget: int'
    ),
    (
        '# TODO: Fill in the missing start and end dates from vacation_info\n        # start=**********\n        # end=***********\n        freq="D"',
        '        start=vacation_info.date_of_arrival,\n        end=vacation_info.date_of_departure,\n        freq="D"'
    ),
]

for old, new in replacements:
    if old not in text:
        print(f'Warning: pattern not found:\n{old[:200]}...')
    text = text.replace(old, new)

old_prompt = '''ITINERARY_AGENT_SYSTEM_PROMPT = f"""
********** < -- Specify the role

## Task

********** < -- Specify the task. Note that, outdoor-only activities should be avoided
********** < -- during rain, events should be chosen based on traveler interests,
********** < -- and the budget should not be exceeded, and there should be at least
********** < -- one activity per day.

## Output Format

Respond using two sections (ANALYSIS AND FINAL OUTPUT) in the following format:

    ANALYSIS:
    ********** < -- Specify the format of the analysis section


    FINAL OUTPUT:

    ```json
    ********* < -- Specify the format of the final output as TravelPlan. Hint: https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_json_schema
    ```

## Context

********** <--- Insert the retreived weather data here
********** <--- Insert the retreived activities data here
"""  # noqa'''

new_prompt = '''ITINERARY_AGENT_SYSTEM_PROMPT = f"""
You are an expert travel planner for AgentsVille. Your job is to create a personalized, day-by-day itinerary that matches the travelers' interests, budget, and the available weather and activity data.

## Task

- Review the provided vacation information, weather forecast, and available activities.
- Generate a coherent travel plan with at least one activity per day.
- Avoid outdoor activities on rainy days and favor indoor or weather-safe alternatives.
- Keep the total cost within budget.
- Ensure all activities are available on the requested dates and aligned with traveler interests.

## Output Format

Respond using two sections (ANALYSIS AND FINAL OUTPUT) in the following format:

    ANALYSIS:
    - Describe how you selected each day's activities.
    - Explain why each activity matches traveler interests and weather.
    - Track the cost and confirm the total remains within budget.

    FINAL OUTPUT:

    ```json
    {TravelPlan.model_json_schema()}
    ```

## Context

Vacation Info: {vacation_info.model_dump_json()}

Weather Data: {weather_for_dates_df.to_json()}

Activities Data: {activities_for_dates_df.to_json()}
"""  # noqa'''

if old_prompt not in text:
    print('Warning: itinerary prompt block not found')
else:
    text = text.replace(old_prompt, new_prompt)

path.write_text(text)
print('done')
