from sample_data import submissions
def filter_by_date(date, submissions):
    """
    Filter submissions based off a specific date
    Paramaters:
        date(str): the day the submission was made
        submission(list of dict):the name of the student, the score, date of submission
    Returns:
        List of dict: submissions from a specific date
    """
    result = []
    for submission in submissions:
        if submission["submission_date"] == date:
            result.append(submission)
    return result


def filter_by_student_id(student_id, submissions):
    """
    Filter submissions based off student ID
    Parameters:
        student_id (int): student ID number
        submissions (list of dict): list of quiz submissions
    Returns:
        list of dict: only the submissions for a specific student
    """
    result = []
    for submission in submissions:
        if submission["student_id"] == student_id:
            result.append(submission)
    return result 


def find_unsubmitted(date, student_names, submissions):
    """
    Find who didn't submit a quiz on a specific date
    Parameters:
        date(str): day of submission
        student_names(list of str): name of the students
        submissions(list of dict): list of quiz submissions
    Returns:
        List of dict: names of students who did not turn in a quiz on that date.
    """
    unsubmitted = student_names
    filtered_submissions = filter_by_date(date, submissions)

    for submission in filtered_submissions:
        if submission["student_name"] in student_names:
            unsubmitted.remove(submission["student_name"])
    return unsubmitted


def get_average_score(submissions):
    """
    Get average from all submissions
    Parameters:
        submission (list of dict): list of submissions
    Returns: 
        Float: the average quiz score across all submissions, rounded to one decimal.
    """
    if not submissions:
        return 0.0
    quiz_total = 0
    count = 0
    for submission in submissions:
        quiz_total += submission["quiz_score"]
        count += 1
    average = quiz_total / count
    return round(average, 1)


def get_average_score_by_module(submissions):
    """
    Get average quiz scores grouped by module.
    Parameters:
        submissions (list of dict): list of submissions
    Returns:
        dict: keys are module names, values are average quiz scores for that module
    """
    if not submissions:
        return {}

    module_totals = {}   
    module_counts = {}   

    for submission in submissions:
        module = submission["quiz_module"]
        score = submission["quiz_score"]

        if module not in module_totals:
            module_totals[module] = 0
            module_counts[module] = 0

        module_totals[module] += score
        module_counts[module] += 1

    averages = {}
    for module in module_totals:
        avg = module_totals[module] / module_counts[module]
        averages[module] = round(avg, 1)

    return averages
