
from os.path import abspath, dirname, join
from google.appengine.ext import vendor

vendor.add(abspath(join(dirname(__file__), 'lib')))
