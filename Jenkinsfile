pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                checkout scm
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'docker build -t your-django-app .'
                sh 'docker run your-django-app python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'docker-compose up -d'  // Use the sh step to execute the shell command
            }
        }
    }
}
