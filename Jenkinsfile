pipeline {
    agent any
    stages {
        stage('rocketmq cluster start'){
            steps {
                sh 'docker run -d --name rmqnamesrv rocketmqinc/rocketmq:4.5.0 sh mqnamesrv'
                sh 'docker run -d --name rmqbroker --link rmqnamesrv:namesrv -e "NAMESRV_ADDR=namesrv:9876" -e "JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.232.b09-0.el7_7.x86_64/jre" rocketmqinc/rocketmq:4.5.0 sh mqbroker'
                sh 'sleep 10'
                sh 'docker exec rmqbroker sh ./mqadmin updateTopic -n namesrv:9876 -b localhost:10911 -t test'
            }
        }
        stage('Debian - Python 2'){
            agent {
                dockerfile {
                    filename 'Dockerfile.debian.python2'
                    args '-u root -e "NAMESRV_ADDR=namesrv:9876" --link rmqnamesrv:namesrv'
                }
            }
            steps {
                sh 'pytest --cov=rocketmq -v tests --junitxml=./test_output.xml'
                junit '*.xml'
                sh 'codecov'
            }
        }
        stage('Debian - Python 3'){
            agent {
                dockerfile {
                    filename 'Dockerfile.debian.python3'
                    args '-u root -e "NAMESRV_ADDR=namesrv:9876" --link rmqnamesrv:namesrv'
                }
            }
            steps {
                sh 'pytest --cov=rocketmq -v tests --junitxml=./test_output.xml'
                junit '*.xml'
                sh 'codecov'
            }
        }
        stage('Centos7 - Python 2'){
            agent {
                dockerfile {
                    filename 'Dockerfile.centos7.python2'
                    args '-u root -e "NAMESRV_ADDR=namesrv:9876" --link rmqnamesrv:namesrv'
                }
            }
            steps {
                sh 'pytest --cov=rocketmq -v tests --junitxml=./test_output.xml'
                junit '*.xml'
                sh 'codecov'
            }
        }
        stage('Centos7 - Python 3'){
            agent {
                dockerfile {
                    filename 'Dockerfile.centos7.python3'
                    args '-u root -e "NAMESRV_ADDR=namesrv:9876" --link rmqnamesrv:namesrv'
                }
            }
            steps {
                sh 'python -m pytest --cov=rocketmq -v tests --junitxml=./test_output.xml'
                junit '*.xml'
                sh 'python -m codecov'
            }
        }
//         stage('Centos6 - Python 2'){
//             agent {
//                 dockerfile {
//                     filename 'Dockerfile.centos6.python2'
//                     args '-u root -e "NAMESRV_ADDR=namesrv:9876" --link rmqnamesrv:namesrv'
//                 }
//             }
//             steps {
//                 sh 'python -m pytest --cov=rocketmq -v tests --junitxml=./test_output.xml'
//                 junit '*.xml'
//                 sh 'python -m codecov'
//             }
//         }
//         stage('Centos6 - Python 3'){
//             agent {
//                 dockerfile {
//                     filename 'Dockerfile.centos6.python3'
//                     args '-u root -e "NAMESRV_ADDR=namesrv:9876" --link rmqnamesrv:namesrv'
//                 }
//             }
//             steps {
//                 sh 'python -m pytest --cov=rocketmq -v tests --junitxml=./test_output.xml'
//                 junit '*.xml'
//                 sh 'python -m codecov'
//             }
//         }
        stage('Ubuntu - Python 2'){
            agent {
                dockerfile {
                    filename 'Dockerfile.ubuntu.python2'
                    args '-u root -e "NAMESRV_ADDR=namesrv:9876" --link rmqnamesrv:namesrv'
                }
            }
            steps {
                sh 'python -m pytest --cov=rocketmq -v tests --junitxml=./test_output.xml'
                junit '*.xml'
                sh 'python -m codecov'
            }
        }
        stage('Ubuntu - Python 3'){
            agent {
                dockerfile {
                    filename 'Dockerfile.ubuntu.python3'
                    args '-u root -e "NAMESRV_ADDR=namesrv:9876" --link rmqnamesrv:namesrv'
                }
            }
            steps {
                sh 'python -m pytest --cov=rocketmq -v tests --junitxml=./test_output.xml'
                junit '*.xml'
                sh 'python -m codecov'
            }
        }
    }
    post {
        always {
            sh 'docker stop  `docker ps -aq --filter name=rmqbroker`'
            sh 'docker rm  `docker ps -aq --filter name=rmqbroker`'
            sh 'docker stop  `docker ps -aq --filter name=rmqnamesrv`'
            sh 'docker rm  `docker ps -aq --filter name=rmqnamesrv`'
        }
    }
}