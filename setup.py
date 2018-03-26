from setuptools import setup


setup(name='tinyotp',
      version='1.0.0',
      license='ISC',
      author='Luiz Berti',
      url='https://github.com/luizberti/tinyotp',
      description='Elegantly simple OTP validation library',
      keywords='otp hotp totp token 2fa tfa authentication security',
      packages=['tinyotp'],
      zip_safe=True,
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: ISC License (ISCL)',
          'Programming Language :: Python :: 3',
          'Topic :: Security',
          'Topic :: Security :: Cryptography',
      ])
