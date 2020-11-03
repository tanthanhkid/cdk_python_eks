from aws_cdk.core import App, Construct
from aws_cdk import (
    core,
    aws_iam as iam,
    aws_ec2 as ec2,
    aws_eks as eks 
)

AWS_CLUSTER_NAME="my-cluster"

class InitStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        vpc = ec2.Vpc(self,"my-vpc",cidr="10.0.0.0/16",max_azs=2,nat_gateways=1 )

        ## 3. Create an EKS Cluster
        eks_cluster = eks.Cluster(
            self, AWS_CLUSTER_NAME,
            cluster_name=AWS_CLUSTER_NAME,
            vpc=vpc, 
            default_capacity_type=eks.DefaultCapacityType.NODEGROUP,
            default_capacity_instance=ec2.InstanceType("t2.micro"),
            default_capacity=2,
            version=eks.KubernetesVersion.V1_17
        )
        