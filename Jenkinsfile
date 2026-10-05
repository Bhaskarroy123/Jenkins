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

                // Start Flask application in background
                bat '''
                start "FlaskApp" /B "%PYTHON%" app.py
                '''

                // Wait and check application using Python
                bat '''
                "%PYTHON%" -c "import urllib.request, time; time.sleep(5); r=urllib.request.urlopen('http://127.0.0.1:5000'); print('Application deployed successfully. HTTP status:', r.status)"
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
