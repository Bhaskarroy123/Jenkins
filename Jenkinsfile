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
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"%PYTHON%" -m pytest tests'
            }
        }

        stage('Build') {
            steps {
                bat '"%PYTHON%" -m py_compile app.py'
                echo 'Student Feedback Application built successfully!'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                start "FlaskApp" /B "%PYTHON%" app.py
                '''

                bat '''
                ping 127.0.0.1 -n 6 > nul
                '''

                bat '''
                curl http://localhost:5000
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }

        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed!'
        }
    }
}
