#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong
import pytest
from base.method import My_request

@pytest.fixture()
def getToken():
    res = My_request().POST(
        url = "https://new.baisuiyun.com/api/admin/blade-auth/oauth/token",
        params = {"tenantKey":"fd12847b38dd4083b3fb334b9b876989","grant_type":"tenant_key","tenantId":"003864","scope":"all"},
        headers = {"Authorization":"Basic bWVjaGM6bWVjaGNfc2VjcmV0"}
    )
    # token
    token_type = str.capitalize(res.json()["token_type"])
    access_token = res.json()["access_token"]
    token = "{0} {1}".format(token_type,access_token)
    return {"blade-auth":token,"authorization":"Basic bWVjaGM6bWVjaGNfc2VjcmV0"}

if __name__ == '__main__':
    print(getToken())

