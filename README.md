# project_attic by Jayant

### Create a project workspace
```
mkdir ~/workspace
cd ~/workspace
git clone https://github.com/jayantdanech/project_attic.git
cd ~/workspace/project_attic
```

### Build docker image and run the docker with our application in /app
```
cd app/
docker build -t attic-app .
docker run -it -d --name app_attic -p 8080:8080 attic-app
```

At this point you will see your docker will be exposed to host port 8080 and will respond to "curl localhost:8080"

EXAMPLE
> jayant@devnode:~/workspace/project_attic/app$ curl localhost:8080
>
> {"ip":"172.17.0.1","timestamp":"2025-12-05T11:44:52.399853+00:00"}


### Configuring AWS:
Make sure you have AWS cli configured on your machine and has credentials in "~/.aws/credentials"

```
cat ~/.aws/credentials 
[default]
aws_access_key_id = *****
aws_secret_access_key = *****
```

### Export AWS Account ID in variable:
```
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
```

### Create an ECR repository
```
aws ecr create-repository --repository-name attic-app --region us-east-1
```

### Authenticate Docker to ECR
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com
```

### Tagging the application image
```
docker tag attic-app:latest ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/attic-app:latest
```

### Push image to ECR
```
docker push ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/attic-app:latest
```

## Create AWS infrastructure to host our application container

### Go back to the project folder
```
cd ~/workspace/project_attic
cd terraform
terraform init
terraform plan
terraform apply
```
