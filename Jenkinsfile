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
                powershell -Command "Start-Process -FilePath '%PYTHON%' -ArgumentList 'app.py' -WindowStyle Hidden"
                '''

                bat 'timeout /t 5 /nobreak'

                bat '''
                powershell -Command "try { Invoke-WebRequest http://localhost:5000 -UseBasicParsing | Out-Null; Write-Host 'Application is running successfully on port 5000' } catch { Write-Host 'Application deployment check failed'; exit 1 }"
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
