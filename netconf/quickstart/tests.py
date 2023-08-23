from django.test import TestCase

# Create your tests here.

class myNetconf():
    def __init__(self, capability):
        self.capability = capability

class GetNetconfig():
    def __init__(self, data, created=None):
        self.data = data