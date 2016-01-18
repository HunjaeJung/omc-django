# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Picture'
        
        db.create_table('cms_picture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('original_image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('compress_image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True)),
            ('regdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cms', ['Picture'])

        # Adding model 'Store'
        db.create_table('cms_store', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('store_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('president_name', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('business_number', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('manager_name', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('manager_phone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=7)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=7)),
            ('dayoff', self.gf('django.db.models.fields.CharField')(max_length=46)),
            ('open_time', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('close_time', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('prime_image', self.gf('django.db.models.fields.related.ForeignKey')(related_name='prime_iamge', null=True, to=orm['cms.Picture'])),
            ('visible_flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('activate_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('regdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cms', ['Store'])

        # Adding M2M table for field pictures on 'Store'
        db.create_table('cms_store_pictures', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('store', models.ForeignKey(orm['cms.store'], null=False)),
            ('picture', models.ForeignKey(orm['cms.picture'], null=False))
        ))
        db.create_unique('cms_store_pictures', ['store_id', 'picture_id'])

        # Adding model 'Member'
        db.create_table('cms_member', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('udid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=16, null=True)),
            ('birthday', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('gender', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('push_acceptable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_login_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('regdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cms', ['Member'])

        # Adding model 'Coupon'
        db.create_table('cms_coupon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Store'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('original_price', self.gf('django.db.models.fields.FloatField')()),
            ('discount_price', self.gf('django.db.models.fields.FloatField')()),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Picture'], null=True)),
            ('activated_date_time', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('expired_date_time', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('weeks', self.gf('django.db.models.fields.CharField')(max_length=46)),
            ('visible_flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('publish_flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('regdate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cms', ['Coupon'])

        # Adding model 'MyCoupon'
        db.create_table('cms_mycoupon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coupon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Coupon'])),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Member'])),
            ('useable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('cms', ['MyCoupon'])

        # Adding model 'StoreReview'
        db.create_table('cms_storereview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Store'])),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Member'])),
            ('contents', self.gf('django.db.models.fields.TextField')()),
            ('regdate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cms', ['StoreReview'])

        # Adding model 'Like'
        db.create_table('cms_like', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Store'])),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Member'])),
            ('regdate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cms', ['Like'])

        # Adding model 'Visit'
        db.create_table('cms_visit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Store'])),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Member'])),
            ('visit_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cms', ['Visit'])

        # Adding model 'Board'
        db.create_table('cms_board', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Store'])),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('contents', self.gf('django.db.models.fields.TextField')()),
            ('reply_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('regdate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cms', ['Board'])

        # Adding model 'BoardReply'
        db.create_table('cms_boardreply', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('board', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Board'])),
            ('contents', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('cms', ['BoardReply'])

        # Adding model 'Bill'
        db.create_table('cms_bill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bill_type', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('point', self.gf('django.db.models.fields.IntegerField')()),
            ('activate_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('expired_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('cms', ['Bill'])

        # Adding model 'MyBill'
        db.create_table('cms_mybill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Store'])),
            ('bill_type', self.gf('django.db.models.fields.IntegerField')()),
            ('point', self.gf('django.db.models.fields.IntegerField')()),
            ('activate_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('expired_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('expense_type', self.gf('django.db.models.fields.IntegerField')()),
            ('expense_price', self.gf('django.db.models.fields.FloatField')()),
            ('regdate', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cms', ['MyBill'])

        # Adding model 'Notice'
        db.create_table('cms_notice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('contents', self.gf('django.db.models.fields.TextField')()),
            ('display_flag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('regdate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cms', ['Notice'])

        # Adding model 'Push'
        db.create_table('cms_push', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contents', self.gf('django.db.models.fields.TextField')()),
            ('activated_date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('regdate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cms', ['Push'])


    def backwards(self, orm):
        # Deleting model 'Picture'
        db.delete_table('cms_picture')

        # Deleting model 'Store'
        db.delete_table('cms_store')

        # Removing M2M table for field pictures on 'Store'
        db.delete_table('cms_store_pictures')

        # Deleting model 'Member'
        db.delete_table('cms_member')

        # Deleting model 'Coupon'
        db.delete_table('cms_coupon')

        # Deleting model 'MyCoupon'
        db.delete_table('cms_mycoupon')

        # Deleting model 'StoreReview'
        db.delete_table('cms_storereview')

        # Deleting model 'Like'
        db.delete_table('cms_like')

        # Deleting model 'Visit'
        db.delete_table('cms_visit')

        # Deleting model 'Board'
        db.delete_table('cms_board')

        # Deleting model 'BoardReply'
        db.delete_table('cms_boardreply')

        # Deleting model 'Bill'
        db.delete_table('cms_bill')

        # Deleting model 'MyBill'
        db.delete_table('cms_mybill')

        # Deleting model 'Notice'
        db.delete_table('cms_notice')

        # Deleting model 'Push'
        db.delete_table('cms_push')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.bill': {
            'Meta': {'object_name': 'Bill'},
            'activate_date': ('django.db.models.fields.DateTimeField', [], {}),
            'bill_type': ('django.db.models.fields.IntegerField', [], {}),
            'expired_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.FloatField', [], {})
        },
        'cms.board': {
            'Meta': {'object_name': 'Board'},
            'contents': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'regdate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'reply_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Store']"}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        'cms.boardreply': {
            'Meta': {'object_name': 'BoardReply'},
            'board': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Board']"}),
            'contents': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'cms.coupon': {
            'Meta': {'object_name': 'Coupon'},
            'activated_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'discount_price': ('django.db.models.fields.FloatField', [], {}),
            'expired_date_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Picture']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'original_price': ('django.db.models.fields.FloatField', [], {}),
            'publish_flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'regdate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Store']"}),
            'visible_flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'weeks': ('django.db.models.fields.CharField', [], {'max_length': '46'})
        },
        'cms.like': {
            'Meta': {'object_name': 'Like'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Member']"}),
            'regdate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Store']"})
        },
        'cms.member': {
            'Meta': {'object_name': 'Member'},
            'birthday': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'gender': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'push_acceptable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'regdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'udid': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'cms.mybill': {
            'Meta': {'object_name': 'MyBill'},
            'activate_date': ('django.db.models.fields.DateTimeField', [], {}),
            'bill_type': ('django.db.models.fields.IntegerField', [], {}),
            'expense_price': ('django.db.models.fields.FloatField', [], {}),
            'expense_type': ('django.db.models.fields.IntegerField', [], {}),
            'expired_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('django.db.models.fields.IntegerField', [], {}),
            'regdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Store']"})
        },
        'cms.mycoupon': {
            'Meta': {'object_name': 'MyCoupon'},
            'coupon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Coupon']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Member']"}),
            'useable': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'cms.notice': {
            'Meta': {'object_name': 'Notice'},
            'contents': ('django.db.models.fields.TextField', [], {}),
            'display_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'regdate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        'cms.picture': {
            'Meta': {'object_name': 'Picture'},
            'compress_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'regdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'cms.push': {
            'Meta': {'object_name': 'Push'},
            'activated_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'contents': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'regdate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'cms.store': {
            'Meta': {'object_name': 'Store'},
            'activate_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'business_number': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'close_time': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'dayoff': ('django.db.models.fields.CharField', [], {'max_length': '46'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'manager_name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'manager_phone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'open_time': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'pictures': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'pictures'", 'symmetrical': 'False', 'to': "orm['cms.Picture']"}),
            'president_name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'prime_image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prime_iamge'", 'null': 'True', 'to': "orm['cms.Picture']"}),
            'regdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'store_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'visible_flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'cms.storereview': {
            'Meta': {'object_name': 'StoreReview'},
            'contents': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Member']"}),
            'regdate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Store']"})
        },
        'cms.visit': {
            'Meta': {'object_name': 'Visit'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Member']"}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Store']"}),
            'visit_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cms']