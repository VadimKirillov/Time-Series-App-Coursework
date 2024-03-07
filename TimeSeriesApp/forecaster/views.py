from django.shortcuts import render
import pandas as pd
from .forms import DataFrameForm
from .models import DataFrame


def dataset_size(request):
    dataset = pd.read_csv('forecaster/csvs/all_streams.csv', sep = ';')

    data_dictionary = {}

    # Получаем список всех колонок в датасете
    columns = dataset.columns

    # Для каждой колонки добавляем название колонки и массив значений в словарь
    for col in columns:
        data_dictionary[col] = dataset[col].values

    print(data_dictionary)

    dataset_info = {
        'n_columns': dataset.shape[1],
        'n_rows': dataset.shape[0],
        'columns': dataset.columns.tolist(),
        'column_types': dataset.dtypes.to_dict(),
        'gulfstqe': dataset['gulfstqe'],
        'gulfstqh': dataset['gulfstqh'],
        'labseaqe': dataset['labseaqe'],
        'labseaqh': dataset['labseaqh'],
        'tropqe': dataset['tropqe'],
        'tropqh': dataset['tropqh'],
        'value_columns': data_dictionary,

    }


    #print(dataset_info)


    return render(request, 'index.html', {'dataset_info': dataset_info})


def upload_dataframe(request):
    if request.method == 'POST':
        form = DataFrameForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            df = pd.read_csv(csv_file)
            num_rows, num_columns = df.shape
            dataframe_obj = DataFrame.objects.create(
                csv_file=csv_file,
                filename=csv_file.name,
                num_rows=num_rows,
                num_columns=num_columns
            )
            context = {'filename': dataframe_obj.filename, 'num_rows': num_rows, 'num_columns': num_columns}
            return render(request, 'dataframes/dataframe_info.html', context)
    else:
        form = DataFrameForm()
    return render(request, 'upload_dataframe.html', {'form': form})