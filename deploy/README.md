# Flask Tic-Tac-Toe and Friends Application - AWS Deployment Guide

This guide explains how to deploy the Flask game application to AWS using Terraform. The deployment creates an ECS Fargate cluster with all necessary networking and security configurations.

## Prerequisites

- [AWS CLI](https://aws.amazon.com/cli/) installed and configured
- [Terraform](https://www.terraform.io/) (version >= 1.0.0)
- Docker image of the Flask application pushed to a container registry

## Project Structure

```
.
├── deploy/
│   ├── main.tf          # Provider configuration and variables
│   ├── network.tf       # VPC and networking configuration
│   ├── ecs.tf          # ECS cluster and service configuration
│   ├── outputs.tf       # Output values
│   └── README.md       # This file
```

## Configuration

1. Configure AWS credentials:
```bash
aws configure
```

2. Update variables as needed:
   - Default region is `us-west-2`
   - Default application name is `flask-game`
   - Default environment is `prod`
   - Container port is set to `5000`

## Deployment Steps

1. Initialize Terraform:
```bash
cd terraform
terraform init
```

2. Review the deployment plan:
```bash
terraform plan -var="docker_image=your-registry-url/flask-game:latest"
```

3. Apply the configuration:
```bash
terraform apply -var="docker_image=your-registry-url/flask-game:latest"
```

4. Wait for deployment to complete and note the outputs.

## Infrastructure Components Created

- VPC with 2 public subnets
- Internet Gateway
- Security Groups
- ECS Fargate Cluster
- ECS Task Definition
- ECS Service (2 tasks)
- CloudWatch Log Group

## Monitoring

- View logs in CloudWatch Logs under the group `/ecs/flask-game`
- Monitor ECS service health in the AWS Console

## Cleaning Up

To destroy all created resources:
```bash
terraform destroy -var="docker_image=your-registry-url/flask-game:latest"
```

## Troubleshooting

1. **Task Definition Registration Failed**
   - Verify your Docker image URL is correct
   - Ensure the image exists in your registry

2. **Tasks Not Starting**
   - Check CloudWatch Logs for container errors
   - Verify security group allows traffic on port 5000
   - Check subnet has route to internet gateway

3. **Network Issues**
   - Verify VPC configuration
   - Check security group rules
   - Ensure public IP assignment is enabled

## Cost Considerations

This deployment includes:
- Fargate tasks (charged per vCPU and memory)
- CloudWatch Logs storage
- Data transfer costs
- VPC networking components

Monitor AWS Cost Explorer to track expenses.

## Security Notes

The current configuration:
- Deploys tasks in public subnets
- Allows inbound traffic on container port (5000)
- Uses AWS CloudWatch for logging

Consider adding:
- SSL/TLS termination
- Private subnets with NAT Gateway
- More restrictive security group rules
- AWS WAF for additional protection

## Next Steps

Consider implementing:
1. Load balancer for better traffic distribution
2. Auto-scaling based on CPU/Memory usage
3. DNS configuration
4. Backup and disaster recovery procedures
