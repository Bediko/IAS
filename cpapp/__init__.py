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

_database_ = {
		"BE03" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"BE04" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"BE05" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"BE06" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"BE07" : {
			"Raumtyp": "Lagerraum",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"BE08" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"BE09" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"BE10" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		
		"BE12" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		
		
		"BE13" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		
		"BE14" : {
			"Raumtyp": "Hörsaal",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"BE15" : {
			"Raumtyp": "Vorraum",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "20",
			"Hinweise": "keine"
		},	
		
		"BE16" : {
			"Raumtyp": "Hörsaal",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},		
		
		"BE17" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"BE18" : {
			"Raumtyp": "Büro",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"BE19" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"BE20" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"BE21" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"BE22" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"BE23" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"BE24" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"BE25" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},	
		
		
		"BE26" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"BE27" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"BE28" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},	
		
		"B103" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B104" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B105" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B106" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B107" : {
			"Raumtyp": "Lagerraum",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B108" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B109" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B110" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		
		"B112" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		
		
		"B113" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		
		"B114" : {
			"Raumtyp": "Hörsaal",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"B115" : {
			"Raumtyp": "Vorraum",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "20",
			"Hinweise": "keine"
		},	
		
		"B116" : {
			"Raumtyp": "Hörsaal",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},		
		
		"B117" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B118" : {
			"Raumtyp": "Büro",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"B119" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B120" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B121" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B122" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B123" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B124" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B125" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},	
		
		
		"B126" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B127" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B128" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B203" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B204" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B205" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B206" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B207" : {
			"Raumtyp": "Lagerraum",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B208" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B209" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B210" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		
		"B212" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		"B213" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		
		"B214" : {
			"Raumtyp": "Hörsaal",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"B215" : {
			"Raumtyp": "Vorraum",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "20",
			"Hinweise": "keine"
		},	
		
		"B216" : {
			"Raumtyp": "Hörsaal",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},		
		
		"B217" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B218" : {
			"Raumtyp": "Büro",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"B219" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B220" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B221" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B222" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B223" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B224" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B225" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},	
		
		
		"B226" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B227" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B228" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},	
		"B303" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B304" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B305" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B306" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B307" : {
			"Raumtyp": "Lagerraum",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B308" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B309" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B310" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		
		"B312" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		
		
		"B313" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"B314" : {
			"Raumtyp": "Hörsaal",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"B315" : {
			"Raumtyp": "Vorraum",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "20",
			"Hinweise": "keine"
		},	
		
		"B316" : {
			"Raumtyp": "Hörsaal",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},		
		
		"B317" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B318" : {
			"Raumtyp": "Büro",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"B319" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B320" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B321" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B322" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B323" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B324" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B325" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},	
		
		
		"B326" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B327" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B328" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},	
			"B403" : {
				"Raumtyp": "Toilette",
				"Beamer": "nein",
				"Tafel": "nein",
				"Sonderausstattung": "keine",
				"Kapazität": "5",
				"Hinweise": "keine"
		},
		"B404" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B405" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B406" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B407" : {
			"Raumtyp": "Lagerraum",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B408" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B409" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B410" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		
		"B412" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		
		
		"B413" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		
		"B414" : {
			"Raumtyp": "Hörsaal",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"B415" : {
			"Raumtyp": "Vorraum",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "20",
			"Hinweise": "keine"
		},	
		
		"B416" : {
			"Raumtyp": "Hörsaal",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},		
		
		"B417" : {	
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B418" : {
			"Raumtyp": "Büro",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"B419" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B420" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B421" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B422" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B423" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B424" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B425" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},	
		
		
		"B426" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B427" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",	
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B428" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},	
		"B503" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B504" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B505" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B506" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B507" : {
			"Raumtyp": "Lagerraum",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"B508" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B509" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"B510" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		
		"B512" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		
		
		"B513" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		
		"B514" : {
			"Raumtyp": "Hörsaal",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"B515" : {
			"Raumtyp": "Vorraum",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "20",
			"Hinweise": "keine"
		},	
		
		"B516" : {
			"Raumtyp": "Hörsaal",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},		
		
		"B517" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B518" : {
			"Raumtyp": "Büro",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"B519" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B520" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B521" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B522" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B523" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B524" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B525" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},	
		
		
		"B526" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B527" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		
		"B528" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},	
		"FE01" : {
			"Raumtyp": "Büro/Labor",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"FE02" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"FE03" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"FE04" : {
			"Raumtyp": "Labor",
			"Beamer": "nein",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"FE05" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"FE06" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "Ja",
			"Tafel": "Ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"FE07" : {
			"Raumtyp": "Labor/Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"FE08" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		"FE09" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"FE10" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "10",
			"Hinweise": "keine"
		},
		"FE12" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "10",
			"Hinweise": "keine"
		},

		"F101" : {
			"Raumtyp": "Büro/Labor",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"F102" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F103" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"F104" : {
			"Raumtyp": "Labor",
			"Beamer": "nein",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F105" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F106" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "Ja",
			"Tafel": "Ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F107" : {
			"Raumtyp": "Labor/Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F108" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		"F109" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"F110" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "10",
			"Hinweise": "keine"
		},
		"F112" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "10",
			"Hinweise": "keine"
		},
		
		"F201" : {
			"Raumtyp": "Büro/Labor",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"F202" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F203" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"F204" : {
			"Raumtyp": "Labor",
			"Beamer": "nein",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F205" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F206" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "Ja",
			"Tafel": "Ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F207" : {
			"Raumtyp": "Labor/Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F208" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		"F209" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"F210" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "10",
			"Hinweise": "keine"
		},
		"F212" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "10",
			"Hinweise": "keine"
		},
		
		"F301" : {
			"Raumtyp": "Büro/Labor",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"F302" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F303" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		
		"F304" : {
			"Raumtyp": "Labor",
			"Beamer": "nein",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F305" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F306" : {
			"Raumtyp": "Seminarraum",
			"Beamer": "Ja",
			"Tafel": "Ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F307" : {
			"Raumtyp": "Labor/Seminarraum",
			"Beamer": "ja",
			"Tafel": "ja",
			"Sonderausstattung": "keine",
			"Kapazität": "50",
			"Hinweise": "keine"
		},
		"F308" : {
			"Raumtyp": "Abstellkammer",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "2",
			"Hinweise": "keine"
		},
		"F309" : {
			"Raumtyp": "Büro",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "5",
			"Hinweise": "keine"
		},
		"F310" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "10",
			"Hinweise": "keine"
		},
		"F312" : {
			"Raumtyp": "Toilette",
			"Beamer": "nein",
			"Tafel": "nein",
			"Sonderausstattung": "keine",
			"Kapazität": "10",
			"Hinweise": "keine"
		}
}

	


class Root(object):
  def index(self):
    template=mylookup.get_template('index.html')
    return template.render()
  index.exposed = True

