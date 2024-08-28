#!/usr/bin/env groovy

def bob = "bob/bob -r \${WORKSPACE}/cicd_files/external/jenkins/rulesets/CompareVersions.yaml"

pipeline {
    agent {
        node {
            label SLAVE
        }
    }

    stages {
        stage('Cleaning Git Repo') {
            steps {
                sh 'git clean -xdff'
                sh 'git submodule sync'
                sh 'git submodule update --init --recursive'
            }
        }
        stage('Build Compare Versions Image') {
            steps {
                sh "${bob} build-compare-versions"
            }

        }
        stage('Run Compare Versions Python Script') {
            steps {
                sh "${bob} run-compare-versions"
            }
        }
        stage('Write Result To Artifact Properties File') {
            steps {
                sh "${bob} write-result-to-artifact-properties"
            }
        }
        stage('Archive Artifact Properties File') {
            steps {
                archiveArtifacts artifacts: 'artifact.properties', onlyIfSuccessful: true
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
