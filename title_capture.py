##!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Vincent(vliao@pacsoft.com.tw)
from google_title_capture import get_google_title


def get_web_title(filename):
    content = []
    with open(filename) as f:
        for line in f:
            content.append(line.replace('\r\n', ''))
    title_list = []
    for i in range(0, len(content)):
        if 'By: ' in content[i]:
            title_list.append(content[i-1].replace('\r\n', ''))
    return title_list


def get_scopus_title(filename):
    content = []
    with open(filename) as f:
        for line in f:
            content.append(line)
    title_list = []
    for i in range(0, len(content)):
        if 'Authors of Document' in content[i]:
            title_list.append(content[i][0:content[i].index('Authors of Document')].replace(' Document ', '', 1))
    return title_list

final_result = []


def modify(x):
    for item in final_result[0]:
        # if name_compare(item, filter(str.isalpha, x.lower())) == 1:
        if item == filter(str.isalpha, x.lower()):
            final_result[0].remove(item)
            final_result[0].append(x)


def main(filename):
    r = {}
    google_title = get_google_title(filename)
    scopus_title = get_scopus_title(filename)
    web_title = get_web_title(filename)
    var_list = [google_title, scopus_title, web_title]
    all = []
    for v in var_list:
        for sub_title in v:
            if len(filter(str.isalpha, sub_title.lower())) / float(len(sub_title)) <= 0.2:
                all.append(sub_title)
            else:
                all.append(filter(str.isalpha, sub_title.lower()))
    merge = list(set(all))
    print 'Total: ' + str(len(merge))
    final_result.append(merge)
    map(modify, google_title)
    map(modify, scopus_title)
    map(modify, web_title)
    r['title'] = final_result[0]
    return r
