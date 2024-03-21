from django.shortcuts import render, redirect, get_object_or_404
import pandas as pd
from .models import Dataset
from .forms import DatasetForm
from django.views.generic import CreateView, UpdateView, DeleteView


def dataset_list(request):
    datasets = Dataset.objects.all()
    return render(request, 'dataset_list.html', {'datasets': datasets})

class DatasetCreate(CreateView):
    # Модель куда выполняется сохранение
    model = Dataset
    # Класс на основе которого будет валидация полей
    form_class = DatasetForm
    # Шаблон с помощью которого
    #будут выводиться данные
    template_name = 'create_dataset.html'
    # На какую страницу будет перенаправление
    #в случае успешного сохранения формы
    success_url = '/datasets/'

def home(request):
    return render(request, 'home.html')


def create_dataset(request):
    return render(request, 'home.html')


def dataset_size(request):
    dataset = pd.read_csv('forecaster/csvs/all_streams.csv', sep=';')

    data_dictionary = {}
    HISTORY_LENGTH = 1000

    # Получаем список всех колонок в датасете
    columns = dataset.columns

    # Для каждой колонки добавляем название колонки и массив значений в словарь
    for col in columns:
        data_dictionary[col] = dataset[col].values

    # print(data_dictionary)

    train_data_dictionary = {}  # Словарь для обучающих данных
    test_data_dictionary = {}  # Словарь для тестовых данных

    for col in data_dictionary.keys():
        col_data = data_dictionary[col]
        train_data = col_data[:-HISTORY_LENGTH]
        test_data = col_data[-HISTORY_LENGTH:]

        train_data_dictionary[col] = train_data
        test_data_dictionary[col] = test_data

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
        'train_values': train_data_dictionary,
        'test_values': test_data_dictionary,

    }

    # print(dataset_info)

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
