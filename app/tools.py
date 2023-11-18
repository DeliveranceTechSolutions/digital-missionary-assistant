def validate_json(json_req):
    # update fields in order to add MANDATORY params only, if you would like them to be optional
    # then do not add your parameters to this list.
    request_fields = [
        "access_token",
        "model",
        "text",
        "language",
    ]

    data = json_req['data'].keys()
    for key in data:
        print(key)
        if key not in fields:
            raise InvalidJsonError(f"Missing {key} in JSON request")

    return json_req


