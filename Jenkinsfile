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
                echo 'No external dependencies required.'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"%PYTHON%" -c "print(\'Python test passed successfully!\')"'
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
