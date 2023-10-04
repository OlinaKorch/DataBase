# Generated by Django 3.2.7 on 2022-12-06 12:21

import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('probe', models.CharField(max_length=100, verbose_name='Probe')),
                ('cipher_section', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'ЗЭС'), (2, 'РС')], null=True, verbose_name='Шифр секции')),
                ('cipher_fond', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Коллекция'), (2, 'Фонд')], null=True, verbose_name='Шифр коллекция/фонд')),
                ('cipher_fond_number', models.BigIntegerField(blank=True, null=True, verbose_name='Номер коллекции/фонда')),
                ('cipher_case_number', models.BigIntegerField(blank=True, null=True, verbose_name='Номер дела')),
                ('cipher_list_number', models.CharField(blank=True, max_length=250, verbose_name='Номер листа')),
                ('sample_number', models.CharField(blank=True, max_length=250, verbose_name='№ образца (для образцов без шифра)')),
                ('year', django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, null=True, verbose_name='Год')),
                ('month', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5, 'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')], null=True, verbose_name='Месяц')),
                ('day', models.PositiveSmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')], null=True, verbose_name='День')),
                ('author', models.CharField(blank=True, max_length=250, verbose_name='Автор')),
                ('short_description', models.CharField(blank=True, max_length=250, verbose_name='Краткое описание')),
                ('place', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Санкт-Петербург'), (2, 'Москва'), (3, 'Олонец'), (4, 'Мадрид'), (5, 'Париж'), (6, 'Берлин'), (7, 'Женева')], null=True, verbose_name='Место создания')),
                ('detailed_description', models.TextField(blank=True, null=True, verbose_name='Подробное описание')),
                ('restoration', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Да'), (2, 'Нет')], null=True, verbose_name='Предыдущая реставрация')),
                ('shade', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Белый'), (2, 'Жёлтый'), (3, 'Голубой'), (4, 'Зелёный')], null=True, verbose_name='Оттенок')),
                ('ebb', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Ручной'), (2, 'Машинный')], null=True, verbose_name='Отлив')),
                ('text_orientation', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Вертикально'), (2, 'Горизонтально')], null=True, verbose_name='Ориентация текста относительно верже')),
                ('cutting', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Да'), (2, 'Нет')], null=True, verbose_name='Обрезка')),
                ('folding', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'бифолио'), (2, 'in-4'), (3, 'in-8'), (4, 'Не определяется')], null=True, verbose_name='Сложение')),
                ('size_width', models.PositiveIntegerField(blank=True, null=True, verbose_name='Ширина (мм)')),
                ('size_height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Высота (мм)')),
                ('avg_sheet_thickness', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Средняя толщина листа (мм)')),
                ('med_sheet_thickness', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Толщина листа медиана (мм)')),
                ('sheet_weight', models.PositiveIntegerField(blank=True, null=True, verbose_name='Вес листа (гр)')),
                ('filigree_pic', models.ImageField(blank=True, null=True, upload_to='images_filig/', verbose_name='Филигрань рисунок')),
                ('filigree_height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Высота филиграни (мм)')),
                ('filigree_description', models.CharField(blank=True, max_length=250, verbose_name='Описание филиграни')),
                ('filigree_conformity', models.CharField(blank=True, max_length=250, verbose_name='Филигрань соответствие')),
                ('filigree_bernstein', models.CharField(blank=True, max_length=250, verbose_name='Филигрань Бернштейн')),
                ('filigree_safety', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Целая'), (2, 'Половина'), (3, 'Четверть')], null=True, verbose_name='Сохранность филиграни')),
                ('countermark_pic', models.ImageField(blank=True, upload_to='images_count/', verbose_name='Контрмарка рисунок')),
                ('countermark_height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Высота контрмарки (мм)')),
                ('countermark_description', models.CharField(blank=True, max_length=250, verbose_name='Описание контрмарки')),
                ('countermark_conformity', models.CharField(blank=True, max_length=250, verbose_name='Контрмарка соответствие')),
                ('countermark_bernstein', models.CharField(blank=True, max_length=250, verbose_name='Контрмарка Бернштейн')),
                ('countermark_safety', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Целая'), (2, 'Половина'), (3, 'Четверть')], null=True, verbose_name='Сохранность контрмарки')),
                ('verge_distance', models.PositiveIntegerField(blank=True, null=True, verbose_name='Расстояние между верже (мм)')),
                ('pontuso_distance', models.PositiveIntegerField(blank=True, null=True, verbose_name='Расстояние между понтюзо (мм)')),
                ('verge_thickness', models.PositiveIntegerField(blank=True, null=True, verbose_name='Толщина верже (мм)')),
                ('pontuso_thickness', models.PositiveIntegerField(blank=True, null=True, verbose_name='Толщина понтюзо (мм)')),
                ('date_of_form', models.DateField(verbose_name='Дата отливочной формы')),
                ('whiteness_avg', models.PositiveIntegerField(blank=True, null=True, verbose_name='Средняя белизна (cie)')),
                ('brightness_avg', models.PositiveIntegerField(blank=True, null=True, verbose_name='Средняя яркость (%)')),
                ('fluorescence', models.PositiveIntegerField(blank=True, null=True, verbose_name='Флуоресценция (%)')),
                ('whiteness_exp', models.CharField(blank=True, max_length=250, null=True, verbose_name='Белизна (параметры измерений)')),
                ('pH_avg', models.PositiveIntegerField(blank=True, null=True, verbose_name='pH-среднее')),
                ('pH_exp', models.CharField(blank=True, max_length=250, null=True, verbose_name='pH (параметры измерений)')),
                ('fiber_composition_herc', models.ImageField(blank=True, null=True, upload_to='images_fiber_comp_herc/', verbose_name='Состав по волокну (Херцберг)')),
                ('fiber_composition_graff', models.ImageField(blank=True, null=True, upload_to='images_fiber_comp_graff/', verbose_name='Состав по волокну (Графф)')),
                ('fiber_composition_description2', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Целлюлоза сульфитная'), (2, 'Целлюлоза сульфатная'), (3, 'Лён'), (4, 'Хлопок'), (5, 'Конопля')], max_length=5, verbose_name='Состав по волокну')),
                ('polmic_pol', models.ImageField(blank=True, null=True, upload_to='images_polmic_pol/', verbose_name='Поляризационная микроскопия в поляризованном свете')),
                ('polmic_cross', models.ImageField(blank=True, null=True, upload_to='images_polmic_cross/', verbose_name='Поляризационная микроскопия в скрещенных николях')),
                ('polmic_param', models.CharField(blank=True, max_length=250, null=True, verbose_name='Поляризационная микроскопия, параметры измерений')),
                ('rfa_spectrum', models.ImageField(blank=True, null=True, upload_to='images_rfa/', verbose_name='Рисунок спектра РФА')),
                ('rfa_composition', models.JSONField(blank=True, null=True, verbose_name='РФА количественые значения')),
                ('rfa_spectrum_format', models.FileField(blank=True, null=True, upload_to='images_rfa_format/', verbose_name='РФА спектр формата')),
                ('rfa_exp_data', models.CharField(blank=True, max_length=250, null=True, verbose_name='РФА (параметры измерений)')),
                ('IRFourier_pic', models.ImageField(blank=True, null=True, upload_to='images_IRF/', verbose_name='ИК-Фурье рисунок')),
                ('IRFourier_spectrum_format', models.FileField(blank=True, null=True, upload_to='images_IRF_format/', verbose_name='ИК-Фурье спектр формата')),
                ('IRFourier_description', models.CharField(blank=True, max_length=250, null=True, verbose_name='ИК-Фурье описание')),
                ('IRFourier_exp_data', models.CharField(blank=True, max_length=250, null=True, verbose_name='ИК-Фурье (параметры измерений)')),
                ('esm_second_pic', models.ImageField(blank=True, null=True, upload_to='images_esm_second/', verbose_name='СЭМ вторичные электроны')),
                ('esm_reverse_pic', models.ImageField(blank=True, null=True, upload_to='images_esn_reverse/', verbose_name='СЭМ обратно рассеянные')),
                ('esm_exp_data', models.CharField(blank=True, max_length=250, null=True, verbose_name='СЭМ (параметры измерений)')),
                ('eds', models.ImageField(blank=True, null=True, upload_to='images_eds_spectrum/', verbose_name='ЭДС рисунок спектра')),
                ('eds_spectrum_format', models.FileField(blank=True, null=True, upload_to='images_eds_format/', verbose_name='ЭДС спектр формата')),
                ('eds_composition', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='ЭДС количественые значения')),
                ('eds_exp_data', models.CharField(blank=True, max_length=250, null=True, verbose_name='ЭДС (параметры измерений)')),
                ('Literature', models.TextField(blank=True, null=True, verbose_name='Литература')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Примечания')),
                ('data', models.DateField(blank=True, null=True, verbose_name='Дата заполнения')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
    ]
