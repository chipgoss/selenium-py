pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = "1"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                    "C:\\Users\\cagoss\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    call venv\\Scripts\\activate
                    pytest --junitxml=results.xml
                """
            }
        }
    }

    post {
        always {
            junit 'results.xml'
        }
    }
}