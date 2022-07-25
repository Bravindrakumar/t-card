from os import walk, path
exclude = {'b/ab', 'b/zx'}
for root, dirs, files in walk('b'):
  if exclude is not None:
    dirs[:] = [d for d in dirs if path.join(b, d) not in exclude]
  for name in files:
    print path.join(b, name)
