from django.contrib import admin
from .models import Us, Home, Photo

from django.urls import  path
from  django.shortcuts import  render, redirect
from django.contrib import messages
from django import forms

class CsvImportForm(forms.Form):
    csv_uploader = forms.FileField()


class PhotoAdd(admin.StackedInline):
    model = Photo
    fields = ('home', 'add_photo')
    extra = 0

class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'description')
    list_display_links = ('id', 'title')
    inlines = [PhotoAdd]

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv-home/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_uploader']
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, "Ошибочный тип файла")
                return redirect('.')

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                print(fields)
                Home.objects.update_or_create(
                    id=fields[0],
                    title=fields[1],
                    images=fields[2],
                    price=fields[3],
                    description=fields[4]


                )

            return redirect('admin:index')

        form = CsvImportForm
        data = {"form": form}
        return render(request, "admin/csv_uploader.html", data)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('home', 'add_photo')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv-photo/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES['csv_uploader']
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, "Ошибочный тип файла")
                return redirect('.')

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                print(fields)
                Photo.objects.update_or_create(
                    id=fields[0],
                    home=Home(fields[1]),
                    add_photo=fields[2][:-1]

                )

            return redirect('admin:index')

        form = CsvImportForm
        data = {"form": form}
        return render(request, "admin/csv_uploader.html", data)

admin.site.register(Us)
admin.site.register(Home, HomeAdmin)
admin.site.register(Photo, PhotoAdmin)
