# Django

[Official docs](https://www.djangoproject.com/)

Django is a MVC system by which you can create and manage your content; however; instead of this being MVC in django, this is known as MTV.

## MCV -> MTV

The contempt between MCV to MTV stays the same, but the terminology used makes a small shift.

M - [Model](https://docs.djangoproject.com/en/5.0/topics/db/models/), (Model -> Model) which is the interface for interaction with data. This is a level of abstraction that allows use to modify that data stored in the database. As a result, this is considered a security improvement.

T - [Template](https://docs.djangoproject.com/en/5.0/topics/templates/) (View -> Template), visible interface aka the the presentation. You can also think of these as the different pages that are generated on different devices. From the user's perspective though, they should have no preservable knowledge of the View nor Model.

V - [View](https://docs.djangoproject.com/en/5.0/topics/http/urls/) (Controller -> View), the logic the dictates the interactions of the interface (templates) with the data (model). The view does not work with the database directly, but goes through the model. 