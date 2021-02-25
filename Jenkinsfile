pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.5.1'
                }
            }
            steps {
                sh 'python -m py_compile main.py user_details.py'
                stash(name: 'compiled-results', includes: '*.py')
            }
        }
        stage('Test') { 
            agent {
                docker {
                    image 'qnib/pytest' 
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml main.py' 
                sh './gradlew check'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                    junit 'build/reports/**/*.xml' 
                }
            }
        }
    }
}