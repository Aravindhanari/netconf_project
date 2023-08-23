from django.test import TestCase

# Create your tests here.

class myData():

    def __init__(self, linkedin, github, my_website, medium, created=None):
        self.linkedin = linkedin
        self.github = github
        self.my_website = my_website
        self.medium = medium

class myNetconf():

    def __init__(self, capability, created=None):
        self.capability = capability

class GetNetconfig():

    def __init__(self, data, created=None):
        self.data = data