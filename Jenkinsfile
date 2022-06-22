pipeline {
  agent any
  stages {
    stage('Clone') {
      steps {
        git(url: 'https://github.com/Sanketkalode/flaskJenkins', branch: 'master')
      }
    }

    stage('Test') {
      steps {
        sh 'echo hello'
      }
    }

  }
}