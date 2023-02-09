import json


class JsonBuilder():
    
    
    def get_json(self, *args):
        if (len(args) ==1):
            return json.dumps({'tables':args[0]})
        else:
            return json.dumps({'tables':args[0], args[1]:args[2]})
        
        