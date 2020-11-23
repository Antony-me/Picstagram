import uuid

def get_slug():
    code = str(uuid.uuid4())[4].replace('-', "").lower

    return code 
