import sys, json, os


def getPayload():
    file = None
    
    if os.environ.has_key('PAYLOAD_FILE'):
        file = os.environ['PAYLOAD_FILE']
    else:
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-payload' and (i + 1) < len(sys.argv):
                file = sys.argv[i + 1]
                break

    with open(file) as content:
        data = json.load(content)

    return data


def getTaskId():
    task_id = None
    
    if os.environ.has_key('TASK_ID'):
        task_id = os.environ['TASK_ID']
    else:
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-id' and (i + 1) < len(sys.argv):
                task_id = sys.argv[i + 1]
                break

    return task_id