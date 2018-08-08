from github import Github

g = Github(ltunnell-ptech, N3v3rmor3s0m3thing)

for repo in g.get_user().get_repos():
  print(repo.name)
