#!/usr/bin/env groovy

def bob = "bob/bob -r \${WORKSPACE}/cicd_files/external/jenkins/rulesets/UpdateBaselineVersion.yaml"
def RETRY_ATTEMPT = 1

pipeline {
    agent {
        node {
            label SLAVE
        }
    }

    options {
        ansiColor('xterm')
    }

    stages {
        stage('Cleaning Git Repo') {
            steps {
                sh 'git clean -xdff'
                sh 'git submodule sync'
                sh 'git submodule update --init --recursive'
            }
        }
        stage ('Update version') {
            steps {
                retry(count: 3) {
                    script{
                        if (RETRY_ATTEMPT > 1) {
                            sh "${bob} hard-reset"
                            echo "Rerunning the \"Update Version\" stage. Retry ${RETRY_ATTEMPT} of 3. Sleeping before retry..."
                            sleep(5)
                        }
                        else {
                            echo "Running the \"Update Version\" stage. Try ${RETRY_ATTEMPT} of 3"
                        }
                        RETRY_ATTEMPT = RETRY_ATTEMPT + 1
                        sh "${bob} pull-latest-changes"
                        sh "${bob} update-versions-file-with-new-install-baseline"
                        sh "${bob} push-changes-to-version-file-if-required"
                        RETRY_ATTEMPT = 1
                    }
                }
            }
        }
        stage('Set Build Name') {
            steps {
                script {
                    currentBuild.displayName = "${currentBuild.number} ${params.KEY_TO_UPDATE_BASELINE_VERSION_OF}:${params.NEW_BASELINE_VERSION}"
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}