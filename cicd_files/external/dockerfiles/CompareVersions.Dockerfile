FROM armdocker.rnd.ericsson.se/dockerhub-ericsson-remote/python:3.8-slim-buster

RUN mkdir -m 777 -p /usr/src/app/out

WORKDIR /usr/src/app/out

ADD cicd_files/external/jenkins/scripts/compare_versions.py .

RUN pip install -U semver==3.0.0

ENTRYPOINT ["python", "/usr/src/app/out/cicd_files/external/jenkins/scripts/compare_versions.py"]
