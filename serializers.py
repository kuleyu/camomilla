
from rest_framework import serializers, permissions
from rest_framework.authtoken.models import Token

from .models import Article, Tag, Category, Content, Media, SitemapUrl, MediaFolder

from hvad.contrib.restframework import TranslatableModelSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db import IntegrityError

from django.utils.translation import ugettext_lazy as _

from rest_framework.validators import UniqueTogetherValidator, ValidationError
from rest_framework.response import Response


class CamomillaBaseTranslatableModelSerializer(TranslatableModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(
            CamomillaBaseTranslatableModelSerializer, self
        ).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            print (expanded_fields)
            return expanded_fields
        else:
            return expanded_fields


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):

    user_permissions = PermissionSerializer(read_only=True, many=True)

    class Meta:
        model = get_user_model()
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True, required=False, allow_null=True, allow_blank=True)
    repassword = serializers.CharField(write_only=True, required=False, allow_null=True, allow_blank=True)
    level = serializers.CharField(required=False)
    has_token = serializers.SerializerMethodField('get_token', read_only=True)

    def get_token(self, obj):
        try:
            obj.auth_token
            return True
        except:
            return False

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'repassword', 'level', 'user_permissions', 'has_token', 'image')

    def validate(self, data):
        new_password = data.get('password', '')
        if new_password and len(new_password) < 8:
            raise serializers.ValidationError(_("Passwords too short"))
        if new_password != data.get('repassword', ''):
            raise serializers.ValidationError(_("Passwords should match"))
        return data

    def create(self, validated_data):
        user = get_user_model()(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            level=validated_data['level']
        )
        if validated_data.get('password', ''):
            user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.level = validated_data.get('level', instance.level)
        if validated_data.get('password', ''):
            instance.set_password(validated_data['password'])
        permissions = validated_data.get('user_permissions', [])
        instance.user_permissions.clear()
        for permission in permissions:
            instance.user_permissions.add(permission)
        instance.save()
        return instance


class TagSerializer(TranslatableModelSerializer):

    def create(self, validated_data):
        try:
             return super(TagSerializer, self).create(validated_data)
        except IntegrityError:
            raise ValidationError({
                "title" : ["Esiste già un Tag con questo titolo"]
            })

    def update(self, instance, data):
        try:
             return super(TagSerializer, self).update(instance, data)
        except IntegrityError:
            return Response({
                'title' : ['Esiste già un Tag con questo titolo']
            })

    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(TranslatableModelSerializer):

    def create(self, validated_data):
        try:
             return super(CategorySerializer, self).create(validated_data)
        except IntegrityError:
            raise ValidationError({
                "title" : ["Esiste già una Categoria con questo titolo"]
            })

    def update(self, instance, data):
        try:
             return super(CategorySerializer, self).update(instance, data)
        except IntegrityError:
            raise ValidationError({
                "title" : ["Esiste già una Categoria con questo titolo"]
            })

    class Meta:
        model = Category
        fields = '__all__'


class UnderTranslateMixin(object):

    def __init__(self, *args, **kwargs):
        self.ulanguage = 'en'
        try:
            self.ulanguage = kwargs.pop('ulanguage')
        except KeyError:
            pass
        super(UnderTranslateMixin, self).__init__(*args, **kwargs)


class ContentSerializer(TranslatableModelSerializer):

    class Meta:
        model = Content
        fields = '__all__'


class MediaSerializer(TranslatableModelSerializer):

    def exclude_fields(self, fields_to_exclude=None):
        if isinstance(fields_to_exclude, list):
            for f in fields_to_exclude:
                f in self.fields.fields and self.fields.fields.pop(f) or next()
    class Meta:
        model = Media
        fields = '__all__'



class MediaFolderSerializer(TranslatableModelSerializer):
    icon = MediaSerializer(read_only=True)
    class Meta:
        model = MediaFolder
        fields = '__all__'


#http://stackoverflow.com/questions/29950956/drf-simple-foreign-key-assignment-with-nested-serializers
class ArticleSerializer(UnderTranslateMixin, TranslatableModelSerializer):

    highlight_image_exp = MediaSerializer(source='highlight_image', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        

class ExpandedArticleSerializer(UnderTranslateMixin, TranslatableModelSerializer):

    tags = serializers.SerializerMethodField('get_translated_tags')
    categories = serializers.SerializerMethodField('get_translated_categories')
    author = serializers.CharField(read_only=True)
    highlight_image_exp = MediaSerializer(source='highlight_image', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

    def get_translated_tags(self, obj):
        tags = Tag.objects.language(self.ulanguage).fallbacks().filter(article__pk=obj.pk)
        return TagSerializer(tags, many=True).data

    def get_translated_categories(self, obj):
        categories = Category.objects.language(self.ulanguage).fallbacks().filter(article__pk=obj.pk)
        return CategorySerializer(categories, many=True).data


class SitemapUrlSerializer(TranslatableModelSerializer):

    class Meta:
        model = SitemapUrl
        fields = '__all__'


class CompactSitemapUrlSerializer(TranslatableModelSerializer):

    class Meta:
        model = SitemapUrl
        fields = ('id', 'identifier', 'title','description', 'permalink', 'og_image')
