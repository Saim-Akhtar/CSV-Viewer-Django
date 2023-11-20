from django.shortcuts import render

from .dataloader import load_data

def patient_detail(request, patient_id):
    data_df = load_data()
    patient = data_df[data_df['patient_id'] == patient_id].to_dict('records')[0]
    patient['image_path'] = f'/media/images/{patient["patient_id"]}-{patient["series_uid"]}.jpg'
    return render(request, 'detail.html', {'patient': patient})

def datatable_view(request):
    data_df = load_data()
    data = data_df.to_dict(orient='records')

    return render(request, 'datatable.html', {'data': data})