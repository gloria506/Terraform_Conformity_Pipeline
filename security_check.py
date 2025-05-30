# security_check.py
import yaml

def check_bucket_public_access(bucket_properties):
    if 'AccessControl' in bucket_properties and bucket_properties['AccessControl'] == 'PublicRead':
        return "Bucket has public read access, which is a security risk."
    return None

def main():
    with open("template.yaml", 'r') as file:
        template = yaml.safe_load(file)

    resources = template.get('Resources', {})
    issues = []

    for name, resource in resources.items():
        if resource['Type'] == 'AWS::S3::Bucket':
            props = resource.get('Properties', {})
            issue = check_bucket_public_access(props)
            if issue:
                issues.append(f"{name}: {issue}")

    if issues:
        print("Security Issues Found:")
        for issue in issues:
            print(f" - {issue}")
        exit(1)
    else:
        print("No security issues found.")

if __name__ == "__main__":
    main()

