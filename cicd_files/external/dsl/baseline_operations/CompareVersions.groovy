import common_classes.CommonSteps
import common_classes.CommonParameters

CommonSteps commonSteps = new CommonSteps()
CommonParameters commonParams = new CommonParameters()


def pipelineBeingGeneratedName = 'BASE-VERS_Compare_Version_With_Baseline_Version'

pipelineJob(pipelineBeingGeneratedName) {
    description(commonSteps.defaultJobDescription(pipelineBeingGeneratedName,
        "<p>The job compares a specified version with the baseline version stored in the baseline-versions repo.</p>",
        "cicd_files/external/dsl/baseline_operations/CompareVersions.groovy",
        "cicd_files/external/jenkins/baseline_operations/CompareVersions.Jenkinsfile",
        "cicd_files/external/jenkins/rulesets/CompareVersions.yaml"))

    parameters {
        stringParam(commonParams.slave())
        stringParam('VERSION_FOR_COMPARISON', '', 'The version which is to be compared against the baseline version stored in the baseline-versions repo.')
        stringParam('BASELINE_VERSION_IN_REPO', '', 'The baseline version currently stored in the baseline-versions repo.')
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
            scriptPath('cicd_files/external/jenkins/baseline_operations/CompareVersions.Jenkinsfile')
        }
    }
}
