from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

drone_plugin_prefix = 'PLUGIN'


def config():
    return {
        'host': os.environ.get(f"{drone_plugin_prefix}_JENKINS_HOST", 'https://jenkins.com'),
        'jenkins_job': os.environ.get(f"{drone_plugin_prefix}_JENKINS_JOB", None),
        'deployment': {
            'stage': os.environ.get(f"{drone_plugin_prefix}_STAGE", None),
            'service_name': os.environ.get(f"{drone_plugin_prefix}_SERVICE_NAME", None),
            'input_delay': int(os.environ.get(f"{drone_plugin_prefix}_INPUT_DELAY", "15")),
            'input_id': os.environ.get(f"{drone_plugin_prefix}_USER_INPUT_ID", "UserInput"),
        },
        'auth': {
            'username': os.environ.get(f"{drone_plugin_prefix}_AUTH_USERNAME", None),
            'password': os.environ.get(f"{drone_plugin_prefix}_AUTH_TOKEN", None),
        }
    }
