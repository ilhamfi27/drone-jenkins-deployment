# Drone Plugin for Jenkins Deployment
A Drone plugin for Jenkins deployment is a software component designed to enable the integration of the Drone Continuous Integration/Continuous Deployment (CI/CD) platform with Jenkins, a popular automation server. This integration allows developers to automate the deployment of their applications and services through Jenkins using the features and capabilities provided by Drone.

## How to Use
On your .drone.yml add step with this plugin.
```yml
  # ...
  - name: build jenkins
    image: ilhamfadhilah/drone-jenkins-deployment:v1.0.0
    settings:
      jenkins_host: # jenkins host (mandatory)
        from_secret: jenkins_host_secret
      auth_username: # jenkins auth username (mandatory)
        from_secret: auth_username_secret
      auth_token: # jenkins auth token (mandatory)
        from_secret: auth_token_secret
      jenkins_job: # jenkins job (mandatory)
      stage: # which stage to deploy? production/staging (mandatory)
      service_name: # your service name (mandatory)
      input_delay: # input delay
      user_input_id: # user input
  # ...
```