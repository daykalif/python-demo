"""
Django settings for bookmanager02 project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ku+5atykhu8ij!d@s9a!9^@jxbr$tbb@@-qm6zk*sq=q*@mki#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS允许以哪个主机的形式访问后端
# 默认是127.0.0.1
# 如果你改变了允许方式，需要将运行的ip/域名添加进来
# 默认的127.0.0.1需要自己添加才可以再次访问
#  安全机制 只能以罗列的 来访问
#  此时启动项目，运行 python manage.py runserver 0:8000   才可以同时访问192.168.50.211:8000 和 127.0.0.1:8000
ALLOWED_HOSTS = ['192.168.50.211', '127.0.0.1', '192.168.8.113']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 注册子应用
    'book.apps.BookConfig',
]

# 中间件
"""
Django中的中间件是一个轻量级、底层的插件系统，可以介入Django的请求和响应处理过程，修改Django的输入或输出。
中间件的设计为开发者提供了一种无侵入式的开发方式，增强了Django框架的健壮性。

我们可以使用中间件，在Django处理视图的不同阶段对输入或输出进行干预
"""
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 注册中间件
    'book.middleware.simple_middleware',
    'book.middleware.simple_middleware2',
]

ROOT_URLCONF = 'bookmanager02.urls'

# 模板
TEMPLATES = [
    {
        # 'BACKEND': 'django.template.backends.django.DjangoTemplates', # Django默认模板
        'BACKEND': 'django.template.backends.jinja2.Jinja2',  # 修改为jinja2模板
        # 2.加载templates路径
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            # 使用jinja2模板后，默认environment就是jinja2_env.environment,
            # 'environment': 'jinja2_env.environment',
            'environment': 'book.jinja2_env.environment',  # 指定jinja2环境
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookmanager02.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # engine 引擎
        'POST': '127.0.0.1',  # 主机
        'PORT': '3306',  # 端口号
        'USER': 'root',  # 用户名
        'PASSWORD': 'root',  # 密码
        'NAME': 'book_42_02',  # 指定数据库
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
