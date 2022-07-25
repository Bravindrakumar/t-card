from os import walk, path
exclude = {'./b/ab', './b/zx'}
for root, dirs, files in walk('.'):
  if exclude is not None:
    dirs[:] = [d for d in dirs if path.join(root, d) not in exclude]
  for name in files:
    print path.join(root, name)
