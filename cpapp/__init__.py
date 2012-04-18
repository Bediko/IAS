#! /usr/bin/python
# coding:utf-8

import cherrypy
import os.path
import pickle
import mako
from pprint import pprint
from mako.template import Template
from mako.lookup import TemplateLookup
from copy import deepcopy
current_dir = os.path.dirname(os.path.abspath(__file__))

mylookup = TemplateLookup(directories=[current_dir +'/templ'], module_directory='/tmp/mako_modules')

class Root(object):
  def index(self):
    template=mylookup.get_template('index.html')
    return template.render()
  index.exposed = True

