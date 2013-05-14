static-files-in-django
======================

[![Build Status](https://api.travis-ci.org/repositories/akshar-raaj/static-files-in-django.png)](https://travis-ci.org/akshar-raaj/static-files-in-django/)

Project used in blog entry which I wrote at <a href="http://agiliq.com/blog/2013/03/serving-static-files-in-django/">Agiliq blog</a>.

###Running test

    python manage.py test some_app other_app --settings=test_project.test_settings

###Running test with coverage.py

    coverage run --source="." manage.py test some_app other_app --settings=test_project.test_settings

#####Generate html report for test

    coverage html
