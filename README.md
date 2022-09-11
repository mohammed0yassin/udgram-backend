# Udgram Backend

## Required Environment Variables
| Environment Variable        | Description                                                 |
|         :-:                 |     :-:                                                     |
| BASTION_HOST                | Bastion host public dns name (from cloudformation outputs)  |
| POSTGRES_USERNAME           | Database Username (Automatticaly added to ansible)          |
| POSTGRES_PASSWORD           | Database Password (Automatticaly added to ansible)          |
| POSTGRES_HOST               | Database Host                                               |
| POSTGRES_DB                 | Database Name                                               |
| PORT                        | Port the host the backend MUST BE: `80`                     |
| JWT_SECRET                  | Random text to create the secret                            |
| ANSIBLE_HOST_KEY_CHECKING   | Disable ansible host checking MUST BE: `False`              |

