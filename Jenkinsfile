pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Set up Python') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run ETL Script') {
            steps {
                echo 'Running ETL script...'
                sh '''
                    . venv/bin/activate
                    python etl.py
                '''
            }
        }
    }
}
