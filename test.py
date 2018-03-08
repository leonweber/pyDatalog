from pyDatalog import pyDatalog

pyDatalog.create_terms("X, works_in, employed_by")

+ works_in('Mary', 'Production')
+ works_in('Sam',  'Marketing')

works_in(X, 'Company') <= works_in(X, 'Production')

# print(works_in('Mary', 'Company'))
print(employed_by('Mary', 'Company'))
