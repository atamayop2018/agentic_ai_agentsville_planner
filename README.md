# AgentsVille Trip Planner

An AI-powered trip planning agent for AgentsVille, built with Python, Pydantic, and OpenAI's API. This project implements a ReAct-based agent that creates personalized itineraries based on user preferences, weather forecasts, and available activities.

## Features

- **Pydantic Models**: Data validation for vacation info, travel plans, and activities using Pydantic v2.
- **Weather and Activity Integration**: Fetches mock weather and activity data to inform itinerary planning.
- **LLM-Powered Itinerary Generation**: Uses OpenAI's GPT models to create detailed, day-by-day travel plans.
- **Weather Compatibility Evaluation**: Ensures activities are suitable for the forecasted weather conditions.
- **ReAct Agent for Revisions**: An iterative agent that revises itineraries based on feedback and evaluations.
- **Tool Integration**: Supports tools like calculators, activity lookups, and evaluation suites.

## Project Structure

- `project_starter.ipynb`: Main Jupyter notebook containing the complete implementation.
- `project_lib.py`: Utility functions, mock APIs, and agent classes.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Git ignore rules for Python projects.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd agentic_ai_agentsville_planner
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key (if using Vocareum or direct API):
   - Create a `.env` file with your API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

1. Open the Jupyter notebook:
   ```bash
   jupyter notebook project_starter.ipynb
   ```

2. Run the cells in order to:
   - Define Pydantic models
   - Fetch weather and activity data
   - Generate initial itinerary
   - Evaluate and revise the plan

3. The notebook includes:
   - Vacation info setup
   - Itinerary agent with CoT prompting
   - Weather compatibility checks
   - ReAct revision agent with tools

## Key Components

- **VacationInfo Model**: Captures traveler preferences, budget, dates, and interests.
- **TravelPlan Model**: Structured output for the generated itinerary.
- **ChatAgent Class**: Base class for LLM interactions.
- **ItineraryAgent**: Generates initial travel plans.
- **ItineraryRevisionAgent**: ReAct agent for iterative improvements.
- **Evaluation Functions**: Checks for budget, dates, interests, and weather compatibility.

## Dependencies

- `pydantic>=2.0`: Data validation and serialization.
- `openai`: OpenAI API client.
- `json-repair`: Handles malformed JSON from LLM responses.

## Contributing

This is a Udacity project. For improvements, ensure all cells in the notebook compile and run successfully.

## License

[Add license if applicable]