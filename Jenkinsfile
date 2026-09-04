pipeline {
agent any

stages {

    stage('Check Out SCM') {
        steps {
            checkout scm
        }
    }

    stage('Build Image') {
        steps {
            sh 'docker build -t ghcr.io/khushi-mishra13/python-calculator:latest .'
        }
    }

    stage('Push it to GHCR') {
        steps {
            withCredentials([
                usernamePassword(
                    credentialsId: 'github-token-id',
                    usernameVariable: 'username',
                    passwordVariable: 'password'
                )
            ]) {
                sh '''
                    echo "$password" | docker login ghcr.io -u "$username" --password-stdin
                    docker push ghcr.io/khushi-mishra13/python-calculator:latest
                '''
            }
        }
    }

    stage('Deployment') {
        steps {
            sshagent(credentials: ['khushi-vm']) {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'github-token-id',
                        usernameVariable: 'username',
                        passwordVariable: 'password'
                    )
                ]) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no -p 5125 khushi@192.168.7.102 << EOF

                            echo "$password" | docker login ghcr.io -u "$username" --password-stdin

                            docker rm -f blue-app || true

                            docker pull ghcr.io/khushi-mishra13/python-calculator:latest

                            docker run -d \
                                --name blue-app \
                                -p 5000:5000 \
                                -e VERSION=Blue-V1 \
                                ghcr.io/khushi-mishra13/python-calculator:latest


EOF
'''
}
}
}
}
}
}
