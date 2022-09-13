# Udgram Backend

## Required Environment Variables
| Environment Variable        | Description                                                                      |
|         :-:                 |     :-:                                                                          |
| FRONTEND_BUCKET_NAME        | Frontend bucket name (from cloudformation outputs `FrontEndBucket`)              | 
| DatabaseSecretName          | Secret Name in Secret Manager (from cloudformation outputs `DatabaseSecretName`) |
| POSTGRES_HOST               | Database Host (from cloudformation outputs `DatabaseEndpoint`)                   |
| POSTGRES_USERNAME           | Database Username (Automatticaly added to ansible)                               |
| POSTGRES_PASSWORD           | Database Password (Automatticaly added to ansible)                               |
| POSTGRES_DB                 | Database Name  `postgres`                                                        |
| PORT                        | Port the host the backend MUST BE: `80`                                          |
| JWT_SECRET                  | Random text to create the secret                                                 |
| ANSIBLE_HOST_KEY_CHECKING   | Disable ansible host checking MUST BE: `False`                                   |

## Add SSH keys to CircleCi
1) Go to project setting
2) Add ec2acc.pem and backendprivate.pem to ssh keys without hostname
3) Modify the fingerprints values in `.circleci\config.yml`

## Pipeline status: [![mohammed0yassin](https://circleci.com/gh/mohammed0yassin/udgram-backend.svg?style=svg)](https://app.circleci.com/pipelines/github/mohammed0yassin/udgram-backend)