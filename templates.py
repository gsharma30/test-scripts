import json
import requests

ORG = "org"
PARENT_TEAM = "parent"
GIT_REPO = "https://github.com/gsharma30/greenops_test.git"
N = 50

TEAM_TEMPLATE = "team_{}"
PIPELINE_TEMPLATE = "pipeline{}"
ATLAS_URL = "https://localhost:8081/"
PIPELINE_CREATION_TEMPLATE = ATLAS_URL + "pipeline/{}/{}/{}"
TEAM_CREATION_TEMPLATE = ATLAS_URL + "team/{}/{}/{}"
PIPELINE_SYNC_TEMPLATE = ATLAS_URL+"sync/{}/{}/{}/{}"

ARGO_CD_CREDS = {'username': "admin", 'password': "bmc1kSiRPhx7n3Gt"}
REVISION_HASH = 'ROOT_COMMIT'


def get_auth_cookie():
    body = json.dumps(ARGO_CD_CREDS).encode("utf-8")
    r = requests.post('https://localhost:8080/api/v1/session', data=body, verify=False)
    token = json.loads(r.text)['token']
    cookie = {"Authorization": token}
    return cookie
