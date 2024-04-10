# Glueproject

1. Create core glue features from scratch by adding AWS users, roles ,policies and creating S3 buckets, KMS keys, SNS notification etc
2. Use codeformation templates to advance further

## 1. Glue catalog

## 2. Glue Crawler

## Glue Classifier 


## 1. Authentication
users | user groups | IAM Role
## 2. Authorization 
IAM policy { Effect:  , Action: , Resource: }
Role -  "trusted entity": who can assume this role

### Types of policies
- Customer managed policy 
-   inline: attach to only on a particular identity
-   Managed Policy: can be attached to multiple identities
- AWS managed policy - created and managed by aws 

### Policy types
- Identity based:granted to identity(users,groups, IAM roles) to grant permission
- Resource based:  can be attached to resources such as s3, KMS

## ----------------------- L A B -----------------------
IAM 
- user user101. demouser101
-   login, program access(CLI),
-   permissions - none
- usergroup - usergroup101 - attach 'admin' policy
-   user101=>usergroup101
- role101
trusted entity:glue service
policy: awsgeneralrole


## ------------------------------- Executing Glue on collab -----------------
glue on colab

# Reference 
https://www.tecracer.com/blog/2021/06/what-i-wish-somebody-had-explained-to-me-before-i-started-to-use-aws-glue.html
