package common_classes

/**
 * Class containing Common groovy parameters
 */
class CommonParameters {

    static List slave(String defaultValue='GridEngine') {
        return ['SLAVE', defaultValue, 'Slave']
    }

    static String repo() {
        return 'OSS/com.ericsson.oss.cicd/baseline-versions'
    }

    static String repoUrl() {
        return '\${GERRIT_MIRROR}/'+repo()
    }

    static List spinnakerPipelineId(String defaultValue='123456') {
        return ['SPINNAKER_PIPELINE_ID', defaultValue, 'ID for Spinnaker pipeline. Used as a placeholder to migitage Jenkins 404 build errors.']
    }

}
