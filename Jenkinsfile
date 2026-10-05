pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\bhask\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    stages {

        stage('Python Version') {
            steps {
                bat '"%PYTHON%" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install --upgrade pip'
                
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"%PYTHON%" -m pytest'
            }
        }

        stage('Build') {
            steps {
                echo 'Build completed successfully!'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }

        success {
            echo 'Pipeline successful!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
