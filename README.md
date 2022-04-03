## AWS, Terraform, and Python Diagrams
### Overview
I'm going to take a diagram from #AWS and build the #terraform modules and configs necessary to deploy it. Then I will recreate the diagrams using Python. 

**Reference:**
- [AWS Reference Architecture Diagrams](https://aws.amazon.com/architecture/reference-architecture-diagrams)
- [Terraform by HashiCorp](https://www.terraform.io/)
- [Diagrams · Diagram as Code](https://diagrams.mingrammer.com/)

### Approach
_Folder structure:_
```shell
.
├── architecture
├── library
│   └── terraform-modules
└── python-diagrams
```

The approach will be pretty simple, I'll nest a directory under `architecture` and include the necessary #terraform to build that infrastructure. I'll build modules for reusability and nest those in the `library/terraform` directory. I'll then write the #python to create the diagrams and next those as individual directories under `reports`.

### Continuous integration
I'll ensure that I also configure some GitHub Actions for the #terraform and #python code. At the very least just to ensure that the code is validated and linted, etc.
