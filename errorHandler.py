def UserErrorHandler(name, age, phone, security, password):
    errorList = []
    # Name validation
    if not name or len(name) < 1 or name.isspace():
        errorList.append("You can not enter in an empty name")

    # Phone validation
    if not phone or len(phone) < 1 or phone.isspace():
        errorList.append("You can not enter in an empty phone number")
        
    # Age validation
    try:
        age_int = int(age)
        if age_int <= 0 or age_int > 121:
            errorList.append("The Age must be a whole number greater than 0 and less than 121")
    except (ValueError, TypeError):
        errorList.append("The Age must be a whole number greater than 0 and less than 121")
        
    # Security validation
    try:
        security_int = int(security)
        if security_int < 1 or security_int > 3:
            errorList.append("The SecurityLevel must be a numeric between 1 and 3")
    except (ValueError, TypeError):
        errorList.append("The SecurityLevel must be a numeric between 1 and 3")
        
    # Password validation
    if not password or len(password) < 1 or password.isspace():
        errorList.append("You can not enter in an empty pwd")
    return errorList

def ContestEntryErrorHandler(name, excellentVotes, okVotes, badVotes):
    errorList = []
    # Name validation
    if not name or len(name) < 1 or name.isspace():
        errorList.append("You can not enter in an empty name")

    # Excelent Votes validation
    try:
        votes = int(excellentVotes)
        if votes < 0:
            errorList.append("The Excellent Votes must be a whole number greater than or equal to 0")
    except (ValueError, TypeError):
        errorList.append("The Excellent Votes must be a whole number greater than or equal to 0")

    # Ok Votes validation
    try:
        votes = int(okVotes)
        if votes < 0:
            errorList.append("The Ok Votes must be a whole number greater than or equal to 0")
    except (ValueError, TypeError):
        errorList.append("The Ok Votes must be a whole number greater than or equal to 0")
        
    # Bad Votes validation
    try:
        votes = int(badVotes)
        if votes < 0:
            errorList.append("The Bad Votes must be a whole number greater than or equal to 0")
    except (ValueError, TypeError):
        errorList.append("The Bad Votes must be a whole number greater than or equal to 0")

    return errorList