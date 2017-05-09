##!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Vincent(vliao@pacsoft.com.tw)

content = []
filter_list = ['[HTML] ', '[PDF] ', '[CITATION] ', '[BOOK] ', '[DOC] ', '\r\n']


def write_into_list(filename):
    with open(filename, 'r') as f:
        for line in f:
            content.append(line)


def slice(filename):
    with open(filename, 'r') as f:
        idx = 0
        idx_list = []
        slice_content = None
        for line in f:
            idx += 1
            if 'Search within citing articles' in line:
                idx_list.append(idx)
            if 'About Google Scholar Privacy Terms Provide feedback' in line:
                idx_list.append(idx)
        if idx_list:
            slice_content = content[idx_list[0]: idx_list[len(idx_list)-1]]
    return slice_content


def check(i, slice_content):
    a = 0
    result = None
    while a != 5:
        a += 1
        if 'Cite' in slice_content[i-a] or ('.' in slice_content[i-a] and '[PDF]' in slice_content[i-a]):
            result = slice_content[i-a+1]
            if '[PDF]' in slice_content[i-a-1]:
                result = slice_content[i-a]
            break
    return result


def get_google_title(filename):
    google_title_list = []
    write_into_list(filename)
    slice_content = slice(filename)
    if slice_content is not None:
        for i in range(0 , len(slice_content)):
            if 'Cite' in slice_content[i] and 'Save' in slice_content[i]:
                ck_result = check(i, slice_content)
                if ck_result is None:
                    slice_tmp = slice_content[i - 5]
                    for item in filter_list:
                        slice_tmp = slice_tmp.replace(item, '', 1)
                    google_title_list.append(slice_tmp)
                else:
                    ck_tmp = ck_result
                    for item in filter_list:
                        ck_tmp = ck_tmp.replace(item, '', 1)
                    google_title_list.append(ck_tmp)
    return google_title_list
