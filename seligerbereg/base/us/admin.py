from django.contrib import admin
from .models import Us, Photo, Home, Photo1,  Attractions, Photo2

from django.urls import  path
from  django.shortcuts import  render, redirect
from django.contrib import messages
from django import forms

class CsvImportForm(forms.Form):
    csv_uploader = forms.FileField()



class PhotoAdd(admin.StackedInline):
    model = Photo
    fields = ('us', 'add_photo')
    extra = 0

class UsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')
    inlines = [PhotoAdd]

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv-us/", self.upload_csv)]
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
                fields = x.split(";")
                print(fields)
                Us.objects.update_or_create(
                    id=fields[0],
                    title=fields[1],
                    featured_images=fields[2],
                    description=fields[3],


                )

            return redirect('admin:index')

        form = CsvImportForm
        data = {"form": form}
        return render(request, "admin/csv_uploader.html", data)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('us', 'add_photo')

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
                    us=Us(fields[1]),
                    add_photo=fields[2][:-1]

                )

            return redirect('admin:index')

        form = CsvImportForm
        data = {"form": form}
        return render(request, "admin/csv_uploader.html", data)


class Photo1Add(admin.StackedInline):
    model = Photo1
    fields = ('home', 'add_photo')
    extra = 0

class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'description')
    list_display_links = ('id', 'title')
    inlines = [Photo1Add]

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
                fields = x.split(";")
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


class Photo1Admin(admin.ModelAdmin):
    list_display = ('home', 'add_photo')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv-photo1/", self.upload_csv)]
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
                Photo1.objects.update_or_create(
                    id=fields[0],
                    home=Home(fields[1]),
                    add_photo=fields[2][:-1]

                )

            return redirect('admin:index')

        form = CsvImportForm
        data = {"form": form}
        return render(request, "admin/csv_uploader.html", data)


class Photo2Add(admin.StackedInline):
    model = Photo2
    fields = ('attractions', 'add_photo')
    extra = 0

class AttractionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')
    inlines = [Photo2Add]

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv-attractions/", self.upload_csv)]
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
                fields = x.split(";")
                print(fields)
                Attractions.objects.update_or_create(
                    id=fields[0],
                    title=fields[1],
                    image=fields[2],
                    description=fields[3],
                    address=fields[4]


                )

            return redirect('admin:index')

        form = CsvImportForm
        data = {"form": form}
        return render(request, "admin/csv_uploader.html", data)

class Photo2Admin(admin.ModelAdmin):
    list_display = ('attractions', 'add_photo')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("upload-csv-photo2/", self.upload_csv)]
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
                Photo2.objects.update_or_create(
                    id=fields[0],
                    home=Attractions(fields[1]),
                    add_photo=fields[2][:-1]

                )

            return redirect('admin:index')

        form = CsvImportForm
        data = {"form": form}
        return render(request, "admin/csv_uploader.html", data)

admin.site.register(Us, UsAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Photo1, Photo1Admin)
admin.site.register(Attractions, AttractionsAdmin)
admin.site.register(Photo2, Photo2Admin)