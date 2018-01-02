# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.db import connections

import pandas as pd

# Create your views here.
def home(request):
	numbers = [1,2,3,4,5]
	name = 'Max Goodridge'
	args = {'myName': name, 'numbers': numbers}
	return render(request, 'accounts/home.html', args)

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = UserCreationForm()
		args = {'form': form}
		return render(request, 'accounts/reg_form.html', args)

def profile(request):
	args = {'user': request.user}
	
	return render(request, 'accounts/profile.html', args)

def logout(request):
    return render(request, 'accounts/logout.html', args)

# @login_required()
# def test_page(request):
# 	return render(request, 'accounts/test.html')

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def get_table_names():
    '''returns a list of table names'''
    with connections['mydb'].cursor() as cursor:
        get_tables_query = '''
        select name from sqlite_master where type = 'table';
        '''
        ex = cursor.execute(get_tables_query)
        tables = []
        for i in ex:
            tables.append(i[0].encode('utf-8'))
    return tables	

# class Rout(object):
#     def db_for_read(self, model, **hints):
#         return 'mydb'

def listfetchall(cursor):
    "Return all rows from a cursor as a list"
    return [
        list(row)
        for row in cursor.fetchall()
    ]

def test_page(request):
    with connections['mydb'].cursor() as cursor:
        tables = ['accounts_code_810', 'TEST2']
        all_records = []
        result = {}
        result['ths'] = ['Invoice Number', 'Customer Number', 'Customer Purchase Order Number', 'DOCTYPE']
        tables_data = []
        names = []
        for table in tables:
            cursor.execute('SELECT * FROM %s' %(table))
            trs = listfetchall(cursor)
            table_data = {'record_set':len(trs), 'trs':trs}
            names.append(table.encode('utf-8'))
            #tables_data[table] = table_data
            table_data = {'name':table,'record_set':len(trs), 'trs':trs}
            tables_data.append(table_data)
        #tables_data['names'] = names
        result['tables_data'] = tables_data
    return render(request, 'accounts/test2.html', context=result)

def get_current_path(request):
    return {
       'current_path': request.get_full_path()
     }
def tables2(request):
    with connections['mydb'].cursor() as cursor:
        tables = ['accounts_code_810', 'TEST2']
        all_records = []
        result = {}
        result['ths'] = ['Invoice Number', 'Customer Number', 'Customer Purchase Order Number', 'DOCTYPE']
        tables_data = []
        path = request.get_full_path().split('/')[-1]
        cursor.execute('SELECT * FROM %s' %(path))
        trs = listfetchall(cursor)
        table_data = {'record_set':len(trs), 'trs':trs}
        result['table_data'] = table_data
    return render(request, 'accounts/tables2.html', context=result)

@login_required()
def buttons(request):
    # missing the headers
    with connections['dbtest'].cursor() as cursor:
        tables = {
            'tempstatus810':'810',
            'tempstatus856':'856',
            'tempstatus997':'997'
            }
        buttons_data = []
        for table in tables:
            cursor.execute('SELECT COUNT(*) FROM %s' %(table))
            name = 'CODE '+tables[table]
            record_set = cursor.fetchone()[0]
            style_class = 'Code_'+tables[table]
            button = {'name':name,'record_set':record_set, 'style_class':style_class}
            buttons_data.append(button)
        result = {}
        result['buttons_data'] = buttons_data
    return render(request, 'accounts/buttons.html', context=result)

def callproc(self, procname):
    return 'placeholder'


import pyodbc
import pandas
import pandas.io.sql as psql

def tables(request):
    #db_info = 'DSN=bentex-amt1;DATABASE=ELI_DB;UID=DBAUser;PWD=DBAUser'
    with connections['dbtest'].cursor() as cursor:
        tables = {
            'Code_810':'tempstatus810',
            'Code_856':'tempstatus856',
            'Code_997':'tempstatus997'
            }
        path = request.get_full_path().split('/')[-1]
        table = tables[path]
        columns = ['Company_Code',
                    'Division_Code',
                    'Record_Number',
                    'Customer_Number',
                    'Customer_Purchase_Order_Number',
                    'DATE_INVOICED',
                    'DATE_CREATED',
                    'DOCTYPE',
                    'SEGMENTSEPERATOR',
                    'ELEMENTSEPERATOR',
                    'REMARKS',
                    'id']
                
        sql = ("SELECT %s,%s,%s,%s,%s,%s,%s,%s,%s,%s FROM %s" \
            %('Company_Code','Division_Code','Record_Number','Customer_Number',
            'Customer_Purchase_Order_Number','DATE_INVOICED','DATE_CREATED','DOCTYPE',
            'REMARKS','id',table))
        cursor.execute(sql)
        data = listfetchall(cursor)
        result = {}
        result['data'] = data
        code = ' '.join(path.split('_'))
        result['code'] = code
        headers = ['Company Code',
            'Division Code',
            'Record Number',
            'Customer Number',
            'PO Number',
            'Date Invoiced',
            'Date Created',
            'Doctype',
            'Remarks',
            'ID']
        result['headers'] = headers
    return render(request, 'accounts/tables.html', context=result)


#cursor.callproc("EMAIL_FAEDI_STATUS")

def tablesNEW(request):
    #db_info = 'DSN=bentex-amt1;DATABASE=ELI_DB;UID=DBAUser;PWD=DBAUser'
    with connections['dbtest'].cursor() as cursor:
        tables = {
            'Code_810':'tempstatus810',
            'Code_856':'tempstatus856',
            'Code_997':'tempstatus997'
            }
        path = request.get_full_path().split('/')[-1]
        table = tables[path]
        result = {}
        result['data'] = data
        code = ' '.join(path.split('_'))
        result['code'] = code
        headers = ['Company Code',
            'Division Code',
            'Record Number',
            'Customer Number',
            'PO Number',
            'Date Invoiced',
            'Date Created',
            'Doctype',
            'Remarks',
            'ID']
        result['headers'] = headers
    return render(request, 'accounts/tables.html', context=result)


# rewrite data variable with models

# result['data'] = data
# result['code'] = code
# result['headers'] = headers
















