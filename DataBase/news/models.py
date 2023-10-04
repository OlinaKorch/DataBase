from django.db import models
from django.contrib.postgres.fields import IntegerRangeField, JSONField
from jsoneditor.forms import JSONEditor
from multiselectfield import MultiSelectField


# from django.db.models import JSONField


class Objects(models.Model):
    SECTION = [
        (1, 'ЗЭС'),
        (2, 'РС')
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
    STAMPPURP = [
        (1, 'Гербовая бумага'),
        (2, 'Производственный знак'),
        (3, 'Личный знак')
    ]
    STAMPTEC = [
        (1, 'Слепое тиснение'),
        (2, 'Золотое тиснение'),
        (3, 'Окрашенный оттиск')
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

    cipher_section = models.PositiveSmallIntegerField("Шифр секции", choices=SECTION, blank=True, null=True)
    cipher_fond = models.PositiveSmallIntegerField("Шифр коллекция/фонд", choices=FOND, blank=True, null=True)
    cipher_fond_number = models.BigIntegerField("Номер коллекции/фонда", blank=True, null=True)
    cipher_case_number = models.BigIntegerField("Номер дела", blank=True, null=True)
    cipher_list_number = models.CharField("Номер листа", max_length=250, blank=True)
    sample_number = models.CharField("№ образца (для образцов без шифра)", max_length=250, blank=True)
    year = models.PositiveSmallIntegerField("Год", blank=True, null=True)
    month = models.PositiveSmallIntegerField("Месяц", choices=MONTH, blank=True, null=True)
    day = models.PositiveSmallIntegerField("День", choices=DAY, blank=True, null=True)
    author = models.CharField("Автор", max_length=250, blank=True)
    short_description = models.CharField("Краткое описание", max_length=250, blank=True)
    place = models.PositiveSmallIntegerField("Место создания", choices=PLACE, blank=True, null=True)
    detailed_description = models.TextField("Подробное описание", blank=True)
    restoration = models.PositiveSmallIntegerField("Предыдущая реставрация", choices=YESNO, blank=True, null=True)
    shade = models.PositiveSmallIntegerField("Оттенок", choices=SHADE, blank=True, null=True)
    ebb = models.PositiveSmallIntegerField("Отлив", choices=EBB, blank=True, null=True)
    text_orientation = models.PositiveSmallIntegerField("Ориентация текста относительно верже", choices=ORIENT,
                                                        blank=True, null=True)
    cutting = models.PositiveSmallIntegerField("Обрезка", choices=CUT, blank=True, null=True)
    folding = models.PositiveSmallIntegerField("Сложение", choices=FOLD, blank=True, null=True)
    size_width = models.PositiveIntegerField("Ширина (мм)", blank=True, null=True)
    size_height = models.PositiveIntegerField("Высота (мм)", blank=True, null=True)
    avg_sheet_thickness = models.PositiveSmallIntegerField("Средняя толщина листа (мм)", blank=True, null=True)
    med_sheet_thickness = models.PositiveSmallIntegerField("Толщина листа медиана (мм)", blank=True, null=True)
    sheet_weight = models.PositiveIntegerField("Вес листа (гр)", blank=True, null=True)
    filigree = models.PositiveSmallIntegerField("Наличие филиграни", choices=YESNO, blank=True, null=True)
    filigree_height = models.PositiveIntegerField("Высота филиграни (мм)", blank=True, null=True)
    filigree_description = models.CharField('Описание филигра  ни', max_length=250, blank=True)
    filigree_conformity = models.CharField('Филигрань соответствие', max_length=250, blank=True)
    filigree_bernstein = models.URLField('Филигрань Бернштейн', max_length=250, blank=True)
    filigree_safety = models.PositiveSmallIntegerField("Сохранность филиграни", choices=SAFE, blank=True, null=True)
    countermark_height = models.PositiveIntegerField("Высота контрмарки (мм)", blank=True, null=True)
    countermark_description = models.CharField('Описание контрмарки', max_length=250, blank=True)
    countermark_conformity = models.CharField('Контрмарка соответствие', max_length=250, blank=True)
    countermark_bernstein = models.CharField('Контрмарка Бернштейн', max_length=250, blank=True)
    countermark_safety = models.PositiveSmallIntegerField("Сохранность контрмарки", choices=SAFE, blank=True, null=True)
    verge_distance = models.PositiveIntegerField("Расстояние между верже (мм)", blank=True, null=True)
    pontuso_distance = models.PositiveIntegerField("Расстояние между понтюзо (мм)", blank=True, null=True)
    verge_thickness = models.PositiveIntegerField("Толщина верже (мм)", blank=True, null=True)
    pontuso_thickness = models.PositiveIntegerField("Толщина понтюзо (мм)", blank=True, null=True)
    date_of_form = models.DateField("Дата отливочной формы", blank=True, null=True)
    stamp = models.PositiveSmallIntegerField("Наличие штемпеля", choices=YESNO, blank=True, null=True)
    stamp_purpose = models.PositiveSmallIntegerField("Назначение штемпеля", choices=STAMPPURP, blank=True, null=True)
    stamp_tec = models.PositiveSmallIntegerField("Штемпель техника", choices=STAMPTEC, blank=True, null=True)
    stamp_description = models.CharField('Описание штемпеля', max_length=250, blank=True)
    whiteness_avg = models.PositiveIntegerField("Средняя белизна (cie)", blank=True, null=True)
    brightness_avg = models.PositiveIntegerField("Средняя яркость (%)", blank=True, null=True)
    fluorescence = models.PositiveIntegerField("Флуоресценция (%)", blank=True, null=True)
    whiteness_exp = models.CharField('Белизна (параметры измерений)', max_length=250, blank=True)
    pH_avg = models.PositiveIntegerField("pH-среднее", blank=True, null=True)
    pH_exp = models.CharField('pH (параметры измерений)', max_length=250, blank=True)
    fiber_composition_description2 = MultiSelectField("Состав по волокну", choices=FIBER, max_choices=5, max_length=5,
                                                      blank=True, null=True)
    polmic_param = models.CharField('Поляризационная микроскопия, параметры измерений', max_length=250, blank=True)
    rfa_composition = models.JSONField('РФА количественые значения', blank=True, null=True)
    rfa_spectrum_format = models.FileField("РФА спектр формата", upload_to='images_rfa_format/', blank=True, null=True)
    rfa_exp_data = models.CharField('РФА (параметры измерений)', max_length=250, blank=True)
    IRFourier_spectrum_format = models.FileField("ИК-Фурье спектр формата", upload_to='images_IRF_format/', blank=True,
                                                 null=True)
    IRFourier_description = models.CharField('ИК-Фурье описание', max_length=250, blank=True)
    IRFourier_exp_data = models.CharField('ИК-Фурье (параметры измерений)', max_length=250, blank=True)
    esm_exp_data = models.CharField('СЭМ (параметры измерений)', max_length=250, blank=True)
    eds_spectrum_format = models.FileField("ЭДС спектр формата", upload_to='images_eds_format/', blank=True,
                                           null=True)
    eds_composition = models.JSONField('ЭДС количественые значения', blank=True, null=True)
    eds_exp_data = models.CharField('ЭДС (параметры измерений)', max_length=250, blank=True)
    Literature = models.TextField('Литература', blank=True)
    notes = models.TextField('Примечания', blank=True)
    data = models.DateField('Дата заполнения', blank=True, null=True)

    def __repr__(self):
        return self.id

    @property
    def square(self):
        if self.size_width is not None and self.size_height is not None:
            a = self.size_width
            b = self.size_height
            c = (a * b) / 1000000
            return round(c, 4)
        else:
            self.square = None
            return print('Размеры объекта не указаны')

    @property
    def mass(self):
        if self.sheet_weight is not None and self.square is not None:
            p = self.sheet_weight
            s = self.square
            m = p / s
            return round(m, 4)
        else:
            return print('Характеристика объекта не указаны')

    @property
    def density(self):
        if self.sheet_weight is not None and self.square is not None and self.avg_sheet_thickness is not None:
            p = self.sheet_weight
            s = self.square
            t = self.avg_sheet_thickness
            tmk = t * 1000
            d = p / (s * tmk)
            return round(d, 4)
        else:
            return print('Характеристики объекта не указаны')

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    @square.setter
    def square(self, value):
        self._square = value


class Filpic(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, blank=True, null=True, related_name='filimgs')
    image = models.ImageField("Филигрань рисунок", upload_to='fil_image/')


class Countpic(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, blank=True, null=True, related_name='countimgs')
    image = models.ImageField("Контрмарка рисунок", upload_to='count_image/')


class Stamppic(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, blank=True, null=True, related_name='stampimgs')
    image = models.ImageField("Штемпель фото", upload_to='stamp_image/')


class FiberHercImg(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, blank=True, null=True, related_name='fiberhercimgs')
    image = models.ImageField("Состав по волокну (Херцберг)", upload_to='herc_image/')


class FiberGraffImg(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, blank=True, null=True, related_name='fibergraffimgs')
    image = models.ImageField("Состав по волокну (Графф)", upload_to='graff_image/')


class PolmicPolImg(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, blank=True, null=True, related_name='polimicpolimgs')
    image = models.ImageField("Поляризационная микроскопия в поляризованном свете", upload_to='pol_image/')


class PolimicCrossImg(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, blank=True, null=True,
                               related_name='polimiccrossimgs')
    image = models.ImageField("Поляризационная микроскопия в скрещенных николях", upload_to='cross_image/')


class RfaSpecImg(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, blank=True, null=True, related_name='rfaimgs')
    image = models.ImageField("Рисунок спектра РФА", upload_to='rfa_image/')


class IRFurImg(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, blank=True, null=True, related_name='irfourierimgs')
    image = models.FileField("ИК-Фурье рисунок", upload_to='fourier_image/')


class EsmSecImg(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, blank=True, null=True, related_name='esmsecimgs')
    image = models.ImageField("СЭМ вторичные электроны", upload_to='esmsec_image/')


class EsmRevImg(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, blank=True, null=True, related_name='esmrevimgs')
    image = models.ImageField("СЭМ обратно рассеянные", upload_to='esmrev_image/')


class EdsImg(models.Model):
    object = models.ForeignKey(Objects, on_delete=models.CASCADE, blank=True, null=True, related_name='edsimgs')
    image = models.ImageField("ЭДС рисунок спектра", upload_to='eds_image/')
