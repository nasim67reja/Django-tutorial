# Django Set up guide

## Install Globally `python -m pip install django`

**Check** ⇒ `django-admin`

**Start Project** ⇒ `django-admin startproject mypage`

**To initialize a Django project, follow these steps:**

1. Install Django globally by running `python -m pip install django` in your command line.
2. Check if Django is installed successfully by running `django-admin` in your command line.
3. Start a new project by running `django-admin startproject mypage` in your command line. Replace "mypage" with the desired name of your project.

After these steps, your Django project will be initialized and ready for further development.

To run the development server and create apps in Django, follow these steps:

**Run the Development Server**

1. Navigate to the root directory of your Django project in the command line.
2. Run the following command: `python manage.py runserver`
3. The development server will start running, and you can access your Django project by visiting `http://localhost:8000` in your web browser.

**Create Apps**

1. Navigate to the root directory of your Django project in the command line.
2. Run the following command to create a new app: `python manage.py startapp myapp`
3. Replace "myapp" with the desired name of your app.
4. Django will create a new directory with the app's name, containing the necessary files and folders to get started with your app's development.

With these steps, you can run the development server and create apps in your Django project.

## Apps

In Django, apps are modular components that serve specific functions within a project. An app can be considered as a self-contained module that encapsulates a specific functionality or feature of a Django project. Each app can have its own models, views, templates, and static files.

Apps allow you to organize your project's functionality into smaller, manageable pieces. They promote modularity, reusability, and maintainability. Apps can be developed independently and can be plugged into different Django projects as needed.

For example, you can create an app for user authentication, another app for blog functionality, and another app for an e-commerce store. Each app can have its own set of models, views, templates, and URLs, making it easier to manage and maintain different parts of your project.

By creating apps, you can keep your project structure organized and maintain a clear separation of concerns. This modular approach makes it easier to add, remove, or update features without affecting other parts of the project. Additionally, apps can be shared and reused across different projects or even shared with the Django community.

To create a new app in Django, you can use the `startapp` command followed by the desired name of your app. This will create a new directory with the app's name and the necessary files and folders to begin developing your app.

Apps play a crucial role in Django's architecture and contribute to the overall flexibility and extensibility of the framework.
