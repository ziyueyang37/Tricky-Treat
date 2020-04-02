def func(name):  
  name.split('/')
  ext = name.split('.')[-1]
  file = name.split('/')[-1]
  directory = name.split(file)[0]
  return directory, file, ext
  
name = '/a/b/c.d'
func(name)
