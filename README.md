# 1. Django App, URLConf, Template

## 장고 프로젝트 구조
- 장고 프로젝트: 장고 프로젝트 규칙에 따라, 파일/디렉토리 구성이 된 디렉토리
- 장고 앱 규칙에 따라서 파일/디렉토리 구성이 된 디렉토리
	- 하나의 장고 프로젝트의 다수 장고 앱이 있음

- 프로젝트는
`django-admin startproject [프로젝트 이름]`
을 통해서 만들 수 잇다.

```
manage.py
project/__init__.py
project/settings.py
project/urls.py
project/wsgi.py
project/templates/layout.html
```
***
프로젝트의 이름을  project로 했을 때의 구조 project 폴더의 이름은 바꿔서는 안된다. 단, manage.py, project 폴더 상위에 있는 project라는 이름은 바꿀 수 있음
***


## 장고 앱 만들기
- 장고 앱은
`python manage.py startapp [App 이름]`
으로 만들 수 있다.
- 장고 앱을 만들면, 장고 앱의 이름으로 폴더가 생성되고 간단한 파일들의 작성된다.
- [django/conf/app_template](https://github.com/django/django/tree/master/django/conf/app_template) 구성으로 생성된다.
- 앱은 만들어진 후 프로젝트에 등록해야 한다. 그렇지 않으면 디렉토리만 생성된 상태에 그친다.
- `project/settings.py`를 편집해서 `INSTALLED_APP` 항묵 끝에 blog 앱 이름을 추가해줘야 한다.

```
INSTALLED_APP = {
	# 생략
    'blog',
}
```