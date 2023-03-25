pipeline {
    agent any
    stages {
        stage('install'){
            when {
                anyOf {
                    branch "master"
                    branch "PR-*"
                }
            }
            steps {
                sh "make ci-install"
            }
        }
        stage('test') {
            // Run tox if package files have changed, tests have changed,
            // requirements have changed, this is our first build, or
            // the previous build failed
            when {
                anyOf {
                    branch "master"
                    branch "PR-*"
                }
                anyOf {
                    changeset "attribute_name_analyzer/**"
                    changeset "setup.py"
                    changeset "setup.cfg"
                    changeset "tests/**"
                    buildingTag()
                    expression {
                        return currentBuild.previousBuild == null
                    }
                    expression {
                        !("SUCCESS".equals(currentBuild.previousBuild.result))
                    }
                }
            }
            steps {
                sh 'make test'
            }
        }
        stage('distribute') {
            // Distribute if this is the master branch and setup files have
            // changed, the previous build failed, or a build tag is detected
            when {
                branch "master"
                anyOf {
                    changeset "setup.py"
                    changeset "setup.cfg"
                    buildingTag()
                    expression {
                        return currentBuild.previousBuild == null
                    }
                    expression {
                        !("SUCCESS".equals(currentBuild.previousBuild.result))
                    }
                }
            }
            steps {
                sh 'make distribute'
            }
        }
    }
}

