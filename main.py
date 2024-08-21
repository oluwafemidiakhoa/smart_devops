import os
import logging
from dotenv import load_dotenv  # Import load_dotenv to load environment variables
from services.planner_service import PlannerService
from services.developer_service import DeveloperService
from services.tester_service import TesterService
from services.deployment_service import DeploymentService
from services.monitor_service import MonitorService

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.INFO)

def run_smart_devops():
    api_key = os.getenv('MISTRAL_API_KEY')
    logging.info(f"API Key Loaded: {api_key}")

    # Initialize services
    developer = DeveloperService()  # Now handles api_key and endpoint internally
    planner = PlannerService()
    tester = TesterService()
    deployer = DeploymentService()
    monitor = MonitorService()

    # Create a backlog
    backlog = planner.create_backlog([
        {"task": "Design REST API", "description": "Design a REST API in Python using Flask that manages a list of items with CRUD operations."},
        {"task": "Develop Feature X", "description": "Develop a feature that takes a list of numbers as input and returns a list with each number squared."},
        {"task": "Create Unit Tests", "description": "Create unit tests in Python using unittest for a function that adds two numbers."},
    ])

    # Process each task in the backlog
    for task in backlog:
        logging.info(f"Starting task: {task['task']}")
        
        # Generate code
        code = developer.generate_code(task["description"])
        if not code:
            logging.error(f"Failed to generate code for task {task['task']}.")
            continue
        logging.info(f"Generated code for task {task['task']}:\n{code}")

        # Test the code
        try:
            tester.run_tests(code)
            logging.info(f"Tests passed for task {task['task']}.")
        except Exception as e:
            logging.error(f"Tests failed with error: {e}")
            continue

        # Deploy the code
        try:
            deployer.deploy_code(code)
            logging.info(f"Deployment successful for task {task['task']}.")
        except Exception as e:
            logging.error(f"Deployment failed with error: {e}")
            continue

        # Monitor the deployment
        try:
            monitor.monitor_task(task["task"])
        except AttributeError:
            logging.error(f"MonitorService missing the monitor_task method.")
        except Exception as e:
            logging.error(f"Monitoring failed with error: {e}")

if __name__ == "__main__":
    run_smart_devops()
