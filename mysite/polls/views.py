from django.shortcuts import render
import os
import joblib
from django.conf import settings

# Create your views here.
def convert_to_one_zero(record):
    if record == 0.076923077:
        return '1'
    elif record == 0.0:
        return '0'
    else:
        return 'none'


def home_screen_view(request):
	
    if request.method == 'POST':
        q1 = float(request.POST.get('q1', 0))
        q2 = float(request.POST.get('q2', 0))
        q3 = float(request.POST.get('q3', 0))
        q4 = float(request.POST.get('q4', 0))
        q5 = float(request.POST.get('q5', 0))
        q6 = float(request.POST.get('q6', 0))
        q7 = float(request.POST.get('q7', 0))
        q8 = float(request.POST.get('q8', 0))
        q9 = float(request.POST.get('q9', 0))
        q10 = float(request.POST.get('q10', 0))
        q11 = float(request.POST.get('q11', 0))
        q12 = float(request.POST.get('q12', 0))
        q13 = float(request.POST.get('q13', 0))

        questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13]

        converted_questions = []
        for record in questions:
            converted_value = convert_to_one_zero(record)
            converted_questions.append(converted_value)
            
        count_yes = 0
        count_no = 0

        for response in questions:
            converted_value = convert_to_one_zero(response)

            if converted_value == '1':
                count_yes += 1
            elif converted_value == '0':
                count_no += 1

        clf_path = os.path.join(settings.BASE_DIR, 'polls/dt_model.joblib')
        clf = joblib.load(clf_path)
        result_data = [converted_questions] 
        prediction = clf.predict(result_data)

        prediction2 = 'Not Poor' if prediction == 'Not Poor' else 'Poor'
        context = {
                'prediction': prediction2,
                'count_yes': count_yes,
                'count_no': count_no
            }

        return render(request, "result.html", context)

    else:
        return render(request, 'eval.html')


def result_screen_view(request):
	print(request.headers)
	return render(request, "result.html", {})