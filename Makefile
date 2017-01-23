.ONESHELL:
.HONY:  test pep8


objects1 = $(shell find . -name *.py)
objects2 = $(shell find ./test -name test_*)
	
pep8: $(objects1) 
	@pep8 --ignore E721 $(objects1)


test: $(objects2)
	@pytest
