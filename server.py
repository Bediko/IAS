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

myconfig = os.path.join(os.path.dirname(__file__),'config_file')

mylookup = TemplateLookup(directories=['./templ'], module_directory='/tmp/mako_modules')

class Start(object):
  def index(self):
    template=mylookup.get_template('index.html')
    return template.render()
  index.exposed = True

cherrypy.quickstart(Start(),config=myconfig)
