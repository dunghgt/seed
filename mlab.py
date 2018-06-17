import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds111299.mlab.com:11299/caytrong

host = "ds111299.mlab.com"
port = 11299
db_name = "caytrong"
user_name = "dangdung"
password = "haha1234"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
