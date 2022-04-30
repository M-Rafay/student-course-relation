# Django REST Framwork (EDWIZ Interview Screening Test)
Student REST API using Django REST Framework

You are required to create a REST API to manage the records of Students and their enrolled courses.

<br>
<h3>Here's what your models.py would look like:</h3>

Courses:
  + course_name : CharField
  + source : CharField

Students:
  + name : CharField
  + enrolled_courses : ManyToManyField(Courses)


<br>
Now, serialize them to create the required output. The sample output is attached in <a href="https://github.com/iihsan/Django-REST-Task/blob/main/sample.json">sample.json</a> file.

<br>
<h3>Here are the some steps</h3>
  <ul>Create these models in models.py (you are free to add more columns if you want)</ul>
  <ul>Create serializers in serializers.py (you are free to use any serializer)</ul>
  <ul>Create their API endpoints in views.py (you are free to use any viewset)</ul>
  <ul>Route these endpoints in urls.py</ul>

<br>
Hint: Nested serializer is required to create the sample output format.


<br>
<br>

<h3 style="color:green">Submission Criteria</h3>
You have 48 hours to submit this task or our HR will communicate you accordingly.

After completing your task, you will be required to submit it:
+ you can upload your task to public git repository and share your link at the given email address <a href="mailto:iihsanofficial@gmail.com">iihsanofficial@gmail.com</a>
+ or alternatively, you can directly share your task to given email address <a href="mailto:hr@edwiz.net">hr@edwiz.net</a> in a zip file

<h3>Sample Output <a href="https://github.com/iihsan/Django-REST-Task/blob/main/sample.json">sample.json</a></h3>
