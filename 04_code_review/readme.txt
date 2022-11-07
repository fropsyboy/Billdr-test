GOAL: The goal here is to do some code reviews of the following file "code_to_review.py"
(this file is actually not working, it's just for the purpose of the exercise, don't try to run it)

CONTEXT: A junior developer is asking you to review his pull request, the feature was to create a CRUD API on the "Project" Model.
Classes "Homeowner", "Contractor", "Project" represent the Data model
Class "APIProject" contains all the functions in charge of the CRUD request 
We assume here that we already have libraries/framework installed like Django, ORM for the models, routing system,...

TIPS: Don't hesitate to give any feedback, to go deep in details, there is actually no bad/wrong answer
For each feedback, pls write down the line and the reason.
Ex:
- Line XX, This part of code is not consistent,...
- Line XX, I would have refacto this part with the following code:...
- ...


### Code Review for 04_code_to_review.py

- Line 29, The display_budget function: A simple switch case could have to used to avoid the multiple line if condition,you can follow the link below for code snippets/examples
                                        `https://docs.python.org/3/tutorial/controlflow.html`

- Line 29, The display_budget function: this function should not come before the init function even though it iss not compulsory, but it is good practice for a read through.


- Line 52, The Class APIProject: Try and arrange all the classes together as said above for a clean read through

- Line 63, Instead of using id, just use the pk; Then you can just do a `Project.objects.get(pk=pk)`

- Line 7, 13, and 20, When creating the models you need to create the ForeignKeys on the models and when you are creating then you need to assign the attribute charateristics
                        ```class Example(models.Model):
                               user = models.ForeignKey(
                                   User, related_name="Example", on_delete=models.DO_NOTHING
                               )
                               body = models.CharField(max_length=140)
                               created_at = models.DateTimeField(auto_now_add=True) ```

                       that is just an example follow the link for more details `https://docs.python.org/3/reference/datamodel.html#objects-values-and-types`

- Line 49, 62, 77, and 97, The line `@action(detail=False, methods=['post'])` this may not run on all compilers, just to be safe you can just add the request object to the function and do
                            a method check directly.
                            ``` def Example(request, pk):
                                    if request.method == "POST":```
                            Also for this, the methods should be in capital letters

- Error handling. You need to add an error library for when your API fails for the backend knows what error code and object to send. You can add a simple try and catch to
                    start while you build out the status file.
                    static status example `status=HTTP_200_OK` from the rest_framework

                    reference - `https://www.django-rest-framework.org/api-guide/status-codes/`

- Response status: `status=status`: your status is undefined throughout for the return response