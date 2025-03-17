provider "aws" {
  region = "us-west-2"  # Change this to your desired region
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  
  name = "eks-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-west-2a", "us-west-2b", "us-west-2c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = true
  
  tags = {
    Environment = "dev"
    Terraform   = "true"
  }
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = "ray-cluster-robin-2"
  cluster_version = "1.32"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  cluster_endpoint_public_access = true
  cluster_endpoint_private_access = true

  eks_managed_node_groups = {
    # ray_cpu = {
    #   min_size     = 2
    #   max_size     = 5
    #   desired_size = 2

    #   instance_types = ["g5.4xlarge"]
    #   capacity_type  = "ON_DEMAND"
    #   ami_type       = "BOTTLEROCKET_x86_64_NVIDIA"
    # }
    ray_gpu = {
      min_size     = 2
      max_size     = 5
      desired_size = 2

      instance_types = ["g5.2xlarge"]
      capacity_type  = "ON_DEMAND"
      disk_size      = 500
      # Use the GPU-optimized AMI
      ami_type       = "BOTTLEROCKET_x86_64_NVIDIA"  # Amazon Linux 2 with GPU support
      
      block_device_mappings = {
        xvda = {
          device_name = "/dev/xvdb"
          ebs = {
            volume_size           = 500
            volume_type           = "gp3"
            delete_on_termination = true
          }
        }
      }
    }
  }

  tags = {
    Environment = "dev"
    Terraform   = "true"
  }
} 