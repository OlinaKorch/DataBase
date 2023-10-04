from django.contrib import admin
from django_admin_json_editor import JSONEditorWidget

from .forms import ObjectsForm
from .models import Objects, Filpic, Countpic, FiberHercImg, FiberGraffImg, PolmicPolImg, PolimicCrossImg, \
    RfaSpecImg, IRFurImg, EsmRevImg, EsmSecImg, EdsImg, Stamppic

from django.db import models

'''
class ObjectImageInline(admin.TabularInline):
    fk_name = 'object'
    model = ObjectImage
'''


class FilpicInline(admin.TabularInline):
    fk_name = 'object'
    model = Filpic


class CountpicInline(admin.TabularInline):
    fk_name = 'object'
    model = Countpic


class StamppicInline(admin.TabularInline):
    fk_name = 'object'
    model = Stamppic


class FiberHercImgInline(admin.TabularInline):
    fk_name = 'object'
    model = FiberHercImg


class FiberGraffImgInline(admin.TabularInline):
    fk_name = 'object'
    model = FiberGraffImg


class PolmicPolImgInline(admin.TabularInline):
    fk_name = 'object'
    model = PolmicPolImg


class PolimicCrossImgInline(admin.TabularInline):
    fk_name = 'object'
    model = PolimicCrossImg


class RfaSpecImgInline(admin.TabularInline):
    fk_name = 'object'
    model = RfaSpecImg


class IRFurImgInline(admin.TabularInline):
    fk_name = 'object'
    model = IRFurImg


class EsmRevImgInline(admin.TabularInline):
    fk_name = 'object'
    model = EsmRevImg


class EsmSecImgInline(admin.TabularInline):
    fk_name = 'object'
    model = EsmSecImg


class EdsImgInline(admin.TabularInline):
    fk_name = 'object'
    model = EdsImg


@admin.register(Objects)
class ObjectsAdmin(admin.ModelAdmin):
    inlines = [FilpicInline, CountpicInline, StamppicInline, FiberHercImgInline, FiberGraffImgInline, PolmicPolImgInline,
               PolimicCrossImgInline, RfaSpecImgInline, IRFurImgInline, EsmRevImgInline, EsmSecImgInline,
               EdsImgInline, ]

# class ObjectImageInline(admin.StackedInline):
#    model = ObjectImage


# class ObjectsAdmin(admin.ModelAdmin):
#    inlines = [ObjectImageInline, ]


# admin.site.register(Objects, ObjectsAdmin)

# admin.site.register(ObjectImage)
# admin.site.register(Objects)
