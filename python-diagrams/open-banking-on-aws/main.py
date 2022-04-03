import grp
from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.general import User, General
from diagrams.onprem.compute import Server
from diagrams.aws.management import Config
from diagrams.aws.security import Guardduty, IAM, KeyManagementService, Inspector, SecretsManager, SecurityHub, CertificateManager, Macie, FirewallManager
from diagrams.aws.network import TransitGateway, DirectConnect, VpnConnection

with Diagram("Open Banking on AWS", filename="open-banking-on-aws", outformat="png"):
    User("Consumer") >> General("Licensed / Accredited Third Party")
    VPN1 = VpnConnection("AWS VPN")
    DC1 = DirectConnect("AWS Direct Connect")

    # Create main group
    with Cluster("Bank's IT Environment"):
        with Cluster("Bank's Data Center"):
            # On prem resources go here
            grp_onprem = [
                Server("System of records"),
                General("Kafka"),
                General("MQ"),
                General("Payment Rails Integration")
            ]

        with Cluster("Networking account"):
            # Include resources from networking account
            TG1 = TransitGateway("AWS Transit Gateway")
            grp_onprem - VPN1 - TG1
            grp_onprem - DC1 - TG1

        with Cluster("AWS Security Services"):
            Guardduty("Amazon Guardduty")
            IAM("AWS Identity and Access Management")
            KeyManagementService("AWS Key Management Service")
            Inspector("Amazon Inspector")
            SecretsManager("AWS Secrets Manager")
            SecurityHub("AWS Security Hub")
            CertificateManager("AWS Certificate Manager")
            Macie("Amazon Macie")
            FirewallManager("AWS Network Firewall")
            Config("AWS Config")
