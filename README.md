# Library_app
This repository has the solution for company's task which is library app service wrapped with docker.

# Quick start 
In order to run the app, you can run:
</br> docker-compose up 
</br> this command will create and process the needed image. 
</br> Then you can go to "http://127.0.0.1:8000/" and project should be run.

# Overview 
Django is a Python framework for developing Web applications. With Django, developers can quickly create object-relational database mappings, REST APIs, user front ends, and even administrative interfaces. Django implements a Model-View-Controller (MVC) pattern that separates the application's data (model) from its user interface (view) and business logic (controller), making it easy to write cleanly structured code.

</br>This template augments the existing power of Django by packaging your Django app into a Docker image, which can then be deployed onto AWS CodePipeline in a few simple steps. You can fork this repo into your own GitHub account and any changes you make to your Django application will automatically be updated via CodePipeline within minutes.

</br>This sample contains the following files:

* A sample Django API and data model, defined in the directory itemslist.
* The API and admin entry points for the Django app, defined in the directory itemsAPP.
* A wsgi.py file (in the itemsAPP directory) for running your Django application on your Docker image using WSGI.
* A Dockerfile that builds the Django application as a Docker image.
* A requirements.txt file that enables the Dockerfile to install Django and other dependencies via the pip command.
* A manage.py file for executing Django administrative tasks from the command line.
* A build.yml file for AWS CodeBuild that builds the image and pushes it to Amazon Elastic Container Registry (ECR).
* A AWS database was used.

# Application
CRUD stands for Create, Read, Update & Delete. These are the four basic operations which are executed on Database Models. We are developing a web app which is capable of performing these operations.
</br>

## Models for Books

```
class Book(models.Model):
    # Store necessary fields
    name = models.CharField(max_length = 50)
    #picture = models.ImageField()
    author = models.CharField(max_length = 30, default='anonymous')
    year = models.IntegerField(('year'), max_length=4, choices=year_dropdown, default=datetime.datetime.now().year)

    #email = models.EmailField(blank = True)
    describe = models.TextField(default = 'DataFlair Django tutorials')
```
</br>
Django will make a table in a database named book. That table will have these fields:

Name, author, year, and description of the book object.

## Model Forms in Book
```
class BookCreate(forms.ModelForm):
    class Meta:
        model = Book

        # Input from user
        fields = '__all__'
 ```
</br>
The BookCreate() class is the form class which represents the Model form. In the MetaClass, we define which model to be used to make the model form.

## View Functions for Django CRUD App
 ```
def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/library.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'book/upload_form.html', {'upload_form':upload})

def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')
    return render(request, 'book/upload_form.html', {'upload_form':book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')
 ```
* 1. Index Function : Read Operation. In this function, we simply retrieve all the objects in the book
* 2. Upload Function : CREATE operation of CRUD. It is simply taking form data from the user and saving it in a database
* 3. Update_book : If the object exists it will return the form filled with the object’s information in it. The user can change the form again. In this case, there will be no creation of new book but the editing of the existing book object.
* 4. Delete Function : Delete Function is the last function of the CRUD application. We are again using the same object method as with Update book function. We are passing the request and book_id to delete the book.

## Templates
* library.html : displaying objects from a database. We are running a for loop to access the data in the dictionary we passed.
* Upload_form.html : We are using csrf token and other form tags. 

## URLs

```
urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book)
]
```
</br>URL lookups for library app as well as settings for Django static files. These settings are used by Django to render the images with the book object.

## DB
Database was used postgres from AWS, and django settings was connected successfully 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'library',
        'USER': 'postgres',
        'PASSWORD': 'C3zLj9JuEv4Bf7PgplDA',
        'HOST': 'database-1.cwmdudwnngey.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
```

## Example of library view 
![Library View](https://github.com/asemsaleh/Library_app/blob/main/library%20view.PNG)
![Upload View](https://github.com/asemsaleh/Library_app/blob/main/book-upload.PNG)


