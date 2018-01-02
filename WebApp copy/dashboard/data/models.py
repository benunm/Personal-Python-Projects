from __future__ import unicode_literals

from django.db import models

class Code_810(models.Model):
    invoice_number = models.IntegerField(db_column='Invoice_Number', blank=True, null=True)  # Field name made lowercase.
    customer_number = models.CharField(db_column='Customer_Number', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer_purchase_order_number = models.IntegerField(db_column='Customer_Purchase_Order_Number', blank=True, null=True)  # Field name made lowercase.
    doctype = models.IntegerField(db_column='DOCTYPE', blank=True, null=True)  # Field name made lowercase.

class Code_856(models.Model):
    invoice_number = models.IntegerField(db_column='Invoice_Number', blank=True, null=True)  # Field name made lowercase.
    customer_number = models.CharField(db_column='Customer_Number', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer_purchase_order_number = models.IntegerField(db_column='Customer_Purchase_Order_Number', blank=True, null=True)  # Field name made lowercase.
    doctype = models.IntegerField(db_column='DOCTYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
    	managed = False
    	db_table = 'TEST2'

class TEST(models.Model):
    invoice_number = models.IntegerField(db_column='Invoice_Number', blank=True, null=True)  # Field name made lowercase.
    customer_number = models.CharField(db_column='Customer_Number', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customer_purchase_order_number = models.IntegerField(db_column='Customer_Purchase_Order_Number', blank=True, null=True)  # Field name made lowercase.
    doctype = models.IntegerField(db_column='DOCTYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
    	managed = False
    	db_table = 'TEST'