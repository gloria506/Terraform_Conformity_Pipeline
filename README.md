# Terraform_Conformity_Pipeline
This project automates the deployment of AWS CloudFormation templates using a CI/CD pipeline integrated with Cloud One – Conformity Template Scanner to ensure all infrastructure follows security best practices and compliance standards before going live.


This project sets up a CI/CD pipeline on AWS using CodeCommit, CodeBuild, and CodePipeline to automatically deploy and validate AWS CloudFormation templates. It integrates **Trend Micro Cloud One – Conformity Template Scanner** to check the templates for security, compliance, and best practice issues before deployment.

The pipeline works as follows:
1. You commit a CloudFormation template to AWS CodeCommit.
2. AWS CodePipeline triggers the process.
3. AWS CodeBuild runs the template through the Conformity Template Scanner.
4. The scanner outputs a report highlighting any issues.
5. You fix any problems found and re-commit the updated template.
6. The pipeline re-runs and ensures the template passes all checks.

This automation helps ensure your infrastructure is secure and follows cloud best practices before it goes live.
