pipeline {
    agent any
    stages {
        stage('test java') {
            agent { docker { image 'openjdk:8-jre'}}
            steps { 
                sh 'java -version'
            }
        }
        stage('test python') {
            agent { docker { image 'python:3.8.2-alpine'}}
            steps { 
                sh 'python --version'
            }
        }
        
    }
}
