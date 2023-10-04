from django_admin_json_editor import JSONEditorWidget

from .models import Objects, Filpic, Countpic, FiberHercImg, FiberGraffImg, PolmicPolImg, PolimicCrossImg, \
    RfaSpecImg, IRFurImg, EsmRevImg, EsmSecImg, EdsImg
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select, URLInput, FileInput, \
    MultipleChoiceField, CheckboxSelectMultiple, NumberInput, JSONField, ClearableFileInput, RadioSelect
from django_jsonform.widgets import JSONFormWidget
from django import forms

SECTION = [
    (1, 'ЗЭС'),
    (2, 'РС'),
]

FOND = [
    (1, 'Коллекция'),
    (2, 'Фонд')
]

MONTH = [
    (1, 'Январь'),
    (2, 'Февраль'),
    (3, 'Март'),
    (4, 'Апрель'),
    (5, 'Май'),
    (6, 'Июнь'),
    (7, 'Июль'),
    (8, 'Август'),
    (9, 'Сентябрь'),
    (10, 'Октябрь'),
    (11, 'Ноябрь'),
    (12, 'Декабрь'),
]
DAY = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'),
       (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'),
       (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'),
       (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')]

FOLD = [
    (1, 'бифолио'),
    (2, 'in-4'),
    (3, 'in-8'),
    (4, 'Не определяется')
]

SAFE = [
    (1, 'Целая'),
    (2, 'Половина'),
    (3, 'Четверть')
]

YESNO = [
    (1, 'Да'),
    (2, 'Нет')
]

SHADE = [
    (1, 'Белый'),
    (2, 'Жёлтый'),
    (3, 'Голубой'),
    (4, 'Зелёный')
]

EBB = [
    (1, 'Ручной'),
    (2, 'Машинный')
]

ORIENT = [
    (1, 'Вертикально'),
    (2, 'Горизонтально')
]

CUT = [
    (1, 'Да'),
    (2, 'Нет')
]

FIBER = [
    (1, 'Целлюлоза сульфитная'),
    (2, 'Целлюлоза сульфатная'),
    (3, 'Лён'),
    (4, 'Хлопок'),
    (5, 'Конопля')
]
PLACE = [
    (1, 'Санкт-Петербург'),
    (2, 'Москва'),
    (3, 'Олонец'),
    (4, 'Мадрид'),
    (5, 'Париж'),
    (6, 'Берлин'),
    (7, 'Женева')
]

DATA_SCHEMA = {
    'type': 'object',
    'title': 'Data',
    'properties': {
        'text': {
            'title': 'Some text',
            'type': 'string',
            'format': 'textarea',
        },
        'status': {
            'title': 'Status',
            'type': 'boolean',
        },
    },
}


class ObjectsForm(ModelForm):
    class Meta:
        model = Objects
        fields = ['cipher_section', 'cipher_fond', 'cipher_fond_number', 'cipher_case_number', 'cipher_list_number',
                  'sample_number', 'year', 'month', 'day', 'author', 'short_description', 'place',
                  'detailed_description', 'restoration', 'shade', 'ebb', 'text_orientation', 'cutting', 'folding',
                  'size_width', 'size_height', 'avg_sheet_thickness', 'med_sheet_thickness', 'sheet_weight',
                  'filigree_height', 'filigree_description', 'filigree_conformity', 'filigree_bernstein',
                  'filigree_safety', 'countermark_height', 'countermark_description', 'countermark_conformity',
                  'countermark_bernstein', 'countermark_safety', 'verge_distance', 'pontuso_distance',
                  'verge_thickness', 'pontuso_thickness', 'date_of_form', 'whiteness_avg', 'brightness_avg',
                  'fluorescence', 'whiteness_exp', 'pH_avg', 'pH_exp', 'fiber_composition_description2', 'polmic_param',
                  'rfa_composition', 'rfa_spectrum_format', 'rfa_exp_data', 'IRFourier_spectrum_format',
                  'IRFourier_description', 'IRFourier_exp_data', 'esm_exp_data', 'eds_spectrum_format',
                  'eds_composition', 'eds_exp_data', 'Literature', 'notes', 'data']
        widgets = {
            "cipher_section": Select(attrs={'class': 'form-select', 'placeholder': 'Шифр секции'}),
            "cipher_fond": Select(attrs={'class': 'form-select', 'placeholder': 'Шифр коллекция/фонд'}),
            "cipher_fond_number": TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер коллекции/фонда'}),
            "cipher_case_number": TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер дела'}),
            "cipher_list_number": TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер листа'}),
            "sample_number": TextInput(
                attrs={'class': 'form-control', 'placeholder': '№ образца(для образцов без шифра)'}),
            "year": TextInput(attrs={'class': 'form-control', 'placeholder': 'Год'}),
            "month": Select(attrs={'class': 'form-select', 'placeholder': 'Месяц'}),
            "day": Select(attrs={'class': 'form-select', 'placeholder': 'День'}),
            "author": TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
            "short_description": TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            "place": Select(attrs={'class': 'form-select', 'placeholder': 'Место создания'}),
            "detailed_description": Textarea(attrs={'class': 'form-control', 'placeholder': 'Подробное описание'}),
            "restoration": Select(attrs={'class': 'form-select', 'placeholder': 'Предыдущая реставрация'}),
            "shade": Select(attrs={'class': 'form-select', 'placeholder': 'Оттенок'}),
            "ebb": Select(attrs={'class': 'form-select', 'placeholder': 'Отлив'}),
            "text_orientation": Select(attrs={'class': 'form-select',
                                              'placeholder': 'Ориентация текста относительно верже'}),
            "cutting": Select(attrs={'class': 'form-select', 'placeholder': 'Обрезка'}),
            "folding": Select(attrs={'class': 'form-select', 'placeholder': 'Сложение'}),
            "size_width": TextInput(attrs={'class': 'form-control', 'placeholder': 'Ширина (мм)'}),
            "size_height": TextInput(attrs={'class': 'form-control', 'placeholder': 'Высота (мм)'}),
            "avg_sheet_thickness": TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Средняя толщина листа (мм)'}),
            "med_sheet_thickness": TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Толщина листа медиана (мм)'}),
            "sheet_weight": TextInput(attrs={'class': 'form-control', 'placeholder': 'Вес листа (гр)'}),
            "filigree_height": TextInput(attrs={'class': 'form-control', 'placeholder': 'Высота филиграни (мм)'}),
            "filigree_description": TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание филиграни'}),
            "filigree_conformity": TextInput(attrs={'class': 'form-control', 'placeholder': 'Филигрань соответствие'}),
            "filigree_bernstein": URLInput(attrs={'class': 'form-control', 'placeholder': 'Филигрань Бернштейн'}),
            "filigree_safety": Select(attrs={'class': 'form-select', 'placeholder': 'Сохранность филиграни'}),
            "countermark_height": TextInput(attrs={'class': 'form-control', 'placeholder': 'Высота контрмарки (мм)'}),
            "countermark_description": TextInput(attrs={'class': 'form-control', 'placeholder': 'Описание контрмарки'}),
            "countermark_conformity": TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Контрмарка соответствие'}),
            "countermark_bernstein": URLInput(attrs={'class': 'form-control', 'placeholder': 'Контрмарка Бернштейн'}),
            "countermark_safety": Select(attrs={'class': 'form-select', 'placeholder': 'Сохранность филиграни'}),
            "verge_distance": TextInput(attrs={'class': 'form-control', 'placeholder': 'Расстояние между верже (мм)'}),
            "pontuso_distance": TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Расстояние между понтюзо (мм)'}),
            "verge_thickness": TextInput(attrs={'class': 'form-control', 'placeholder': 'Толщина верже (мм)'}),
            "pontuso_thickness": TextInput(attrs={'class': 'form-control', 'placeholder': 'Толщина понтюзо (мм)'}),
            "date_of_form": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата отливочной формы'}),
            "whiteness_avg": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Средняя белизна (cie)'}),
            "brightness_avg": TextInput(attrs={'class': 'form-control', 'placeholder': 'Средняя яркость (%)'}),
            "fluorescence": TextInput(attrs={'class': 'form-control', 'placeholder': 'Флуоресценция (%)'}),
            "whiteness_exp": TextInput(attrs={'class': 'form-control', 'placeholder': 'Белизна (параметры измерений)'}),
            "pH_avg": TextInput(attrs={'class': 'form-control', 'placeholder': 'pH-среднее'}),
            "pH_exp": TextInput(attrs={'class': 'form-control', 'placeholder': 'pH (параметры измерений)'}),
            "fiber_composition_description2": CheckboxSelectMultiple(
                attrs={'placeholder': 'Состав по волокну'}),
            "polmic_param": TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Поляризационная микроскопия, параметры измерений'}),
            "rfa_composition": TextInput(attrs={'class': 'form-control', 'placeholder': 'РФА количественые значения'}),
            "rfa_spectrum_format": FileInput(attrs={'class': 'form-control', 'placeholder': 'РФА спектр формата'}),
            "rfa_exp_data": TextInput(attrs={'class': 'form-control', 'placeholder': 'РФА (параметры измерений)'}),
            "IRFourier_spectrum_format": FileInput(
                attrs={'class': 'form-control', 'placeholder': 'ИК-Фурье спектр формата'}),
            "IRFourier_description": TextInput(attrs={'class': 'form-control', 'placeholder': 'ИК-Фурье описание'}),
            "IRFourier_exp_data": TextInput(
                attrs={'class': 'form-control', 'placeholder': 'ИК-Фурье (параметры измерений)'}),
            "esm_exp_data": TextInput(attrs={'class': 'form-control', 'placeholder': 'СЭМ (параметры измерений)'}),
            "eds_spectrum_format": FileInput(attrs={'class': 'form-control', 'placeholder': 'ЭДС спектр формата'}),
            "eds_composition": TextInput(attrs={'class': 'form-control', 'placeholder': 'ЭДС количественые значения'}),
            "eds_exp_data": TextInput(attrs={'class': 'form-control', 'placeholder': 'ЭДС (параметры измерений)'}),
            "Literature": Textarea(attrs={'class': 'form-control', 'placeholder': 'Литература'}),
            "notes": TextInput(attrs={'class': 'form-control', 'placeholder': 'Примечания'}),
            "data": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата заполнения',
                                         'type': 'datetime-local'}),
        }


'''
class ObjectsImageForm(ModelForm):
    class Meta:
        model = ObjectImage
        fields = ['name', 'object', 'image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Филигрань рисунок',
                                               'multiple': True}),
        }
'''


class FilpicForm(ModelForm):
    class Meta:
        model = Filpic
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Филигрань рисунок',
                                               'multiple': True}),
        }


class CountpicForm(ModelForm):
    class Meta:
        model = Countpic
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Контрмарка рисунок',
                                               'multiple': True}),
        }


class FiberHercImgForm(ModelForm):
    class Meta:
        model = FiberHercImg
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Состав по волокну (Херцберг)',
                                               'multiple': True}),
        }


class FiberGraffImgForm(ModelForm):
    class Meta:
        model = FiberGraffImg
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Состав по волокну (Графф)',
                                               'multiple': True}),
        }


class PolmicPolImgForm(ModelForm):
    class Meta:
        model = PolmicPolImg
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'form-control',
                                               'placeholder': 'Поляризационная микроскопия в поляризованном свете',
                                               'multiple': True}),
        }


class PolimicCrossImgForm(ModelForm):
    class Meta:
        model = PolimicCrossImg
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'form-control',
                                               'placeholder': 'Поляризационная микроскопия в скрещенных николях',
                                               'multiple': True}),
        }


class RfaSpecImgForm(ModelForm):
    class Meta:
        model = RfaSpecImg
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'form-control',
                                               'placeholder': 'Рисунок спектра РФА',
                                               'multiple': True}),
        }


class IRFurImgForm(ModelForm):
    class Meta:
        model = IRFurImg
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'form-control',
                                               'placeholder': 'ИК-Фурье рисунок',
                                               'multiple': True}),
        }


class EsmRevImgForm(ModelForm):
    class Meta:
        model = EsmRevImg
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'form-control',
                                               'placeholder': 'СЭМ обратно рассеянные',
                                               'multiple': True}),
        }


class EsmSecImgForm(ModelForm):
    class Meta:
        model = EsmSecImg
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'form-control',
                                               'placeholder': 'СЭМ вторичные электроны',
                                               'multiple': True}),
        }


class EdsImgForm(ModelForm):
    class Meta:
        model = EdsImg
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'class': 'form-control',
                                               'placeholder': 'ЭДС рисунок спектра',
                                               'multiple': True}),
        }
