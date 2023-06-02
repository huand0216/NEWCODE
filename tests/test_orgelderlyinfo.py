#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:Huandong
import pytest

from utils.operationExcel import OperationExcel
from utils.operationYaml import OperationYaml
from base.method import My_request
from faker import Faker

class TestElderlyInfo(object):
    excel_obj = OperationExcel(fileName="datas.xls", sheetName="老人档案")
    excelData = excel_obj.getExcelData()

    operation_yaml_obj = OperationYaml(dirName="datas",fileName="data.yaml")

    @pytest.mark.parametrize(
        "excelData",excelData
    )
    def test_elderInfo(self,excelData,getToken):
        case_id = excelData[self.excel_obj.CASE_ID]
        remarks = excelData[self.excel_obj.REMARKS]
        url = excelData[self.excel_obj.URL]
        method = excelData[self.excel_obj.METHOD]
        parameter = self.operation_yaml_obj.get_mapping_ExcelToYaml(excelData[self.excel_obj.PARAMETER])
        expect = excelData[self.excel_obj.EXPECT]

        if method == "GET":
            res = My_request().GET(
                url = url,
                headers = getToken,
                params = parameter
            )

        elif method == "POST":
            res = My_request().POST(
                url = url,
                headers = getToken,
                json = parameter
            )
            if case_id == "case001":
                new_yaml = TestElderlyInfo.operation_yaml_obj.getYaml_dict()

                elder_name = Faker(locale='zh_CN').name()
                new_yaml["case001"]["realName"]  = f"自动化新增{elder_name}"   #修改老人姓名

                from random import randint
                id_card = str(randint(1000000,999999999))
                new_yaml["case001"]["idCard"] = id_card

                #更新新的参数到yaml文件
                TestElderlyInfo.operation_yaml_obj.writeYaml(new_yaml)
        assert expect in res.text
if __name__ == '__main__':
    pytest.main(["-v","-s","test_orgelderlyinfo.py"])