pipeline {
    agent any

    stages {
        stage('Env Prep') {
            steps {
                echo "Installing Python Deps"
                sh 'pip3 install -r requirements.txt --user'
            }
        }
        stage('Gen Unittest Report') {
            steps {
                echo "Running Unittest and Creating Report"
                sh 'python3 -m pytest test_unittest1.py  > test-report.txt'
            }
        }
        stage('Test Run'){
            steps {
                sh 'python3 app.py'
            }
        }
    }
}
