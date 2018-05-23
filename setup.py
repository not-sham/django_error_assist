from setuptools import setup

setup(name='django_error_assist',
      version='0.1.5',
      description='Allows user to search the django errors on google/stackoverflow with a link.',
      url='http://github.com/not-sham/django_error_assist',
      author='Sham Nagamangala Satyaprasad',
      author_email='shyam.ns114@gmail.com',
      license='MIT',
      packages=['django_error_assist'],
      install_requires=[
          'django',
      ],
      zip_safe=False)
