# Django-Exercise: Creating Dynamic Templates
 
Creating a new Django project from scratch. We'll set up the project, create an app, define a model, create views and templates, and run the project. Here’s a step-by-step breakdown.

---
![Description of Image](./1.jpg)
![Description of Image](./2.jpg)


### **1. Install Django**

First, make sure you have Django installed. If you don't have it installed, you can do so by running:

```bash
pip install django

```

If you already have Django installed, you can check the version by running:

```bash
django-admin --version

```

---

### **2. Create a New Django Project**

Now, let's create a new Django project named `myproject`.

```bash
django-admin startproject myproject

```

This will create a new directory `myproject` with the basic structure of a Django project. Navigate into this directory:

```bash
cd myproject

```

---

### **3. Start a New Django App**

Next, we’ll create a Django app inside the project. For this example, let’s call the app `myapp`.

```bash
python manage.py startapp myapp

```

This creates a new app folder called `myapp`. Now, open the `myproject/settings.py` file and add `myapp` to the list of `INSTALLED_APPS`:

```python
# myproject/settings.py

INSTALLED_APPS = [
    ...
    'myapp',
]

```

---

### **4. Define a Model in `models.py`**

Now, let’s define the `Menu` model that will store menu items and their prices. Open the `models.py` file in `myapp`:

```python
# myapp/models.py
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name

```

This `Menu` model has two fields:

- `name`: A character field to store the name of the menu item.
- `price`: An integer field to store the price of the item.

---

### **5. Apply Migrations**

Django uses migrations to apply database changes. First, we need to create and apply migrations for the `Menu` model.

Run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate

```

---

### **6. Create a View to Display Menu Items**

Now we’ll create a view to fetch all the menu items and pass them to the template.

1. Open `views.py` in `myapp` and create a function that fetches the `Menu` objects and renders them to a template:

```python
# myapp/views.py
from django.shortcuts import render
from .models import Menu

def menu(request):
    menu_items = Menu.objects.all()
    context = {'menu': menu_items}
    return render(request, 'menu.html', context)

```

This view fetches all the menu items from the database and passes them to the `menu.html` template via a dictionary called `context`.

---

### **7. Set Up URL Routing**

Next, we need to create a URL route for the `menu` view. Open `myproject/urls.py` and include a path for the menu:

```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', views.menu, name='menu'),
]

```

This maps the `/menu` URL to the `menu` view we created.

---

### **8. Create the Template `menu.html`**

Now, let's create the HTML template to display the menu items.

1. Create a new folder named `templates` inside your `myapp` directory:
    
    ```bash
    mkdir myapp/templates
    
    ```
    
2. Inside the `templates` folder, create a new file named `menu.html` and add the following content:

```html
<!-- myapp/templates/menu.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menu</title>
</head>
<body>
    <h1>Menu</h1>

    {% if menu %}
        <ul>
            {% for item in menu %}
                <li>{{ item.name }}: ${{ item.price }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No items available in the menu.</p>
    {% endif %}
</body>
</html>

```

This template checks if the `menu` object has any items. If it does, it loops through and displays each item's name and price.

---

### **9. Run the Development Server**

Now that everything is set up, let's run the Django development server to see our app in action:

```bash
python manage.py runserver

```

Go to your browser and navigate to http://127.0.0.1:8000/menu.

If everything is working, you should see a menu page listing your items, or a message saying "No items available" if your database is empty.

---

### **10. Create a Superuser (Optional)**

To add some menu items through the Django admin interface, you can create a superuser by running:

```bash
python manage.py createsuperuser

```

Follow the prompts to create your superuser, then go to http://127.0.0.1:8000/admin, log in, and add some `Menu` items.

Once you add some items, revisit http://127.0.0.1:8000/menu and see the updated menu.

---

### **Conclusion**

You've successfully created a Django project from scratch, built an app, defined a model, created a view, and used templates to display dynamic content. You can now add more functionality, such as user authentication, or extend the menu by adding more fields like descriptions or images.

Let's go through the steps and solve the lab.

---

### **Step 1: Review the `models.py` File**

First, check the `models.py` to ensure the `Menu` model is properly set up with the necessary fields.

```python
# models.py
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name

```

Ensure this code is present in your `models.py`. This model should already exist based on the lab instructions.

---

### **Step 2: Create the View Function in `views.py`**

Now, let's create the view function that will fetch all the menu items and pass them to the template.

1. Open `views.py` inside the `myapp` folder.
2. Add the following code to define the view:

```python
# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

def menu(request):
    # Fetch all items from the Menu model
    menu_items = Menu.objects.all()

    # Create a dictionary to pass to the template
    items_dict = {'menu': menu_items}

    # Render the template with the menu items
    return render(request, 'menu.html', items_dict)

```

---

### **Step 3: Update the `menu.html` Template**

Next, we need to modify the template `menu.html` to display the dynamic content.

1. In the `templates` folder, open or create `menu.html`.
2. Add the following code to display the menu items dynamically using Django Template Language (DTL):

```html
<!-- menu.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Menu</title>
</head>
<body>
    <h1>Little Lemon Menu</h1>

    <!-- Check if there are items in the menu -->
    {% if menu %}
        <!-- Loop through the items in the menu -->
        {% for item in menu %}
            {{ item.name }}: {{ item.price }} <br>
        {% endfor %}
    {% else %}
        <p>No items to display</p>
    {% endif %}
</body>
</html>

```

---

### **Step 4: Migrations**

If the migrations have not been run, ensure the model is applied to the database. Run the following commands in the terminal to handle migrations:

```bash
# Make migrations if needed
python manage.py makemigrations

# Apply the migrations
python manage.py migrate

```

---

### **Step 5: Start the Django Development Server**

Now, start the development server to check the menu page.

```bash
# Start the server
python manage.py runserver

```

Open your browser and go to http://127.0.0.1:8000/menu to see if the dynamic menu is displayed.

---

### **Step 6: Create a Superuser and Add Menu Items (Optional)**

If you'd like to manage the menu items through Django's admin interface, create a superuser and add entries for the `Menu` model:

1. Create a superuser:

```bash
python manage.py createsuperuser

```

1. Go to http://127.0.0.1:8000/admin, log in, and add some menu items like `Pizza` or `Baklava`.
2. Refresh the `/menu` page to see the updated dynamic content.

---

### **Conclusion:**

You have now successfully solved the lab. You created a Django view, passed dynamic content from the `Menu` model to a template, and rendered the content dynamically on a web page using Django Template Language (DTL).

You can add the content to the database either through the Django Admin interface or directly using Django's shell.

I'll show you both methods:

---

### **Option 1: Using Django Admin Interface**

1. **Create a Superuser (if you haven't already):**
   Run the following command to create a superuser, which allows you to access the Django Admin:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a username, email, and password.

2. **Login to Django Admin:**
   Start the server (if it's not already running):

   ```bash
   python manage.py runserver
   ```

   Go to http://127.0.0.1:8000/admin, log in with your superuser credentials, and find the `Menu` model in the admin panel.

3. **Add Menu Items:**
   Click on the `Menu` model, and then click **Add Menu**. Add the following items manually:
   - **Falafel: 12**
   - **Shawarma: 15**
   - **Gyro: 10**
   - **Hummus: 7**
   - **Baklava: 10**

4. **Check the Menu Page:**
   Once the items are added, navigate to http://127.0.0.1:8000/menu to see them displayed on the menu page.

---

### **Option 2: Using Django Shell**

You can also use the Django shell to directly insert the menu items into the database.

1. Open the Django shell by running the following command:

   ```bash
   python manage.py shell
   ```

2. In the shell, execute the following code to insert the items into the database:

   ```python
   from myapp.models import Menu

   # Adding menu items
   Menu.objects.create(name='Falafel', price=12)
   Menu.objects.create(name='Shawarma', price=15)
   Menu.objects.create(name='Gyro', price=10)
   Menu.objects.create(name='Hummus', price=7)
   Menu.objects.create(name='Baklava', price=10)
   ```

3. Exit the shell by typing:

   ```bash
   exit()
   ```

4. **Check the Menu Page:**
   Now, go to http://127.0.0.1:8000/menu to see the newly added menu items displayed on the page.

---

### **Conclusion**
Both methods allow you to easily add the content to your database. The Admin interface is user-friendly, while the shell is quick for bulk inserts or testing.

Let me know if you need further assistance!

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/d3321d89-e35a-4594-a677-588cc7031c0b/3cdfa89a-be7e-4857-8eb0-11129f7edb2d/image.png)

### Exercise: Creating Dynamic Templates in Django

### Goal

The goal of this exercise is to practice fetching dynamic content from a Django model, passing it to a view, and then rendering it in a template using the Django Template Language (DTL).

---

### Steps:

### **Step 1: Review the Model**

- Open `models.py` to see the structure of the `Menu` model.
- It should have at least two fields: `name` (CharField) and `price` (IntegerField), which represent the menu items.

### **Step 2: Create a View for the Menu**

1. Open `views.py` inside your project directory.
2. Create a view function named `menu` to handle the request for the menu page.
3. **Import the `HttpResponse`** from `django.http` to return content (even though we will return HTML with `render()` in this case).
4. **Import the `Menu` model** from `models.py` so you can query it.

### **Step 3: Define the Logic in the `menu` View**

1. Inside the `menu` view function, pass the `request` object.
2. Query all the menu items from the `Menu` model:
    
    ```python
    menu_items = Menu.objects.all()
    
    ```
    
3. Create a dictionary called `items_dict` with a key `"menu"` and assign `menu_items` as its value:
    
    ```python
    items_dict = {'menu': menu_items}
    
    ```
    
4. Return the `render()` function that will load the template and pass the `items_dict` dictionary:
    
    ```python
    return render(request, 'menu.html', items_dict)
    
    ```
    

### **Step 4: Update `menu.html` Template**

1. Open the `menu.html` file from the `templates` folder.
2. Use the **Django Template Language (DTL)** to display dynamic content:
    - **Check if the `menu` dictionary is populated:**
        
        ```html
        {% if menu %}
        
        ```
        
    - **Loop through the items in `menu`:**
        
        ```html
        {% for item in menu %}
            {{ item.name }}: {{ item.price }} <br>
        {% endfor %}
        
        ```
        
    - **Add an else condition to handle the case where the menu is empty:**
        
        ```html
        {% else %}
            No items to display
        {% endif %}
        
        ```
        

### **Step 5: Run Migrations (If Needed)**

- The migration for the `Menu` model might already be completed, but if required, ensure all migrations are up to date:
    
    ```bash
    python manage.py migrate
    
    ```
    

### **Step 6: Start the Development Server**

- In the terminal, run the Django development server:
    
    ```bash
    python manage.py runserver
    
    ```
    
- Open your browser and navigate to http://127.0.0.1:8000/menu.
- Ensure that the dynamic content from the database is displayed correctly.

### **Step 7: (Optional) Create a Superuser and Add Data**

- Create a superuser for accessing the Django admin panel:
    
    ```bash
    python manage.py createsuperuser
    
    ```
    
- Log in to the Django admin at http://127.0.0.1:8000/admin and add items to the `Menu` model. After adding items, refresh the `/menu` page to see the updated content.

---

### **Concluding Thoughts:**

In this lab, you practiced creating a view, passing dynamic content from a model to a template, and displaying it using the Django Template Language (DTL). This skill is essential for creating dynamic websites that display real-time data from a database.