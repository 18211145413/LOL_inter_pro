import pytest;

import os;

pytest.main(["-sv","-k","manage","../case_f/goods_doctor_sele.py","--alluredir","../report_f/data"]);

os.system("allure generate ../report_f/data -o ../report_f/html --clean");