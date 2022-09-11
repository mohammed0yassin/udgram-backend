# Udgram Backend

## Required Environment Variables
| Environment Variable        | Description                                                 |
|         :-:                 |     :-:                                                     |
| POSTGRES_USERNAME           | Database Username (Automatticaly added to ansible)          |
| POSTGRES_PASSWORD           | Database Password (Automatticaly added to ansible)          |
| POSTGRES_HOST               | Database Host (from cloudformation outputs)                 |
| POSTGRES_DB                 | Database Name  `postgres`                                   |
| PORT                        | Port the host the backend MUST BE: `80`                     |
| JWT_SECRET                  | Random text to create the secret                            |
| ANSIBLE_HOST_KEY_CHECKING   | Disable ansible host checking MUST BE: `False`              |

## Add SSH keys to CircleCi
1) Go to project setting
2) Add ec2acc.pem and backendprivate.pem to ssh keys without hostname