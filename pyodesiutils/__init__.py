#!/usr/bin/python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import json


def parse_this_xml_file(filename):
    soup = BeautifulSoup(open(filename), "xml")
    return soup

def retrieve_label_and_qstnlit(filename):
    soup = parse_this_xml_file(filename)
    var =  soup.find_all('var')
    node_found = []

    for i in var:
        #is there a node named 'qstnLit'
        if i.find('qstnLit'):
            #making sure there is a text in the node
            if len(i.find('qstnLit').text.strip()) >0 and len(i.find('labl').text.strip()) >0:
                variable_name = i['name']
                g = lambda elem: i.find(elem).text.strip()
                label  = g('labl')
                qstnLit = g('qstnLit')
                node_found.append({'label': label,
                            'qstnLit': qstnLit, 'variable_name':variable_name,
                            'label_warning': len(label)>251 } )
    return node_found

def bilingual_files(xml_fr,xml_en):
    #first file in French the second one in English
    soup = parse_this_xml_file(xml_fr)
    soup_other = parse_this_xml_file(xml_en)
    var =  soup.find_all('var')
    var_other = soup_other.find_all('var')
    node_found = []

    for i in var:
        if i.find('qstnLit'):
            if len(i.find('qstnLit').text.strip()) >0 and len(i.find('labl').text.strip()) >0:
                g = lambda x,elem: x.find(elem).text.strip()
                label = g(i,'labl')
                qstnLit = g(i, 'qstnLit')
                variable_name = i['name']

                #other language
                try:
                	  other_lang = soup_other.find("var", {"name":variable_name})
                	  label_en = g(other_lang, 'labl')
                	  qstnLit_en = g(other_lang, 'qstnLit')
                except:
                	  label_en = ""
                	  qstnLit_en = ""

                tmp = {'label_fr': label,
                'qstnLit_fr': qstnLit, 'variable_name':variable_name,
                'label_warning_fr': len(label)>251 ,
                 'label_en':label_en, 'qstnLit_en':qstnLit_en,
                 'label_warning_en': len(label_en)>251
                 }
                node_found.append(tmp)
                print(tmp)
    return node_found

