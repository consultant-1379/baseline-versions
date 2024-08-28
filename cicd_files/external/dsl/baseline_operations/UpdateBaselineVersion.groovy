import common_classes.CommonSteps
import common_classes.CommonParameters

CommonSteps commonSteps = new CommonSteps()
CommonParameters commonParams = new CommonParameters()


def pipelineBeingGeneratedName = 'BASE-VERS_Update_Baseline_Version_In_Repository'

pipelineJob(pipelineBeingGeneratedName) {
    description(commonSteps.defaultJobDescription(pipelineBeingGeneratedName,
        "<p>The job updates the baseline version in a given versions file.</p>",
        "cicd_files/external/dsl/baseline_operations/UpdateBaselineVersion.groovy",
        "cicd_files/external/jenkins/baseline_operations/UpdateBaselineVersion.Jenkinsfile",
        "cicd_files/external/jenkins/rulesets/UpdateBaselineVersion.yaml"))

    parameters {
        stringParam(commonParams.slave())
        stringParam('VERSIONS_FILENAME', '', 'The name of the versions file to be used. Enter one of the following: [versions, autoapp_versions]')
        stringParam('KEY_TO_UPDATE_BASELINE_VERSION_OF', '', 'The key in the version file, you wish to update the version for.')
        stringParam('NEW_BASELINE_VERSION', '', 'The new baseline version to update.')
    }
    disabled(false)
    keepDependencies(false)
    logRotator(commonSteps.defaultLogRotatorValues())

    properties {
        disableConcurrentBuilds {
            abortPrevious(false)
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
                }
            }
            scriptPath('cicd_files/external/jenkins/baseline_operations/UpdateBaselineVersion.Jenkinsfile')
        }
    }
}
