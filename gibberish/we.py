def example(**kwargs):
  for key in kwargs:
    kwargs[key]
  print(kwargs)


example(a=1)


# class super_class:
#   def __init__(self, **kwargs):
#     kwargs['name'] = None
    
    
#     # print(kwargs)



# class sub_class(super_class):
#   def __init__(self):
#     super().__init__()
#     self['name'] = "Muwaffug"

# sc = super_class()
# sbc = sub_class()
