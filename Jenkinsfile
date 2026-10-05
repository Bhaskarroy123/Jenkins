pipeline {
    agent any

    stages {

        stage('Python Version') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m pip install --upgrade pip
                    if exist requirements.txt (
                        python -m pip install -r requirements.txt
                    )
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    if exist tests (
                        python -m pytest tests
                    ) else (
                        echo No tests directory found
                    )
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Build completed successfully'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }

        always {
            echo 'Pipeline finished.'
        }
    }
}
