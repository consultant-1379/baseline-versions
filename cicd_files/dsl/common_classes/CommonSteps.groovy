package common_classes

/**
 * Class containing Common groovy steps
 */
class CommonSteps {

    static Object defaultLogRotatorValues() {
        return {
            daysToKeep 25
            numToKeep 20
        }
    }

    static String defaultJobDescription(String jobName, String jobDescription, String groovyFilePath, String jenkinsFilePath, String rulesetFilePath=null) {
        String rulesetFilePathString = ""
        if (rulesetFilePath != null) {
            rulesetFilePathString = "<p><b>Ruleset file location:</b> <a href='https://gerrit-gamma.gic.ericsson.se/plugins/gitiles/OSS/com.ericsson.oss.cicd/baseline-versions/+/master/${rulesetFilePath}'>${rulesetFilePath}</a></p>"
        }
        return """
            <div style='width:fit-content;background:#fbf6e1;padding:1em;border-radius:1em;box-shadow: 0 0.1em 0.3em #005499bd;
            color: #242424;font-family: &quot;Ericsson Hilda&quot;, Helvetica, Arial, sans-serif;'>
            <h2> DO NOT UPDATE JOB without Contacting THUNDERBEE</h2>
            <h2 style='text-align:left;'>Job Description:</h2>
            ${jobDescription}<br/>
            <h2 style='text-align:left;'>Job Information:</h2>
            <p><b>Repository:</b> <a href="https://gerrit-gamma.gic.ericsson.se/#/q/project:OSS/com.ericsson.oss.cicd/baseline-versions">OSS/com.ericsson.oss.cicd/baseline-versions</a></p>
            <p><b>Groovy file location:</b> <a href='https://gerrit-gamma.gic.ericsson.se/plugins/gitiles/OSS/com.ericsson.oss.cicd/baseline-versions/+/master/${groovyFilePath}'>${groovyFilePath}</a></p>
            <p><b>Jenkinsfile location:</b> <a href='https://gerrit-gamma.gic.ericsson.se/plugins/gitiles/OSS/com.ericsson.oss.cicd/baseline-versions/+/master/${jenkinsFilePath}'>${jenkinsFilePath}</a></p>
            ${rulesetFilePathString}
            <p style="text-align:center"><b>&#x26A1; Job developed and maintained by Thunderbee &#x26A1;</b><br/>
            <a href="mailto:PDLENMCOUN@pdl.internal.ericsson.com?Subject=${jobName}%20Job">&#128231; Send Mail to provide feedback</a></p>
            </div>"""
    }
}
