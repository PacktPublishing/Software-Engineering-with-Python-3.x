import setuptools

with open("README.txt", "r") as fh:
	long_description = fh.read()

with open("LICENCSE.txt", "r") as fh:
	license = fh.read()

setuptools.setup(
	 name='my_package',  
	 version='0.966',
	 author="Some Random Python Developer",
	 author_email="some_xyz@gmail.com",
	 description="Creates a relation graph",
	 long_description=long_description,
	 packages=['my_package'],
	 license=license,
)