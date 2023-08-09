import json
import time
from jenkinsapi.jenkins import Jenkins
from src.config import config
from src.request import Request

build_params = {
    "parameter": [
        {"name": "Deploy", "value": "Deploy"},
        {"name": "CHOICES", "value": "staging"},
        {"name": "SERVICENAME", "value": "apim-developer-portal"}
    ]
}
conf = config()

req = Request(conf['host'], conf['auth'])


def get_server_instance():
    jenkins_url = conf['host']

    print(f'get server instance: {jenkins_url} - start')
    server = Jenkins(jenkins_url,
                     username=conf['auth']['username'],
                     password=conf['auth']['password']
                     )
    print(f'get server instance: {jenkins_url} - done')
    return server


def build_job():
    server = get_server_instance()
    print(f'build job: {conf["jenkins_job"]} - start')
    job = server.get_job(conf['jenkins_job'])

    # Invoking Job
    job.invoke(quiet_period=0)
    print(f'build job: {conf["jenkins_job"]} - done')

    print(f'wait sleep for {conf["deployment"]["input_delay"]} seconds')

    # Wait for 1 second
    time.sleep(conf['deployment']['input_delay'])

    print(f'fill job input: {conf["jenkins_job"]} - start')
    # Get latest build number
    latest_build = job.get_last_buildnumber()

    # get jenkins job: apim-gitops/master
    jenkins_job = conf['jenkins_job'].split('/')
    build_input = {
        "parameter": [
            {"name": "Deploy", "value": "Deploy"},
            {"name": "CHOICES", "value": conf['deployment']['stage']},
            {"name": "SERVICENAME",
                "value": conf['deployment']['service_name']}
        ]
    }
    payload = {"json": json.dumps(build_input)}
    req.post(
        f"/job/{jenkins_job[0]}/job/{jenkins_job[1]}/{latest_build}/input/{conf['deployment']['input_id']}/submit?proceed=Proceed",
        data=payload
    )
    print(f'resume deploy: {conf["jenkins_job"]} for ${conf["deployment"]["service_name"]} to ${conf["deployment"]["stage"]} - done')
