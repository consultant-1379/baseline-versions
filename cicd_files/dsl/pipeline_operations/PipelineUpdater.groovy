import common_classes.CommonSteps
import common_classes.CommonParameters

CommonSteps commonSteps = new CommonSteps()
CommonParameters commonParams = new CommonParameters()


def pipelineBeingGeneratedName = "baseline-versions_Pipeline_Updater"

pipelineJob(pipelineBeingGeneratedName) {
    description(commonSteps.defaultJobDescription(pipelineBeingGeneratedName,
        "<p>The ${pipelineBeingGeneratedName} job updates the Jenkins Pipelines for the Baseline Versions repo.</p>",
        "cicd_files/dsl/pipelines_operations/PipelineUpdater.groovy",
        "cicd_Files/jenkins/files/pipeline_operations/PipelineUpdater.Jenkinsfile"))

    parameters {
        stringParam(commonParams.slave())
    }

    logRotator(commonSteps.defaultLogRotatorValues())

    triggers {
        gerrit {
            project(commonParams.repo(), "master")
            events {
                changeMerged()
            }
        }
    }

    definition {
        cpsScm {
            scm {
                git {
                    branch('master')
                    remote {
                        url(commonParams.repoUrl())
                    }
                    extensions {
                        cleanBeforeCheckout()
                        localBranch 'master'
                    }
                }
            }
            scriptPath("cicd_files/jenkins/files/pipeline_operations/PipelineUpdater.Jenkinsfile")
        }
    }
}
