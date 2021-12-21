node{
  def app
  stage('Clone Repository'){
      checkout scm
  }
  
  stage('Build Image'){
      app = docker.build('jchatter123/first_repo')
  }
  
  stage('Test Image'){
    app.inside {
        sh 'echo "hello test"'
    }
  }
  
  stage('Push Image'){
    docker.withRegistry('https://registry.hub.docker.com', 'git'){
      app.push("${env.BUILD_NUMBER}")
      app.push("latest")
    }
  }
}
