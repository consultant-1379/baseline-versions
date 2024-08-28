sectionedView('Baseline Versions CICD') {
    description('''<div style="padding:1em;border-radius:1em;text-align:center;background:#fbf6e1;box-shadow:0 0.1em 0.3em #525000">
        <b>Baseline Versions</b><br>
       CICD Pipelines and Source Control Jobs.<br><br>
        Team: <b>Thunderbee &#x26A1</b><br>
    </div>''')
    sections {
        listView {
            name('Baseline Versions CICD Pipelines')
            jobs {
                name("BASE-VERS_Compare_Version_With_Baseline_Version")
                name("BASE-VERS_Retrieve_Baseline_Version")
                name("BASE-VERS_Update_Baseline_Version_In_Repository")
            }
            columns setViewColumns()
        }
        listView {
            name('Baseline Versions CICD Pipeline Source Control')
            jobs {
                name("baseline-versions_Pipeline_Generator")
                name("baseline-versions_Pipeline_Updater")
            }
            columns setViewColumns()
        }
    }
}

static Object setViewColumns() {
    return {
        status()
        weather()
        name()
        lastSuccess()
        lastFailure()
        lastDuration()
        buildButton()
    }
}
