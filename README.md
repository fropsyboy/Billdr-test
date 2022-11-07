### Docmentation

### Assignment files  - `02_front`
### Installation details - `./bulldr-test/README.md`

### Screenshots for quick view - .`/bulldr-test/screenshots`

### - `./bulldr-test/src/screens/userList` - Question 02_front -> 1(a)
### - `./bulldr-test/src/screens/userDescription` - Question 02_front -> 1(b)
### - `./bulldr-test/src/screens/userList` - Question 02_front -> 2
### - `./bulldr-test/src/screens/userDescription` - Question 02_front -> 3
### -    Question 4 - I used pure `bootstrap` as the css framework

### Test file - - `./bulldr-test/src/setupTest.js` : didn't set it up but just added the structure needed to set it up. Tool - ```jest``` for test.

### Env examples: file name - ```.env.development```, ```.env``` : either is fine depending on your setup

```REACT_APP_ENVIRONMENT=development```
```REACT_APP_BASE_URL=https://jsonplaceholder.typicode.com```
```REACT_APP_BASE_URL_AVATAR=https://ui-avatars.com/api```
```REACT_APP_BASE_GOOGLE_KEY=xxxxxxxxxxxx-FMPLxxxxCeyxxxxq-xxxxxxx```

### Assets: - ./bulldr-test/src/assets

### Added feature - Added the search feature: Onclick on the search button the app searching through the whole record.


### Assignment - `04_code_review`


### Code Review for 04_code_to_review.py

### - Line 29, The display_budget function: A simple switch case could have to used to avoid the multiple line if condition,you can follow the link below for code snippets/examples
  `https://docs.python.org/3/tutorial/controlflow.html`

### - Line 29, The display_budget function: this function should not come before the init function even though it iss not compulsory, but it is good practice for a read through.


### - Line 52, The Class APIProject: Try and arrange all the classes together as said above for a clean read through

### - Line 63, Instead of using id, just use the pk; Then you can just do a `Project.objects.get(pk=pk)`

### - Line 49, 62, 77, and 97, The line `@action(detail=False, methods=['post'])` this may not run on all compilers, just to be safe you can just add the request object to the function and do a method check directly.
   ```def Example(request, pk):```
  ```if request.method == "POST":```
  ```Also for this, the methods should be in capital letters```
  
### - Line 7, 13, and 20, When creating the models you need to create the ForeignKeys on the models and when you are creating then you need to assign the attribute charateristics
  ``class Example(models.Model):``
      ``user = models.ForeignKey(``
      ``User, related_name="Example", on_delete=models.DO_NOTHING``
     ``)`` 
      ``body = models.CharField(max_length=140)``
      ``created_at = models.DateTimeField(auto_now_add=True)``

     that is just an example follow the link for more details `https://docs.python.org/3/reference/datamodel.html#objects-values-and-types`


### - Error handling. You need to add an error library for when your API fails for the backend knows what error code and object to send. You can add a simple try and catch to start while you build out the status file.
  ```static status example `status=HTTP_200_OK` from the rest_framework```

    reference - `https://www.django-rest-framework.org/api-guide/status-codes/`

### - Response status: `status=status`: your status is undefined throughout for the return response