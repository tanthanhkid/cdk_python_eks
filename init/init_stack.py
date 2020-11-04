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
        
    def getOrCreateVPC(self):

        vpc_name = "EKS-VPC"
        vpc_cidr =  "10.10.0.0/18"


        #vpc = ec2.Vpc(self,"my-vpc",cidr="10.0.0.0/16",max_azs=2,nat_gateways=1 )
        if(self.node.try_get_context('use_default_vpc')=='1'):
            ec2.Vpc.from_lookup(self,vpc_name=vpc_name,is_default=true)
        else
            if(self.node.try_get_context("use_default_vpc")):
                ec2.Vpc.from_lookup(self,vpc_name=vpc_name,vpc_id=self.node.try_get_context("use_default_vpc"))
            else
                ec2.Vpc(self,vpc_name=vpc_name,cidr=vpc_cidr,max_azs=2,nat_gateways=1,subnet_configuration=)