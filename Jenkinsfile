pipeline {
    agent any
    environment {
        github_url = 'https://github.com/GadCoder/FISI-Horarios-API.git'
        vps_code_folder = '/home/${credentials(user)}/code/horarios-api/'
    }

    stages {
        stage('Checkout') {
            steps {
                git "${github_url}"
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build and Deploy') {
            steps {
                script {
                    // Clone FastAPI project from Git onto VPS
                   sshagent(['oci-server']) {
                        sshScript(
                            remote: credentials('host'),
                            user: credentials('user'),
                            script: "git clone ${github_url} ${vps_code_folder}"
                        )
                    }


                    // Build Docker image on VPS
                    sshagent(['oci-server']) (
                        sshScript(
                            remote: credentials('host'),
                            user: credentials('user'),
                            script: 'cd ${vps_code_folder} && docker build -t horarios-api .'
                        )
                    )

                    // Run Docker container on VPS
                    sshagent(['oci-server']) (
                        sshScript(
                            remote: credentials('host'),
                            user: credentials('user'),
                            script: 'docker run -d -p 8080:8080 horarios-api'
                        )
                    )
                }
            }
        }
    }


}
