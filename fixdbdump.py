#!/usr/bin/python

import re

with open('database.sql', 'r+') as sql_file:
    content = sql_file.read()
    sql_file.seek(0)

    new_content = "SET autocommit=0;\nSET unique_checks=0;\nSET foreign_key_checks=0;\n"

    content = re.sub("DEFAULT CHARSET=[a-z0-9]+", "", content)
    content = re.sub("COLLATE=[a-z0-9_]+", "", content)
    content = re.sub("COLLATE [a-z0-9_]+", "", content)

    new_content = new_content + content + "COMMIT;\nSET unique_checks=1;\nSET foreign_key_checks=1;\n"

    sql_file.write(new_content)