# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Picture(models.Model):
    original_image = models.FileField(null=True, upload_to='picture/%Y%m%d')
    compress_image = models.FileField(null=True, upload_to='picture/%Y%m%d')
    regdate = models.DateTimeField(null=False, auto_now_add=True)

    def __unicode__(self):
        result = u'사진'
        return result


class Store(models.Model):
    user = models.ForeignKey(User, unique=True)
    store_name = models.CharField(max_length=50, null=False)
    president_name = models.CharField(max_length=16, null=False)
    business_number = models.CharField(max_length=16, null=False)
    manager_name = models.CharField(max_length=16, null=False)
    manager_phone = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=80, null=False)
    description = models.TextField(null=True)
    latitude = models.FloatField(null=False, default=0.0)
    longitude = models.FloatField(null=False, default=0.0)
    dayoff = models.CharField(max_length=46, null=False)
    open_time = models.CharField(max_length=16, null=False)
    close_time = models.CharField(max_length=16, null=False)
    prime_image = models.ForeignKey(Picture, null=True, related_name='prime_iamge')
    pictures = models.ManyToManyField(Picture, related_name='pictures')
    # 가맹점 탈퇴여부에따라 목록노출.
    visible_flag = models.BooleanField(null=False, default=True)
    # 가맹점 승인되어야 flag 변경됨. true로변경됨.
    activate_flag = models.BooleanField(default=False)
    search = models.CharField(max_length=70, null=False)
    regdate = models.DateTimeField(null=False, auto_now_add=True)

    def __unicode__(self):
        result = u'가맹점'
        return result


class Member(models.Model):
    udid = models.CharField(max_length=50, null=False)
    nickname = models.CharField(max_length=16, null=True)
    birthday = models.DateTimeField(null=True)
    gender = models.NullBooleanField(null=True)
    push_acceptable = models.BooleanField(null=False, default=False)
    fake_download_count = models.IntegerField(null=False, default=0)
    fake_coupon_used_count = models.IntegerField(null=False, default=0)
    is_fake_id = models.BooleanField(null=False, default=False)
    last_login_time = models.DateTimeField(null=False, auto_now_add=True, auto_now=True)
    visible_flag = models.BooleanField(null=False, default=True)
    regdate = models.DateTimeField(null=False, auto_now_add=True)
    push_id = models.CharField(max_length=140, null=True)

    def __unicode__(self):
        result = u'회원'
        return result


class Coupon(models.Model):
    store = models.ForeignKey(Store, null=False)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    count = models.IntegerField(null=False)
    original_price = models.IntegerField(null=False, default=0)
    discount_price = models.IntegerField(null=False, default=0)
    discount_percentage = models.IntegerField(null=False, default=0)
    image = models.ForeignKey(Picture, null=True)
    activated_date_time = models.DateTimeField(null=True)
    expired_date_time = models.DateTimeField(null=True)
    weeks = models.CharField(max_length=46, null=False)
    visible_flag = models.BooleanField(null=False, default=True)
    publish_flag = models.BooleanField(null=False, default=True)
    # 쿠폰등록시 해당상점이 정액제상품이용중인지 판단하여 flag 를 true로 변경함.
    subscription_flag = models.BooleanField(null=False, default=False)
    search = models.CharField(max_length=50, null=False)
    regdate = models.DateTimeField(null=False, auto_now_add=True)

    def __unicode__(self):
        result = u'쿠폰 상세'
        return result


class MyCoupon(models.Model):
    coupon = models.ForeignKey(Coupon, null=False)
    member = models.ForeignKey(Member, null=False)
    # 쿠폰을 사용하면 useable flag를 False로 변경.
    useable = models.BooleanField(null=False, default=True)
    usedate = models.DateTimeField(null=True, auto_now_add=True, auto_now=True)
    # 정액제상품을 이용중에 발행한쿠폰인경우.
    subscription_flag = models.BooleanField(null=False, default=False)
    regdate = models.DateTimeField(null=True, auto_now_add=True, auto_now=False)

    def __unicode__(self):
        result = u'나의쿠폰함'
        return result


class StoreReview(models.Model):
    store = models.ForeignKey(Store, null=False)
    member = models.ForeignKey(Member, null=True)
    name = models.CharField(null=True, max_length=20)
    contents = models.TextField(null=False)
    regdate = models.DateTimeField(null=False, auto_now_add=True, auto_now=True)

    def __unicode__(self):
        result = u'가맹점리뷰'
        return result


class Like(models.Model):
    store = models.ForeignKey(Store, null=False)
    member = models.ForeignKey(Member, null=False)
    regdate = models.DateTimeField(null=False, auto_now_add=True, auto_now=True)

    def __unicode__(self):
        result = u'좋아요'
        return result


class Visit(models.Model):
    store = models.ForeignKey(Store, null=False)
    member = models.ForeignKey(Member, null=False)
    visit_date = models.DateTimeField(null=False, auto_now=True, auto_now_add=True)

    def __unicode__(self):
        result = u'방문자'
        return result


class Board(models.Model):
    store = models.ForeignKey(Store, null=False)
    title = models.TextField(null=False)
    contents = models.TextField(null=False)
    reply_flag = models.BooleanField(null=False, default=False)
    regdate = models.DateTimeField(null=False, auto_now_add=True, auto_now=True)

    def __unicode__(self):
        result = u'게시판'
        return result


class BoardReply(models.Model):
    board = models.ForeignKey(Board, null=False)
    contents = models.TextField(null=False)

    def __unicode__(self):
        result = u'게시판댓글'
        return result


class Bill(models.Model):
    # bill_type : 1: 직접 포인트 입력, 2: 기간제 (무제한)
    bill_type = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    point = models.IntegerField(null=False)
    visible_flag = models.BooleanField(null=False, default=True)

    def __unicode__(self):
        result = u'포인트구매'
        return result


class MyBill(models.Model):
    store = models.ForeignKey(Store, null=False)
    point = models.IntegerField(null=False)
    activated_date = models.DateTimeField(null=True)
    expired_date = models.DateTimeField(null=True)
    expense_type = models.IntegerField(null=False)
    expense_price = models.IntegerField(null=False)
    tid = models.CharField(null=False, max_length=40)
    # 2번째 성공페이지 출력시 api/s/payment/verify 에서 성공결과확인후 인증하여 값바꿈.
    verify = models.BooleanField(null=False, default=False)
    # 환불시에만 useble flag 가 False로 변경됨.
    useable = models.BooleanField(null=False, default=True)
    regdate = models.DateTimeField(null=False, auto_now_add=True)

    def __unicode__(self):
        result = u'나의포인트'
        return result


class Notice(models.Model):
    title = models.TextField(null=False)
    contents = models.TextField(null=False)
    display_flag = models.BooleanField(null=False, default=False)
    regdate = models.DateTimeField(null=False, auto_now_add=True, auto_now=True)

    def __unicode__(self):
        result = u'공지사항'
        return result


class Push(models.Model):
    contents = models.TextField(null=False)
    activated_date_time = models.DateTimeField(null=False)
    regdate = models.DateTimeField(null=False, auto_now_add=True, auto_now=True)

    def __unicode__(self):
        result = u'푸쉬'
        return result