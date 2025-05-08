# Hub
## Instructions for Starting the Project
To start the Hub, follow these steps:
1. Clone the repository to your local machine:
```bash
git clone https://github.com/Toolf/hub.git
cd hub
```
2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```
3. Install the project dependencies:
```bash
pip install -r requirements.txt
```
4. Run the system:
```bash
python ./app/main.py
```
The system will start collecting data from the agent through MQTT and processing it.
## Running Tests
To run tests for the project, use the following command:
```bash
python -m unittest discover tests
```
## Common Commands
### 1. Saving Requirements
To save the project dependencies to the requirements.txt file:
```bash
pip freeze > requirements.txt
```