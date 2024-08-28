import common_classes.CommonSteps
import common_classes.CommonParameters

CommonSteps commonSteps = new CommonSteps()
CommonParameters commonParams = new CommonParameters()


def pipelineBeingGeneratedName = 'BASE-VERS_Retrieve_Baseline_Version'

pipelineJob(pipelineBeingGeneratedName) {
    description(commonSteps.defaultJobDescription(pipelineBeingGeneratedName,
        "<p>The job retrieves the baseline version from a given versions file.</p>",
        "cicd_files/external/dsl/baseline_operations/RetrieveBaselineVersion.groovy",
        "cicd_files/external/jenkins/baseline_operations/RetrieveBaselineVersion.Jenkinsfile",
        "cicd_files/external/jenkins/rulesets/RetrieveBaselineVersion.yaml"))

    parameters {
        stringParam(commonParams.slave())
        stringParam('VERSIONS_FILENAME', '', 'The name of the versions file to be used. Enter one of the following: [versions, autoapp_versions]')
        stringParam('KEY_TO_RETRIEVE_BASELINE_VERSION_OF', '', 'The key in the version file, you wish to retrieve the version for.')
        stringParam('SPECIFIED_VERSION_FOR_PIPELINE', '0.0.0', 'The version to run the pipeline against. You may either specifiy a version or use 0.0.0 for the version in the baseline repo.')
        stringParam(commonParams.spinnakerPipelineId())
    }
    disabled(false)
    keepDependencies(false)
    logRotator(commonSteps.defaultLogRotatorValues())
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
            scriptPath('cicd_files/external/jenkins/baseline_operations/RetrieveBaselineVersion.Jenkinsfile')
        }
    }
    quietPeriod(0)
}
