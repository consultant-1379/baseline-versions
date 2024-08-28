#!/usr/bin/env groovy

def bob = "bob/bob -r \${WORKSPACE}/cicd_files/external/jenkins/rulesets/RetrieveBaselineVersion.yaml"

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
        stage('Retrieve Required Baseline Version') {
            steps {
                sh "${bob} retrieve-required-baseline-version"
            }
        }
        stage('Write Retrieved Version To Artifact Properties File') {
            steps {
                sh "${bob} write-version-to-artifact-properties"
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
