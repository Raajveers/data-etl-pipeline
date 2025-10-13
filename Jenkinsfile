pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
                // Jenkins clones your Git repo automatically, so we just print here
            }
        }

        stage('Set up Python') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run ETL Script') {
            steps {
                echo 'Running ETL script...'
                sh '''
                    source venv/bin/activate
                    python etl.py
                '''
            }
        }
    }
}
