pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                // Creates a virtual environment and installs your requirements
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Runs pytest and generates the report
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=results.xml
                '''
            }
        }
    }

    post {
        always {
            // This makes the results show up in Jenkins just like Maven results!
            junit 'results.xml'
        }
    }
}