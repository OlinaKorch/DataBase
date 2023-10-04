from django.shortcuts import render, redirect
from .models import Objects, Filpic, Countpic, FiberHercImg, FiberGraffImg, PolmicPolImg, \
    PolimicCrossImg, RfaSpecImg, IRFurImg, EsmRevImg, EsmSecImg, EdsImg, Stamppic
from .forms import ObjectsForm, FilpicForm, CountpicForm, FiberHercImgForm, FiberGraffImgForm, PolmicPolImgForm, \
    PolimicCrossImgForm, RfaSpecImgForm, IRFurImgForm, EsmRevImgForm, EsmSecImgForm, EdsImgForm
from django.views.generic import DetailView, UpdateView


def news_home(request):
    news = Objects.objects.order_by('data')
    return render(request, 'news/news_home.html', {'news': news})


class ObjectsDetailView(DetailView):
    model = Objects
    template_name = 'news/details_view.html'
    context_object_name = 'object'


class FilpicDetailView(DetailView):
    model = Filpic
    template_name = 'news/details_view.html'
    context_object_name = 'fil_pic'


class CountpicDetailView(DetailView):
    model = Countpic
    template_name = 'news/details_view.html'
    context_object_name = 'count_pic'


class FiberHercImgDetailView(DetailView):
    model = FiberHercImg
    template_name = 'news/details_view.html'
    context_object_name = 'fiber_herc_img'


class FiberGraffImgDetailView(DetailView):
    model = FiberGraffImg
    template_name = 'news/details_view.html'
    context_object_name = 'fiber_graff_img'


class PolmicPolImgDetailView(DetailView):
    model = PolmicPolImg
    template_name = 'news/details_view.html'
    context_object_name = 'polmic_pol_img'


class PolimicCrossImgDetailView(DetailView):
    model = PolimicCrossImg
    template_name = 'news/details_view.html'
    context_object_name = 'polimic_cross_img'


class FRfaSpecImgDetailView(DetailView):
    model = RfaSpecImg
    template_name = 'news/details_view.html'
    context_object_name = 'rfa_spec_img'


class IRFurImgDetailView(DetailView):
    model = IRFurImg
    template_name = 'news/details_view.html'
    context_object_name = 'IRfur_img'


class EsmRevImgDetailView(DetailView):
    model = EsmRevImg
    template_name = 'news/details_view.html'
    context_object_name = 'esm_rev_img'


class EsmSecImgDetailView(DetailView):
    model = EsmSecImg
    template_name = 'news/details_view.html'
    context_object_name = 'esm_sec_img'


class EdsImgDetailView(DetailView):
    model = EdsImg
    template_name = 'news/details_view.html'
    context_object_name = 'eds_img'


# def detail_view(request, pk):
#    news = Objects.objects.order_by('pk')
#    return render(request, 'news/details_view.html', {'news': news})


class ObjectsUpdateView(UpdateView):
    model = Objects
    template_name = 'news/create.html'
    form_class = ObjectsForm


def create(request):
    if request.method == 'POST':
        form1 = ObjectsForm(request.POST, request.FILES, prefix='form1')
        # form2 = ObjectsImageForm(request.POST, request.FILES, prefix='form2')
        form3 = FilpicForm(request.POST, request.FILES, prefix='form3')
        form4 = CountpicForm(request.POST, request.FILES, prefix='form4')
        form5 = FiberHercImgForm(request.POST, request.FILES, prefix='form5')
        form6 = FiberGraffImgForm(request.POST, request.FILES, prefix='form6')
        form7 = PolmicPolImgForm(request.POST, request.FILES, prefix='form7')
        form8 = PolimicCrossImgForm(request.POST, request.FILES, prefix='form8')
        form9 = RfaSpecImgForm(request.POST, request.FILES, prefix='form9')
        form10 = IRFurImgForm(request.POST, request.FILES, prefix='form10')
        form11 = EsmRevImgForm(request.POST, request.FILES, prefix='form11')
        form12 = EsmSecImgForm(request.POST, request.FILES, prefix='form12')
        form13 = EdsImgForm(request.POST, request.FILES, prefix='form13')
        form14 = Stamppic(request.POST, request.FILES, prefix='form13')
        if all([form1.is_valid(), '''form2.is_valid()''', form3.is_valid(), form4.is_valid(), form5.is_valid(),
                form6.is_valid(), form7.is_valid(), form8.is_valid(), form9.is_valid(), form10.is_valid(),
                form11.is_valid(), form12.is_valid(), form13.is_valid(), form14.is_valid()]):
            form1.save()
            # form2.save()
            form3.save()
            form4.save()
            form5.save()
            form6.save()
            form7.save()
            form8.save()
            form9.save()
            form10.save()
            form11.save()
            form12.save()
            form13.save()
            form14.save()
    #    if form.is_valid():
    #        form.save()
    #        return redirect('home')
    # else:
    #     form = ObjectsForm()
    else:
        form1 = ObjectsForm(prefix='form1')
        # form2 = ObjectsImageForm(prefix='form2')
        form3 = FilpicForm(prefix='form3')
        form4 = CountpicForm(prefix='form4')
        form5 = FiberHercImgForm(prefix='form5')
        form6 = FiberGraffImgForm(prefix='form6')
        form7 = PolmicPolImgForm(prefix='form7')
        form8 = PolimicCrossImgForm(prefix='form8')
        form9 = RfaSpecImgForm(prefix='form9')
        form10 = IRFurImgForm(prefix='form10')
        form11 = EsmRevImgForm(prefix='form11')
        form12 = EsmSecImgForm(prefix='form12')
        form13 = EdsImgForm(prefix='form13')
        form14 = EdsImgForm(prefix='form14')
    return render(request, 'news/create.html', {'form1': form1,
                                                # 'form2': form2,
                                                'form3': form3,
                                                'form4': form4,
                                                'form5': form5,
                                                'form6': form6,
                                                'form7': form7,
                                                'form8': form8,
                                                'form9': form9,
                                                'form10': form10,
                                                'form11': form11,
                                                'form12': form12,
                                                'form13': form13,
                                                'form14': form14
                                                })
